from gitbook_worker.utils import wrap_wide_tables


def test_wrap_wide_tables_adds_landscape(tmp_path):
    md = tmp_path / "wide.md"
    md.write_text("|A|B|C|D|E|F|G|\n|--|--|--|--|--|--|--|\n|1|2|3|4|5|6|7|\n")
    wrap_wide_tables(str(md), threshold=5)
    text = md.read_text()
    assert text.startswith("\\begin{landscape}\n")
    assert text.strip().endswith("\\end{landscape}")


def test_wrap_wide_tables_ignores_narrow(tmp_path):
    md = tmp_path / "narrow.md"
    md.write_text("|A|B|\n|--|--|\n|1|2|\n")
    wrap_wide_tables(str(md), threshold=5)
    text = md.read_text()
    assert "\\begin{landscape}" not in text
    assert "\\end{landscape}" not in text
