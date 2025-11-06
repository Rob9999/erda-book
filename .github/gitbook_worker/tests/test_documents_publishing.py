#!/usr/bin/env python3
import logging
import os
import pathlib
import shutil
import sys
from typing import Any, Dict, List

import pytest

# Import von der Root des .github-Pakets
from tools.publishing.publisher import (
    build_pdf,
    find_publish_manifest,
    get_publish_list,
    prepare_publishing,
)

from . import GH_TEST_LOGS_DIR, GH_TEST_OUTPUT_DIR

pytestmark = [
    pytest.mark.skipif(
        shutil.which("pandoc") is None or shutil.which("lualatex") is None,
        reason="pandoc or lualatex not installed",
    ),
    pytest.mark.slow,  # These tests take a very long time (275+ documents)
]


def collect_markdown_files(base_dir: pathlib.Path) -> List[Dict[str, Any]]:
    """Collect all markdown files from content directory and prepare publish entries."""
    entries = []
    documents_dir = base_dir / "content"

    if not documents_dir.exists():
        return entries

    for root, _, files in os.walk(documents_dir):
        root_path = pathlib.Path(root)
        for file in files:
            if file.lower().endswith((".md", ".markdown")):
                rel_path = root_path.relative_to(base_dir)
                file_path = root_path / file
                # Create output path maintaining directory structure
                out_path = rel_path / file.replace(".md", ".pdf").replace(
                    ".markdown", ".pdf"
                )

                entries.append(
                    {
                        "path": str(file_path),
                        "out": str(out_path),
                        "type": "file",
                        "use_summary": False,
                        "keep_combined": False,
                    }
                )

    return entries


def test_publish_all_documents(logger: logging.Logger):
    """Test publishing all documents from content directory to PDFs."""
    # Get repo root
    repo_root = pathlib.Path(__file__).resolve().parents[3]

    # Use test output directory instead of actual publish directory
    publish_dir = GH_TEST_OUTPUT_DIR / "publish-singles"

    # Ensure publish directory exists
    publish_dir.mkdir(parents=True, exist_ok=True)

    # Collect all markdown files
    publish_entries = collect_markdown_files(repo_root)
    assert publish_entries, "No markdown files found in content directory"
    # Sort entries by path length to process simpler documents first
    publish_entries.sort(key=lambda x: len(pathlib.Path(x["path"]).parts))
    # Build PDF
    _build_pdf(publish_entries, publish_dir, logger)


def test_publishing_using_publish_manifest(logger: logging.Logger):
    """Test publishing using a predefined publish manifest."""
    # Get repo root
    repo_root = pathlib.Path(__file__).resolve().parents[3]

    # Use test output directory instead of actual publish directory
    publish_dir = GH_TEST_OUTPUT_DIR / "publish-combined"

    # Ensure publish directory exists
    publish_dir.mkdir(parents=True, exist_ok=True)

    # Load publish manifest and get entries
    manifest = find_publish_manifest("publish.yml")
    targets = get_publish_list(manifest)
    assert targets, "Keine zu publizierenden Einträge (build: true)."
    # Add repo root to relative paths
    for entry in targets:
        entry_path = pathlib.Path(entry["path"])
        if not entry_path.is_absolute():
            entry["path"] = str(repo_root / entry["path"])
    # Build PDF
    _build_pdf(targets, publish_dir, logger)


def _build_pdf(
    publish_entries: List[Dict[str, Any]],
    publish_dir: pathlib.Path,
    logger: logging.Logger,
):

    # Create logs subdirectory for build logs only
    log_dir = GH_TEST_LOGS_DIR / publish_dir.name
    if log_dir.exists():
        shutil.rmtree(log_dir)  # Only clean the logs directory
    log_dir.mkdir(exist_ok=True)

    # Prepare the environment (pandoc, LaTeX, fonts, etc.)
    prepare_publishing(no_apt=True)  # Set no_apt=True since we're in Docker

    # Track results
    built: List[str] = []
    failed: List[Dict[str, str]] = []

    # Process each entry
    for i, entry in enumerate(publish_entries, 1):
        doc_name = pathlib.Path(entry["path"]).stem
        logger.info(
            "============================NEXT DOCUMENT================================"
        )
        logger.info(f"Processing document {i}/{len(publish_entries)}: {doc_name}")

        log_file = log_dir / f"{doc_name}_build.log"
        try:
            # Log the build attempt
            with open(log_file, "w", encoding="utf-8") as f:
                f.write(f"Building {entry['path']} -> {entry['out']}\n")

            success, msg = build_pdf(
                path=entry["path"],
                out=entry["out"],
                typ=entry["type"],
                use_summary=entry["use_summary"],
                keep_combined=entry["keep_combined"],
                publish_dir=str(publish_dir),
            )

            if success:
                built.append(entry["out"])
                logger.info(f"  ✓ Successfully built {doc_name}")
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write("\nBuild successful!\n")
            else:
                error_msg = "ERROR: " + (msg if msg else "Unknown error")
                failed.append(
                    {
                        "path": entry["path"],
                        "out": entry["out"],
                        "error": error_msg,
                        "log": str(log_file),
                    }
                )
                logger.info(f"  ✗ Failed to build {doc_name}: {error_msg}")
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"\nBuild failed: {error_msg}\n")

        except Exception as e:
            error_msg = str(e)
            failed.append(
                {
                    "path": entry["path"],
                    "out": entry["out"],
                    "error": error_msg,
                    "log": str(log_file),
                }
            )
            logger.info(
                f"  ✗ Error processing {doc_name}: {error_msg}", file=sys.stderr
            )
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"\nError occurred: {error_msg}\n")

        logger.info(
            "============================END DOCUMENT================================="
        )

    # Write detailed report
    report_file = publish_dir / "build_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"Build Report\n{'='*40}\n\n")
        f.write(f"Total documents: {len(publish_entries)}\n")
        f.write(f"Successfully built: {len(built)}\n")
        f.write(f"Failed: {len(failed)}\n\n")

        if built:
            f.write("\nSuccessful Builds:\n")
            for b in built:
                f.write(f"  ✓ {b}\n")

        if failed:
            f.write("\nFailed Builds:\n")
            for f_entry in failed:
                f.write(f"\n  ✗ {f_entry['path']}\n")
                f.write(f"    Output: {f_entry['out']}\n")
                f.write(f"    Error: {f_entry['error']}\n")
                f.write(f"    Log: {f_entry['log']}\n")

    # The test should fail if any documents failed to build
    if failed:
        print(f"\nDetailed build report written to: {report_file}")
        assert (
            False
        ), f"{len(failed)} documents failed to build. See {report_file} for details."
