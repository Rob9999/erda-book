import shutil
import pytest
from gitbook_worker.utils import wrap_wide_tables


def test_wrap_wide_tables_adds_landscape(tmp_path):
    md = tmp_path / "wide.md"
    md.write_text("|A|B|C|D|E|F|G|\n|--|--|--|--|--|--|--|\n|1|2|3|4|5|6|7|\n")
    wrap_wide_tables(str(md), threshold=5)
    text = md.read_text()
    assert text.startswith("::: {.landscape cols=7}\n")
    assert text.strip().endswith(":::")


def test_wrap_wide_tables_ignores_narrow(tmp_path):
    md = tmp_path / "narrow.md"
    md.write_text("|A|B|\n|--|--|\n|1|2|\n")
    wrap_wide_tables(str(md), threshold=5)
    text = md.read_text()
    assert "::: {.landscape" not in text
    assert ":::" not in text

@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_wrap_wide_tables_html(tmp_path):
    md = tmp_path / "html.md"
    md.write_text(
        "<table><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr></table>"
    )
    wrap_wide_tables(str(md), threshold=5)
    text = md.read_text()
    assert text.startswith("::: {.landscape cols=7}\n")
    assert text.strip().endswith(":::")
