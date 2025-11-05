# ERDA CC-BY CJK Font# ERDA CC-BY CJK Font



## 📁 VerzeichnisstrukturThis directory contains a minimalist fallback font that covers the characters

used in the Japanese, Korean, and Traditional Chinese licence translations of 

```the ERDA book. The font was created specifically for this repository and is 

.github/fonts/released under the Creative Commons Attribution 4.0 International Licence (CC BY 4.0).

├── README.md                    # Diese Datei

├── build_ccby_cjk_font.py      # Hauptskript zum Bauen der Font* `erda-ccby-cjk.ttf` – generated font file.

├── erda-ccby-cjk.ttf           # Die finale Font (CC BY 4.0)* `build_ccby_cjk_font.py` – generator script that converts handcrafted

│  bitmap patterns into TrueType outlines.

├── docs/                        # Dokumentation* `FONT-CACHE-TROUBLESHOOTING.md` – comprehensive guide to Windows font caches

│   ├── README-fonts.md         # Ausführliche Font-Dokumentation* `CODE-REVIEW-REPORT.md` – detailed code review and cache issues analysis

│   ├── LICENSE.txt             # CC BY 4.0 Lizenz* `clear-all-caches.ps1` – PowerShell script for admin-level cache clearing

│   ├── CODE-REVIEW-REPORT.md   # Code-Review-Bericht* `test-font-version.html` – HTML page to verify font version and rendering

│   └── FONT-CACHE-TROUBLESHOOTING.md  # Cache-Troubleshooting

│## Quick Start

├── scripts/                     # Hilfsskripte

│   ├── clear-all-caches.ps1    # Windows Font Cache löschenBuild the font with default settings:

│   └── test-admin-cache-refresh.ps1  # Admin-Cache-Refresh-Test

│```bash

├── tests/                       # Test-Dateienpython build_ccby_cjk_font.py

│   ├── test_chars.py           # Testet ob Zeichen in Font enthalten```

│   ├── test_dict.py            # Testet HANZI_KANJI Dictionary

│   ├── debug_chars.py          # Debug-Script für ZeichenBuild and refresh the font cache (recommended):

│   ├── check_translation.py    # Prüft Translation-Strings

│   └── test-font-version.html  # HTML-Testseite für Font-Anzeige```bash

│python build_ccby_cjk_font.py --refresh-cache

└── build/                       # Build-Artefakte (nicht versioniert)```

    ├── erda-ccby-cjk-test.ttf  # Test-Versionen

    └── __pycache__/            # Python CacheBuild, install, and refresh (full setup):

```

```bash

## 🚀 Schnellstartpython build_ccby_cjk_font.py --install --refresh-cache

```

### Font bauen

**⚠️ Font Not Updating?** See [FONT-CACHE-TROUBLESHOOTING.md](FONT-CACHE-TROUBLESHOOTING.md) for comprehensive cache clearing instructions.

```bash

python build_ccby_cjk_font.py --output erda-ccby-cjk.ttf --refresh-cache## Usage

```

```

### Font installierenusage: build_ccby_cjk_font.py [-h] [-o OUTPUT] [-r] [-i] [-v]



```bashoptions:

python build_ccby_cjk_font.py --install --refresh-cache  -h, --help            show this help message and exit

```  -o OUTPUT, --output OUTPUT

                        Output font file path (default: erda-ccby-cjk.ttf)

### Tests ausführen  -r, --refresh-cache   Refresh the font cache after building

  -i, --install         Install the font to user fonts directory

```bash  -v, --verbose         Enable verbose output

cd tests```

python test_chars.py      # Testet japanische Kanji

python test_dict.py       # Testet Dictionary-Vollständigkeit## Features

```

### Automatic Font Versioning 🎯 NEW!

## 📊 Font-Details

Every build generates a unique font version with timestamp:

- **Version:** Dynamisch mit Timestamp (z.B. `Version 1.0.20251105.115845`)- **Format:** `Version 1.0.YYYYMMDD.HHMMSS`

- **Größe:** ~86 KB- **Example:** `Version 1.0.20251104.200610`

- **Zeichen:** ~3300+ Glyphen- **Purpose:** Forces Windows to invalidate font cache

  - Katakana (vollständig)- **Benefit:** Ensures applications load new font version

  - Hiragana (Platzhalter)

  - Hangul (11,172 Zeichen algorithmisch)**Verify Font Version:**

  - Kanji/Hanzi (107 handdesignte + CJK-Platzhalter)- Right-click `erda-ccby-cjk.ttf` → Properties → Details → "Product version"

  - Interpunktion und Symbole- Open `test-font-version.html` in browser (shows loaded version)



## 🛠️ Entwicklung### Platform Support



### Font erweiternThe script supports automatic font installation and cache refresh on:



Neue Kanji/Hanzi-Zeichen in `build_ccby_cjk_font.py` zum `HANZI_KANJI` Dictionary hinzufügen:- **Windows**: User fonts directory + registry registration + cache clearing

- **Linux**: `~/.local/share/fonts` + fc-cache

```python- **macOS**: `~/Library/Fonts` (system-managed cache)

