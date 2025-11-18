"""Test configuration for ERDA CC-BY CJK font project.

Ensures the package root, generator, and tools directories are on sys.path
so unit tests can import modules without relying on the current working
directory.
"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
GENERATOR_DIR = PROJECT_ROOT / "generator"
TOOLS_DIR = PROJECT_ROOT / "tools"

for path in (PROJECT_ROOT, GENERATOR_DIR, TOOLS_DIR):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
