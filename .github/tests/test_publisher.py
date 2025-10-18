import json
from pathlib import Path

import yaml
from tools.publishing import publisher


def _parse(text: str) -> dict:
    lines = text.splitlines()
    assert lines[0] == "---"
    end = lines.index("---", 1)
    return yaml.safe_load("\n".join(lines[1:end])) or {}


def test_get_publish_list(monkeypatch, tmp_path):
    manifest = tmp_path / "publish.yml"
    data = {
        "publish": [
            {
                "path": "a.md",
                "out": "a.pdf",
                "out_dir": "publish",
                "out_format": "PDF",
                "build": True,
                "source_type": "FOLDER",
                "source_format": "Markdown",
                "use_summary": "true",
                "use_book_json": True,
                "keep_combined": 1,
            },
            {"path": "b.md", "out": "b.pdf", "build": False},
        ]
    }
    manifest.write_text(json.dumps(data), encoding="utf-8")

    monkeypatch.setattr(publisher, "prepareYAML", lambda: None)

    def fake_load_yaml(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    monkeypatch.setattr(publisher, "_load_yaml", fake_load_yaml)

    result = publisher.get_publish_list(str(manifest))
    assert result == [
        {
            "path": "a.md",
            "out": "a.pdf",
            "out_dir": "publish",
            "out_format": "pdf",
            "source_type": "folder",
            "source_format": "markdown",
            "use_summary": True,
            "use_book_json": True,
            "keep_combined": True,
        }
    ]


def test_convert_folder_adds_latex_packages(tmp_path, monkeypatch):
    folder = tmp_path / "docs"
    folder.mkdir()
    (folder / "a.md").write_text("Hello", encoding="utf-8")

    captured: dict[str, str] = {}

    def fake_run_pandoc(md_path, pdf_out, add_toc=False, title=None):
        with open(md_path, "r", encoding="utf-8") as f:
            captured["content"] = f.read()

    monkeypatch.setattr(publisher, "_run_pandoc", fake_run_pandoc)

    publish_dir = tmp_path / "pub"
    publisher.build_pdf(
        str(folder), "out.pdf", typ="folder", publish_dir=str(publish_dir)
    )

    meta = _parse(captured["content"])
    hi = "\n".join(meta.get("header-includes", []))
    assert "geometry" in meta
    assert "\\usepackage{geometry}" not in hi
    assert "\\usepackage{pdflscape}" not in hi


def test_convert_folder_respects_existing_header_includes(
    tmp_path, monkeypatch
):  # noqa: E501
    folder = tmp_path / "docs"
    folder.mkdir()
    content = (
        "---\n"
        "header-includes:\n"
        "  - \\usepackage{foo}\n"
        "author: Bob\n"
        "---\n"
        "Hello"
    )
    (folder / "a.md").write_text(content, encoding="utf-8")

    captured: dict[str, str] = {}

    def fake_run_pandoc(md_path, pdf_out, add_toc=False, title=None):
        with open(md_path, "r", encoding="utf-8") as f:
            captured["content"] = f.read()

    monkeypatch.setattr(publisher, "_run_pandoc", fake_run_pandoc)

    publish_dir = tmp_path / "pub"
    publisher.build_pdf(
        str(folder), "out.pdf", typ="folder", publish_dir=str(publish_dir)
    )

    meta = _parse(captured["content"])
    hi = meta.get("header-includes", [])
    assert "\\usepackage{foo}" in hi
    assert all("\\usepackage{geometry}" not in line for line in hi)


def test_convert_folder_landscape_enabled(tmp_path, monkeypatch):
    folder = tmp_path / "docs"
    folder.mkdir()
    (folder / "a.md").write_text("Hello", encoding="utf-8")

    captured: dict[str, str] = {}

    def fake_run_pandoc(md_path, pdf_out, add_toc=False, title=None):
        with open(md_path, "r", encoding="utf-8") as f:
            captured["content"] = f.read()

    monkeypatch.setattr(publisher, "_run_pandoc", fake_run_pandoc)

    publish_dir = tmp_path / "pub"
    publisher.build_pdf(
        str(folder),
        "out.pdf",
        typ="folder",
        publish_dir=str(publish_dir),
        paper_format="a4-landscape",
    )

    meta = _parse(captured["content"])
    opts = "\n".join(meta.get("geometry", []))
    assert "paperwidth=297mm" in opts
    assert "paperheight=210mm" in opts
def test_build_pdf_reads_uppercase_summary(tmp_path, monkeypatch):
    folder = tmp_path / "book"
    folder.mkdir()
    (folder / "a.md").write_text("A", encoding="utf-8")
    (folder / "b.md").write_text("B", encoding="utf-8")
    (folder / "SUMMARY.md").write_text(
        "* [A](a.md)\n* [B](b.md)\n", encoding="utf-8"
    )

    captured: dict[str, list[str]] = {}

    def fake_combine(files, paper_format="a4"):
        captured["files"] = [Path(f).name for f in files]
        return "---\n---\n"

    monkeypatch.setattr(publisher, "combine_markdown", fake_combine)
    monkeypatch.setattr(publisher, "add_geometry_package", lambda text, paper_format="a4": text)
    monkeypatch.setattr(publisher, "_run_pandoc", lambda *args, **kwargs: None)

    publish_dir = tmp_path / "out"
    publisher.build_pdf(
        path=str(folder),
        out="out.pdf",
        typ="folder",
        use_summary=True,
        publish_dir=str(publish_dir),
    )

    assert captured["files"] == ["a.md", "b.md"]


def test_build_pdf_refreshes_summary_from_book_json(tmp_path, monkeypatch):
    folder = tmp_path / "book"
    folder.mkdir()
    (folder / "README.md").write_text("# Root", encoding="utf-8")
    (folder / "chapter.md").write_text("# Chapter", encoding="utf-8")
    (folder / "book.json").write_text(
        json.dumps(
            {
                "title": "Demo",
                "root": ".",
                "structure": {"summary": "SUMMARY.md"},
            }
        ),
        encoding="utf-8",
    )
    # outdated summary pointing to non-existing file
    (folder / "SUMMARY.md").write_text("* [Old](old.md)\n", encoding="utf-8")

    captured: dict[str, list[str]] = {}

    def fake_combine(files, paper_format="a4"):
        captured["files"] = [Path(f).name for f in files]
        return "---\n---\n"

    monkeypatch.setattr(publisher, "combine_markdown", fake_combine)
    monkeypatch.setattr(publisher, "add_geometry_package", lambda text, paper_format="a4": text)
    monkeypatch.setattr(publisher, "_run_pandoc", lambda *args, **kwargs: None)

    publish_dir = tmp_path / "out"
    publisher.build_pdf(
        path=str(folder),
        out="book.pdf",
        typ="folder",
        use_summary=False,
        use_book_json=True,
        publish_dir=str(publish_dir),
    )

    assert captured["files"] == ["README.md", "chapter.md"]
