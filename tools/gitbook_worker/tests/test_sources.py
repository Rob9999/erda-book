import gitbook_worker


def test_header_pattern_matches_multiple_languages():
    pattern = gitbook_worker.get_language_dependent_header_pattern_for_sources()
    assert pattern.match("## Quellen")
    assert pattern.match("## Sources")


def test_extract_sources_with_english_header(tmp_path):
    md = tmp_path / "test.md"
    md.write_text("# T\n\n## Sources\n1. Example https://example.com\n")
    result = gitbook_worker.extract_sources_of_a_md_file_to_dict(str(md))
    assert result[str(md)]
