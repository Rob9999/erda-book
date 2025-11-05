#!/usr/bin/env python3
"""Generate the ERDA CC BY 4.0 compliant fallback CJK font."""

from __future__ import annotations

import argparse
import os
import platform
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables.O_S_2f_2 import Panose

# Import character data from modular modules
from katakana import (
    KATAKANA_BASE,
    SMALL_KATAKANA,
    DAKUTEN,
    HANDAKUTEN,
    DAKUTEN_COMBOS,
    HANDAKUTEN_COMBOS,
)
from hangul import (
    L_PATTERNS,
    V_PATTERNS,
    T_PATTERNS,
    L_LIST,
    V_LIST,
    T_LIST,
    SBASE,
)
from hanzi import HANZI_KANJI
from punctuation import PUNCTUATION
from hiragana import HIRAGANA
from font_logger import FontBuildLogger

EM = 1000
PIXELS = 8
CELL = EM // (PIXELS + 2)
MARGIN = CELL


def _glyph_from_bitmap(bitmap: List[str]) -> Tuple[object, int]:
    pen = TTGlyphPen(None)
    rows = len(bitmap)
    cols = len(bitmap[0]) if rows else 0
    for row_index, row in enumerate(bitmap):
        for col_index, bit in enumerate(row):
            if bit != "#":
                continue
            x = MARGIN + col_index * CELL
            y = MARGIN + (rows - 1 - row_index) * CELL
            _draw_rect(pen, x, y, CELL, CELL)
    glyph = pen.glyph()
    width = (cols + 2) * CELL
    return glyph, width


def _draw_rect(pen: TTGlyphPen, x: int, y: int, w: int, h: int) -> None:
    pen.moveTo((x, y))
    pen.lineTo((x + w, y))
    pen.lineTo((x + w, y + h))
    pen.lineTo((x, y + h))
    pen.closePath()


def _merge_bitmaps(*bitmaps: Iterable[List[str]]) -> List[str]:
    width = len(bitmaps[0][0])
    height = len(bitmaps[0])
    grid = [["." for _ in range(width)] for _ in range(height)]
    for bitmap in bitmaps:
        for y, row in enumerate(bitmap):
            for x, cell in enumerate(row):
                if cell == "#":
                    grid[y][x] = "#"
    return ["".join(row) for row in grid]


def _bitmap_for_hangul(char: str) -> List[str]:
    code = ord(char)
    if not (0xAC00 <= code <= 0xD7A3):
        raise ValueError(f"Unsupported Hangul syllable: {char}")
    index = code - SBASE
    l_index = index // 588
    v_index = (index % 588) // 28
    t_index = index % 28
    l_jamo = L_LIST[l_index]
    v_jamo = V_LIST[v_index]
    t_jamo = T_LIST[t_index]

    grid = [["." for _ in range(8)] for _ in range(8)]

    def stamp(pattern: List[str], x_offset: int, y_offset: int) -> None:
        for y, row in enumerate(pattern):
            for x, val in enumerate(row):
                if val == "#":
                    gx = x_offset + x
                    gy = y_offset + y
                    if 0 <= gx < 8 and 0 <= gy < 8:
                        grid[gy][gx] = "#"

    vertical_vowels = {"ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅣ"}
    horizontal_vowels = {"ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ"}

    if v_jamo in vertical_vowels:
        stamp(L_PATTERNS[l_jamo], 0, 1)
        stamp(V_PATTERNS[v_jamo], 4, 1)
    elif v_jamo in horizontal_vowels:
        stamp(L_PATTERNS[l_jamo], 1, 0)
        stamp(V_PATTERNS[v_jamo], 1, 4)
    else:
        stamp(L_PATTERNS[l_jamo], 0, 0)
        stamp(V_PATTERNS[v_jamo], 3, 3)

    if t_jamo:
        stamp(T_PATTERNS[t_jamo], 2, 4)

    return ["".join(row) for row in grid]


