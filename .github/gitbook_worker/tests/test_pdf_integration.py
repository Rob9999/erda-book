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


def test_documents_folder_to_pdf(tmp_path, monkeypatch):
    monkeypatch.setattr(publisher, "_run_pandoc", _run_lualatex)
    docs_root = (
        pathlib.Path(__file__).resolve().parents[3] / "docs" / "public" / "documents"
    )
    md_files = [p for p in docs_root.rglob("*.md") if p.name != "summary.md"][:5]
    for md_file in md_files:
        rel_dir = md_file.relative_to(docs_root).parent
        out_dir = tmp_path / rel_dir
        out_dir.mkdir(parents=True, exist_ok=True)
        publisher.build_pdf(
            str(md_file), f"{md_file.stem}.pdf", typ="file", publish_dir=str(out_dir)
        )
        assert (out_dir / f"{md_file.stem}.pdf").is_file()


def test_table_pdf_lualatex(tmp_path):
    publisher.prepare_publishing(no_apt=True)
    table_md = (
        pathlib.Path(__file__).resolve().parents[3]
        / "docs"
        / "public"
        / "documents"
        / "08-glossary-partners-institutions-legal-notices-and-overall-appendices"
        / "8.4-overall-appendices"
        / "8.4.8-appendix-t-tables"
        / "table-1-evol00-decks-000-015-r-korr63-roehrenmodell-exakt-sli.md"
    )
    out_dir = tmp_path
    ok = publisher.build_pdf(
        str(table_md), "table.pdf", typ="file", publish_dir=str(out_dir)
    )
    assert ok
    assert (out_dir / "table.pdf").is_file()
