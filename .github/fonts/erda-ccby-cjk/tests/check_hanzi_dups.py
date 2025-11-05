#!/usr/bin/env python3
"""Quick check for duplicate keys in HANZI_KANJI dictionary."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from hanzi import HANZI_KANJI

chars = list(HANZI_KANJI.keys())
print(f"Total characters in HANZI_KANJI: {len(chars)}")

# Check for duplicates
seen = set()
dups = []
for c in chars:
    if c in seen:
        dups.append(c)
    seen.add(c)

if dups:
    print(f"\nDuplicate keys found: {dups}")
else:
    print("\nNo duplicate keys found - dictionary is clean!")
