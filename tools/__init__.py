"""
Small shim package to expose the real tools package located under
`.github/tools` as the importable top-level `tools` package.

This keeps the repository layout intact while allowing `python -m tools.xxx`
invocations to work from the repository root or when the repo root is on
sys.path. It's intentionally tiny and uses a path hack to include the
`.github/tools` directory in the package search path.

Note: This is a pragmatic shim. A more robust long-term solution is to
adjust packaging metadata so `tools` is installed into the environment
properly (e.g. via setup.cfg / pyproject metadata). For now this avoids
requiring PYTHONPATH tweaks for interactive use.
"""

from __future__ import annotations

import importlib.util
import pathlib
import sys

# Resolve the absolute path to the `.github/tools` directory relative to
# this file. We add it to the package __path__ so imports like
# `import tools.workflow_orchestrator` will load modules from there.
_HERE = pathlib.Path(__file__).resolve()
_REPO_ROOT = _HERE.parent.parent
_GITHUB_TOOLS = _REPO_ROOT.joinpath(".github", "tools")

if _GITHUB_TOOLS.exists():
    # Insert at front so real files in `.github/tools` take precedence.
    __path__.insert(0, str(_GITHUB_TOOLS))
else:
    # Fallback: don't crash on import; modules will raise ImportError as usual.
    pass
