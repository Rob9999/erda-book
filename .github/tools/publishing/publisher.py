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
from collections import OrderedDict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from tools.logging_config import get_logger

from tools.publishing.markdown_combiner import (
    add_geometry_package,
    combine_markdown,
    normalize_md,
)
from tools.publishing.preprocess_md import process
from tools.publishing.gitbook_style import (
    DEFAULT_MANUAL_MARKER,
    SummaryContext,
    ensure_clean_summary,
    get_summary_layout,
)

# ------------------------------- Utils ------------------------------------- #

logger = get_logger(__name__)


_TRUE_VALUES = {"1", "true", "yes", "on", "y"}

_SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+][0-9A-Za-z.-]+)?$"
)
_MANIFEST_VERSION_MIN = (0, 1, 0)
_MANIFEST_VERSION_CURRENT = (0, 1, 0)


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in _TRUE_VALUES
    return default


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


def _parse_semver(value: str) -> Tuple[int, int, int]:
    if not isinstance(value, str):
        raise ValueError("Manifest-Version muss ein String sein.")
    candidate = value.strip()
    match = _SEMVER_RE.match(candidate)
    if not match:
        raise ValueError(
            "Manifest-Version muss dem SemVer-Format MAJOR.MINOR.PATCH entsprechen."
        )
    major_s, minor_s, patch_s = match.groups()
    return int(major_s), int(minor_s), int(patch_s)


def _format_semver(parts: Tuple[int, int, int]) -> str:
    return ".".join(str(p) for p in parts)


def _resolve_publish_directory(base_dir: Path, value: Optional[str]) -> Path:
    target = Path(value) if value else Path("publish")
    if not target.is_absolute():
        target = (base_dir / target).resolve()
    return target


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

    version_value = data.get("version")
    if version_value is None:
        logger.error("Manifest-Version fehlt (Schlüssel 'version').")
        sys.exit(3)

    try:
        manifest_version = _parse_semver(str(version_value))
    except ValueError as exc:
        logger.error("Ungültige Manifest-Version '%s': %s", version_value, exc)
        sys.exit(3)

    if manifest_version[0] != _MANIFEST_VERSION_CURRENT[0]:
        logger.error(
            "Manifest-Major-Version %s wird nicht unterstützt (erwartet %d.x.x).",
            version_value,
            _MANIFEST_VERSION_CURRENT[0],
        )
        sys.exit(3)

    if manifest_version < _MANIFEST_VERSION_MIN:
        logger.error(
            "Manifest-Version %s ist zu alt. Minimal unterstützt: %s.",
            version_value,
            _format_semver(_MANIFEST_VERSION_MIN),
        )
        sys.exit(3)

    if manifest_version > _MANIFEST_VERSION_CURRENT:
        logger.warning(
            "Manifest-Version %s ist neuer als die getestete %s – versuche fortzufahren.",
            version_value,
            _format_semver(_MANIFEST_VERSION_CURRENT),
        )

    data["_manifest_version"] = manifest_version

    if "publish" not in data or not isinstance(data["publish"], list):
        logger.error("Ungültiges Manifest – Top-Level 'publish' (Liste) fehlt.")
        sys.exit(3)
    return data


def _save_yaml(path: str, data: Dict[str, Any]) -> None:
    import yaml

    serialisable = {k: v for k, v in data.items() if not str(k).startswith("_")}
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(serialisable, f, sort_keys=False, allow_unicode=True)


# --------------------------- Public API (A) -------------------------------- #


