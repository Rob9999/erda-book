#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Selective Publisher
- Liest publish.yml|yaml aus dem Repo-Root
- Ermittelt alle Einträge mit build: true -> get_publish_list()
- Bereitet Umgebung vor (PyYAML, optional Pandoc/LaTeX & Emoji-Fonts) -> prepareYAML(), prepare_publishing()
- Baut PDFs für 'file' und 'folder' -> build_pdf()
- Setzt nach erfolgreichem Build das Flag per reset-publish-flag.py zurück -> main()

Aufrufbeispiele:
  python .github/tools/publishing/publisher.py
  python .github/tools/publishing/publisher.py --manifest publish.yml --use-summary
  python .github/tools/publishing/publisher.py --no-apt --only-prepare

Optionen siehe argparse unten.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from tools.logging_config import get_logger

from tools.publishing.markdown_combiner import (
    add_geometry_package,
    combine_markdown,
    normalize_md,
)
from tools.publishing.preprocess_md import process

# ------------------------------- Utils ------------------------------------- #

logger = get_logger(__name__)


def _run(
    cmd: List[str],
    check: bool = True,
    capture: bool = False,
    env: Optional[Dict[str, str]] = None,
) -> subprocess.CompletedProcess:
    kwargs: Dict[str, Any] = {"text": True}
    if capture:
        kwargs["stdout"] = subprocess.PIPE
        kwargs["stderr"] = subprocess.PIPE
    if env:
        kwargs["env"] = {**os.environ, **env}
    logger.info("→ %s", " ".join(cmd))
    cp = subprocess.run(cmd, **kwargs)
    if check and cp.returncode != 0:
        if capture:
            logger.info(cp.stdout or "")
            logger.error(cp.stderr or "")
        raise subprocess.CalledProcessError(cp.returncode, cmd)
    return cp


def _which(name: str) -> Optional[str]:
    return shutil.which(name)


def _is_debian_like() -> bool:
    return pathlib.Path("/etc/debian_version").exists()


def _ensure_dir(path: str) -> None:
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def _download(url: str, dest: str) -> None:
    import urllib.request

    logger.info("↓ Download %s -> %s", url, dest)
    pathlib.Path(os.path.dirname(dest)).mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as r, open(dest, "wb") as f:
        f.write(r.read())


# ----------------------------- YAML Helpers -------------------------------- #


def prepareYAML() -> None:
    """Installiert PyYAML, falls nicht vorhanden."""
    try:
        import yaml  # noqa: F401

        return
    except Exception:
        pass
    py = sys.executable or "python"
    _run([py, "-m", "pip", "install", "--upgrade", "pip"], check=False)
    _run([py, "-m", "pip", "install", "pyyaml"])


def find_publish_manifest(explicit: Optional[str] = None) -> str:
    if explicit and os.path.exists(explicit):
        return explicit
    for name in ("publish.yml", "publish.yaml"):
        if os.path.exists(name):
            return name
    logger.error("publish.yml|yaml nicht im Repo-Root gefunden.")
    sys.exit(2)


def _load_yaml(path: str) -> Dict[str, Any]:
    import yaml

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if "publish" not in data or not isinstance(data["publish"], list):
        logger.error("Ungültiges Manifest – Top-Level 'publish' (Liste) fehlt.")
        sys.exit(3)
    return data


def _save_yaml(path: str, data: Dict[str, Any]) -> None:
    import yaml

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


# --------------------------- Public API (A) -------------------------------- #


def get_publish_list(manifest_path: Optional[str] = None) -> List[Dict[str, str]]:
    """
    Liest publish.yml und liefert alle Einträge mit build: true als Liste
    [{path, out, type}, ...]
    """
    prepareYAML()
    mpath = find_publish_manifest(manifest_path)
    data = _load_yaml(mpath)
    res: List[Dict[str, str]] = []
    for e in data.get("publish", []):
        if e.get("build"):
            res.append(
                {
                    "path": str(e.get("path", "")),
                    "out": str(e.get("out", "")),
                    "type": str(e.get("type", "file")),
                    "use_summary": str(e.get("use_summary", False)).lower() == "true",
                    "keep_combined": str(e.get("keep_combined", False)).lower()
                    == "true",
                }
            )
    return res


