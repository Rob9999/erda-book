#!/usr/bin/env python3
"""Check external links in files named *staatenprofil*.md."""

import argparse
import csv
import os
import re
import requests
import logging
from typing import Iterable, List

logger = logging.getLogger(__name__)


LINK_PATTERN = re.compile(r"\[.*?\]\((https?://[^)]+)\)")


def iter_staatenprofil_files(root: str) -> Iterable[str]:
    """Yield paths of markdown files containing 'staatenprofil' in the name."""
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".md") and "staatenprofil" in name:
                yield os.path.join(dirpath, name)


def check_links(files: Iterable[str]) -> List[List[str]]:
    """Return rows describing broken links."""
    broken: List[List[str]] = []
    for md in files:
        with open(md, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                for url in LINK_PATTERN.findall(line):
                    try:
                        resp = requests.head(url, allow_redirects=True, timeout=5)
                        if resp.status_code >= 400:
                            broken.append([
                                md,
                                str(lineno),
                                url,
                                str(resp.status_code),
                                resp.reason,
                            ])
                    except Exception as e:  # network failure or similar
                        broken.append([md, str(lineno), url, "ERR", str(e)])
    return broken


def write_report(rows: List[List[str]], output: str) -> None:
    with open(output, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File", "Line", "URL", "Status", "Error"])
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Check links in staatenprofil markdown files")
    parser.add_argument("--root", default=".", help="Root directory to search")
    parser.add_argument(
        "--output", default="staatenprofil_link_report.csv", help="Output CSV filename"
    )
    args = parser.parse_args()

    files = list(iter_staatenprofil_files(args.root))
    if not files:
        logger.info("No staatenprofil markdown files found.")
        return

    rows = check_links(files)
    write_report(rows, args.output)
    logger.info(
        "Report written to %s. %d problem links found.", args.output, len(rows)
    )


if __name__ == "__main__":
    main()
