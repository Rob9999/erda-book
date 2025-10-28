"""Deprecated Docker helpers maintained for backwards compatibility."""

from __future__ import annotations

import warnings
from pathlib import Path

from tools.utils.docker import ensure_daemon_ready as _ensure_daemon_ready
from tools.utils.docker import ensure_image as _ensure_image

_DEPRECATION_MESSAGE = (
    "gitbook_worker.docker_tools is deprecated; use tools.utils.docker instead."
)


def ensure_docker_image(image_name: str, dockerfile_path: str | Path) -> None:
    warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
    _ensure_image(image_name, Path(dockerfile_path))


def ensure_docker_desktop(wait_seconds: int = 120) -> None:
    warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
    _ensure_daemon_ready(wait_seconds=wait_seconds)
