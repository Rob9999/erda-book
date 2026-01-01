# Release History

## 1.0.2 – 1 Jan 2026
- **Responsible:** Robert Alexander Massinger (Lead) with support from ChatGPT/OpenAI for translation.
- **Goal:** 
  - Technical: 
    - Build a translation workspace, align metadata with the next release cycle and document translation rules. 
    - The gitbook_worker tool comes from a pip-installable package.
    - Reorganize repository structure: `/de` for German version, `/en` for English version.
  - Informational: 
    - Publish the British English version "The ERDA Book".
    - Each language version gets its own repo folder with dedicated Licensing, Citation, publish.yml, Attribution, certification, and publish description. 
- **Highlights:** 
  - Version bump to 1.0.2
  - **Multi-language structure**: `/de` (German), `/en` (English)
  - Dedicated pipelines per language (content, licenses, citation files, publisher config)
  - Formal translation workflow (`translation_instruction.md`)
  - Repository-wide release history
  - Matrix-based CI/CD workflows for parallel language builds

## 1.0.1 – 15 Nov 2025
- **Responsible:** Robert Alexander Massinger (Author) with support from ChatGPT/OpenAI for tooling guidance.
- **Goal:** Technical refresh of the PDF build, typography, metadata harmonisation and reproducible publishing (see `release-notes-v1.0.1.md`).
- **Highlights:** End-to-end publishing pipeline, consistent ERDA CC-BY CJK font usage, improved layout/readability, harmonised `CITATION.cff`, `.zenodo.json` and attribution documentation.

## 1.0.0 – 6 Jul 2025
- **Responsible:** Robert Alexander Massinger (Founder, ERDA Initiative).
- **Goal:** First public release of "Das ERDA Buch" on Zenodo, providing the conceptual foundation for ERDA's democratic resilience roadmap.
- **Highlights:** Comprehensive German manuscript published as CC BY-SA 4.0 on Zenodo (doi pending in repository history), establishing the baseline content that remains the single source of truth for all translations.
