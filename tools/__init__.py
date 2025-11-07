"""
Top-level shim package for repository-local tools.

This package makes the real implementation under
`.github/gitbook_worker/tools` importable as `tools.*` so the
debugger/launcher can run `-m tools.workflow_orchestrator`.

It's intentionally minimal and safe: it only adjusts the package
search path at import time and doesn't execute any repo logic.
"""

from pathlib import Path
import os

# Compute the path to the real tools directory inside .github/gitbook_worker
# Parent of this `tools` package is the repository root, so go up one more level.
_repo_root = Path(__file__).resolve().parent.parent
_real_tools = str(_repo_root / ".github" / "gitbook_worker" / "tools")

# Prepend to package search path so subpackages under that folder
# become available as `tools.<submodule>`.
if _real_tools not in __path__:
    __path__.insert(0, _real_tools)

# Expose the resolved path for debugging if needed
__real_tools_path__ = _real_tools

# Ensure subprocess/text IO uses UTF-8 where possible to avoid
# platform-default codec (cp1252) decoding errors when the
# tools package launches other processes that emit UTF-8.
# This mirrors setting PYTHONUTF8=1 and PYTHONIOENCODING=utf-8 for
# local invocations (harmless if already set).
os.environ.setdefault("PYTHONUTF8", "1")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