JAPANESE_TRANSLATION = """
本作品のあらゆる利用・処理・再処理は、人工知能・機械学習・自動化システムによるものを含め、オープンライセンス CC BY-SA 4.0（表示・同一条件での共有）に従います。これには、派生作品、AIが生成したコンテンツ、リミックス・プロジェクト、および アルゴリズムで変換された形式が明示的に含まれます。改変されていない引用は、別ライセンスのコレクションの一部として掲載できますが、当該コンテンツは引き続き CC BY-SA 4.0 です。
""".strip()

KOREAN_TRANSLATION = """
이 저작물의 모든 이용, 처리 또는 재처리는 인공지능, 기계학습, 자동화 시스템을 통한 경우를 포함하여 오픈 라이선스 CC BY-SA 4.0 (저작자 표시, 동일조건변경허락)을 따릅니다. 이는 명시적으로 2차적 저작물, AI 생성 콘텐츠, 리믹스 프로젝트 및 알고리즘으로 변환된 형식을 포함합니다. 변경되지 않은 수록물은 다른 라이선스의 모음집에 포함될 수 있지만, 해당 콘텐츠는 CC BY-SA 4.0으로 유지됩니다.
""".strip()

CHINESE_TRADITIONAL_TRANSLATION = """
本作品的任何使用、處理或再處理——包括透過人工智慧、機器學習或自動化系統——皆須遵循開放授權 CC BY-SA 4.0（姓名標示、相同方式分享）。此授權明確涵蓋衍生作品、AI 產生的內容、重混專案及演算法轉換的格式。未經改動的收錄可作為其他授權之集合的一部分，但相關內容仍屬 CC BY-SA 4.0。
""".strip()


def _collect_characters(*texts: str) -> List[str]:
    required: set[str] = set()
    for text in texts:
        for char in text:
            if char in {"\n", "\r"}:
                continue
            if char == " ":
                continue
            required.add(char)
    return sorted(required)


REQUIRED_CHARS = _collect_characters(
    JAPANESE_TRANSLATION, KOREAN_TRANSLATION, CHINESE_TRADITIONAL_TRANSLATION
)

# Add all explicitly defined HANZI_KANJI characters
# This ensures that all characters we've carefully designed are included
for char in HANZI_KANJI.keys():
    if char not in REQUIRED_CHARS:
        REQUIRED_CHARS.append(char)
REQUIRED_CHARS.sort()


