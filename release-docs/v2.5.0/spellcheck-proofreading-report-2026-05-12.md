# Spellcheck and Proofreading Report - 2026-05-12

## Scope

- German source content: `de/content/**/*.md`
- English source content: `en/content/**/*.md`
- Generated publish Markdown and PDFs were not rebuilt in this pass. PDF rebuilds are intentionally deferred until the current proofreading wave is complete.

## Tooling

- `cspell` via `npx.cmd`, configured in `cspell.json`.
- Project dictionary: `.cspell/erda-terms.txt`.
- Local LanguageTool 6.6 via Java, downloaded under `tmp/LanguageTool` and run against a Markdown-prepared copy.
- Markdown preparation script: `scripts/quality/prepare_languagetool_markdown.py`.

## Reports

- English cspell report: `logs/quality/cspell-en-2026-05-12.txt`.
- German LanguageTool report: `logs/quality/languagetool-de-2026-05-12.txt`.

`logs/quality/` is intentionally git-ignored; the reports are local review artifacts, not release content.

## Corrections Applied

Clear source-level typos and encoding issues fixed in this pass:

- `ENSIA Threat Landscape 2024` -> `ENISA Threat Landscape 2024` in the German ENISA citations.
- `Chipher-Plan` -> `Chip-Plan`.
- `Zensored Creativity Engines` -> `Censored Creativity Engines`.
- `Pflegen ich` -> `Pflege ich`.
- `Bürgerrevier-Kommissionen` -> `Bürgerreview-Kommissionen`.
- English terminology aligned to `Censored Creativity Engines`.
- Duplicated German title `Institutionelle BalanceInstitutionelle Balance` -> `Institutionelle Balance`.
- Broken emoji entities in the German institutional-balance impulse restored to light-bulb glyphs.
- Broken magic-wand entity in the German GitBook chapter template restored.
- Damaged Ireland Nobel-prize entry `cu��` replaced with explicit laureates: Yeats, Shaw, Beckett, Heaney; English counterpart synchronized.
- English `not fully sabotagable` replaced with `not fully vulnerable to sabotage`.
- Decomposed German umlauts normalized in `Bürger`, `Ergänzendes` and `über` to avoid false proofreading/encoding hits.

## Triage Notes

- `cspell` is now useful as an English/project-term gate, but it still reports intentional bilingual terms, citation names, acronyms and some source-link path fragments. These should be triaged rather than auto-corrected.
- LanguageTool is useful for German spelling and grammar, but Markdown tables, block labels, citations and intentionally capitalized headings create false positives. The preprocessor reduces noise while keeping original line numbers stable.
- No automatic LanguageTool suggestions were applied.

## Follow-Up

- Review remaining cspell hits for actual residual German text in English prose versus intentional legal/citation terms.
- Review LanguageTool findings by chapter, prioritizing `GERMAN_SPELLER_RULE` matches that are not acronyms, citations, Markdown labels or project terms.
- Rebuild DE/EN publish artifacts after the proofreading wave, then rerun release quality gates and visual/PDF checks as needed.
