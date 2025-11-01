"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import importlib
import logging
import pathlib
import subprocess
import sys
from collections.abc import Iterator

import pytest


GITHUB_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(GITHUB_DIR) not in sys.path:
    sys.path.insert(0, str(GITHUB_DIR))


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
