import os
from gitbook_worker.utils import _write_pandoc_header, EMOJI_RANGES

def test_write_pandoc_header_creates_file(tmp_path):
    md = tmp_path / "combined.md"
    md.write_text("text")
    header = _write_pandoc_header(
        str(tmp_path),
        "OpenMoji Color",
        "Sans",
        "Mono",
        "Main",
        False,
        6,
        str(md),
    )
    assert os.path.isfile(header)
    content = open(header, encoding="utf-8").read()
    assert "\\usepackage{fontspec}" in content
    assert "\\setsansfont{Sans}" in content
    assert "\\setmonofont{Mono}" in content
    assert "\\setmainfont{Main}" in content
    expected = f"\\newfontfamily\\EmojiOne{{OpenMoji Color}}[Range={{{EMOJI_RANGES}}}]"
    assert expected in content


def test_write_pandoc_header_wrap_tables(tmp_path, monkeypatch):
    md = tmp_path / "tables.md"
    md.write_text("|A|B|C|D|E|F|G|\n|--|--|--|--|--|--|--|\n|1|2|3|4|5|6|7|\n")
    called = {}
    def fake_wrap(md_file, threshold):
        called['md'] = md_file
        called['th'] = threshold
    monkeypatch.setattr('gitbook_worker.utils.wrap_wide_tables', fake_wrap)
    header = _write_pandoc_header(
        str(tmp_path),
        "Segoe UI Emoji",
        "Sans",
        "Mono",
        "Main",
        True,
        5,
        str(md),
    )
    assert called == {'md': str(md), 'th': 5}
    content = open(header, encoding="utf-8").read()
    assert "\\usepackage{pdflscape}" in content
    assert "\\IfFontExistsTF{Segoe UI Emoji}" in content
    assert "luaotfload.add_fallback(\"mainfont\", \"Segoe UI Emoji:mode=harf\")" in content


def test_write_pandoc_header_no_emoji(tmp_path):
    md = tmp_path / "file.md"
    md.write_text("t")
    header = _write_pandoc_header(
        str(tmp_path),
        "",
        "Sans",
        "Mono",
        "Main",
        False,
        6,
        str(md),
    )
    content = open(header, encoding="utf-8").read()
    assert "EmojiOne" not in content

