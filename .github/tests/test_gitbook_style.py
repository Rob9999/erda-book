from __future__ import annotations

import json

from tools.publishing.gitbook_style import (
    ensure_clean_summary,
    get_summary_layout,
    rename_to_gitbook_style,
)


def test_rename_to_gitbook_style(tmp_path):
    root = tmp_path / "docs"
    root.mkdir()
    (root / "My File.txt").write_text("content", encoding="utf-8")
    nested = root / "Sub Dir"
    nested.mkdir()
    (nested / "Another File.MD").write_text("data", encoding="utf-8")
    (nested / "ignore.py").write_text("print('hi')", encoding="utf-8")

    rename_to_gitbook_style(root, use_git=False)

    assert not (root / "My File.txt").exists()
    assert (root / "my-file.txt").read_text(encoding="utf-8") == "content"
    assert (root / "sub-dir").is_dir()
    assert (root / "sub-dir" / "another-file.md").read_text(encoding="utf-8") == "data"
    # Python files should not be renamed.
    assert (root / "sub-dir" / "ignore.py").exists()


def test_ensure_clean_summary(tmp_path):
    base = tmp_path / "book"
    base.mkdir()
    (base / "README.md").write_text("# Root Title", encoding="utf-8")
    section = base / "Section One"
    section.mkdir()
    (section / "README.md").write_text("# Section Intro", encoding="utf-8")
    (section / "Topic.md").write_text("# Topic Title", encoding="utf-8")

    summary_path = base / "summary.md"
    summary_path.write_text("outdated", encoding="utf-8")

    changed = ensure_clean_summary(base, run_git=False)
    assert changed is True

    expected = "\n".join(
        [
            "# Summary",
            "",
            "* [Root Title](README.md)",
            "* [Section Intro](Section One/README.md)",
            "  * [Topic Title](Section One/Topic.md)",
            "",
        ]
    )

    assert summary_path.read_text(encoding="utf-8") == expected

    # Second invocation should be idempotent.
    assert ensure_clean_summary(base, run_git=False) is False


def test_get_summary_layout_resolves_uppercase(tmp_path):
    base = tmp_path / "book"
    base.mkdir()
    (base / "book.json").write_text(
        json.dumps(
            {
                "title": "Demo",
                "root": ".",
                "structure": {"summary": "SUMMARY.md"},
            }
        ),
        encoding="utf-8",
    )
    (base / "SUMMARY.md").write_text("", encoding="utf-8")

    layout = get_summary_layout(base)
    assert layout.summary_path == (base / "SUMMARY.md").resolve()
    assert layout.root_dir == base.resolve()
