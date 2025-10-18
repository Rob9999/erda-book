"""Utilities for maintaining GitBook compatible structures.

This module exposes two commands used by the ``gitbook-style`` GitHub Action:

``rename``
    Normalises file and directory names to the GitBook style by converting them
    to lower case and replacing whitespace with ``-``. Renaming happens via
    ``git mv`` when possible to preserve history, with a graceful fallback to a
    standard filesystem rename when the repository context is unavailable.

``summary``
    Regenerates ``SUMMARY.md`` based on ``book.json`` configuration. The
    resulting structure mirrors the inline Python that historically lived inside
    the workflow definition, but it is now testable and reusable.

The functions contain the actual logic so that unit tests can exercise the
behaviour without shelling out to Git. The command-line interface is a thin
wrapper around those functions.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List
from tools.logging_config import get_logger

SKIP_DIRS: set[str] = {
    ".git",
    ".github",
    "node_modules",
    "__pycache__",
    ".venv",
    "simulations",
}
MD_EXTENSIONS: set[str] = {".md"}
logger = get_logger(__name__)


def _normalise_name(name: str) -> str:
    """Convert ``name`` to the canonical GitBook style."""

    cleaned = re.sub(r"[^a-z0-9.-]+", "-", name.lower()).strip("-")
    return cleaned or name


def _remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def safe_git_mv(src: Path, dst: Path, *, use_git: bool = True) -> None:
    """Move ``src`` to ``dst`` preserving Git history when possible."""

    if src == dst:
        return

    dst.parent.mkdir(parents=True, exist_ok=True)

    if dst.exists() and src.resolve() != dst.resolve():
        if use_git:
            subprocess.run(
                ["git", "rm", "-r", "--cached", str(dst)],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        if dst.exists():
            _remove_path(dst)

    if use_git:
        result = subprocess.run(["git", "mv", str(src), str(dst)], check=False)
        if result.returncode == 0:
            return

    src.rename(dst)


def rename_to_gitbook_style(root: Path, *, use_git: bool = True) -> None:
    """Rename files and directories below ``root`` to match GitBook style."""

    logger.info(f"Renaming files in {root} to GitBook style")
    for current_root, dirs, files in os.walk(root, topdown=True):
        current_path = Path(current_root)
        rel = current_path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            dirs[:] = []
            continue

        for index, directory in enumerate(list(dirs)):
            try:
                logger.debug(f"Processing directory: '{directory}'")
                if directory in SKIP_DIRS or directory.startswith(".git"):
                    dirs.remove(directory)
                    logger.debug(f"Skipping directory: '{directory}'")
                    continue

                new_name = _normalise_name(directory)
                if new_name != directory:
                    src = current_path / directory
                    dst = current_path / new_name
                    safe_git_mv(src, dst, use_git=use_git)
                    logger.info(f"Renamed directory: '{src}' to '{dst}'")
                    dirs[index] = new_name
            except Exception as ex:  # pragma: no cover - best effort
                logger.warning(f"Failed to rename directory '{directory}': {ex}")
                dirs.remove(directory)

        for file_name in files:
            try:
                logger.debug(f"Processing file: '{file_name}'")
                if file_name.startswith(".") or file_name.endswith(".py"):
                    logger.debug(f"Skipping file: '{file_name}'")
                    continue
                new_name = _normalise_name(file_name)
                if new_name != file_name:
                    src = current_path / file_name
                    dst = current_path / new_name
                    safe_git_mv(src, dst, use_git=use_git)
                    logger.info(f"Renamed file: '{src}' to '{dst}'")
            except Exception as ex:  # pragma: no cover - best effort
                logger.warning(f"Failed to rename file '{file_name}': {ex}")
    logger.info("Renaming complete")


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _first_heading(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return re.sub(r"^#+\s*", "", stripped).strip()
    return None


def _title_from_filename(path: Path) -> str:
    name = re.sub(r"[-_]+", " ", path.stem)
    name = re.sub(r"\s+", " ", name).strip()
    return name.title() if name else path.stem


def _natural_key(value: str) -> List[int | str]:
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", value)
    ]


@dataclass(frozen=True)
class SummaryContext:
    base_dir: Path
    root_dir: Path
    summary_path: Path


def _find_book_base(base_dir: Path) -> Path | None:
    """Locate the directory containing ``book.json`` starting from ``base_dir``.

    The search walks up the directory tree so tools can run inside nested
    folders while still re-using the repository level metadata.
    """

    for candidate in [base_dir, *base_dir.parents]:
        if (candidate / "book.json").exists():
            return candidate
    return None


def _build_summary_context(base_dir: Path) -> SummaryContext:
    base_dir = base_dir.resolve()
    book_base = _find_book_base(base_dir) or base_dir
    book_path = book_base / "book.json"
    book = read_json(book_path) if book_path.exists() else {}
    root_dir = (book_base / book.get("root", ".")).resolve()
    structure = book.get("structure") or {}
    summary_rel = structure.get("summary")

    if not summary_rel:
        for candidate in ("SUMMARY.md", "summary.md"):
            if (root_dir / candidate).exists():
                summary_rel = candidate
                break
        else:
            summary_rel = "SUMMARY.md"

    summary_path = (root_dir / summary_rel).resolve()
    return SummaryContext(
        base_dir=book_base, root_dir=root_dir, summary_path=summary_path
    )


def get_summary_layout(base_dir: Path) -> SummaryContext:
    """Return the resolved GitBook summary layout for ``base_dir``."""

    return _build_summary_context(base_dir)


def _md_files_in_dir(directory: Path, summary_path: Path) -> List[Path]:
    files = [
        p
        for p in directory.iterdir()
        if p.is_file() and p.suffix.lower() in MD_EXTENSIONS
    ]
    files = [p for p in files if p.resolve() != summary_path.resolve()]
    readme_files = [p for p in files if p.name.lower() == "readme.md"]
    other_files = sorted(
        (p for p in files if p.name.lower() != "readme.md"),
        key=lambda p: _natural_key(p.name),
    )
    return readme_files + other_files


def _child_dirs(directory: Path) -> List[Path]:
    dirs = [p for p in directory.iterdir() if p.is_dir()]
    dirs = [p for p in dirs if p.name not in SKIP_DIRS and not p.name.startswith(".")]
    return sorted(dirs, key=lambda p: _natural_key(p.name))


def _relative_link(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def _make_item_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        text = ""
    heading = _first_heading(text) or _title_from_filename(path)
    return heading.replace("[", "(").replace("]", ")")


def build_summary_lines(context: SummaryContext) -> List[str]:
    lines = ["# Summary", ""]

    def emit_directory(directory: Path, level: int) -> None:
        files = _md_files_in_dir(directory, context.summary_path)
        readme = next((p for p in files if p.name.lower() == "readme.md"), None)

        if directory != context.root_dir:
            title = directory.name
            title = re.sub(r"[-_]+", " ", title).strip().title()
            if readme is not None:
                title = _make_item_title(readme)
                if title.lower() == "readme":
                    title = _title_from_filename(directory)
                lines.append(
                    "  " * level
                    + f"* [{title}]({_relative_link(readme, context.root_dir)})"
                )
            else:
                lines.append("  " * level + f"* {title}")

        for file_path in files:
            if file_path.name.lower() == "readme.md" and directory != context.root_dir:
                continue
            if directory == context.root_dir and file_path.name.lower() == "readme.md":
                lines.append(
                    "  " * level
                    + f"* [{_make_item_title(file_path)}]({_relative_link(file_path, context.root_dir)})"
                )
            elif file_path.name.lower() != "readme.md":
                indent = level if directory == context.root_dir else level + 1
                lines.append(
                    "  " * indent
                    + f"* [{_make_item_title(file_path)}]({_relative_link(file_path, context.root_dir)})"
                )

        for child in _child_dirs(directory):
            emit_directory(child, level if directory == context.root_dir else level + 1)

    top_files = _md_files_in_dir(context.root_dir, context.summary_path)
    top_readme = [p for p in top_files if p.name.lower() == "readme.md"]
    top_others = [p for p in top_files if p.name.lower() != "readme.md"]

    for file_path in top_readme:
        lines.append(
            f"* [{_make_item_title(file_path)}]({_relative_link(file_path, context.root_dir)})"
        )

    for file_path in top_others:
        lines.append(
            f"* [{_make_item_title(file_path)}]({_relative_link(file_path, context.root_dir)})"
        )

    for child in _child_dirs(context.root_dir):
        emit_directory(child, level=0)

    return lines


def ensure_clean_summary(base_dir: Path, *, run_git: bool = True) -> bool:
    """Regenerate SUMMARY.md from book.json structure.
    Returns True if the file was changed.
    """
    logger.info(f"Ensuring clean SUMMARY.md in {base_dir}")
    context = get_summary_layout(base_dir)
    new_content = "\n".join(build_summary_lines(context)).rstrip() + "\n"
    context.summary_path.parent.mkdir(parents=True, exist_ok=True)
    old_content = ""
    if context.summary_path.exists():
        try:
            old_content = context.summary_path.read_text(encoding="utf-8")
        except Exception:
            old_content = ""

    if old_content == new_content:
        logger.info(f"No changes to {context.summary_path}")
        return False

    context.summary_path.write_text(new_content, encoding="utf-8")
    if run_git:
        subprocess.run(["git", "add", str(context.summary_path)], check=False)
    logger.info(f"Updated {context.summary_path}")
    return True


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GitBook style utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    rename_parser = subparsers.add_parser(
        "rename", help="Rename files to GitBook style"
    )
    rename_parser.add_argument(
        "--root", type=Path, default=Path("."), help="Directory to process"
    )
    rename_parser.add_argument(
        "--no-git", action="store_true", help="Disable git integration (for tests)"
    )

    summary_parser = subparsers.add_parser(
        "summary", help="Ensure SUMMARY.md matches book.json"
    )
    summary_parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Base directory containing book.json",
    )
    summary_parser.add_argument(
        "--no-git", action="store_true", help="Do not stage files with git"
    )

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    logger.info(f"GitBook style utility (args={argv})")
    args = parse_args(argv)

    if args.command == "rename":
        rename_to_gitbook_style(args.root.resolve(), use_git=not args.no_git)
        return 0

    if args.command == "summary":
        changed = ensure_clean_summary(args.root.resolve(), run_git=not args.no_git)
        print("SUMMARY.MD UPDATED" if changed else "SUMMARY.MD OK")
        return 0

    raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
