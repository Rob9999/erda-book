"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import importlib
import json
import logging
import pathlib
import subprocess
import sys
from collections.abc import Iterator

import pytest


GITHUB_DIR = pathlib.Path(__file__).resolve().parents[2]
WORKER_DIR = GITHUB_DIR / "gitbook_worker"
for _path in (WORKER_DIR, GITHUB_DIR):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))


from . import GH_TEST_ARTIFACTS_DIR, GH_TEST_LOGS_DIR, GH_TEST_OUTPUT_DIR
from tools.logging_config import make_specific_logger


def _ensure(pkg: str) -> None:
    """Install ``pkg`` with pip if it cannot be imported."""
    try:
        importlib.import_module(pkg)
    except ImportError:  # pragma: no cover - only runs when dependency missing
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])


for _pkg in ["pyyaml", "tabulate", "emoji", "beautifulsoup4"]:
    _ensure(_pkg)


@pytest.fixture
def logger(request: pytest.FixtureRequest) -> Iterator[logging.Logger]:
    """Provide a test-specific logger that writes to GH_TEST_LOGS_DIR."""
    log_path = GH_TEST_LOGS_DIR / f"{request.node.name}.log"
    with make_specific_logger(
        request.node.name,
        log_path=log_path,
        rootless=False,
    ) as log:
        yield log


@pytest.fixture
def output_dir(request: pytest.FixtureRequest) -> pathlib.Path:
    """Return a unique output directory for the current test."""
    path: pathlib.Path = GH_TEST_OUTPUT_DIR / request.node.name
    path.mkdir(parents=True, exist_ok=True)
    return path


@pytest.fixture
def artifact_dir(request: pytest.FixtureRequest) -> pathlib.Path:
    """Return a unique artifacts directory for the current test."""
    path: pathlib.Path = GH_TEST_ARTIFACTS_DIR / request.node.name
    path.mkdir(parents=True, exist_ok=True)
    return path


# ========================= Path Resolution Fixtures ========================= #


def _find_repo_root(start_path: pathlib.Path | None = None) -> pathlib.Path:
    """Find the repository root by looking for .git, publish.yml, or book.json.

    This matches the logic used in publisher.py's _get_repo_root().
    """
    if start_path is None:
        start_path = pathlib.Path(__file__).resolve()

    parents = [start_path, *start_path.parents]
    for candidate in parents:
        if (candidate / ".git").is_dir():
            return candidate
        if (candidate / "publish.yml").exists() or (
            candidate / "publish.yaml"
        ).exists():
            return candidate
        if (candidate / "book.json").exists():
            return candidate
    return parents[-1]


def _find_publish_yml(repo_root: pathlib.Path) -> pathlib.Path:
    """Resolve publish.yml path following the standard search order.

    This matches the logic in convert_assets.py's _resolve_manifest_path().
    """
    # Check repo root for publish.yml or publish.yaml
    for name in ("publish.yml", "publish.yaml"):
        candidate = repo_root / name
        if candidate.exists():
            return candidate.resolve()

    # Fallback (may not exist)
    return (repo_root / "publish.yml").resolve()


def _find_book_json(start_path: pathlib.Path) -> pathlib.Path:
    """Locate book.json by searching up the directory tree.

    This matches the logic in gitbook_style.py's _find_book_base().
    """
    for candidate in [start_path, *start_path.parents]:
        book_json = candidate / "book.json"
        if book_json.exists():
            return book_json.resolve()

    # Fallback to start_path / "book.json" (may not exist)
    return (start_path / "book.json").resolve()


def _get_content_root(book_json_path: pathlib.Path) -> pathlib.Path:
    """Extract the content root directory from book.json.

    This matches the logic in gitbook_style.py's _build_summary_context().
    """
    if not book_json_path.exists():
        return book_json_path.parent

    with book_json_path.open("r", encoding="utf-8") as f:
        book_data = json.load(f)

    root_value = book_data.get("root", ".")
    # Remove trailing slash if present
    root_value = root_value.rstrip("/")

    if not root_value or root_value == ".":
        return book_json_path.parent

    return (book_json_path.parent / root_value).resolve()


@pytest.fixture(scope="session")
def repo_root() -> pathlib.Path:
    """Return the repository root directory."""
    return _find_repo_root()


@pytest.fixture(scope="session")
def publish_yml_path(repo_root: pathlib.Path) -> pathlib.Path:
    """Return the path to publish.yml (or publish.yaml)."""
    return _find_publish_yml(repo_root)


@pytest.fixture(scope="session")
def book_json_path(repo_root: pathlib.Path) -> pathlib.Path:
    """Return the path to book.json."""
    return _find_book_json(repo_root)


@pytest.fixture(scope="session")
def book_json_data(book_json_path: pathlib.Path) -> dict:
    """Return the parsed book.json data."""
    with book_json_path.open("r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def content_root(book_json_path: pathlib.Path) -> pathlib.Path:
    """Return the content root directory from book.json configuration.

    For integration tests, this returns the actual repo content directory.
    Individual tests should use their own test data fixtures if they need
    controlled test content instead of the full repository content.
    """
    return _get_content_root(book_json_path)


@pytest.fixture
def test_content_root() -> pathlib.Path:
    """Return the test data directory for controlled test scenarios.

    Use this fixture instead of content_root when tests need isolated
    test data rather than the full repository content directory.
    """
    return pathlib.Path(__file__).parent / "data"