# ---------------------- Environment Prep (B / B.1) ------------------------- #


def prepare_publishing(no_apt: bool = False) -> None:
    """
    Installiert die System- und Python-Abhängigkeiten für den PDF-Build.
    - PyYAML (via prepareYAML)
    - Pandoc + LaTeX (apt-get auf Debian/Ubuntu)
    - OpenMoji Font + fc-cache
    - latex-emoji.lua (Pandoc Lua-Filter)
    """
    prepareYAML()  # B.1

    # Pandoc vorhanden?
    have_pandoc = _which("pandoc") is not None
    have_lualatex = _which("lualatex") is not None

    if not (have_pandoc and have_lualatex):
        if no_apt:
            logger.warning(
                "pandoc/lualatex fehlen, --no-apt gesetzt. Bitte vorinstallieren."
            )
        elif _is_debian_like():
            sudo = _which("sudo")
            prefix = [sudo] if sudo else []
            _run(prefix + ["apt-get", "update"])
            _run(
                prefix
                + [
                    "apt-get",
                    "install",
                    "-y",
                    "pandoc",
                    "texlive-luatex",
                    "texlive-fonts-recommended",
                    "texlive-latex-extra",
                    "texlive-lang-cjk",
                    "fonts-dejavu-core",
                    "wget",
                ]
            )
        else:
            logger.warning(
                "Nicht-Debian System erkannt – installiere pandoc/LaTeX manuell."
            )

    # OpenMoji-Font & fc-cache
    font_dir = ".github/tools/publishing/fonts/truetype/openmoji"
    font_path = os.path.join(font_dir, "OpenMoji-black-glyf.ttf")
    if not os.path.exists(font_path):
        try:
            _ensure_dir(font_dir)
            url = "https://github.com/hfg-gmuend/openmoji/raw/master/font/OpenMoji-black-glyf/OpenMoji-black-glyf.ttf"
            _download(url, font_path)
            if _which("fc-cache"):
                _run(["fc-cache", "-f", "-v"], check=False)
        except Exception as e:
            logger.warning("Konnte OpenMoji nicht installieren: %s", e)

    # latex-emoji.lua Filter
    lua_dir = ".github/tools/publishing/lua"
    lua_path = os.path.join(lua_dir, "latex-emoji.lua")
    if not os.path.exists(lua_path):
        try:
            _ensure_dir(lua_dir)
            url = "https://gist.githubusercontent.com/zr-tex8r/a5410ad20ab291c390884b960c900537/raw/latex-emoji.lua"
            _download(url, lua_path)
        except Exception as e:
            logger.warning("Konnte latex-emoji.lua nicht laden: %s", e)


# --------------------------- PDF Build (C) --------------------------------- #


def _get_book_title(folder: str) -> Optional[str]:
    try:
        # Pfad zum book.json eine Ebene über dem Ordner
        book_json_path = pathlib.Path(folder).parent / "book.json"
        if not book_json_path.exists():
            return None
        with book_json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("title")
    except Exception:
        return None


def _run_pandoc(
    md_path: str, pdf_out: str, add_toc: bool = False, title: Optional[str] = None
) -> None:
    _ensure_dir(os.path.dirname(pdf_out))
    cmd = [
        "pandoc",
        md_path,
        "-o",
        pdf_out,
        "--pdf-engine",
        "lualatex",
        "-V",
        "mainfont=DejaVu Sans",
        "-V",
        "monofont=DejaVu Sans Mono",
        "-V",
        "emoji=OpenMoji-black-glyf.ttf",
        "-V",
        "geometry=margin=1in",
        "--lua-filter",
        ".github/tools/publishing/lua/latex-emoji.lua",
        "-H",
        ".github/tools/publishing/texmf/tex/latex/local/deeptex.sty",
        "-M",
        "emojifont=OpenMoji-black-glyf.ttf",
        "-M",
        "color=false",
        "--variable",
        "longtable=true",
        "--variable",
        "max-list-depth=9",
    ]
    if add_toc:
        cmd.append("--toc")
    if title:
        cmd.extend(["-V", f"title={title}"])
    _run(cmd)


