import json

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
            {"path": "a.md", "out": "a.pdf", "build": True, "type": "file"},
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
            "type": "file",
            "use_summary": False,
            "keep_combined": False,
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