def build_font(output: str = "../true-type/erda-ccby-cjk.ttf") -> None:
    # Initialize logger
    logger = FontBuildLogger()

    try:
        logger.log_build_start(output, len(REQUIRED_CHARS))

        glyph_order = [".notdef", "space"]
        glyphs: Dict[str, object] = {}
        advance_widths: Dict[str, Tuple[int, int]] = {}
        cmap: Dict[int, str] = {32: "space"}

        notdef_glyph, notdef_width = _glyph_from_bitmap(
            [
                "########",
                "########",
                "########",
                "########",
                "########",
                "########",
                "########",
                "########",
            ]
        )
        glyphs[".notdef"] = notdef_glyph
        advance_widths[".notdef"] = (notdef_width, 0)

        space_glyph, space_width = _glyph_from_bitmap(["........"] * 8)
        glyphs["space"] = space_glyph
        advance_widths["space"] = (space_width, 0)

        def add_char(char: str, bitmap: List[str], source: str = "unknown") -> None:
            name = f"uni{ord(char):04X}"
            if name in glyphs:
                return
            glyph, width = _glyph_from_bitmap(bitmap)
            glyph_order.append(name)
            glyphs[name] = glyph
            advance_widths[name] = (width, 0)
            cmap[ord(char)] = name
            logger.track_character(char, source)
            logger.track_glyph(name, width)

        for char in REQUIRED_CHARS:
            if char in KATAKANA_BASE:
                add_char(char, KATAKANA_BASE[char], "katakana")
                continue
            if char in SMALL_KATAKANA:
                add_char(char, SMALL_KATAKANA[char], "katakana")
                continue
            if char in DAKUTEN_COMBOS:
                base = KATAKANA_BASE[DAKUTEN_COMBOS[char]]
                add_char(char, _merge_bitmaps(base, DAKUTEN), "katakana")
                continue
            if char in HANDAKUTEN_COMBOS:
                base = KATAKANA_BASE[HANDAKUTEN_COMBOS[char]]
                add_char(char, _merge_bitmaps(base, HANDAKUTEN), "katakana")
                continue
            if char in PUNCTUATION:
                add_char(char, PUNCTUATION[char], "punctuation")
                continue
            if char == "ー":
                add_char(char, KATAKANA_BASE["ー"], "katakana")
                continue
            # Check HANZI_KANJI BEFORE the CJK range fallback
            if char in HANZI_KANJI:
                add_char(char, HANZI_KANJI[char], "hanzi")
                continue
            code = ord(char)
            if 0xAC00 <= code <= 0xD7A3:
                add_char(char, _bitmap_for_hangul(char), "hangul")
                continue
            # Hiragana range (U+3040 - U+309F)
            if 0x3040 <= code <= 0x309F:
                if char in HIRAGANA:
                    add_char(char, HIRAGANA[char], "hiragana")
                    continue
                # Simple placeholder for Hiragana not explicitly defined
                hiragana_placeholder = [
                    "..####..",
                    ".#....#.",
                    "#......#",
                    "#......#",
                    "#......#",
                    "#......#",
                    ".#....#.",
                    "..####..",
                ]
                add_char(char, hiragana_placeholder, "fallback")
                continue
            # CJK Unified Ideographs (U+4E00 - U+9FFF) - common Kanji/Hanzi range
            # This MUST come AFTER the HANZI_KANJI check!
            if 0x4E00 <= code <= 0x9FFF:
                # Simple placeholder for CJK Ideographs not explicitly defined
                cjk_placeholder = [
                    "########",
                    "#......#",
                    "#..##..#",
                    "#..##..#",
                    "#..##..#",
                    "#......#",
                    "########",
                    "........",
                ]
                add_char(char, cjk_placeholder, "fallback")
                continue
            # Simple fallback for ASCII and other characters - use a placeholder
            if 0x0021 <= code <= 0x007E:  # ASCII printable range
                # Simple placeholder for now
                placeholder = [
                    "..####..",
                    ".#....#.",
                    ".#....#.",
                    ".#....#.",
                    ".#....#.",
                    ".#....#.",
                    ".#....#.",
                    "..####..",
                ]
                add_char(char, placeholder, "fallback")
                continue
            # Numbers 0-9
            if 0x0030 <= code <= 0x0039:
                number_placeholder = [
                    "..####..",
                    ".##..##.",
                    "#....#.#",
                    "#....#.#",
                    "#....#.#",
                    "#....#.#",
                    ".##..##.",
                    "..####..",
                ]
                add_char(char, number_placeholder, "fallback")
                continue
            # Fullwidth forms (U+FF00 - U+FFEF) - commonly used in CJK text
            if 0xFF00 <= code <= 0xFFEF:
                fullwidth_placeholder = [
                    "..####..",
                    ".#....#.",
                    "#......#",
                    "#......#",
                    "#......#",
                    "#......#",
                    ".#....#.",
                    "..####..",
                ]
                add_char(char, fullwidth_placeholder, "fallback")
                continue
            logger.error(f"Unsupported character {char!r} (U+{code:04X})")
            raise ValueError(f"Unsupported character {char!r} (U+{code:04X})")

        ascent = int(EM * 0.8)
        descent = -int(EM * 0.2)

        fb = FontBuilder(EM, isTTF=True)
        fb.setupGlyphOrder(glyph_order)
        fb.setupCharacterMap(cmap)
        fb.setupGlyf(glyphs)
        fb.setupHorizontalMetrics(advance_widths)
        fb.setupHorizontalHeader(ascent=ascent, descent=descent)
        panose = Panose()
        panose.bFamilyType = 2
        panose.bSerifStyle = 11
        panose.bWeight = 5
        panose.bProportion = 9
        panose.bContrast = 3
        panose.bStrokeVariation = 9
        panose.bArmStyle = 2
        panose.bLetterForm = 3
        panose.bMidline = 2
        panose.bXHeight = 4
        fb.setupOS2(
            sTypoAscender=ascent,
            sTypoDescender=descent,
            sTypoLineGap=200,
            usWinAscent=ascent,
            usWinDescent=-descent,
            bFamilyClass=0,
            panose=panose,
            ulUnicodeRange1=0x00000001,
            ulUnicodeRange2=0x00000000,
            ulUnicodeRange3=0x00000000,
            ulUnicodeRange4=0x00000000,
            fsSelection=0x40,
            usWeightClass=400,
            usWidthClass=5,
            ySubscriptXSize=650,
            ySubscriptYSize=699,
            ySubscriptXOffset=0,
            ySubscriptYOffset=140,
            ySuperscriptXSize=650,
            ySuperscriptYSize=699,
            ySuperscriptXOffset=0,
            ySuperscriptYOffset=479,
            yStrikeoutSize=50,
            yStrikeoutPosition=250,
            sxHeight=500,
            sCapHeight=700,
        )
        # Generate version string with timestamp to force cache refresh
        import datetime

        timestamp = datetime.datetime.now().strftime("%Y%m%d.%H%M%S")
        version_string = f"Version 1.0.{timestamp}"

        fb.setupNameTable(
            {
                "familyName": "ERDA CC-BY CJK",
                "styleName": "Regular",
                "psName": "ERDACCbyCJK-Regular",
                "fullName": "ERDA CC-BY CJK Regular",
                "uniqueFontIdentifier": f"ERDA CC-BY CJK Regular {timestamp}",
                "version": version_string,
            }
        )
        fb.setupPost()
        fb.setupMaxp()
        fb.save(output)

        # Log build completion
        file_size = Path(output).stat().st_size
        logger.log_build_complete(output, file_size)

        return output

    except Exception as e:
        logger.log_build_failed(str(e))
        raise


