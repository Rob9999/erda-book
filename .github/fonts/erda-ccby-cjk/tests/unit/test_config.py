from pathlib import Path

import pytest

from generator.config import (
    BuildConfig,
    CharacterConfig,
    FontConfig,
    FontMetadata,
    GridConfig,
    load_config,
)


def test_grid_and_metadata_validation():
    grid = GridConfig(em=1000, pixels=16)
    grid.validate()
    assert grid.cell == grid.margin

    with pytest.raises(ValueError):
        GridConfig(em=0).validate()
    with pytest.raises(ValueError):
        GridConfig(pixels=7).validate()

    metadata = FontMetadata(family_name="ERDA CC-BY CJK", version="1.0.1")
    metadata.validate()
    with pytest.raises(ValueError):
        FontMetadata(family_name="", version="1.0.1").validate()
    with pytest.raises(ValueError):
        FontMetadata(family_name="ERDA", version="").validate()


def test_build_and_character_config_validation():
    build = BuildConfig(output_filename="custom.ttf")
    build.validate()
    assert build.output_path.name == "custom.ttf"

    with pytest.raises(ValueError):
        BuildConfig(output_filename="font.otf").validate()
    with pytest.raises(ValueError):
        BuildConfig(output_filename="").validate()

    characters = CharacterConfig(
        include_hiragana=True,
        include_katakana=False,
        include_hangul_algorithmic=False,
        include_hanzi_kanji=False,
        include_punctuation=False,
    )
    characters.validate()

    with pytest.raises(ValueError):
        CharacterConfig(
            include_hiragana=False,
            include_katakana=False,
            include_hangul_algorithmic=False,
            include_hanzi_kanji=False,
            include_punctuation=False,
        ).validate()


def test_yaml_round_trip(tmp_path: Path):
    config = FontConfig()
    config.validate()

    yaml_path = tmp_path / "font-config.yaml"
    config.to_yaml(yaml_path)
    assert yaml_path.exists()

    loaded = FontConfig.from_yaml(yaml_path)
    assert loaded.grid.pixels == config.grid.pixels
    assert loaded.metadata.family_name == config.metadata.family_name
    assert loaded.build.output_filename == config.build.output_filename
    assert loaded.characters.include_hiragana is True

    config.characters.include_hiragana = False
    config.to_yaml(yaml_path)
    reloaded = load_config(yaml_path)
    assert reloaded.characters.include_hiragana is False
