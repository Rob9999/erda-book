#!/usr/bin/env python3
"""Prepare Markdown files for local LanguageTool checks.

The exporter keeps line numbers stable by replacing ignored Markdown regions with
blank lines instead of deleting them. This makes LanguageTool line references
usable against the original source files while avoiding front matter, tables,
code fences, HTML tags, and link targets that otherwise dominate the report.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path

FENCE_RE = re.compile(r"^\s*(```|~~~)")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
RAW_URL_RE = re.compile(r"https?://\S+")
HTML_TAG_RE = re.compile(r"<[^>]+>")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")


def clean_line(line: str, *, in_front_matter: bool, in_fence: bool) -> str:
    if in_front_matter or in_fence:
        return "\n"

    stripped = line.lstrip()
    if stripped.startswith("|") or TABLE_SEPARATOR_RE.match(line):
        return "\n"

    cleaned = html.unescape(line)
    cleaned = LINK_RE.sub(lambda match: match.group(1), cleaned)
    cleaned = RAW_URL_RE.sub("", cleaned)
    cleaned = HTML_TAG_RE.sub("", cleaned)
    cleaned = cleaned.replace("✅", "")
    cleaned = cleaned.replace("❌", "")
    cleaned = cleaned.replace("⚠️", "")
    cleaned = cleaned.replace("📌", "")
    cleaned = cleaned.replace("🧠", "")
    cleaned = cleaned.replace("🎛️", "")
    cleaned = cleaned.replace("🌍", "")
    cleaned = cleaned.replace("❓", "")
    cleaned = cleaned.replace("🪄", "")
    cleaned = cleaned.replace("💡", "")
    return cleaned


def convert_file(source: Path, destination: Path) -> None:
    text = source.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines(keepends=True)

    in_front_matter = bool(lines and lines[0].strip() == "---")
    front_matter_open = in_front_matter
    in_fence = False
    output: list[str] = []

    for index, line in enumerate(lines):
        if front_matter_open:
            output.append("\n")
            if index > 0 and line.strip() == "---":
                front_matter_open = False
                in_front_matter = False
            continue

        if FENCE_RE.match(line):
            in_fence = not in_fence
            output.append("\n")
            continue

        output.append(
            clean_line(line, in_front_matter=in_front_matter, in_fence=in_fence)
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("".join(output), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare Markdown files for LanguageTool."
    )
    parser.add_argument("roots", nargs="+", type=Path, help="Markdown roots to export")
    parser.add_argument("--output", required=True, type=Path, help="Output directory")
    parser.add_argument(
        "--clean", action="store_true", help="Delete the output directory first"
    )
    args = parser.parse_args()

    output_root = args.output
    if args.clean and output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    manifest_lines = ["source\tprepared\n"]
    for root in args.roots:
        root = root.resolve()
        for source in sorted(root.rglob("*.md")):
            relative = source.relative_to(root)
            destination = output_root / root.name / relative
            convert_file(source, destination)
            manifest_lines.append(f"{source.as_posix()}\t{destination.as_posix()}\n")

    (output_root / "manifest.tsv").write_text("".join(manifest_lines), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
