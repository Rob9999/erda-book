from __future__ import annotations

from pathlib import Path

import pytest

from tools.publishing import set_publish_flag as spf


def test_get_entry_type_prefers_source_type():
    entry = {"source_type": "FOLDER", "type": "file"}
    assert spf.get_entry_type(entry) == "folder"


def test_resolve_entry_path_for_root_manifest(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    repo_root.mkdir()
    (repo_root / "chapters").mkdir()

    resolved = spf.resolve_entry_path("chapters", str(repo_root), str(repo_root))
    assert resolved == "chapters"


def test_resolve_entry_path_for_nested_manifest(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    manifest_dir = repo_root / "docs" / "public"
    manifest_dir.mkdir(parents=True)
    (manifest_dir / "chapters").mkdir()

    resolved = spf.resolve_entry_path("chapters", str(manifest_dir), str(repo_root))
    assert resolved == "docs/public/chapters"


@pytest.mark.parametrize(
    "entry_type, entry_path, changed",  # noqa: E231 - compact parametrisation
    [
        ("folder", "chapters", "chapters/intro.md"),
        ("file", "README.md", "README.md"),
    ],
)
def test_is_match_handles_relative_paths(
    entry_type: str, entry_path: str, changed: str
):
    assert spf.is_match(entry_path, entry_type, changed) is True


def test_git_changed_files_falls_back_when_base_missing(monkeypatch):
    calls: list[list[str]] = []

    def fake_run(cmd: list[str]) -> tuple[int, str, str]:
        calls.append(cmd)
        if cmd[:3] == ["git", "diff", "--name-only"]:
            return 128, "", "fatal: bad revision 'base'"
        assert cmd[:2] == ["git", "diff-tree"]
        return 0, "docs/example.md\n", ""

    monkeypatch.setattr(spf, "run", fake_run)

    files = spf.git_changed_files("commit", base="base")

    assert files == ["docs/example.md"]
    assert calls[0][:3] == ["git", "diff", "--name-only"]
    assert calls[1][0] == "git"
