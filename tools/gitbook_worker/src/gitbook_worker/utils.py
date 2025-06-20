import os
import re
import subprocess
import sys
import logging
from typing import List

try:
    import textstat
except ImportError:  # pragma: no cover - optional dep
    textstat = None

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def run(cmd, cwd=None, capture_output=False):
    """Execute a shell command. Exit on failure or return output."""
    logging.info("Running command: %s", cmd)
    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=True,
        stdout=subprocess.PIPE if capture_output else None,
        stderr=subprocess.PIPE if capture_output else None,
        text=True,
    )
    if capture_output:
        return result.stdout, result.stderr, result.returncode
    if result.returncode != 0:
        logging.error("Command failed (%s): %s", result.returncode, cmd)
        sys.exit(result.returncode)


def parse_summary(summary_path):
    """Parse SUMMARY.md to get an ordered list of markdown file paths."""
    files = []
    base = os.path.dirname(summary_path)
    try:
        with open(summary_path, encoding="utf-8") as f:
            for line in f:
                match = re.match(r"\s*\*+\s*\[.*\]\(([^)]+\.md)\)", line)
                if match:
                    files.append(os.path.join(base, match.group(1)))
    except Exception as e:
        logging.error("Failed to read SUMMARY.md: %s", e)
        sys.exit(1)
    return files


def readability_report(md_files):
    """Compute readability scores for each markdown file."""
    report = []
    if not textstat:
        logging.warning("textstat not installed; skipping readability checks.")
        return report
    for md in md_files:
        try:
            with open(md, encoding="utf-8") as f:
                text = f.read()
            fre = textstat.flesch_reading_ease(text)
            fk = textstat.flesch_kincaid_grade(text)
            report.append((md, fre, fk))
        except Exception as e:
            logging.warning("Readability check failed for %s: %s", md, e)
    return report


def wrap_wide_tables(md_file: str, threshold: int = 6) -> None:
    """Wrap wide markdown tables in a fenced ``Div`` with class ``landscape``.

    Consecutive lines starting with a pipe character are considered part of a
    table. If the table contains more columns than ``threshold`` it is wrapped
    inside ``::: {.landscape}`` and ``:::` markers. A Pandoc Lua filter can
    later convert this ``Div`` into the appropriate LaTeX ``landscape``
    environment. The file is modified in place.
    """

    try:
        with open(md_file, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to read %s: %s", md_file, e)
        raise

    new_lines: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("|"):
            table = []
            max_cols = line.count("|") - 1
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table.append(lines[i])
                max_cols = max(max_cols, lines[i].count("|") - 1)
                i += 1
            if max_cols > threshold:
                new_lines.append("::: {.landscape}\n")
                new_lines.extend(table)
                new_lines.append(":::\n")
            else:
                new_lines.extend(table)
        else:
            new_lines.append(line)
            i += 1

    try:
        with open(md_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to write %s: %s", md_file, e)
        raise


def validate_table_columns(md_file: str) -> List[str]:
    """Return a list of errors for tables with inconsistent column counts."""

    try:
        with open(md_file, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to read %s: %s", md_file, e)
        raise

    errors: List[str] = []
    ref_cols = 0
    in_table = False
    for idx, line in enumerate(lines, start=1):
        if line.lstrip().startswith("|"):
            cols = line.count("|") - 1
            if not in_table:
                in_table = True
                ref_cols = cols
            if cols != ref_cols:
                errors.append(
                    f"Line {idx}: has {cols} columns (expected {ref_cols})"
                )
        else:
            in_table = False
            ref_cols = 0

    return errors