"新": [  # new/新

    "########",### Character Support

    "#......#",

    "..####..",The font includes support for:

    "...##...",

    "########",- **Japanese**: Full Katakana, Hiragana (placeholder), and common Kanji

    "#.#..#.#",- **Korean**: Complete Hangul syllable composition (U+AC00-U+D7A3)

    "#.####.#",- **Traditional Chinese**: 100+ handcrafted Hanzi characters + fallback glyphs

    "########",- **Punctuation**: CJK and ASCII punctuation marks

],- **ASCII**: Basic Latin characters (fallback placeholders)

```

### Font Cache Management (Enhanced) 🔧 NEW!

Alle Zeichen im `HANZI_KANJI` Dictionary werden automatisch in die Font integriert.

**Windows Cache Refresh (4-Stage Approach):**

### Cache-Probleme beheben

The `--refresh-cache` option now uses **4 methods** to clear Windows font caches:

```powershell

# Windows: Alle Caches löschen (als Admin)1. **WM_FONTCHANGE Broadcast** ✅ (Always)

.\scripts\clear-all-caches.ps1   - Notifies all running applications of font changes

   - Works without administrator privileges

# Oder: FontCache-Service neu starten   - Immediate effect for well-behaved applications

.\scripts\test-admin-cache-refresh.ps1

```2. **Cache File Deletion** ✅ (Always attempted)

   - Deletes cache files from 7 locations:

## 📜 Lizenz     * User Font Cache (`%LOCALAPPDATA%\Microsoft\Windows\Fonts`)

     * Windows Caches (`%LOCALAPPDATA%\Microsoft\Windows\Caches`)

**CC BY 4.0** - Creative Commons Attribution 4.0 International     * FontCache Service (`%WINDIR%\ServiceProfiles\LocalService\...`)

     * Temp Caches (`%TEMP%\font*.tmp`)

Siehe [docs/LICENSE.txt](docs/LICENSE.txt) für Details.     * And more...

   - Reports deleted file count

## 🔗 Integration   - Handles permission errors gracefully



Die Font wird in `publish.yml` referenziert:3. **FontCache Service Restart** ⚠️ (Requires Administrator)

   - Stops and restarts Windows FontCache service

```yaml   - Clears service-level font cache

fonts:   - Only runs when script executed as Administrator

  - name: ERDA CC-BY CJK   - Graceful fallback if not admin

    path: .github/fonts/erda-ccby-cjk.ttf

4. **fontconfig (fc-cache)** ℹ️ (Optional)

publish:   - Runs if fc-cache available (MSYS2/Cygwin/WSL)

  - pdf_options:   - Updates fontconfig cache for cross-platform apps

      mainfont_fallback: "OpenMoji Color:mode=harf; [.github/fonts/erda-ccby-cjk.ttf]:mode=harf"   - Not required on pure Windows

```

**Success Metrics:**

## 📝 Weitere Informationen```

📊 Cache refresh summary: X/4 methods succeeded

Siehe [docs/README-fonts.md](docs/README-fonts.md) für ausführliche Dokumentation.✓ Font cache refresh completed


⚠ Important next steps:
  1. Close and reopen applications (browsers, PDF readers, Office)
  2. Clear browser caches (Ctrl+Shift+Delete)
  3. Consider restarting Windows for system-wide changes
```

**Linux:**
- Runs `fc-cache -f -v` to rebuild the font information cache
- Updates only the user font directory for fast refresh
- Requires `fontconfig` package (usually pre-installed)

**macOS:**
- Attempts to use `atsutil` for cache management (if available)
- System automatically manages font cache on newer versions
- Font available after application restart

### Font Installation

**Windows:**
The `--install` option:

1. Copies the font to `%LOCALAPPDATA%\Microsoft\Windows\Fonts`
2. Registers the font using Windows API (`AddFontResourceW`)
3. Adds registry entry for persistent installation
4. Makes the font available system-wide without administrator privileges

**Linux:**
The `--install` option:

1. Copies the font to `~/.local/share/fonts/`
2. Runs `fc-cache` to update the font cache
3. Font becomes available immediately for new applications
4. No root privileges required

**macOS:**
The `--install` option:

1. Copies the font to `~/Library/Fonts/`
2. System automatically detects the new font
3. Font available after restarting applications
4. No administrator privileges required

**Note**: If the font is already installed and in use by an application, the script
will attempt to unload and replace it. If this fails, close all applications using
the font and try again.

## Troubleshooting

### Windows: "Permission denied" Error

If you encounter a permission error during installation:

1. Close all applications that might be using the font (browsers, PDF readers, etc.)
2. Wait a few seconds for Windows to release file locks
3. Run the installation command again
4. If the problem persists, restart your computer

The script includes automatic retry logic and will attempt to:
- Unload the existing font from Windows
- Remove the old font file
- Install the new version with multiple retry attempts

### Linux: "fc-cache not found"

Install the fontconfig package:

```bash
# Ubuntu/Debian
sudo apt install fontconfig

