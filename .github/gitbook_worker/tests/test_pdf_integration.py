import pathlib
import shutil
import subprocess
import sys

import pytest
from tools.converter import convert_assets

# Import von der Root des .github-Pakets
from tools.publishing import publisher

from . import GH_TEST_LOGS_DIR, GH_TEST_OUTPUT_DIR

pytestmark = [
    pytest.mark.skipif(
        shutil.which("pandoc") is None or shutil.which("lualatex") is None,
        reason="pandoc or lualatex not installed",
    ),
    pytest.mark.slow,  # These tests involve PDF generation
]


def _run_lualatex(
    md_path: str, pdf_out: str, add_toc: bool = False, title: str | None = None
) -> None:
    cmd = ["pandoc", md_path, "-o", pdf_out, "--pdf-engine", "lualatex"]
    if add_toc:
        cmd.append("--toc")
    if title:
        cmd.extend(["-V", f"title={title}"])
    subprocess.run(cmd, check=True)


def test_end_to_end_pdf_generation(tmp_path, monkeypatch):
    monkeypatch.setattr(publisher, "_run_pandoc", _run_lualatex)
    data_dir = pathlib.Path(__file__).parent / "data"
    complex_md = data_dir / "evol00-decks-000-015-r-korr63-roehrenmodell-exakt-sli.md"
    csv_path = data_dir / "sample.csv"
    assets_dir = tmp_path / "assets"
    template_dir = tmp_path / "templates"
    template_dir.mkdir()
    (template_dir / "table.md").write_text("{table}", encoding="utf-8")
    monkeypatch.setattr(convert_assets, "TEMPLATES", template_dir)
    convert_assets.convert_csv(csv_path, assets_dir)
    generated_md = assets_dir / "tables" / "sample.md"
    assert "\\_" in generated_md.read_text()
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    shutil.copy(complex_md, docs_dir / "complex.md")
    shutil.copy(data_dir / "sample.md", docs_dir / "sample.md")
    shutil.copy(generated_md, docs_dir / "table.md")
    publish_dir = tmp_path / "publish"
    ok = publisher.build_pdf(
        str(docs_dir), "out.pdf", typ="folder", publish_dir=str(publish_dir)
    )
    assert ok
    pdf_path = publish_dir / "out.pdf"
    assert pdf_path.is_file()
    assert pdf_path.stat().st_size > 0


def test_documents_folder_to_pdf(tmp_path, monkeypatch, content_root):
    """Test PDF generation from actual content directory markdown files.

    This test uses the content_root fixture to dynamically locate markdown files
    instead of hardcoding a 'docs/public/documents' path.
    """
    monkeypatch.setattr(publisher, "_run_pandoc", _run_lualatex)

    # Use the content_root from book.json instead of hardcoded path
    md_files = [
        p
        for p in content_root.rglob("*.md")
        if p.name.lower() not in ("summary.md", "readme.md")
    ][:5]

    # Skip test if no markdown files found
    if not md_files:
        pytest.skip(f"No markdown files found in content root: {content_root}")

    for md_file in md_files:
        rel_dir = md_file.relative_to(content_root).parent
        out_dir = tmp_path / rel_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        publisher.build_pdf(
            str(md_file), f"{md_file.stem}.pdf", typ="file", publish_dir=str(out_dir)
        )
        assert (out_dir / f"{md_file.stem}.pdf").is_file()


def test_table_pdf_lualatex(tmp_path, content_root):
    """Test PDF generation from a table markdown file.

    This test dynamically searches for table markdown files in the content root
    instead of using a hardcoded path.
    """
    publisher.prepare_publishing(no_apt=True)

    # Search for a table markdown file in the content root
    table_files = list(content_root.rglob("table-*.md"))

    # Skip test if no table files found
    if not table_files:
        pytest.skip(f"No table-*.md files found in content root: {content_root}")

    # Use the first table file found
    table_md = table_files[0]
    out_dir = tmp_path
    ok = publisher.build_pdf(
        str(table_md), "table.pdf", typ="file", publish_dir=str(out_dir)
    )
    assert ok
    assert (out_dir / "table.pdf").is_file()
