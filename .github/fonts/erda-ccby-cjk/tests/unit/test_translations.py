from generator.translations import (
    CHINESE_TRADITIONAL_TRANSLATION,
    JAPANESE_TRANSLATION,
    KOREAN_TRANSLATION,
    LICENSE_TRANSLATIONS,
    get_all_translation_characters,
)


def test_translation_texts_and_characters():
    assert LICENSE_TRANSLATIONS.all_texts() == [
        JAPANESE_TRANSLATION,
        KOREAN_TRANSLATION,
        CHINESE_TRADITIONAL_TRANSLATION,
    ]

    characters = get_all_translation_characters()
    assert "本" in characters
    assert "作" in characters
    assert len(characters) == len(set(characters))


def test_translation_sets_include_expected_scripts():
    characters = LICENSE_TRANSLATIONS.all_characters()
    hiragana = [c for c in characters if 0x3040 <= ord(c) <= 0x309F]
    katakana = [c for c in characters if 0x30A0 <= ord(c) <= 0x30FF]
    hangul = [c for c in characters if 0xAC00 <= ord(c) <= 0xD7A3]
    cjk_unified = [c for c in characters if 0x4E00 <= ord(c) <= 0x9FFF]

    assert hiragana
    assert katakana
    assert hangul
    assert cjk_unified