def _extract_md_paths_from_summary(folder: str) -> List[str]:
    summary_path = os.path.join(folder, "summary.md")
    if not os.path.exists(summary_path):
        return []
    paths: List[str] = []
    with open(summary_path, "r", encoding="utf-8") as f:
        for line in f:
            for match in re.findall(r"\(([^)]+\.md)\)", line):
                if not match.startswith(("http://", "https://")):
                    paths.append(os.path.normpath(os.path.join(folder, match)))
    return paths


def _collect_folder_md(folder: str, use_summary: bool) -> List[str]:
    if use_summary:
        md_files = _extract_md_paths_from_summary(folder)
        logger.info(
            "ℹ %d Markdown-Dateien aus summary.md in %s gefunden.",
            len(md_files),
            folder,
        )
        if md_files:
            return md_files
    # Fallback: alle .md rekursiv, README bevorzugt
    md_files: List[str] = []
    for root, _, files in os.walk(folder):
        for fname in sorted(files):
            if fname.lower().endswith((".md", ".markdown")):
                full = os.path.join(root, fname)
                if fname.lower() == "readme.md":
                    md_files.insert(0, full)
                else:
                    md_files.append(full)
    logger.info("ℹ %d Markdown-Dateien in %s gefunden.", len(md_files), folder)
    return md_files