# Fedora/RHEL/CentOS
sudo dnf install fontconfig

# Arch Linux
sudo pacman -S fontconfig

# Alpine Linux
sudo apk add fontconfig
```

### Linux: Font Not Showing Up

1. Verify the font was copied:
   ```bash
   ls -l ~/.local/share/fonts/erda-ccby-cjk.ttf
   ```

2. Manually refresh font cache:
   ```bash
   fc-cache -f -v
   ```

3. Verify font is detected:
   ```bash
   fc-list | grep "ERDA CC-BY CJK"
   ```

4. Restart your application

### macOS: Font Not Appearing

If the font doesn't appear in applications after installation:

1. Verify the font was copied:
   ```bash
   ls -l ~/Library/Fonts/erda-ccby-cjk.ttf
   ```

2. Open Font Book app and verify the font is listed

3. Restart the application trying to use the font

4. In some cases, you may need to log out and log back in

### General: Font Not Appearing

If the font doesn't appear in applications after installation:

1. Run with `--refresh-cache` option
2. Restart the application
3. Check if the font is listed in system font settings:
   - **Windows**: Settings → Personalization → Fonts
   - **Linux**: `fc-list | grep ERDA`
   - **macOS**: Font Book app
4. As a last resort, restart your computer

## Technical Details

The generator script embeds the exact Japanese (Katakana/Hiragana), Korean 
(Hangul), and Traditional Chinese (Hanzi) texts used in Anhang J Kapitel J.8
of the ERDA book, guaranteeing that any future update of those strings
automatically refreshes the glyph set.

Character ranges:
- **Katakana**: U+30A0-U+30FF
- **Hiragana**: U+3040-U+309F
- **Hangul**: U+AC00-U+D7A3
- **CJK Ideographs**: U+4E00-U+9FFF
- **Fullwidth Forms**: U+FF00-U+FFEF

### Platform-Specific Details

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| **Font Location** | `%LOCALAPPDATA%\Microsoft\Windows\Fonts` | `~/.local/share/fonts` | `~/Library/Fonts` |
| **Cache Tool** | Windows API + fc-cache | fc-cache | atsutil (optional) |
| **Registry** | Yes (HKEY_CURRENT_USER) | No | No |
| **Admin Required** | No | No | No |
| **Auto-Detection** | Via WM_FONTCHANGE | Via fc-cache | Automatic |
| **Instant Refresh** | Yes (with --refresh-cache) | Yes (with fc-cache) | After app restart |

### Linux Distribution Examples

**Ubuntu/Debian:**
```bash
# Install dependencies
sudo apt install python3 python3-fonttools fontconfig

# Build and install
python3 build_ccby_cjk_font.py --install --refresh-cache

# Verify installation
fc-list | grep "ERDA CC-BY CJK"
```

**Fedora/RHEL:**
```bash
# Install dependencies
sudo dnf install python3 python3-fonttools fontconfig

# Build and install
python3 build_ccby_cjk_font.py --install --refresh-cache

# Verify installation
fc-list | grep "ERDA CC-BY CJK"
```

**Arch Linux:**
```bash
# Install dependencies
sudo pacman -S python python-fonttools fontconfig

# Build and install
python build_ccby_cjk_font.py --install --refresh-cache

# Verify installation
fc-list | grep "ERDA CC-BY CJK"
```

### macOS Example

```bash
# Install dependencies (using Homebrew)
brew install python fonttools

# Build and install
python3 build_ccby_cjk_font.py --install

# Verify installation
ls -l ~/Library/Fonts/erda-ccby-cjk.ttf

# Check in Font Book
open -a "Font Book"
```

## License

This font is dual-licensed:
- **CC BY 4.0** (Creative Commons Attribution 4.0 International)
- **MIT License**

You may choose either license for your use case. See the main repository
`LICENSE-FONTS` file for full details.
