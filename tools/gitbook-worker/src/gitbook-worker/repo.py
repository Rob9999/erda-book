"""Deprecated Git helpers maintained for backwards compatibility."""

from __future__ import annotations

import warnings
from pathlib import Path

from tools.utils.git import checkout_branch as _checkout_branch
from tools.utils.git import clone_or_update_repo as _clone_or_update_repo
from tools.utils.git import remove_tree as _remove_tree

_DEPRECATION_MESSAGE = (
    "gitbook_worker.repo is deprecated; import from tools.utils.git instead."
)


def remove_tree(path: str | Path) -> None:
    warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
    _remove_tree(path)


def checkout_branch(repo_dir: str | Path, branch_name: str) -> None:
    warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
    _checkout_branch(repo_dir, branch_name)


def clone_or_update_repo(
    repo_url: str,
    clone_dir: str | Path,
    branch_name: str | None = None,
    force: bool = False,
) -> None:
    warnings.warn(_DEPRECATION_MESSAGE, DeprecationWarning, stacklevel=2)
    _clone_or_update_repo(
        repo_url,
        clone_dir,
        branch_name=branch_name,
        force=force,
    )
