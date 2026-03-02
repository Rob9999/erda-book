<!-- License: CC BY-SA 4.0 (Text); MIT (Code); CC BY 4.0/MIT (Fonts) -->
# Media & Licence Attribution

**Licence matrix (short):** Texts = **CC BY-SA 4.0** · Code = **MIT** · Fonts (own) = **CC BY 4.0 / MIT** · Emojis = **Twemoji (CC BY 4.0)**.  
Details: see **Appendix J: Licence & Openness** and the LICENSE files.

## Overview

| Category | Asset | Author / Rights Holder | Licence | Source / Note | Usage |
| --- | --- | --- | --- | --- | --- |
| Emoji | Twemoji Color Font v15.1.0 | Twitter, Inc. & Contributors (via 13rac1/twemoji-color-font) | CC BY 4.0 | https://github.com/13rac1/twemoji-color-font/releases/tag/v15.1.0 | Colour emoji glyphs (SVG-in-OpenType) for PDF generation and documentation. |
| Font | ERDA CJK (own development) | Robert Alexander Massinger / Project | CC BY 4.0 **or** MIT | Source & TTF files in the repo (`.github/fonts/`) | CJK coverage for multilingual chapters. |
| Font | DejaVu Serif/Sans/Mono v2.37 | © 2003 Bitstream, Inc. (base); DejaVu changes Public Domain | Bitstream Vera License | https://dejavu-fonts.github.io/ · Ubuntu fonts-dejavu-core | Body text (Serif), UI elements (Sans), code blocks (Mono) in PDF. Font files may not be sold separately; use in documents is unrestricted. |
| Logo | ERDA Book Logo | Robert Alexander Massinger; usage rights for ERDA Institute | CC BY 4.0 | Original files in the project archive | Cover, chapter headers, communication materials. |

> Notes:
> - **Twemoji** requires attribution; modifications are permitted.
> - **Own fonts** are dual-licensed (CC BY 4.0 / MIT). No OFL/GPL/proprietary fonts in the repo.
> - Additional third-party assets should be added to the table above (source, version, licence) and noted in the commit message.

## Maintenance Notes

### ⚠️ Observe the Attribution Hierarchy

This file is the **primary source** for all third-party content. When fonts, emojis or assets change, **three levels** must be kept in sync:

1. **`ATTRIBUTION.md`** (this file) — extend the table
2. **`content/appendix-l-colophon.md`** — update section L.2 Typography
3. **`content/appendix-j-license-and-openness.md`** — check licence matrix (if a new licence category is added)

### Checklist for new assets

- [ ] New row in the table above with all required fields (Asset, Author, Licence, Source, Usage)
- [ ] Licence compatible with `AGENTS.md` (no OFL/GPL/UFL/proprietary)
- [ ] Version and source documented precisely
- [ ] `content/appendix-l-colophon.md` section L.2 updated
- [ ] `content/appendix-j-license-and-openness.md` licence matrix (J.2) checked
- [ ] Commit with `Signed-off-by:` (DCO)
- [ ] CI/CD compliance check successful

**Note:** Licence and source information must match the actual files in the repo.
