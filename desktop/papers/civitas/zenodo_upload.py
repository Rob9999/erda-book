#!/usr/bin/env python3
"""
zenodo_upload.py — CIVITAS Public Paper Uploader for Zenodo

Uploads the CIVITAS Public concept paper to Zenodo (or Zenodo Sandbox)
with full metadata. Supports:
  - DOI reservation before upload
  - File upload (PDF, Markdown, supplementary files)
  - Full metadata configuration
  - Draft-only or immediate publish mode
  - Sandbox testing before production upload

Usage:
  # 1. Set your token as environment variable:
  set ZENODO_TOKEN=your_token_here          (production)
  set ZENODO_SANDBOX_TOKEN=your_token_here  (sandbox)

  # 2. Test with sandbox first:
  python zenodo_upload.py --sandbox --draft

  # 3. Upload to production (draft mode — review before publishing):
  python zenodo_upload.py --draft

  # 4. Upload and publish immediately:
  python zenodo_upload.py --publish

Requirements:
  pip install requests

License: MIT (as part of ERDA toolchain)
Author: Robert Alexander Massinger / ERDA Initiative
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package required. Install with: pip install requests")
    sys.exit(1)

# Auto-load .env file from script directory (if python-dotenv is available)
_env_path = Path(__file__).parent / ".env"
try:
    from dotenv import load_dotenv

    if _env_path.exists():
        load_dotenv(_env_path)
except ImportError:
    # Fallback: manual .env parsing (key=value, comments/empty lines ignored)
    if _env_path.exists():
        with open(_env_path) as _f:
            for _line in _f:
                _line = _line.strip()
                if _line and not _line.startswith("#") and "=" in _line:
                    _k, _v = _line.split("=", 1)
                    _k, _v = _k.strip(), _v.strip()
                    if _v and _k not in os.environ:
                        os.environ[_k] = _v

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ZENODO_API = "https://zenodo.org/api"
ZENODO_SANDBOX_API = "https://sandbox.zenodo.org/api"

# Metadata for the CIVITAS Public paper
METADATA = {
    "title": "CIVITAS Public: Building a European Digital Agora — A Call to Action",
    "upload_type": "publication",
    "publication_type": "workingpaper",
    "publication_date": "2026-04-06",
    "creators": [
        {
            "name": "Massinger, Robert Alexander",
            "affiliation": "ERDA Initiative / Independent Concept Development, Munich, Germany",
        }
    ],
    "description": (
        "This concept paper presents CIVITAS Public as a concrete, actionable first "
        "step towards a European digital civic infrastructure. CIVITAS Public is "
        "conceived as a non-commercial, open-source, multilingual platform for "
        "verified publication, structured debate, polling, trend observation, civic "
        "questions, and future participatory expansion — governed by transparent rules, "
        "independent oversight, and rule-of-law safeguards. Situated within the ERDA "
        "(European Resilience and Democratic Architecture) framework, CIVITAS Public "
        "is designed to be both immediately useful and institutionally extensible. "
        "The paper concludes with a call to action directed at civic-technology "
        "communities, European institutions, media organisations, academic networks, "
        "and civil society to collaborate in launching CIVITAS Public as the first "
        "building block of Europe's democratic digital future."
    ),
    "keywords": [
        "CIVITAS",
        "ERDA",
        "digital democracy",
        "European public sphere",
        "civic technology",
        "democratic infrastructure",
        "public debate",
        "verification",
        "Europe",
        "open source",
        "digital agora",
    ],
    "language": "eng",
    "version": "1.0",
    "access_right": "open",
    "license": "cc-by-4.0",
    "notes": (
        "Working paper / concept paper. Part of the ERDA Initiative. "
        "This upload may be followed by revised versions, annexes, "
        "implementation notes, governance diagrams, or prototype materials."
    ),
    "related_identifiers": [
        {
            "identifier": "10.5281/zenodo.18827190",
            "relation": "isPartOf",
            "resource_type": "publication-book",
        }
    ],
    "communities": [],  # Add community IDs if applicable, e.g. [{"identifier": "zenodo"}]
}

# Default files to upload (relative to this script's directory)
DEFAULT_FILES = [
    "publish/civitas-public-v1.0-zenodo.pdf",
    "CITATION.cff",
    "LICENSE",
    "LICENSE-CODE",
    "LICENSE-FONTS",
]


# ---------------------------------------------------------------------------
# Zenodo API Client
# ---------------------------------------------------------------------------


class ZenodoUploader:
    """Client for the Zenodo REST API (v1-compatible deposit endpoint)."""

    def __init__(self, token: str, sandbox: bool = False):
        self.token = token
        self.base_url = ZENODO_SANDBOX_API if sandbox else ZENODO_API
        self.sandbox = sandbox
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        self.deposit_id = None
        self.doi = None
        self.deposit_url = None

    def _check_response(self, resp: requests.Response, context: str):
        """Check HTTP response and raise on error."""
        if resp.status_code >= 400:
            print(f"\nERROR during {context}:")
            print(f"  HTTP {resp.status_code}")
            try:
                detail = json.dumps(resp.json(), indent=2)
            except Exception:
                detail = resp.text[:500]
            print(f"  Response: {detail}")
            sys.exit(1)

    def create_deposit(self) -> dict:
        """Create a new empty deposit and reserve a DOI."""
        print("Creating new deposit...")
        resp = self.session.post(
            f"{self.base_url}/deposit/depositions",
            json={},
        )
        self._check_response(resp, "create deposit")
        data = resp.json()
        self.deposit_id = data["id"]
        self.doi = data.get("metadata", {}).get("prereserve_doi", {}).get("doi", "N/A")
        self.deposit_url = data.get("links", {}).get("html", "")
        print(f"  Deposit ID: {self.deposit_id}")
        print(f"  Reserved DOI: {self.doi}")
        print(f"  URL: {self.deposit_url}")
        return data

    def set_metadata(self, metadata: dict) -> dict:
        """Set metadata on the deposit."""
        print("Setting metadata...")
        payload = {"metadata": metadata}
        resp = self.session.put(
            f"{self.base_url}/deposit/depositions/{self.deposit_id}",
            json=payload,
        )
        self._check_response(resp, "set metadata")
        print("  Metadata set successfully.")
        return resp.json()

    def upload_file(self, filepath: Path) -> dict:
        """Upload a single file to the deposit."""
        filename = filepath.name
        filesize = filepath.stat().st_size
        print(f"Uploading: {filename} ({filesize:,} bytes)...")
        with open(filepath, "rb") as f:
            resp = self.session.post(
                f"{self.base_url}/deposit/depositions/{self.deposit_id}/files",
                data={"name": filename},
                files={"file": (filename, f)},
            )
        self._check_response(resp, f"upload file '{filename}'")
        print(f"  Uploaded: {filename}")
        return resp.json()

    def publish(self) -> dict:
        """Publish the deposit (makes it permanent and assigns DOI)."""
        print("Publishing deposit...")
        resp = self.session.post(
            f"{self.base_url}/deposit/depositions/{self.deposit_id}/actions/publish",
        )
        self._check_response(resp, "publish")
        data = resp.json()
        final_doi = data.get("doi", self.doi)
        final_url = data.get("links", {}).get("html", self.deposit_url)
        print(f"  Published successfully!")
        print(f"  DOI: {final_doi}")
        print(f"  URL: {final_url}")
        return data


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def find_files(script_dir: Path, file_patterns: list[str]) -> list[Path]:
    """Resolve file paths relative to script directory."""
    files = []
    for pattern in file_patterns:
        p = script_dir / pattern
        if p.exists():
            files.append(p)
        else:
            print(f"  WARNING: File not found: {p}")
    return files


def main():
    parser = argparse.ArgumentParser(
        description="Upload CIVITAS Public paper to Zenodo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python zenodo_upload.py --sandbox --draft          # Test on sandbox
  python zenodo_upload.py --draft                    # Production draft
  python zenodo_upload.py --publish                  # Production + publish
  python zenodo_upload.py --publish --files paper.pdf supplementary.zip
        """,
    )
    parser.add_argument(
        "--sandbox",
        action="store_true",
        help="Use Zenodo Sandbox (for testing). Requires ZENODO_SANDBOX_TOKEN.",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--draft",
        action="store_true",
        help="Upload as draft (review on Zenodo before publishing).",
    )
    mode.add_argument(
        "--publish",
        action="store_true",
        help="Upload and publish immediately (permanent, assigns DOI).",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        help="Files to upload (paths relative to script directory or absolute). "
        "Defaults to the Markdown source.",
    )
    parser.add_argument(
        "--token",
        help="Zenodo API token. Overrides environment variable.",
    )
    parser.add_argument(
        "--metadata-file",
        help="Path to .zenodo.json file. Overrides built-in METADATA.",
    )

    args = parser.parse_args()

    # Resolve token
    if args.token:
        token = args.token
    elif args.sandbox:
        token = os.environ.get("ZENODO_SANDBOX_TOKEN", "")
    else:
        token = os.environ.get("ZENODO_TOKEN", "")

    if not token:
        env_var = "ZENODO_SANDBOX_TOKEN" if args.sandbox else "ZENODO_TOKEN"
        print(f"ERROR: No API token provided.")
        print(f"  Set {env_var} environment variable or use --token.")
        print(
            f"  Get your token at: https://{'sandbox.' if args.sandbox else ''}zenodo.org/account/settings/applications/tokens/new/"
        )
        sys.exit(1)

    # Resolve paths
    script_dir = Path(__file__).parent

    # Resolve metadata
    if args.metadata_file:
        meta_path = Path(args.metadata_file)
        if not meta_path.is_absolute():
            meta_path = script_dir / meta_path
        if not meta_path.exists():
            print(f"ERROR: Metadata file not found: {meta_path}")
            sys.exit(1)
        print(f"Loading metadata from: {meta_path}")
        with open(meta_path, encoding="utf-8") as mf:
            metadata = json.load(mf)
    else:
        # Try .zenodo.json in script directory
        default_meta = script_dir / ".zenodo.json"
        if default_meta.exists():
            print(f"Loading metadata from: {default_meta}")
            with open(default_meta, encoding="utf-8") as mf:
                metadata = json.load(mf)
        else:
            metadata = METADATA

    # Resolve files
    if args.files:
        file_list = args.files
    else:
        file_list = DEFAULT_FILES

    files = find_files(script_dir, file_list)
    if not files:
        print("ERROR: No files found to upload.")
        sys.exit(1)

    # Print plan
    env_label = "SANDBOX" if args.sandbox else "PRODUCTION"
    action_label = "PUBLISH" if args.publish else "DRAFT"
    print("=" * 60)
    print(f"  CIVITAS Public — Zenodo Upload")
    print(f"  Environment: {env_label}")
    print(f"  Mode:        {action_label}")
    print(f"  Files:       {', '.join(f.name for f in files)}")
    print("=" * 60)
    print()

    # Execute upload
    uploader = ZenodoUploader(token=token, sandbox=args.sandbox)

    # Step 1: Create deposit
    uploader.create_deposit()
    print()

    # Step 2: Set metadata
    uploader.set_metadata(metadata)
    print()

    # Step 3: Upload files
    for f in files:
        uploader.upload_file(f)
    print()

    # Step 4: Publish (if requested)
    if args.publish:
        # Safety prompt for production publish
        if not args.sandbox:
            print("WARNING: Publishing to PRODUCTION Zenodo is permanent.")
            print("         The DOI will be minted and cannot be deleted.")
            confirm = input("         Type 'yes' to confirm: ").strip().lower()
            if confirm != "yes":
                print("  Aborted. Deposit remains as draft.")
                print(f"  Review at: {uploader.deposit_url}")
                return
        uploader.publish()
    else:
        print(f"Draft created successfully.")
        print(f"  Review and publish at: {uploader.deposit_url}")

    # Summary
    print()
    print("=" * 60)
    print("  DONE")
    print(f"  DOI:     {uploader.doi}")
    print(f"  URL:     {uploader.deposit_url}")
    print(f"  Status:  {'Published' if args.publish else 'Draft'}")
    print("=" * 60)


if __name__ == "__main__":
    main()