def get_publish_list(manifest_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return all manifest entries that should be built."""

    prepareYAML()
    mpath = find_publish_manifest(manifest_path)
    data = _load_yaml(mpath)
    manifest_version = data.get("_manifest_version")
    if isinstance(manifest_version, tuple):
        logger.info("Manifest-Version: %s", _format_semver(manifest_version))
    res: List[Dict[str, Any]] = []

    for entry in data.get("publish", []):
        if not _as_bool(entry.get("build"), default=False):
            continue

        path = entry.get("path")
        out = entry.get("out")
        if not path or not out:
            logger.warning("Überspringe Manifest-Eintrag ohne path/out: %s", entry)
            continue

        out_dir = entry.get("out_dir")
        result: Dict[str, Any] = {
            "path": str(path),
            "out": str(out),
            "out_dir": str(out_dir) if out_dir not in (None, "") else None,
            "out_format": str(entry.get("out_format", "pdf") or "pdf").lower(),
            "source_type": str(entry.get("source_type") or entry.get("type") or "")
            .lower()
            .strip(),
            "source_format": str(entry.get("source_format", "markdown") or "markdown")
            .lower()
            .strip(),
            "use_summary": _as_bool(entry.get("use_summary")),
            "use_book_json": _as_bool(entry.get("use_book_json")),
            "keep_combined": _as_bool(entry.get("keep_combined")),
            "summary_mode": entry.get("summary_mode"),
            "summary_order_manifest": entry.get("summary_order_manifest"),
            "summary_manual_marker": entry.get("summary_manual_marker"),
            "summary_appendices_last": entry.get("summary_appendices_last"),
            "reset_build_flag": _as_bool(entry.get("reset_build_flag")),
        }
        res.append(result)

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
        "--lua-filter",
        ".github/tools/publishing/lua/image-path-resolver.lua",
        "-H",
        ".github/tools/publishing/texmf/tex/latex/local/deeptex.sty",
        "-M",
        "emojifont=OpenMoji-black-glyf.ttf",
        "--resource-path",
        ".:assets:.gitbook/assets",
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


def _extract_md_paths_from_summary(summary_path: Path, root_dir: Path) -> List[str]:
    if not summary_path.exists():
        return []

    resolved: "OrderedDict[str, None]" = OrderedDict()
    pattern = re.compile(r"\(([^)]+\.(?:md|markdown))\)", re.IGNORECASE)

    try:
        with summary_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                for match in pattern.findall(line):
                    target = match.split("#", 1)[0].strip()
                    if not target or target.startswith(("http://", "https://")):
                        continue
                    candidate = (root_dir / target).resolve()
                    if candidate.suffix.lower() not in {".md", ".markdown"}:
                        continue
                    resolved[str(candidate)] = None
    except Exception as exc:
        logger.warning("Konnte SUMMARY in %s nicht lesen: %s", summary_path, exc)
        return []

    return list(resolved.keys())


def _iter_summary_candidates(folder: Path, summary_path: Optional[Path]) -> List[Path]:
    candidates: List[Path] = []
    seen: set[Path] = set()

    if summary_path is not None:
        resolved = summary_path.resolve()
        candidates.append(resolved)
        seen.add(resolved)

    for name in ("SUMMARY.md", "summary.md"):
        candidate = (folder / name).resolve()
        if candidate not in seen:
            candidates.append(candidate)
            seen.add(candidate)

    return candidates


def _collect_folder_md(
    folder: str,
    use_summary: bool,
    *,
    summary_layout: Optional[SummaryContext] = None,
) -> List[str]:
    folder_path = Path(folder).resolve()
    root_dir = summary_layout.root_dir if summary_layout else folder_path
    summary_candidates = _iter_summary_candidates(
        folder_path, summary_layout.summary_path if summary_layout else None
    )

    if use_summary:
        for candidate in summary_candidates:
            md_files = _extract_md_paths_from_summary(candidate, root_dir)
            logger.info(
                "ℹ %d Markdown-Dateien aus %s gelesen.",
                len(md_files),
                candidate,
            )
            if md_files:
                return md_files
    # Fallback: alle .md rekursiv, README bevorzugt
    md_files: List[str] = []
    for root, _, files in os.walk(folder_path):
        for fname in sorted(files):
            if fname.lower().endswith((".md", ".markdown")):
                full = os.path.join(root, fname)
                if fname.lower() == "readme.md":
                    md_files.insert(0, full)
                else:
                    md_files.append(full)
    logger.info("ℹ %d Markdown-Dateien in %s gefunden.", len(md_files), folder_path)
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
    summary_layout: Optional[SummaryContext] = None,
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

    md_files = _collect_folder_md(
        folder, use_summary=use_summary, summary_layout=summary_layout
    )
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
        if title:
            logger.info("ℹ Buch-Titel aus book.json: %s", title)
        else:
            logger.info("ℹ Kein Buch-Titel")
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
    path: str | Path,
    out: str,
    typ: str,
    use_summary: bool = False,
    use_book_json: bool = False,
    keep_combined: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
    summary_mode: Optional[str] = None,
    summary_order_manifest: Optional[Path] = None,
    summary_manual_marker: Optional[str] = DEFAULT_MANUAL_MARKER,
    summary_appendices_last: bool = False,
) -> Tuple[bool, Optional[str]]:
    """
    Baut ein PDF gemäß Typ ('file'/'folder').
    Gibt True bei Erfolg zurück und False bei Fehlern plus eine detaillierte Fehlernachricht.
    """
    publish_path = Path(publish_dir).resolve()
    _ensure_dir(str(publish_path))
    pdf_out = publish_path / out
    path_obj = Path(path).resolve()

    logger.info("✔ Building %s from %s (type=%s)", pdf_out, path_obj, typ)

    # Typ autodetektion, falls leer/ungewohnt
    _typ = (typ or "").lower().strip()
    if not _typ or _typ not in {"file", "folder"}:
        if path_obj.is_dir():
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
                str(path_obj),
                str(pdf_out),
                keep_converted_markdown=True,
                publish_dir=str(publish_path),
                paper_format=paper_format,
            )
        elif _typ == "folder":
            summary_layout: Optional[SummaryContext] = None
            needs_summary_refresh = (
                use_book_json
                or summary_mode is not None
                or summary_order_manifest is not None
                or (
                    summary_manual_marker is not None
                    and summary_manual_marker != DEFAULT_MANUAL_MARKER
                )
            )
            if needs_summary_refresh:
                try:
                    summary_layout = get_summary_layout(path_obj)
                    ensure_clean_summary(
                        summary_layout.base_dir,
                        run_git=False,
                        summary_mode=summary_mode,
                        summary_order_manifest=summary_order_manifest,
                        manual_marker=summary_manual_marker,
                        summary_appendices_last=summary_appendices_last,
                    )
                except Exception as exc:  # pragma: no cover - best effort logging
                    logger.warning(
                        "Konnte SUMMARY via book.json nicht aktualisieren: %s", exc
                    )
            convert_a_folder(
                str(path_obj),
                str(pdf_out),
                use_summary=use_summary or use_book_json or summary_layout is not None,
                keep_converted_markdown=keep_combined,
                publish_dir=str(publish_path),
                paper_format=paper_format,
                summary_layout=summary_layout,
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
        default="publish",
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

    manifest_path = Path(manifest).resolve()
    manifest_dir = manifest_path.parent
    default_publish_dir = _resolve_publish_directory(manifest_dir, args.publish_dir)

    # C + Reset je nach Erfolg
    for entry in targets:
        original_path = entry["path"]
        path = Path(original_path)
        if not path.is_absolute():
            path = (manifest_dir / path).resolve()
        out = entry["out"]
        out_format = entry.get("out_format", "pdf")
        if out_format.lower() != "pdf":
            msg = f"Unsupported out_format='{out_format}'"
            logger.warning("⚠ %s – Eintrag wird übersprungen.", msg)
            failed.append(f"{out}: {msg}")
            continue

        typ = entry.get("source_type") or entry.get("type", "")
        publish_base = entry.get("out_dir")
        publish_dir_path = (
            _resolve_publish_directory(manifest_dir, publish_base)
            if publish_base
            else default_publish_dir
        )
        summary_mode = entry.get("summary_mode")
        if summary_mode is not None:
            summary_mode = str(summary_mode).strip() or None
        manifest_value = entry.get("summary_order_manifest")
        summary_manifest_path: Optional[Path]
        if manifest_value:
            summary_manifest_path = Path(str(manifest_value))
            if not summary_manifest_path.is_absolute():
                summary_manifest_path = (manifest_dir / summary_manifest_path).resolve()
        else:
            summary_manifest_path = None
        summary_manual_marker_value = entry.get("summary_manual_marker")
        if summary_manual_marker_value is None:
            summary_manual_marker = DEFAULT_MANUAL_MARKER
        else:
            summary_manual_marker = str(summary_manual_marker_value)

        ok, msg = build_pdf(
            path=path,
            out=out,
            typ=typ,
            use_summary=entry["use_summary"],
            use_book_json=entry.get("use_book_json", False),
            keep_combined=entry["keep_combined"],
            paper_format=args.paper_format,
            publish_dir=str(publish_dir_path),
            summary_mode=summary_mode,
            summary_order_manifest=summary_manifest_path,
            summary_manual_marker=summary_manual_marker,
            summary_appendices_last=_as_bool(entry.get("summary_appendices_last")),
        )
        if ok:
            built.append(str((publish_dir_path / out).resolve()))
            # Reset publish-Flag (D) – nur bei Erfolg und wenn reset_build_flag true ist
            if entry.get("reset_build_flag", False):
                reset_tool = args.reset_script
                if os.path.exists(reset_tool):
                    try:
                        _run(
                            [
                                sys.executable or "python",
                                reset_tool,
                                "--path",
                                str(path),
                                "--multi",
                            ],
                            check=True,
                        )
                    except Exception as e:
                        logger.warning(
                            "Konnte reset-publish-flag nicht aufrufen: %s", e
                        )
                else:
                    # Fallback: direkt im Manifest auf false setzen
                    try:
                        data = _load_yaml(manifest)
                        for e in data.get("publish", []):
                            if str(e.get("path")) == original_path:
                                e["build"] = False
                        _save_yaml(manifest, data)
                    except Exception as e:
                        logger.warning(
                            "Konnte Manifest-Fallback-Reset nicht schreiben: %s", e
                        )
        else:
            failed.append(
                str((publish_dir_path / out).resolve()) + (f": {msg}" if msg else "")
            )

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