def refresh_font_cache_linux() -> bool:
    """
    Refresh the Linux font cache using fc-cache.
    Returns True if successful, False otherwise.
    """
    if platform.system() != "Linux":
        print("⚠ This font cache refresh method is for Linux only.")
        return False

    print("🔄 Refreshing Linux font cache...")

    try:
        # Run fc-cache to rebuild font information cache
        result = subprocess.run(
            ["fc-cache", "-f", "-v"],
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode == 0:
            print("✓ fc-cache executed successfully")
            if result.stdout:
                # Show relevant output lines
                lines = result.stdout.strip().split("\n")
                for line in lines[-5:]:  # Show last 5 lines
                    if line.strip():
                        print(f"  → {line}")
            return True
        else:
            print(f"✗ fc-cache failed with return code {result.returncode}")
            if result.stderr:
                print(f"  Error: {result.stderr}")
            return False

    except FileNotFoundError:
        print("✗ fc-cache not found")
        print("  Please install fontconfig:")
        print("    Ubuntu/Debian: sudo apt install fontconfig")
        print("    Fedora/RHEL:   sudo dnf install fontconfig")
        print("    Arch:          sudo pacman -S fontconfig")
        return False
    except subprocess.TimeoutExpired:
        print("✗ fc-cache timed out")
        return False
    except Exception as e:
        print(f"✗ Error running fc-cache: {e}")
        return False


def refresh_font_cache_macos() -> bool:
    """
    Refresh the macOS font cache.
    Returns True if successful, False otherwise.
    """
    if platform.system() != "Darwin":
        print("⚠ This font cache refresh method is for macOS only.")
        return False

    print("🔄 Refreshing macOS font cache...")

    try:
        # macOS doesn't need explicit cache refresh in most cases
        # But we can use atsutil to clear caches if needed
        result = subprocess.run(
            ["atsutil", "databases", "-remove"],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode == 0:
            print("✓ Font database cleared")
            # Restart font server
            subprocess.run(
                ["atsutil", "server", "-shutdown"],
                capture_output=True,
                timeout=10,
            )
            subprocess.run(
                ["atsutil", "server", "-ping"],
                capture_output=True,
                timeout=10,
            )
            print("✓ Font server restarted")
            return True
        else:
            print("ℹ atsutil not available or failed")
            print("  Font should still be available after application restart")
            return False

    except FileNotFoundError:
        print("ℹ atsutil not found (normal on newer macOS versions)")
        print("  Font cache is managed automatically by the system")
        return True  # Not an error on macOS
    except Exception as e:
        print(f"⚠ Error: {e}")
        return False


def refresh_font_cache() -> bool:
    """
    Refresh the font cache for the current platform.
    Returns True if successful, False otherwise.
    """
    system = platform.system()

    if system == "Windows":
        return refresh_font_cache_windows()
    elif system == "Linux":
        return refresh_font_cache_linux()
    elif system == "Darwin":
        return refresh_font_cache_macos()
    else:
        print(f"⚠ Font cache refresh not supported on {system}")
        return False


def refresh_font_cache_windows() -> bool:
    """
    Refresh the Windows font cache by:
    1. Broadcasting WM_FONTCHANGE message
    2. Deleting Windows font cache files
    3. Restarting FontCache service (if elevated)
    4. Running fc-cache if available

    Returns True if successful, False otherwise.
    """
    if platform.system() != "Windows":
        print("⚠ Font cache refresh is only supported on Windows.")
        return False

    print("🔄 Refreshing Windows font cache...")
    success_count = 0

    try:
        # Method 1: Broadcast WM_FONTCHANGE message
        import ctypes
        from ctypes import wintypes

        user32 = ctypes.WinDLL("user32", use_last_error=True)
        SendMessageW = user32.SendMessageW
        SendMessageW.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            wintypes.LPARAM,
        ]
        SendMessageW.restype = wintypes.LPARAM

        HWND_BROADCAST = 0xFFFF
        WM_FONTCHANGE = 0x001D

        result = SendMessageW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0)
        print(f"  ✓ WM_FONTCHANGE broadcast sent (result: {result})")
        success_count += 1

    except Exception as e:
        print(f"  ✗ WM_FONTCHANGE broadcast failed: {e}")

    try:
        # Method 2: Delete Windows font cache files
        import glob

        cache_patterns = [
            (os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts"), ["*.fot"]),
            (
                os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Caches"),
                ["*.dat", "*.tmp"],
            ),
            (
                os.path.expandvars(
                    r"%WINDIR%\ServiceProfiles\LocalService\AppData\Local\FontCache"
                ),
                ["*.dat", "*.tmp", "*.fot"],
            ),
            (
                os.path.expandvars(
                    r"%WINDIR%\ServiceProfiles\LocalService\AppData\Local\FontCache-S-1-5-21"
                ),
                ["*.dat", "*.tmp"],
            ),
            (os.path.expandvars(r"%TEMP%"), ["font*.tmp"]),
        ]

        deleted_count = 0
        for cache_dir, patterns in cache_patterns:
            if not os.path.exists(cache_dir):
                continue

            print(f"  📁 Checking: {cache_dir}")
            for pattern in patterns:
                for cache_file in glob.glob(os.path.join(cache_dir, pattern)):
                    try:
                        os.remove(cache_file)
                        print(f"    ✓ Deleted: {os.path.basename(cache_file)}")
                        deleted_count += 1
                    except (PermissionError, OSError) as e:
                        print(
                            f"    ⚠ Cannot delete {os.path.basename(cache_file)}: {e}"
                        )

        if deleted_count > 0:
            print(f"  ✓ Deleted {deleted_count} cache file(s)")
            success_count += 1
        else:
            print(f"  ℹ No cache files found (may already be clean)")

    except Exception as e:
        print(f"  ⚠ Cache file deletion failed: {e}")

    try:
        # Method 3: Restart FontCache service (requires admin)
        import ctypes

        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if is_admin:
            print(f"  🔧 Restarting FontCache service...")

            # Check if service is running first
            check_result = subprocess.run(
                ["sc", "query", "FontCache"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=5,
            )

            service_running = "RUNNING" in check_result.stdout

            if service_running:
                # Stop service
                result_stop = subprocess.run(
                    ["net", "stop", "FontCache"],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=10,
                )
                if result_stop.returncode == 0:
                    print(f"  ✓ FontCache service stopped")
                time.sleep(1)

            # Start service
            result_start = subprocess.run(
                ["net", "start", "FontCache"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=10,
            )

            # Check for "already started" error (not a real error)
            if result_start.returncode == 0:
                print(f"  ✓ FontCache service started")
                success_count += 1
            elif result_start.returncode == 2 and "2182" in result_start.stderr:
                # Service already running - this is fine
                print(f"  ✓ FontCache service already running")
                success_count += 1
            else:
                stderr_msg = (
                    result_start.stderr.strip()
                    if result_start.stderr
                    else "Unknown error"
                )
                print(f"  ⚠ FontCache restart issue: {stderr_msg}")
        else:
            print(f"  ℹ Not admin - skipping FontCache service restart")
            print(f"    (Run as Administrator for full cache refresh)")

    except Exception as e:
        print(f"  ⚠ FontCache service restart failed: {e}")

    try:
        # Method 4: Run fc-cache if available (for apps using fontconfig)
        result = subprocess.run(
            ["fc-cache", "-f", "-v"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
        )
        if result.returncode == 0:
            print("  ✓ fc-cache executed successfully")
            success_count += 1
        else:
            print("  ℹ fc-cache not available (normal on Windows)")
    except FileNotFoundError:
        print("  ℹ fc-cache not found (not required on Windows)")
    except Exception as e:
        print(f"  ⚠ fc-cache execution failed: {e}")

    # Summary
    print(f"\n📊 Cache refresh summary: {success_count}/4 methods succeeded")

    if success_count > 0:
        print("✓ Font cache refresh completed")
        print("\n⚠ Important next steps:")
        print("  1. Close and reopen applications (browsers, PDF readers, Office)")
        print("  2. Clear browser caches (Ctrl+Shift+Delete)")
        print("  3. Consider restarting Windows for system-wide changes")
        return True
    else:
        print("⚠ Font cache refresh had limited success")
        print("  Try running as Administrator or restart Windows manually")
        return False
        print("  Manual steps:")
        print("  1. Close all applications using the font")
        print(
            "  2. Restart Windows Font Cache service: net stop FontCache & net start FontCache"
        )
        print("  3. Or restart your computer")

    return success


def install_font_windows(font_path: str) -> bool:
    """
    Install the font file to the Windows user fonts directory.
    Returns True if successful, False otherwise.
    """
    if platform.system() != "Windows":
        print("⚠ Font installation is only supported on Windows.")
        return False

    try:
        import ctypes
        from ctypes import wintypes
        import shutil
        import time

        # Get the user fonts directory
        fonts_dir = Path(os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts"))
        fonts_dir.mkdir(parents=True, exist_ok=True)

        # Copy font file
        font_path_obj = Path(font_path)
        dest_path = fonts_dir / font_path_obj.name

        print(f"📦 Installing font to: {dest_path}")

        # Try to remove existing font file if it exists
        if dest_path.exists():
            print(f"  ℹ Existing font file found, attempting to replace...")
            try:
                # First, try to unload the font from Windows
                gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)
                RemoveFontResourceW = gdi32.RemoveFontResourceW
                RemoveFontResourceW.argtypes = [wintypes.LPCWSTR]
                RemoveFontResourceW.restype = wintypes.BOOL

                # Try to unload the existing font
                RemoveFontResourceW(str(dest_path))
                time.sleep(0.1)  # Brief pause to let Windows release the file

                # Try to delete the file
                dest_path.unlink()
                print(f"  ✓ Removed existing font file")
            except Exception as e:
                print(f"  ⚠ Could not remove existing font: {e}")
                print(f"  → Trying to overwrite...")

        # Copy the new font file (with retry logic)
        max_retries = 3
        for attempt in range(max_retries):
            try:
                shutil.copy2(font_path, dest_path)
                break
            except PermissionError as e:
                if attempt < max_retries - 1:
                    print(f"  ⚠ Copy attempt {attempt + 1} failed, retrying...")
                    time.sleep(0.5)
                else:
                    raise e

        # Load gdi32.dll
        gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)

        # Define the AddFontResourceW function
        AddFontResourceW = gdi32.AddFontResourceW
        AddFontResourceW.argtypes = [wintypes.LPCWSTR]
        AddFontResourceW.restype = ctypes.c_int

        # Add the font resource
        result = AddFontResourceW(str(dest_path))
        if result > 0:
            print(f"✓ Font installed successfully ({result} font(s) added)")

            # Register in registry for persistent installation
            try:
                import winreg

                font_name = "ERDA CC-BY CJK (TrueType)"
                reg_path = r"Software\Microsoft\Windows NT\CurrentVersion\Fonts"

                with winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_SET_VALUE
                ) as key:
                    winreg.SetValueEx(
                        key, font_name, 0, winreg.REG_SZ, font_path_obj.name
                    )
                    print(f"✓ Font registered in user registry")

            except Exception as e:
                print(f"⚠ Registry registration failed: {e}")
                print("  Font will be available for this session only")

            return True
        else:
            print(f"⚠ AddFontResourceW returned {result}")
            return False

    except PermissionError as e:
        print(f"✗ Font installation failed: Permission denied")
        print(f"  The font file may be in use by another application.")
        print(f"  Please try the following:")
        print(f"  1. Close all applications that might be using the font")
        print(f"  2. Wait a few seconds and try again")
        print(f"  3. If the problem persists, restart your computer")
        return False
    except Exception as e:
        print(f"✗ Font installation failed: {e}")
        return False


def install_font_linux(font_path: str) -> bool:
    """
    Install the font file to the Linux user fonts directory.
    Returns True if successful, False otherwise.
    """
    if platform.system() != "Linux":
        print("⚠ This installation method is for Linux only.")
        return False

    try:
        import shutil

        # Get the user fonts directory (~/.local/share/fonts)
        fonts_dir = Path.home() / ".local" / "share" / "fonts"
        fonts_dir.mkdir(parents=True, exist_ok=True)

        # Copy font file
        font_path_obj = Path(font_path)
        dest_path = fonts_dir / font_path_obj.name

        print(f"📦 Installing font to: {dest_path}")

        # Remove existing font if it exists
        if dest_path.exists():
            print(f"  ℹ Existing font file found, replacing...")
            dest_path.unlink()

        # Copy the new font file
        shutil.copy2(font_path, dest_path)
        print(f"✓ Font copied successfully")

        # Update font cache
        print(f"  → Running fc-cache to update font cache...")
        result = subprocess.run(
            ["fc-cache", "-f", str(fonts_dir)],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode == 0:
            print(f"✓ Font cache updated")
            print(f"✓ Font installed successfully")
            return True
        else:
            print(f"⚠ fc-cache returned {result.returncode}")
            print(f"  Font may still be available after application restart")
            return True  # File was copied, so partial success

    except FileNotFoundError:
        print(f"⚠ fc-cache not found")
        print(f"  Font was copied but cache not updated")
        print(f"  Install fontconfig: sudo apt install fontconfig")
        return True  # File was copied
    except Exception as e:
        print(f"✗ Font installation failed: {e}")
        return False


def install_font_macos(font_path: str) -> bool:
    """
    Install the font file to the macOS user fonts directory.
    Returns True if successful, False otherwise.
    """
    if platform.system() != "Darwin":
        print("⚠ This installation method is for macOS only.")
        return False

    try:
        import shutil

        # Get the user fonts directory (~/Library/Fonts)
        fonts_dir = Path.home() / "Library" / "Fonts"
        fonts_dir.mkdir(parents=True, exist_ok=True)

        # Copy font file
        font_path_obj = Path(font_path)
        dest_path = fonts_dir / font_path_obj.name

        print(f"📦 Installing font to: {dest_path}")

        # Remove existing font if it exists
        if dest_path.exists():
            print(f"  ℹ Existing font file found, replacing...")
            dest_path.unlink()

        # Copy the new font file
        shutil.copy2(font_path, dest_path)
        print(f"✓ Font copied successfully")
        print(f"✓ Font installed successfully")
        print(f"  ℹ Font will be available after restarting applications")

        return True

    except Exception as e:
        print(f"✗ Font installation failed: {e}")
        return False


def install_font(font_path: str) -> bool:
    """
    Install the font file for the current platform.
    Returns True if successful, False otherwise.
    """
    system = platform.system()

    if system == "Windows":
        return install_font_windows(font_path)
    elif system == "Linux":
        return install_font_linux(font_path)
    elif system == "Darwin":
        return install_font_macos(font_path)
    else:
        print(f"⚠ Font installation not supported on {system}")
        return False


def main():
    """Main entry point with CLI argument parsing."""
    parser = argparse.ArgumentParser(
        description="Build the ERDA CC BY 4.0 compliant CJK fallback font",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_ccby_cjk_font.py
  python build_ccby_cjk_font.py --output custom-font.ttf
  python build_ccby_cjk_font.py --refresh-cache
  python build_ccby_cjk_font.py --install --refresh-cache
        """,
    )

    parser.add_argument(
        "-o",
        "--output",
        default="../true-type/erda-ccby-cjk.ttf",
        help="Output font file path (default: ../true-type/erda-ccby-cjk.ttf)",
    )

    parser.add_argument(
        "-r",
        "--refresh-cache",
        action="store_true",
        help="Refresh the Windows font cache after building",
    )

    parser.add_argument(
        "-i",
        "--install",
        action="store_true",
        help="Install the font to Windows user fonts directory",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    try:
        print("=" * 60)
        print("ERDA CC BY 4.0 CJK Font Builder")
        print("=" * 60)
        print()

        # Build the font
        print("🔨 Building font...")
        output_path = build_font(args.output)
        print()

        # Install if requested
        if args.install:
            if install_font(output_path):
                print()
            else:
                print("⚠ Font installation failed")
                print()

        # Refresh cache if requested
        if args.refresh_cache:
            refresh_font_cache()
            print()

        print("=" * 60)
        print("✓ Font build completed successfully")
        print("=" * 60)
        print()
        print(f"Output file: {Path(output_path).absolute()}")
        print(f"File size: {os.path.getsize(output_path):,} bytes")
        print()

        if not args.refresh_cache and not args.install:
            system = platform.system()
            print("💡 Tip: Use --refresh-cache to refresh the font cache")
            if system == "Windows":
                print("💡 Tip: Use --install to install the font to Windows")
            elif system == "Linux":
                print(
                    "💡 Tip: Use --install to install the font to ~/.local/share/fonts"
                )
            elif system == "Darwin":
                print("💡 Tip: Use --install to install the font to ~/Library/Fonts")
            print()

        return 0

    except KeyboardInterrupt:
        print("\n\n⚠ Build interrupted by user")
        return 130
    except Exception as e:
        print(f"\n✗ Error: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
