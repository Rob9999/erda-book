import sys
import argparse
import io
import os
import logging
from datetime import datetime
from .utils import run, parse_summary, readability_report, wrap_wide_tables
from .linkcheck import (
    check_links,
    check_images,
    check_duplicate_headings,
    check_citation_numbering,
    list_todos,
)
from .source_extract import extract_sources
from .ai_tools import (
    proof_and_repair_internal_references,
    proof_and_repair_external_references,
)
from .repo import clone_or_update_repo
from . import lint_markdown, validate_metadata, spellcheck


def main():

    parser = argparse.ArgumentParser(
        description="Works on a GITBook; e.g. builds a PDF and or runs quality checks"
    )
    parser.add_argument("repo_url", help="URL of the Git repository")
    parser.add_argument(
        "--branch",
        type=str,
        default="published",
        help="Branch of the Git repository",
    )
    parser.add_argument(
        "--pdf",
        type=str,
        default="",
        help="Export a pdf. (Path File) name for the output PDF.",
    )
    parser.add_argument(
        "-o",
        "--out-dir",
        type=str,
        default=".",
        help="Output directory to place all generated documents, lists, etc - except temp files.",
    )
    parser.add_argument(
        "-c",
        "--clone-dir",
        type=str,
        default="gitbook_repo",
        help="Directory to clone the repository into.",
    )
    parser.add_argument(
        "-q",
        "--temp-dir",
        type=str,
        default="temp",
        help="Directory to place all temp results into.",
    )
    parser.add_argument(
        "--wrap-wide-tables",
        action="store_true",
        help="Wrap tables wider than a threshold in a landscape environment.",
    )
    parser.add_argument(
        "--table-threshold",
        type=int,
        default=6,
        help="Number of columns considered wide for --wrap-wide-tables.",
    )
    parser.add_argument(
        "-s", "--export-sources", action="store_true", help="Export sources to CSV."
    )
    parser.add_argument(
        "-l", "--check-links", action="store_true", help="Check for broken HTTP links."
    )
    parser.add_argument(
        "-m", "--markdownlint", action="store_true", help="Run markdownlint."
    )
    parser.add_argument(
        "-i", "--check-images", action="store_true", help="Verify image references."
    )
    parser.add_argument(
        "-r", "--readability", action="store_true", help="Generate readability report."
    )
    parser.add_argument(
        "-d", "--metadata", action="store_true", help="Validate YAML metadata."
    )
    parser.add_argument(
        "-u",
        "--duplicate-headings",
        action="store_true",
        help="Find duplicate headings.",
    )
    parser.add_argument(
        "-a", "--citations", action="store_true", help="Check citation numbering."
    )
    parser.add_argument(
        "-t", "--todos", action="store_true", help="List TODO/FIXME items."
    )
    parser.add_argument(
        "-p", "--spellcheck", action="store_true", help="Run spellchecker."
    )
    parser.add_argument(
        "--fix-internal-links",
        action="store_true",
        help="Proof and repair internal GitBook links using Summary.md and generate a report.",
    )
    parser.add_argument(
        "--ai-url",
        type=str,
        default="https://api.openai.com/v1/chat/completions",
        help="URL of the AI API endpoint (default: OpenAI).",
    )
    parser.add_argument(
        "--ai-api-key",
        type=str,
        default="",
        help="API key for the AI service (required for OpenAI and GenAI).",
    )
    parser.add_argument(
        "--ai-provider",
        type=str,
        default="genai",
        help="AI provider (default: OpenAI). Options: 'openai', 'genai'.",
    )
    parser.add_argument(
        "--ai-prompt-reference",
        type=str,
        default="Proof and repair the reference",
        help="Prompt for the AI service (default: 'Proof and repair the reference').",
    )
    parser.add_argument(
        "--fix-external-references",
        action="store_true",
        help="Proof and repair external references using AI.",
    )

    try:
        args = parser.parse_args()
    except SystemExit as e:
        if e.code == 2:  # Exit code 2 indicates an argument parsing error
            error_output = io.StringIO()
            parser.print_usage(file=error_output)  # Kurze Usage-Nachricht
            parser.print_help(file=error_output)  # Detaillierte Hilfe
            error_message = error_output.getvalue()
            error_output.close()
            print("\nError: Invalid or missing arguments.\n")
            print("Details:")
            print(error_message)  # Zeige die vollständige Fehlermeldung an
        sys.exit(e.code)

    # Get the current working directory
    current_dir = os.getcwd()

    # Create out directory if it doesn't exist
    out_dir = args.out_dir
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)
    out_dir = os.path.abspath(out_dir)

    # Create temp directory if it doesn't exist
    temp_dir = args.temp_dir
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    temp_dir = os.path.abspath(temp_dir)

    # Clone or update repository
    clone_dir = args.clone_dir  # resolve path
    clone_dir = os.path.abspath(clone_dir)
    clone_or_update_repo(args.repo_url, clone_dir, branch_name=args.branch)

    # Parse SUMMARY.md
    summary_path = os.path.join(clone_dir, "SUMMARY.md")
    if not os.path.isfile(summary_path):
        logging.error("SUMMARY.md not found in %s", clone_dir)
        sys.exit(1)
    md_files = parse_summary(summary_path)
    if not md_files:
        logging.error("No markdown files listed in SUMMARY.md")
        sys.exit(1)

    # Combine markdown into one file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    combined_md = os.path.join(temp_dir, f"combined_{timestamp}.md")
    try:
        with open(combined_md, "w", encoding="utf-8") as out:
            for md in md_files:
                if os.path.isfile(md):
                    with open(md, encoding="utf-8") as mdf:
                        out.write(mdf.read())
                        out.write("\n\n")
                else:
                    logging.warning("Skipping missing file: %s", md)
    except Exception as e:
        logging.error("Failed to write combined markdown: %s", e)
        sys.exit(1)

    if args.wrap_wide_tables:
        wrap_wide_tables(combined_md, threshold=args.table_threshold)

    if args.pdf:
        # Build PDF with Pandoc
        pdf_output = args.pdf
        # Remove .pdf extension if present
        if pdf_output.endswith(".pdf"):
            pdf_output = pdf_output[:-4]
        # Add timestamp to output filename
        pdf_output = f"{pdf_output}_{timestamp}.pdf"
        out, err, code = run(
            f'pandoc "{combined_md}" -o "{pdf_output}" --pdf-engine=xelatex --toc',
            capture_output=True,
        )
        if code != 0:
            logging.error("Pandoc failed with exit code %s", code)
            sys.exit(code)
        if err:
            log_file = os.path.join(clone_dir, f"pandoc_warnings_{timestamp}.log")
            with open(log_file, "w", encoding="utf-8") as lf:
                lf.write(err)
            logging.warning("Pandoc warnings logged to %s", log_file)
        logging.info("PDF generated: %s", pdf_output)

    # Run quality checks based on flags
    if args.export_sources:
        extract_sources(
            md_files,
            os.path.join(current_dir, f"sources_{timestamp}.csv"),
        )
    if args.check_links:
        check_links(
            md_files,
            os.path.join(current_dir, f"report_check_links_{timestamp}.csv"),
        )
    if args.markdownlint:
        lint_out, _ = lint_markdown(clone_dir)
        print(lint_out)
    if args.check_images:
        missing_imgs = check_images(md_files)
        for mi in missing_imgs:
            print("Missing image:", mi)
    if args.readability:
        scores = readability_report(md_files)
        for sc in scores:
            print("Readability:", sc)
    if args.metadata:
        meta_issues = validate_metadata(md_files)
        for mi in meta_issues:
            print("Metadata issue:", mi)
    if args.duplicate_headings:
        duplicates = check_duplicate_headings(md_files)
        for dup in duplicates:
            print("Duplicate heading:", dup)
    if args.citations:
        citation_gaps = check_citation_numbering(md_files)
        for gap in citation_gaps:
            print("Citation gaps:", gap)
    if args.todos:
        todos = list_todos(md_files)
        for todo in todos:
            print("TODO/FIXME:", todo)
    if args.spellcheck:
        spell_out, _ = spellcheck(clone_dir)
        print(spell_out)
    if args.fix_internal_links:
        summary_md = os.path.join(clone_dir, "Summary.md")
        if not os.path.isfile(summary_md):
            logging.error("Summary.md not found at %s", summary_md)
            sys.exit(1)
        report = proof_and_repair_internal_references(md_files, summary_md)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = os.path.join(
            out_dir, f"internal_link_proof_and_repair_report_{timestamp}.md"
        )
        with open(report_filename, "w", encoding="utf-8") as rf:
            rf.write(
                f"# Internal Link Proof and Repair Report\nGenerated: {datetime.now().isoformat()}\n\n"
            )
            for e in report:
                rf.write(f"- Action: {e['action']}\n")
                if "file" in e:
                    rf.write(f"  - File: {e['file']}\n")
                if "target" in e:
                    rf.write(f"  - Target: {e['target']}\n")
                if "title" in e:
                    rf.write(f"  - Title: {e['title']}\n")
                if "link" in e:
                    rf.write(f"  - Link: {e['link']}\n")
                if "index" in e:
                    rf.write(f"  - Index: {e['index']}\n")
                if "orig" in e:
                    rf.write(f"  - Original: {e['orig']}\n")
                if "new" in e:
                    rf.write(f"  - New: {e['new']}\n")
                rf.write("\n")
        print(f"Report generated: {report_filename}")
        logging.info(
            "Internal link proof and repair report generated: %s", report_filename
        )
    if args.fix_external_references:
        report = proof_and_repair_external_references(
            md_files,
            prompt=args.ai_prompt_reference,
            ai_url=args.ai_url,
            ai_api_key=args.ai_api_key,
            ai_provider=args.ai_provider,
        )
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = os.path.join(
            out_dir, f"external_reference_proof_and_repair_report_{timestamp}.md"
        )
        with open(report_filename, "w", encoding="utf-8") as rf:
            rf.write(
                f"# External Reference Proof and Repair Report\nGenerated: {datetime.now().isoformat()}\n\n"
            )
            for e in report:
                rf.write(f"- Action: {e['action']}\n")
                rf.write(f"  - File: {e['file']}\n")
                rf.write(f"  - Line Number: {e['lineno']}\n")
                if "orig" in e:
                    rf.write(f"  - Original: {e['orig']}\n")
                if "error" in e:
                    rf.write(f"  - Error: {e['error']}\n")
                if "new" in e:
                    rf.write(f"  - New: {e['new']}\n")
                rf.write("\n")
        print(f"Report generated: {report_filename}")
        logging.info(
            "External reference proof and repair report generated: %s", report_filename
        )

    logging.info("All quality checks completed.")


if __name__ == "__main__":
    main()
