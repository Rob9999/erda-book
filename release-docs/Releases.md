# Release History

## 2.5.0 – 12 May 2026
- **Responsible:** Robert Alexander Massinger (Lead) with support from ChatGPT/OpenAI and GitHub Copilot/Anthropic.
- **Codename:** Democratic Knowledge
- **Goal:**
  - Content:
    - "Demokratisches Wissen" (Democratic Knowledge) – seven normative principles for democratic agency (power, non-democracy-willing states, peace & security, truth & deception, democracy, technology/AI, inner condition).
    - Desktop materials (DE + EN) in `desktop/misc/`.
    - Integration of three papers from `desktop/misc/` into the book:
      - **Kindererziehung essay** → new §11.3.7 (DE+EN): guiding vision for raising children in freedom and responsibility.
      - **Mosaik-Prinzip** → new §5.8.4 (DE+EN): strategic reflection on mosaic warfare principle and democratic DSN resilience.
      - **Anti-Game-Over paper** → **Appendix P.1** (DE translation + EN original): developmental-philosophical model of prosperative life (DOI: 10.5281/zenodo.19244929; APA citation in the paper header).
      - **CIVITAS Public paper** → **Appendix P.2** (DE contextual wrapper + EN original): working paper on Europe's digital agora and first operational CIVITAS layer (DOI: 10.5281/zenodo.19443256; APA citation in the paper header).
      - **CIVITAS chapter deepening** → Chapter 6: governance, publication formats, review levels, technical layers, safeguards, partnerships, education and roadmap.
      - **ARKTIS chapter consolidation and stress-test appendices** → Chapter 8: merged short sections, deepened strategic pillars (international law, alliance architecture, hybrid threats, thresholds, finance, data governance, indigenous institutions), added escalation ladder and resilience dashboard, and four stress-test appendices (8.A Greenland, 8.B Svalbard, 8.C undersea cables, 8.D permafrost methane).
      - **AI democratic maturity frame** → new §10.2.1 (DE+EN): democracy as an order of mature responsibility across humans, AI and possible future mature beings.
      - **Book-project yardstick** → **Appendix M**: measurable release criteria, source standards and project decisions.
    - Cross-references to Appendix P.1 in chapters 11.2, 11.3, 3.5, 4.3.5.
  - Editorial:
    - README "Contributions and quality" sections rewritten in professional editorial voice (DE + EN).
  - Technical:
    - Version bump to v2.5.0.
    - Release documentation in `release-docs/v2.5.0/`.
    - `book.json` date updated to 2026-05-12 (DE+EN).
    - Vendored gitbook_worker updated to 2.9.2; publish artefacts rebuilt after Chapter 8 stress-test appendices and §10.2.1 (DE 858 pages / 4,402,170 bytes; EN 825 pages / 4,420,023 bytes) and the editorial-quality gate passed with warnings (DE 40, EN 43, Project 83), 0 blocked and 0 fail findings.
    - Final-scope source/link gate documented by gitbook_worker dry-run, link audit, sources export and manual web verification.
- **Highlights:**
  - **Seven principles of democratic knowledge** as standalone reference
  - **Editorial quality initiative** for project communication
  - **Appendix M – Measure** as measurable book-project yardstick (bilingual)
  - **Appendix P.1 – Anti-Game-Over Principle** as paper appendix (bilingual)
  - **Appendix P.2 – CIVITAS Public** as paper appendix (bilingual wrapper / English original)
  - **Chapter 6 CIVITAS deepening** as operational democratic digital infrastructure
  - **Chapter 8 ARKTIS consolidation with stress-test appendices 8.A–8.D** (Greenland, Svalbard, undersea cables, permafrost methane) and expanded strategic pillars
  - **Chapter 10 §10.2.1 Democracy of the Mature** as a democratic responsibility frame for humans, AI and possible future mature beings
  - **Guiding vision for child-rearing** (§11.3.7) with 12 democratic education principles
  - **Mosaic Principle reflection** (§5.8.4) linking decentralised warfare theory to DSN architecture
  - Full release planning with status tracking

## 2.0.0 – 1 Mar 2026
- **Responsible:** Robert Alexander Massinger (Lead) with support from ChatGPT/OpenAI and GitHub Copilot/Anthropic.
- **Codename:** Human AI Democrazy
- **Goal:**
  - Content:
    - Expand the book from 9 to 14 chapters: AI governance (Ch. 10), civic resilience (Ch. 11), democratic transformation rules (Ch. 12), strategic sovereignty (Ch. 13), and democratic coalitions of the willing with a draft treaty (Ch. 14).
    - Normative sharpening of the ERDA guiding principle across all chapters.
    - Integration of real-world war insights (Zaluzhnyi/Chatham House 2026) across 6 chapters.
    - New D.5 strategy paper, D.6 executive summary block, glossary expansion (11 new terms).
  - Technical:
    - Full DE↔EN synchronisation of all new and revised content.
    - Updated publish artefacts (PDF/MD) for both languages.
- **Highlights:**
  - Version bump to 2.0.0
  - **Five new chapters** (10–14) with 200+ pages of new content
  - **KI governance** with Co-evolution Index (KEI)
  - **Citizen duty model** linking rights with responsibility
  - **Seven transformation rules** for social democracy
  - **Strategic sovereignty toolbox** (air defence, attrition, hybrid defence)
  - **EDDRC alliance architecture** with tier model, democracy chain, and 155 treaty articles
  - **Zaluzhnyi integration** (kill zones, transparent battlespace, drone warfare)
  - Complete release documentation (notes, description, certification, status)

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