def convert_a_file(
    md_file: str,
    pdf_out: str,
    keep_converted_markdown: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
) -> None:
    logger.info(
        "========================================================================"
    )
    logger.info("Convert a new single file")
    logger.info(
        "------------------------------------------------------------------------"
    )
    logger.info("File                    : %s", md_file)
    logger.info("PDF OUT                 : %s", pdf_out)
    logger.info("Keep Converted Markdown : %s", keep_converted_markdown)
    logger.info("Publish Dir             : %s", publish_dir)
    logger.info("Paper Format            : %s", paper_format)

    # preprocess for wide content (tables, images), will change page geometry
    processed = process(md_file, paper_format=paper_format)
    logger.info("%s: Nach Preprocessing %d Zeichen.", md_file, len(processed))
    # normalize for pandoc
    normalized = normalize_md(processed)
    logger.info("%s: Nach Normalisierung %d Zeichen.", md_file, len(normalized))
    # add geometry package
    content = add_geometry_package(
        normalized,
        paper_format=paper_format,
    )
    with tempfile.NamedTemporaryFile(
        "w", suffix=".md", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(content)
        tmp_md = tmp.name
    try:
        _run_pandoc(tmp_md, pdf_out)
    finally:
        try:
            if not keep_converted_markdown:
                os.unlink(tmp_md)
            else:
                converted_md_path = pdf_out.replace(".pdf", ".md")
                logger.info(
                    "Keeping converted markdown in %s",
                    converted_md_path,
                )
                print(
                    "Keeping converted markdown in " + converted_md_path,
                )
                shutil.move(str(tmp_md), str(converted_md_path))
        except OSError as e:
            logger.error("Failed to operate on converted markdown caused by %s", e)
            pass
        logger.info(
            "------------------------------------------------------------------------"
        )
        logger.info("%s", content)
        logger.info(
            "========================================================================"
        )


def convert_a_folder(
    folder: str,
    pdf_out: str,
    use_summary: bool = True,
    keep_converted_markdown: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
) -> None:

    logger.info(
        "========================================================================"
    )
    logger.info("Convert a folder")
    logger.info(
        "------------------------------------------------------------------------"
    )
    logger.info("Folder                  : %s", folder)
    logger.info("PDF OUT                 : %s", pdf_out)
    logger.info("Keep Converted Markdown : %s", keep_converted_markdown)
    logger.info("Publish Dir             : %s", publish_dir)
    logger.info("Paper Format            : %s", paper_format)

    md_files = _collect_folder_md(folder, use_summary=use_summary)
    if not md_files:
        logger.info("ℹ Keine Markdown-Dateien in %s – übersprungen.", folder)
        raise Exception(f"No markdown files found in {folder}")
    combined = add_geometry_package(
        combine_markdown(md_files, paper_format=paper_format), paper_format=paper_format
    )
    with tempfile.NamedTemporaryFile(
        "w", suffix=".md", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(combined)
        tmp_md = tmp.name
    try:
        title = _get_book_title(folder)
        logger.info(
            "ℹ Buch-Titel aus book.json: %s" if title else "ℹ Kein Buch-Titel",
            title,
        )
        _run_pandoc(tmp_md, pdf_out, add_toc=True, title=title)
    finally:
        try:
            if not keep_converted_markdown:
                os.unlink(tmp_md)
            else:
                converted_markdown = pdf_out.replace(".pdf", ".md")
                logger.info("ℹ Behalte kombiniertes Markdown in %s", converted_markdown)
                _ensure_dir(publish_dir)
                shutil.move(str(tmp_md), str(converted_markdown))
        except OSError as e:
            logger.error("Failed to operate on converted markdown caused by %s", e)
            pass
        logger.info(
            "------------------------------------------------------------------------"
        )
        logger.info("%s", combined)
        logger.info(
            "========================================================================"
        )


def build_pdf(
    path: str,
    out: str,
    typ: str,
    use_summary: bool = False,
    keep_combined: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
) -> Tuple[bool, str]:
    """
    Baut ein PDF gemäß Typ ('file'/'folder').
    Gibt True bei Erfolg zurück und False bei Fehlern plus eine detailierte Error Message.
    """
    pdf_out = os.path.join(publish_dir, out)
    logger.info("✔ Building %s from %s (type=%s)", pdf_out, path, typ)
    _ensure_dir(publish_dir)

    # Typ autodetektion, falls leer/ungewohnt
    _typ = (typ or "").lower().strip()
    if not _typ or _typ not in {"file", "folder"}:
        if os.path.isdir(path):
            _typ = "folder"
        else:
            _typ = "file"

    try:
        if _typ == "file":
            # _convert_single_file(
            #    path,
            #    pdf_out,
            #    paper_format=paper_format,
            # )
            convert_a_file(
                path,
                pdf_out,
                keep_converted_markdown=True,
                publish_dir=publish_dir,
                paper_format=paper_format,
            )
        elif _typ == "folder":
            convert_a_folder(
                path,
                pdf_out,
                use_summary=use_summary,
                keep_converted_markdown=keep_combined,
                publish_dir=publish_dir,
                paper_format=paper_format,
            )
        else:
            logger.warning("⚠ Unbekannter type='%s' – übersprungen.", typ)
            return False, f"Unknown type='{typ}' - skipped"
        return True, None
    except subprocess.CalledProcessError as e:
        logger.error("Pandoc/LaTeX Build fehlgeschlagen (rc=%s).", e.returncode)
        return False, str(e) + "\n" + (e.stdout or "") + "\n" + (e.stderr or "")
    except Exception as e:
        logger.error("Build-Fehler: %s", e)
        stdout = getattr(e, "stdout", "")
        stderr = getattr(e, "stderr", "")
        return False, f"{e}\n{stdout}\n{stderr}"


# -------------------------------- Main (D) --------------------------------- #


def _write_github_outputs(built: List[str], failed: List[str], manifest: str) -> None:
    gh_out = os.getenv("GITHUB_OUTPUT")
    if gh_out:
        try:
            with open(gh_out, "a", encoding="utf-8") as f:
                f.write(f"built_count={len(built)}\n")
                f.write(f"built_files={json.dumps(built, ensure_ascii=False)}\n")
                f.write(f"failed_files={json.dumps(failed, ensure_ascii=False)}\n")
                f.write(f"manifest={manifest}\n")
        except Exception as e:
            logger.warning("Konnte GITHUB_OUTPUT nicht schreiben: %s", e)


def main() -> None:
    logger.info("Selective Publisher gestartet: argv=%s", sys.argv)
    ap = argparse.ArgumentParser(description="Selective publisher für publish.yml")
    ap.add_argument("--manifest", help="Pfad zu publish.yml|yaml (Default: Root)")
    ap.add_argument(
        "--no-apt", action="store_true", help="Keine apt-Installation versuchen"
    )
    ap.add_argument(
        "--only-prepare",
        action="store_true",
        help="Nur Umgebung vorbereiten und beenden",
    )
    ap.add_argument(
        "--reset-script",
        default=".github/tools/publishing/reset-publish-flag.py",
        help="Pfad zum Reset-Tool",
    )
    ap.add_argument(
        "--paper-format",
        help="Enable landscape orientation for wide content",
        default="a4",
    )
    ap.add_argument(
        "--publish-dir",
        help="The directory to publish to.",
        default="docs/public/publish",
    )
    args = ap.parse_args()

    if args.only_prepare:
        # B.1 + B
        prepare_publishing(no_apt=args.no_apt)
        logger.info("✔ Umgebung vorbereitet. (only-prepare)")
        return

    # prepareYAML()  # B.1
    prepareYAML()
    # get manifest publish list (A)
    manifest = find_publish_manifest(args.manifest)
    targets = get_publish_list(manifest)

    if not targets:
        logger.info("ℹ Keine zu publizierenden Einträge (build: true).")
        _write_github_outputs([], [], manifest)
        return

    logger.info("ℹ %d zu publizierende Einträge gefunden.", len(targets))
    # prepare huge environment (B)
    prepare_publishing(no_apt=args.no_apt)
    built: List[str] = []
    failed: List[str] = []

    manifest_dir = Path(manifest).parent

    # C + Reset je nach Erfolg
    for entry in targets:
        path = entry["path"]
        path = Path(path)
        if not path.is_absolute():
            path = manifest_dir / path
        out = entry["out"]
        typ = entry.get("type", "file")
        ok, msg = build_pdf(
            path=path,
            out=out,
            typ=typ,
            use_summary=entry["use_summary"],
            keep_combined=entry["keep_combined"],
            paper_format=args.paper_format,
            publish_dir=args.publish_dir,
        )
        if ok:
            built.append(out)
            # Reset publish-Flag (D) – nur bei Erfolg
            reset_tool = args.reset_script
            if os.path.exists(reset_tool):
                try:
                    _run(
                        [
                            sys.executable or "python",
                            reset_tool,
                            "--path",
                            path,
                            "--multi",
                        ],
                        check=True,
                    )
                except Exception as e:
                    logger.warning("Konnte reset-publish-flag nicht aufrufen: %s", e)
            else:
                # Fallback: direkt im Manifest auf false setzen
                try:
                    data = _load_yaml(manifest)
                    for e in data.get("publish", []):
                        if e.get("path") == path:
                            e["build"] = False
                    _save_yaml(manifest, data)
                except Exception as e:
                    logger.warning(
                        "Konnte Manifest-Fallback-Reset nicht schreiben: %s", e
                    )
        else:
            failed.append(out + (f": {msg}" if msg else ""))

    # Outputs
    logger.info("::group::publisher.outputs")
    logger.info(
        json.dumps(
            {
                "built_count": len(built),
                "built_files": built,
                "failed_files": failed,
                "manifest": manifest,
            },
            ensure_ascii=False,
        )
    )
    logger.info("::endgroup::")

    _write_github_outputs(built, failed, manifest)

    # Exit-Code, wenn Builds fehlgeschlagen sind (aber nicht hart abbrechen, wenn ein Teil ok ist)
    if built and not failed:
        sys.exit(0)
    elif failed and not built:
        sys.exit(1)
    else:
        # Teilweise erfolgreich
        sys.exit(0)


if __name__ == "__main__":
    main()
