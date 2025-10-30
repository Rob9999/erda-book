import json
from pathlib import Path

import pytest
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
    assert len(result) == 1
    entry = result[0]
    expected = {
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
    for key, value in expected.items():
        assert entry[key] == value


def test_convert_folder_adds_latex_packages(tmp_path, monkeypatch):
    folder = tmp_path / "docs"
    folder.mkdir()
    (folder / "a.md").write_text("Hello", encoding="utf-8")

    captured: dict[str, str] = {}

    def fake_run_pandoc(md_path, pdf_out, add_toc=False, title=None, **kwargs):
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

    def fake_run_pandoc(md_path, pdf_out, add_toc=False, title=None, **kwargs):
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

    def fake_run_pandoc(md_path, pdf_out, add_toc=False, title=None, **kwargs):
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


def test_convert_file_emits_emoji_report(tmp_path, monkeypatch):
    md_file = tmp_path / "doc.md"
    md_file.write_text("Hallo 😀", encoding="utf-8")

    pdf_out = tmp_path / "doc.pdf"
    report_dir = tmp_path / "reports"

    monkeypatch.setattr(
        publisher,
        "process",
        lambda path, paper_format="a4": Path(path).read_text(encoding="utf-8"),
    )
    monkeypatch.setattr(publisher, "normalize_md", lambda text: text)
    monkeypatch.setattr(
        publisher,
        "add_geometry_package",
        lambda text, paper_format="a4": text,
    )

    def fake_run(md_path, pdf_out, **kwargs):
        assert Path(md_path).exists()

    monkeypatch.setattr(publisher, "_run_pandoc", fake_run)

    publisher.convert_a_file(
        str(md_file),
        str(pdf_out),
        emoji_options=publisher.EmojiOptions(report=True, report_dir=report_dir),
    )

    reports = list(report_dir.glob("*_emoji_report_*.md"))
    assert len(reports) == 1
    content = reports[0].read_text(encoding="utf-8")
    assert "# Emoji usage report" in content
    assert "Emoticons" in content


def test_build_pdf_reads_uppercase_summary(tmp_path, monkeypatch):
    folder = tmp_path / "book"
    folder.mkdir()
    (folder / "a.md").write_text("A", encoding="utf-8")
    (folder / "b.md").write_text("B", encoding="utf-8")
    (folder / "SUMMARY.md").write_text("* [A](a.md)\n* [B](b.md)\n", encoding="utf-8")

    captured: dict[str, list[str]] = {}

    def fake_combine(files, paper_format="a4"):
        captured["files"] = [Path(f).name for f in files]
        return "---\n---\n"

    monkeypatch.setattr(publisher, "combine_markdown", fake_combine)
    monkeypatch.setattr(
        publisher, "add_geometry_package", lambda text, paper_format="a4": text
    )
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
    monkeypatch.setattr(
        publisher, "add_geometry_package", lambda text, paper_format="a4": text
    )
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


def test_run_pandoc_host_arguments(monkeypatch, tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Hello", encoding="utf-8")
    pdf = tmp_path / "doc.pdf"

    captured: dict[str, list[str]] = {}

    class DummyResult:
        returncode = 0

    def fake_run(cmd, check=True, capture=False, env=None):
        captured["cmd"] = cmd
        return DummyResult()

    publisher._reset_pandoc_defaults_cache()
    monkeypatch.setattr(publisher, "_run", fake_run)
    monkeypatch.setattr(publisher, "_get_pandoc_version", lambda: (3, 1, 12))
    monkeypatch.setattr(
        publisher, "_select_emoji_font", lambda color: ("OpenMoji Black", False)
    )

    publisher._run_pandoc(
        str(md),
        str(pdf),
        add_toc=True,
        title="Demo",
        resource_paths=["assets"],
        lua_filters=["filter.lua", "other.lua"],
        metadata={"color": ["true"], "foo": ["bar", "baz"]},
        variables={"max-list-depth": "5", "custom": "value"},
        header_path="header.sty",
        pdf_engine="tectonic",
        from_format="gfm",
        to_format="latex",
        extra_args=["--pdf-engine-opt=foo"],
        toc_depth=3,
    )

    cmd = captured["cmd"]
    pairs = list(zip(cmd, cmd[1:]))
    assert cmd[:4] == ["pandoc", str(md), "-o", str(pdf)]
    assert "--pdf-engine" in cmd and cmd[cmd.index("--pdf-engine") + 1] == "tectonic"
    assert "-f" in cmd and cmd[cmd.index("-f") + 1] == "gfm"
    assert "-t" in cmd and cmd[cmd.index("-t") + 1] == "latex"
    assert cmd.count("--lua-filter") == 2
    assert ("-M", "emojifont=OpenMoji Black") in pairs
    assert ("-M", "color=true") in pairs
    assert ("-M", "foo=bar") in pairs
    assert cmd.count("-M") >= 4
    assert ("--variable", "custom=value") in pairs
    assert ("--variable", "mainfont=DejaVu Sans") in pairs
    assert ("--variable", "max-list-depth=5") in pairs
    assert any(arg.endswith("pandoc-fonts.tex") for arg in cmd)
    assert "--toc" in cmd and ("--toc-depth", "3") in pairs
    assert cmd[-1] == "--pdf-engine-opt=foo"


def test_run_pandoc_uses_default_arguments(monkeypatch, tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Hello", encoding="utf-8")
    pdf = tmp_path / "build" / "doc.pdf"

    captured: dict[str, list[str]] = {}

    class DummyResult:
        returncode = 0

    def fake_run(cmd, check=True, capture=False, env=None):
        captured["cmd"] = cmd
        return DummyResult()

    publisher._reset_pandoc_defaults_cache()
    monkeypatch.setattr(publisher, "_run", fake_run)
    monkeypatch.setattr(publisher, "_get_pandoc_version", lambda: (3, 1, 12))
    monkeypatch.setattr(
        publisher, "_select_emoji_font", lambda color: ("OpenMoji Black", False)
    )

    publisher._run_pandoc(str(md), str(pdf))

    cmd = captured["cmd"]
    pairs = list(zip(cmd, cmd[1:]))
    assert cmd[:4] == ["pandoc", str(md), "-o", str(pdf)]
    assert ("--pdf-engine", "lualatex") in pairs
    assert cmd.count("--lua-filter") == 1
    assert ("-H", ".github/tools/publishing/texmf/tex/latex/local/deeptex.sty") in pairs
    assert any(arg.endswith("pandoc-fonts.tex") for arg in cmd)
    assert ("-M", "emojifont=OpenMoji Black") in pairs
    assert ("-M", "color=false") in pairs
    assert ("--variable", "mainfont=DejaVu Sans") in pairs
    assert ("--variable", "monofont=DejaVu Sans Mono") in pairs
    assert ("--variable", "geometry=margin=1in") in pairs
    assert ("--variable", "longtable=true") in pairs
    assert ("--variable", "max-list-depth=9") in pairs


def test_run_pandoc_env_overrides(monkeypatch, tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Hello", encoding="utf-8")
    pdf = tmp_path / "doc.pdf"

    captured: dict[str, list[str]] = {}

    class DummyResult:
        returncode = 0

    def fake_run(cmd, check=True, capture=False, env=None):
        captured["cmd"] = cmd
        return DummyResult()

    monkeypatch.setenv(
        "ERDA_PANDOC_DEFAULTS_JSON",
        json.dumps(
            {
                "pdf_engine": "xelatex",
                "header_path": None,
                "lua_filters": {"append": ["custom.lua"]},
                "metadata": {"color": ["true"], "new": ["value"]},
                "variables": {"geometry": "margin=2cm", "custom": "1"},
                "extra_args": ["--top-level-division=chapter"],
            }
        ),
    )
    publisher._reset_pandoc_defaults_cache()
    monkeypatch.setattr(publisher, "_run", fake_run)
    monkeypatch.setattr(publisher, "_get_pandoc_version", lambda: (3, 1, 11))
    monkeypatch.setattr(
        publisher, "_select_emoji_font", lambda color: ("Segoe UI Emoji", True)
    )

    publisher._run_pandoc(
        str(md),
        str(pdf),
        extra_args=["--no-tex-ligatures"],
    )

    cmd = captured["cmd"]
    pairs = list(zip(cmd, cmd[1:]))
    assert ("--pdf-engine", "xelatex") in pairs
    assert any(arg.endswith("pandoc-fonts.tex") for arg in cmd)
    assert cmd.count("--lua-filter") == 2
    assert ("-M", "color=true") in pairs
    assert ("-M", "new=value") in pairs
    assert ("-M", "emojifont=Segoe UI Emoji") in pairs
    assert ("--variable", "geometry=margin=2cm") in pairs
    assert ("--variable", "custom=1") in pairs
    assert all(
        pair != ("-V", "mainfontfallback=Segoe UI Emoji:mode=harf") for pair in pairs
    )
    assert cmd[-2:] == ["--top-level-division=chapter", "--no-tex-ligatures"]


def test_run_pandoc_metadata_mapping_override(monkeypatch, tmp_path):
    md = tmp_path / "doc.md"
    md.write_text("Hello", encoding="utf-8")
    pdf = tmp_path / "doc.pdf"

    captured: dict[str, list[str]] = {}

    class DummyResult:
        returncode = 0

    def fake_run(cmd, check=True, capture=False, env=None):
        captured["cmd"] = cmd
        return DummyResult()

    publisher._reset_pandoc_defaults_cache()
    monkeypatch.setattr(publisher, "_run", fake_run)
    monkeypatch.setattr(publisher, "_get_pandoc_version", lambda: (3, 1, 12))
    monkeypatch.setattr(
        publisher, "_select_emoji_font", lambda color: ("OpenMoji Black", False)
    )

    publisher._run_pandoc(
        str(md),
        str(pdf),
        metadata={"color": {"append": ["true"]}},
    )

    cmd = captured["cmd"]
    assert cmd.count("-M") == 3
    assert "color=false" in " ".join(cmd)
    assert "color=true" in " ".join(cmd)
