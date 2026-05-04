#!/usr/bin/env python3
"""Scan Markdown content for legal-compliance wording that needs review.

The script is intentionally heuristic. It does not decide whether a passage is
legally correct; it finds places where editorial review should distinguish
between requirements/target architecture and already-certified compliance.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


LEGAL_TERMS = re.compile(
    r"\b(DSGVO|GDPR|Digital Services Act|DSA|eIDAS|EMRK|ECHR|Grundrechte|"
    r"fundamental rights?|Datenschutz|data protection|Plattformrecht|platform law|"
    r"rechtlich|legal|rechtsstaatlich|rule[- ]of[- ]law|privacy[- ]by[- ]design)\b",
    re.IGNORECASE,
)

ASSERTIVE_TERMS = re.compile(
    r"\b(rechtskonform|rechtssicher|konform|compliant|compliance|guarantee[sd]?|"
    r"garantier(?:t|en)|gewährleistet|certified|zertifiziert|legally checked|"
    r"rechtlich geprüft|fully compliant|vollständig konform)\b",
    re.IGNORECASE,
)

REQUIREMENT_TERMS = re.compile(
    r"\b(muss|müssen|soll|sollen|sollte|sollten|bedarf|benötigt|vor .*?Pilot|"
    r"zu prüfen|festzulegen|maßgeblich|Anforderung|Startbedingung|Zielrahmen|"
    r"must|should|requires?|required|requirement|before .*?pilot|to be defined|"
    r"needs? to|may|can|relevant|starting condition|framework|safeguards?)\b",
    re.IGNORECASE,
)

ALLOWED_SUFFIXES = {".md", ".markdown", ".txt"}


@dataclass(frozen=True)
class Finding:
    path: Path
    line_number: int
    level: str
    reason: str
    text: str


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file()
                and child.suffix.lower() in ALLOWED_SUFFIXES
                and not any(part.startswith(".") for part in child.parts)
            )
        elif path.is_file():
            files.append(path)
    return sorted(dict.fromkeys(files))


def classify(line: str) -> tuple[str, str] | None:
    if not LEGAL_TERMS.search(line):
        return None

    has_assertive = bool(ASSERTIVE_TERMS.search(line))
    has_requirement = bool(REQUIREMENT_TERMS.search(line))

    if has_assertive and not has_requirement:
        return "review-high", "assertive legal/compliance wording without an obvious requirement qualifier"
    if has_assertive and has_requirement:
        return "review-medium", "assertive wording appears in a requirement or target context"
    return "review-low", "legal framework reference"


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        lines = path.read_text(encoding="utf-8-sig").splitlines()

    in_frontmatter = bool(lines and lines[0].strip() == "---")
    for index, line in enumerate(lines, start=1):
        if in_frontmatter:
            if index > 1 and line.strip() == "---":
                in_frontmatter = False
            continue
        classification = classify(line)
        if classification is None:
            continue
        level, reason = classification
        findings.append(
            Finding(
                path=path,
                line_number=index,
                level=level,
                reason=reason,
                text=line.strip(),
            )
        )
    return findings


def markdown_report(findings: list[Finding], root: Path) -> str:
    counts: dict[str, int] = {"review-high": 0, "review-medium": 0, "review-low": 0}
    for finding in findings:
        counts[finding.level] = counts.get(finding.level, 0) + 1

    lines = [
        "# Legal Claims Scan Report",
        "",
        "This report is a heuristic editorial aid. It is not legal advice and does not certify legal compliance.",
        "",
        "## Summary",
        "",
        f"- Files with findings: {len({finding.path for finding in findings})}",
        f"- Total findings: {len(findings)}",
        f"- Review high: {counts.get('review-high', 0)}",
        f"- Review medium: {counts.get('review-medium', 0)}",
        f"- Review low: {counts.get('review-low', 0)}",
        "",
        "## Findings",
        "",
    ]

    if not findings:
        lines.append("No legal-compliance wording candidates found.")
        lines.append("")
        return "\n".join(lines)

    lines.append("| Level | File | Line | Reason | Text |")
    lines.append("|---|---|---:|---|---|")
    for finding in findings:
        try:
            display_path = finding.path.resolve().relative_to(root.resolve())
        except ValueError:
            display_path = finding.path
        text = finding.text.replace("|", "\\|")
        reason = finding.reason.replace("|", "\\|")
        lines.append(
            f"| {finding.level} | `{display_path.as_posix()}` | {finding.line_number} | {reason} | {text} |"
        )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find legal/compliance wording that needs editorial review.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["de/content", "en/content"],
        help="Files or directories to scan. Defaults to de/content and en/content.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root used for relative paths in reports.",
    )
    parser.add_argument(
        "--output",
        help="Optional Markdown report path.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 2 when review-high findings are present.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    paths = [Path(path) for path in args.paths]
    files = iter_files(paths)
    findings = [finding for file_path in files for finding in scan_file(file_path)]
    report = markdown_report(findings, root)

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8", newline="\n")
    else:
        sys.stdout.write(report)

    if args.strict and any(finding.level == "review-high" for finding in findings):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))