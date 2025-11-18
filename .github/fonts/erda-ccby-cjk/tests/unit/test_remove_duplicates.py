import importlib.util
import sys
from pathlib import Path
from types import ModuleType

TOOLS_ROOT = Path(__file__).resolve().parents[2] / "tools"
MODULE_PATH = TOOLS_ROOT / "remove_duplicates.py"


def load_remove_duplicates() -> ModuleType:
    tools_package = ModuleType("tools")
    tools_package.__path__ = [str(TOOLS_ROOT)]  # type: ignore[attr-defined]
    sys.modules.setdefault("tools", tools_package)

    spec = importlib.util.spec_from_file_location("tools.remove_duplicates", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules["tools.remove_duplicates"] = module
    spec.loader.exec_module(module)  # type: ignore[call-arg]
    return module


remove_duplicates_module = load_remove_duplicates()
find_duplicates = remove_duplicates_module.find_duplicates
remove_duplicates = remove_duplicates_module.remove_duplicates


def test_find_duplicates_detects_repeated_characters(tmp_path: Path):
    content = '\n'.join(
        [
            "HANZI_KANJI = {",
            '    "人": [1],',
            '    "人": [2],',
            '    "力": [3],',
            "}",
        ]
    )
    hanzi_file = tmp_path / "hanzi.py"
    hanzi_file.write_text(content, encoding="utf-8")

    duplicates = find_duplicates(hanzi_file)
    assert set(duplicates.keys()) == {"人"}
    assert len(duplicates["人"]) == 2

    # Dry-run keeps file intact
    assert remove_duplicates(hanzi_file, dry_run=True) == 1
    assert hanzi_file.read_text(encoding="utf-8").count('"人"') == 2

    # Fix run removes the first occurrence but keeps the last
    assert remove_duplicates(hanzi_file, dry_run=False) == 0
    remaining = hanzi_file.read_text(encoding="utf-8")
    assert remaining.count('"人"') == 1
    assert '"力"' in remaining
