#!/usr/bin/env python3
"""Scan Markdown and PDFs for layout risks before release builds.

The Markdown checks are heuristic and source-oriented. The PDF checks use
Poppler's `pdftotext -bbox-layout` output and can flag rendered text blocks or
lines that extend beyond the page width.
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ALLOWED_SUFFIXES = {".md", ".markdown"}
TABLE_SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
RAW_URL_RE = re.compile(r"https?://[^\s<>()\]]+", re.IGNORECASE)
LONG_TOKEN_RE = re.compile(r"\S{80,}")


@dataclass(frozen=True)
class Finding:
    source: str
    path: Path
    line_number: int | None
    level: str
    kind: str
    message: str
    text: str


def display_path(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def iter_markdown_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file()
                and child.suffix.lower() in ALLOWED_SUFFIXES
                and ".git" not in child.parts
                and "__pycache__" not in child.parts
            )
        elif path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES:
            files.append(path)
    return sorted(dict.fromkeys(files))


def read_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig").splitlines()


def split_table_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if "|" not in stripped:
        return None
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells = [cell.strip() for cell in stripped.split("|")]
    if not cells or any(not cell for cell in cells):
        return None
    return cells


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    if cells is None:
        return False
    return all(
        TABLE_SEPARATOR_CELL_RE.fullmatch(cell.replace(" ", "")) for cell in cells
    )


def normalize_separator_cell(cell: str) -> str:
    compact = cell.strip().replace(" ", "")
    left = compact.startswith(":")
    right = compact.endswith(":")
    dashes = "----"
    if left and right:
        return f":{dashes}:"
    if left:
        return f":{dashes}"
    if right:
        return f"{dashes}:"
    return dashes


def normalize_table_separator(line: str) -> str:
    cells = split_table_row(line)
    if cells is None:
        return line
    normalized = [normalize_separator_cell(cell) for cell in cells]
    return "| " + " | ".join(normalized) + " |"


def scan_markdown_file(
    path: Path,
    token_limit: int,
    code_limit: int,
    table_limit: int,
) -> list[Finding]:
    findings: list[Finding] = []
    lines = read_lines(path)
    in_fence = False
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if in_frontmatter:
            if index > 1 and stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue

        if is_table_separator(line) and line != normalize_table_separator(line):
            findings.append(
                Finding(
                    "markdown",
                    path,
                    index,
                    "fixable",
                    "table-separator-spacing",
                    "Markdown table separator should use spaced cells such as `| ---- |`.",
                    line.strip(),
                )
            )

        if in_fence and len(line) > code_limit:
            findings.append(
                Finding(
                    "markdown",
                    path,
                    index,
                    "review-medium",
                    "long-code-line",
                    f"Code/preformatted line is {len(line)} characters; it may overflow in PDF.",
                    line.strip(),
                )
            )
            continue

        if "|" in line and len(line) > table_limit:
            findings.append(
                Finding(
                    "markdown",
                    path,
                    index,
                    "review-medium",
                    "wide-table-row",
                    f"Table-like row is {len(line)} characters; consider prose, bullets, or shorter cells.",
                    line.strip(),
                )
            )

        visible_line = MARKDOWN_LINK_RE.sub(r"\1", line)

        for match in RAW_URL_RE.finditer(visible_line):
            if len(match.group(0)) > token_limit:
                findings.append(
                    Finding(
                        "markdown",
                        path,
                        index,
                        "review-medium",
                        "long-url",
                        f"Raw URL is {len(match.group(0))} characters; use Markdown link text or a source list.",
                        match.group(0),
                    )
                )

        without_urls = RAW_URL_RE.sub("", visible_line)
        for match in LONG_TOKEN_RE.finditer(without_urls):
            token = match.group(0)
            if len(token) > token_limit:
                findings.append(
                    Finding(
                        "markdown",
                        path,
                        index,
                        "review-low",
                        "long-unbreakable-token",
                        f"Unbreakable token is {len(token)} characters; it may overflow in PDF.",
                        token,
                    )
                )
    return findings


def fix_table_separators(files: list[Path]) -> int:
    changed = 0
    for path in files:
        lines = read_lines(path)
        new_lines: list[str] = []
        file_changed = False
        for line in lines:
            if is_table_separator(line):
                normalized = normalize_table_separator(line)
                if normalized != line:
                    line = normalized
                    file_changed = True
            new_lines.append(line)
        if file_changed:
            path.write_text("\n".join(new_lines) + "\n", encoding="utf-8", newline="\n")
            changed += 1
    return changed


def tag_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def attr_float(element: ET.Element, name: str, default: float = 0.0) -> float:
    value = element.attrib.get(name)
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return default


def element_text(element: ET.Element, max_chars: int = 160) -> str:
    text = " ".join("".join(element.itertext()).split())
    text = html.unescape(text)
    if len(text) > max_chars:
        return text[: max_chars - 1] + "..."
    return text


def run_pdftotext_bbox(
    pdf: Path, first_page: int | None, last_page: int | None
) -> Path:
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    temp_path = Path(temp.name)
    temp.close()
    command = ["pdftotext", "-bbox-layout"]
    if first_page is not None:
        command.extend(["-f", str(first_page)])
    if last_page is not None:
        command.extend(["-l", str(last_page)])
    command.extend([str(pdf), str(temp_path)])
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return temp_path


def scan_pdf(
    pdf: Path,
    right_margin: float,
    first_page: int | None,
    last_page: int | None,
    max_pdf_findings: int,
) -> list[Finding]:
    findings: list[Finding] = []
    bbox_path = run_pdftotext_bbox(pdf, first_page, last_page)
    current_page = 0
    page_width = 0.0
    try:
        for event, element in ET.iterparse(bbox_path, events=("start", "end")):
            name = tag_name(element)
            if event == "start" and name == "page":
                current_page += 1
                page_width = attr_float(element, "width")
                continue
            if event != "end" or name not in {"line", "block"}:
                continue
            x_max = attr_float(element, "xMax")
            limit = page_width - right_margin
            if page_width and x_max > limit:
                overflow = x_max - limit
                findings.append(
                    Finding(
                        "pdf",
                        pdf,
                        current_page,
                        "review-high" if x_max > page_width else "review-medium",
                        f"pdf-{name}-right-overflow",
                        f"Rendered {name} extends {overflow:.1f} pt beyond the right review limit ({limit:.1f} pt).",
                        element_text(element),
                    )
                )
                if len(findings) >= max_pdf_findings:
                    break
            element.clear()
    finally:
        try:
            bbox_path.unlink()
        except OSError:
            pass
    return findings


def markdown_report(findings: list[Finding], root: Path, changed_files: int) -> str:
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.kind] = counts.get(finding.kind, 0) + 1

    lines = [
        "# Markdown/PDF Layout Scan Report",
        "",
        "This report is a heuristic release aid. Markdown findings identify source risks; PDF findings identify rendered bounding boxes that need visual review.",
        "",
        "## Summary",
        "",
        f"- Findings: {len(findings)}",
        f"- Files changed by table fixer: {changed_files}",
    ]
    for kind in sorted(counts):
        lines.append(f"- {kind}: {counts[kind]}")
    lines.extend(["", "## Findings", ""])

    if not findings:
        lines.extend(["No layout findings.", ""])
        return "\n".join(lines)

    lines.append("| Source | Level | Kind | File/PDF | Line/Page | Message | Text |")
    lines.append("| ---- | ---- | ---- | ---- | ----: | ---- | ---- |")
    for finding in findings:
        location = "" if finding.line_number is None else str(finding.line_number)
        path_text = display_path(finding.path, root)
        text = finding.text.replace("|", "\\|")
        message = finding.message.replace("|", "\\|")
        lines.append(
            f"| {finding.source} | {finding.level} | {finding.kind} | `{path_text}` | {location} | {message} | {text} |"
        )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan Markdown table formatting and PDF layout overflow risks.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["de/content", "en/content"],
        help="Markdown files/directories to scan. Defaults to de/content and en/content.",
    )
    parser.add_argument(
        "--root", default=".", help="Repository root for relative report paths."
    )
    parser.add_argument(
        "--fix-tables",
        action="store_true",
        help="Rewrite Markdown table separator rows to `| ---- |` style.",
    )
    parser.add_argument(
        "--pdf",
        action="append",
        default=[],
        help="PDF file to scan with pdftotext -bbox-layout. Can be used more than once.",
    )
    parser.add_argument(
        "--pdf-first-page", type=int, help="First PDF page to scan, for spot checks."
    )
    parser.add_argument(
        "--pdf-last-page", type=int, help="Last PDF page to scan, for spot checks."
    )
    parser.add_argument(
        "--pdf-right-margin",
        type=float,
        default=36.0,
        help="Right-side review margin in PDF points. Default: 36.",
    )
    parser.add_argument(
        "--max-pdf-findings",
        type=int,
        default=200,
        help="Maximum PDF findings per PDF. Default: 200.",
    )
    parser.add_argument(
        "--token-limit",
        type=int,
        default=80,
        help="Maximum unbreakable token length before review. Default: 80.",
    )
    parser.add_argument(
        "--code-line-limit",
        type=int,
        default=100,
        help="Maximum fenced code line length before review. Default: 100.",
    )
    parser.add_argument(
        "--table-line-limit",
        type=int,
        default=160,
        help="Maximum table-like row length before review. Default: 160.",
    )
    parser.add_argument("--output", help="Optional Markdown report path.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 2 when findings remain after optional fixes.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    markdown_paths = [Path(path) for path in args.paths]
    files = iter_markdown_files(markdown_paths)
    changed_files = fix_table_separators(files) if args.fix_tables else 0

    findings: list[Finding] = []
    for file_path in files:
        findings.extend(
            scan_markdown_file(
                file_path,
                token_limit=args.token_limit,
                code_limit=args.code_line_limit,
                table_limit=args.table_line_limit,
            )
        )

    for pdf_arg in args.pdf:
        pdf_path = Path(pdf_arg)
        if not pdf_path.exists():
            findings.append(
                Finding(
                    "pdf",
                    pdf_path,
                    None,
                    "error",
                    "pdf-missing",
                    "PDF file does not exist.",
                    "",
                )
            )
            continue
        try:
            findings.extend(
                scan_pdf(
                    pdf_path,
                    right_margin=args.pdf_right_margin,
                    first_page=args.pdf_first_page,
                    last_page=args.pdf_last_page,
                    max_pdf_findings=args.max_pdf_findings,
                )
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as exc:
            findings.append(
                Finding(
                    "pdf",
                    pdf_path,
                    None,
                    "error",
                    "pdf-scan-failed",
                    "Could not run pdftotext -bbox-layout.",
                    str(exc),
                )
            )

    report = markdown_report(findings, root, changed_files)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(report)

    if args.strict and findings:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
