<!-- License: CC BY-SA 4.0 (Text); MIT (Code); CC BY 4.0/MIT (Fonts) -->
# Media and Licence Attribution

This file is the repository-level primary source for third-party and project-specific assets used by the ERDA Book. Language-specific generated copies may exist under `de/publish/` and `en/publish/`, but this root file is the canonical attribution table for compliance checks and release review.

## Licence Matrix

| Content type | Licence | Repository file |
|---|---|---|
| Text, graphics, diagrams | CC BY-SA 4.0 | `LICENSE` |
| Code, build scripts, toolchain | MIT | `LICENSE-CODE` |
| Own fonts | CC BY 4.0 or MIT | `LICENSE-FONTS` |
| Emojis | Twemoji, CC BY 4.0 | This file; Appendix L colophon |

## Asset Attribution

| Category | Asset | Author / rights holder | Licence | Source / version | Repository usage |
|---|---|---|---|---|---|
| Emoji font | Twemoji Mozilla / Twemoji COLR font | Twitter, Inc. and contributors; Mozilla packaging contributors | CC BY 4.0 | Vendored local file: `fonts-storage/twemoji-colr/TwemojiMozilla.ttf`; upstream project: https://github.com/mozilla/twemoji-colr | Colour emoji rendering in PDF generation and documentation. |
| Font | ERDA CC-BY CJK | Robert Alexander Massinger / ERDA project | CC BY 4.0 or MIT | Local source and generated TTF: `.github/fonts/erda-ccby-cjk/`; generated font: `.github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf` | CJK fallback coverage for multilingual licence text and PDF output. |
| Font | DejaVu Serif, DejaVu Sans, DejaVu Sans Mono | Bitstream, Inc.; DejaVu project contributors | Bitstream Vera License; DejaVu changes public domain | Local copies in `fonts-storage/dejavu/`; upstream: https://dejavu-fonts.github.io/ | Main text, headings/UI fallback and monospace/code rendering in PDF output. |
| Logo | ERDA Book logo | Robert Alexander Massinger; ERDA project usage rights | CC BY 4.0 | Original project/archive files | Cover, chapter headers and project communication where used. |

## Related Documentation

| Level | File | Purpose |
|---|---|---|
| Repository | `ATTRIBUTION.md` | Canonical, machine-readable attribution table for all assets. |
| German PDF/book | `de/content/anhang-l-kolophon.md` | Reader-facing typography and production colophon. |
| English PDF/book | `en/content/appendix-l-colophon.md` | Reader-facing typography and production colophon. |
| German licence concept | `de/content/anhang-j-lizenz---offenheit.md` | Licence philosophy and ShareAlike explanation. |
| English licence concept | `en/content/appendix-j-license-and-openness.md` | Licence philosophy and ShareAlike explanation. |
| German generated attribution | `de/publish/ATTRIBUTION.md` | Language-specific generated/publication copy. |
| English generated attribution | `en/publish/ATTRIBUTION.md` | Language-specific generated/publication copy. |

## Maintenance Rules

When fonts, emojis or other third-party assets change, update all attribution layers in the same change set where possible:

- Add or update the row in this root `ATTRIBUTION.md`.
- Update the German and English colophon files.
- Check the German and English licence appendix files.
- Regenerate or update language-specific publication attribution copies if they are part of the release artifacts.
- Record the source, version, licence and usage in the commit or release notes.

Do not add assets with OFL, GPL, UFL, proprietary or otherwise incompatible licensing unless the repository licence policy is explicitly changed first.
