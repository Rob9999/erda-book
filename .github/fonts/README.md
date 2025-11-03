# ERDA CC-BY CJK Font

This directory contains a minimalist fallback font that covers the characters
used in the Japanese and Korean licence translations of the ERDA book. The
font was created specifically for this repository and is released under the
Creative Commons Attribution 4.0 International Licence (CC BY 4.0).

* `erda-ccby-cjk.ttf` – generated font file.
* `build_ccby_cjk_font.py` – generator script that converts handcrafted
  bitmap patterns into TrueType outlines. Run it to regenerate the font:

```bash
python build_ccby_cjk_font.py
```

The generator script embeds the exact Japanese (Katakana) and Korean texts used
in the publication, guaranteeing that any future update of those strings
automatically refreshes the glyph set.
