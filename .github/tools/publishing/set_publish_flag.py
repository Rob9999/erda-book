#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setzt in publish.yaml/yml das build-Flag auf true, wenn der Commit relevante Pfade geändert hat.
Optional: setzt alle anderen Einträge auf false (--reset-others).
Nutzung:
  python .github/tools/publishing/set_publish_flag.py --commit <SHA> [--base <BASE_SHA>] [--branch <name>] [--reset-others] [--dry-run]

Typische Aufrufe in GitHub Actions:
  # Push: vergleiche "before" und "after"
  python .github/tools/publishing/set_publish_flag.py --commit "$GITHUB_SHA" --base "${{ github.event.before }}" --reset-others

  # PR: vergleiche Base- und Head-SHA
  python .github/tools/publishing/set_publish_flag.py --commit "${{ github.event.pull_request.head.sha }}" --base "${{ github.event.pull_request.base.sha }}" --reset-others
"""
import argparse
import json
import logging
import os
import posixpath
import subprocess
import sys
from typing import Any, Dict, List, Tuple

from tools.logging_config import get_logger

logger = get_logger(__name__)

try:
    import yaml  # PyYAML
except ImportError:
    logger.error(
        "PyYAML nicht installiert. Bitte `pip install pyyaml` im Workflow ausführen."
    )
    sys.exit(2)


def run(cmd: List[str]) -> Tuple[int, str, str]:
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = p.communicate()
    return p.returncode, out, err


def find_publish_file(explicit: str = None) -> str:
    if explicit and os.path.isfile(explicit):
        return explicit
    for name in ("publish.yaml", "publish.yml"):
        candidate = os.path.join(os.getcwd(), name)
        if os.path.isfile(candidate):
            return candidate
    logger.error("publish.yaml oder publish.yml im Repo-Root nicht gefunden.")
    sys.exit(3)


def normalize_posix(path_str: str) -> str:
    # Git gibt immer forward slashes aus -> POSIX-Style beibehalten
    # Entferne führendes './' und normalisiere Mehrfach-Slashes.
    p = path_str.replace("\\", "/")
    p = p.lstrip("./")
    return posixpath.normpath(p)


def get_entry_type(entry: Dict[str, Any]) -> str:
    value = entry.get("source_type") or entry.get("type") or "auto"
    if isinstance(value, str):
        return value.strip().lower()
    return str(value).strip().lower()


def detect_repo_root(start_dir: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", start_dir, "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        )
        candidate = result.stdout.strip()
        return candidate or os.path.abspath(start_dir)
    except Exception:
        return os.path.abspath(start_dir)


def resolve_entry_path(entry_path: str, publish_dir: str, repo_root: str) -> str:
    full_entry_path = os.path.normpath(os.path.join(publish_dir, entry_path))
    try:
        rel_path = os.path.relpath(full_entry_path, repo_root)
    except ValueError:
        rel_path = full_entry_path
    return normalize_posix(rel_path)


def is_match(entry_path: str, entry_type: str, changed_file: str) -> bool:
    ep = normalize_posix(entry_path)
    cf = normalize_posix(changed_file)
    if entry_type == "folder":
        # Treffer, wenn Datei im Ordner (oder der Ordner selbst) liegt
        return cf == ep or cf.startswith(ep + "/")
    elif entry_type == "file":
        return cf == ep
    else:
        # "auto": heuristisch – Ordner wenn kein Punkt im letzten Segment und Pfad existiert/ist Dir,
        # sonst Datei. Fallback: Datei.
        last = posixpath.basename(ep)
        if os.path.isdir(ep) or (("." not in last) and not posixpath.splitext(last)[1]):
            return cf == ep or cf.startswith(ep + "/")
        return cf == ep


def git_changed_files(commit: str, base: str = None) -> List[str]:
    """Return the list of changed files between ``base`` and ``commit``.

    GitHub Actions checkouts often use ``fetch-depth=1`` which means the
    provided base revision might not exist locally. When that happens the
    initial ``git diff`` call fails with errors such as ``bad revision``.  In
    that case we fall back to analysing the single commit so that publishing
    decisions still work instead of aborting the workflow.
    """

    def _diff_tree_single(target_commit: str) -> Tuple[int, str, str]:
        return run(
            ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", target_commit]
        )

    if base:
        code, out, err = run(["git", "diff", "--name-only", base, commit])
        ctx = f"{base}..{commit}"
        if code != 0:
            lowered_error = err.lower()
            missing_base = any(
                token in lowered_error
                for token in (
                    "bad revision",
                    "unknown revision",
                    "ambiguous argument",
                    "not a valid object name",
                    "bad object",
                )
            )
            if missing_base:
                logger.warning(
                    "Konnte Basis-Commit %s nicht finden (fetch-depth?). Fallback auf Einzel-Commit.",
                    base,
                )
                code, out, err = _diff_tree_single(commit)
                ctx = commit
    else:
        # Einzel-Commit
        code, out, err = _diff_tree_single(commit)
        ctx = commit

    if code != 0:
        logger.error("Git-Aufruf fehlgeschlagen (%s): %s", ctx, err.strip())
        sys.exit(4)

    files = [normalize_posix(line) for line in out.splitlines() if line.strip()]
    return files


def load_publish(publish_path: str) -> Dict[str, Any]:
    with open(publish_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if "publish" not in data or not isinstance(data["publish"], list):
        logger.error(
            "Ungültiges publish.yaml-Format: Top-Level-Schlüssel 'publish' (Liste) fehlt."
        )
        sys.exit(5)
    return data


def save_publish(publish_path: str, data: Dict[str, Any]) -> None:
    # Hinweis: PyYAML formatiert neu; falls Format/Kommentare erhalten bleiben sollen -> ruamel.yaml verwenden.
    with open(publish_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def main():
    parser = argparse.ArgumentParser(
        description="Setzt build-Flags in publish.yaml basierend auf Git-Änderungen."
    )
    parser.add_argument(
        "--commit",
        default=os.getenv("GITHUB_SHA", "HEAD"),
        help="Ziel-Commit (default: GITHUB_SHA oder HEAD)",
    )
    parser.add_argument(
        "--base",
        help="Basis-Commit zum Vergleichen (z. B. github.event.before oder PR-Base-SHA)",
    )
    parser.add_argument("--branch", help="optionaler Branch-Name (nur Logging)")
    parser.add_argument(
        "--publish-file", help="Pfad zu publish.yaml/yml (default: Repo-Root)"
    )
    parser.add_argument(
        "--reset-others",
        action="store_true",
        help="Nicht betroffene Einträge explizit auf false setzen",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Nur anzeigen, keine Datei schreiben"
    )
    parser.add_argument("--debug", action="store_true", help="Debug-Ausgaben")
    args = parser.parse_args()

    publish_path = find_publish_file(args.publish_file)
    publish_dir = os.path.dirname(publish_path)
    repo_root = detect_repo_root(publish_dir)

    changed_files = git_changed_files(args.commit, args.base)
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Changed files (%d):", len(changed_files))
        for c in changed_files:
            logger.debug("  - %s", c)

    data = load_publish(publish_path)
    entries = data["publish"]

    touched_entries = []
    for idx, entry in enumerate(entries):
        ep = entry.get("path")
        etype = get_entry_type(entry)
        if not ep:
            logger.warning("publish[%d] ohne 'path' – übersprungen.", idx)
            continue

        resolved_ep = resolve_entry_path(ep, publish_dir, repo_root)
        hit = any(is_match(resolved_ep, etype, cf) for cf in changed_files)

        # Baue altes/newes Flag
        old_build = bool(entry.get("build", False))
        new_build = True if hit else (False if args.reset_others else old_build)

        if old_build != new_build:
            entry["build"] = new_build
            touched_entries.append(
                {"path": ep, "type": etype, "from": old_build, "to": new_build}
            )
        else:
            # Stelle sicher, dass build-Schlüssel existiert
            entry["build"] = new_build

    # Outputs (für GitHub Actions)
    outputs = {
        "changed_files": changed_files,
        "modified_entries": touched_entries,
        "any_build_true": any(e.get("build", False) for e in entries),
    }

    # Schreiben
    if args.dry_run:
        logger.info("[DRY-RUN] Änderungen würden geschrieben werden.")
    else:
        save_publish(publish_path, data)

    # Menschlich lesbares Log
    logger.info("publish file: %s", publish_path)
    logger.info(
        "commit: %s%s%s",
        args.commit,
        f" | base: {args.base}" if args.base else "",
        f" | branch: {args.branch}" if args.branch else "",
    )
    if touched_entries:
        logger.info("geänderte build-Flags:")
        for t in touched_entries:
            logger.info(
                "  - %s (%s): %s -> %s", t["path"], t["type"], t["from"], t["to"]
            )
    else:
        logger.info("keine build-Flag-Änderungen.")

    # Maschine-lesbar (JSON auf stdout ans Ende hängen, damit von anderen Steps geparst werden kann)
    logger.info("::group::set_publish_flag.outputs")
    logger.info(json.dumps(outputs, ensure_ascii=False))
    logger.info("::endgroup::")

    # Zusätzlich GitHub-Outputs schreiben, falls verfügbar
    gh_out = os.getenv("GITHUB_OUTPUT")
    if gh_out:
        try:
            with open(gh_out, "a", encoding="utf-8") as f:
                f.write(
                    f"changed_files={json.dumps(changed_files, ensure_ascii=False)}\n"
                )
                f.write(
                    f"modified_entries={json.dumps(touched_entries, ensure_ascii=False)}\n"
                )
                f.write(
                    f"any_build_true={'true' if outputs['any_build_true'] else 'false'}\n"
                )
        except Exception as e:
            logger.warning("Konnte GITHUB_OUTPUT nicht schreiben: %s", e)


if __name__ == "__main__":
    main()
