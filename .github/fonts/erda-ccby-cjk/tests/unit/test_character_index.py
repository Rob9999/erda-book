from generator.character_index import (
    CharacterIndex,
    get_character_bitmap,
    get_character_index,
    lookup_character,
)
from hanzi import HANZI_KANJI
from hiragana import HIRAGANA
from katakana import DAKUTEN_COMBOS, SMALL_KATAKANA
from punctuation import PUNCTUATION


def test_lookup_and_bitmap_sources():
    index = CharacterIndex()

    info = index.lookup("あ")
    assert info is not None
    assert info.source == "hiragana"
    assert index.get_bitmap("あ") == info.bitmap
    assert get_character_bitmap("あ") == info.bitmap

    dakuten_char = next(iter(DAKUTEN_COMBOS.keys()))
    dakuten_info = lookup_character(dakuten_char)
    assert dakuten_info is not None
    assert dakuten_info.sub_source == "dakuten"

    punctuation_char = next(iter(PUNCTUATION.keys()))
    assert index.has_character(punctuation_char)
    assert index.get_bitmap(punctuation_char) is not None


def test_stats_and_character_listing_are_consistent():
    index = CharacterIndex()
    stats = index.stats()

    assert stats["hiragana"] == len(HIRAGANA)
    assert stats["katakana"] >= len(SMALL_KATAKANA)
    assert stats["hanzi"] == len(HANZI_KANJI)
    assert stats["punctuation"] == len(PUNCTUATION)
    assert stats["total"] == len(index.list_characters())

    hiragana_chars = index.list_characters("hiragana")
    assert "あ" in hiragana_chars
    assert all(char in HIRAGANA for char in hiragana_chars)


def test_singleton_reuses_index_instance():
    first = get_character_index()
    second = get_character_index()
    assert first is second
