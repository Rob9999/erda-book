---
source: content/anhang-l-kolophon.md
status: draft
---

# Appendix L: Colophon

## L.1 About this colophon

This colophon documents the **technical and typographic details** of the production of the ERDA book. It serves **transparency** and fulfils the **attribution obligations** for the fonts, tools and resources used. All components listed here are available under **open or compatible licences** and were selected in accordance with the licensing principles defined in **Appendix J**.

Author and editor: Robert Alexander Massinger.

Author email: [robert.alexander.massinger@outlook.de](mailto:robert.alexander.massinger@outlook.de)

Editorial work: ERDA Book editorial team (LLM-assisted language editing under editorial control).

---

## L.2 Typography and fonts

The ERDA book uses the following font families:

### L.2.1 DejaVu font family

**DejaVu Serif** (body text), **DejaVu Sans** (headings, UI elements), **DejaVu Sans Mono** (code blocks)

- **Version:** 2.37  
- **Licence:** Bitstream Vera License + Public Domain (for DejaVu modifications)  
- **Copyright:** © 2003 Bitstream, Inc. (Bitstream Vera base); DejaVu modifications in the public domain  
- **Source:** <https://dejavu-fonts.github.io/>  
- **Distribution:** Ubuntu package `fonts-dejavu-core`  
- **Legal note:** The font files may not be sold separately. Embedding in documents (including PDF) is permitted without restriction.

**Rationale for selection:**  
The DejaVu family offers excellent **Unicode coverage** for European languages, mathematical symbols and special characters. The fonts are technically mature, highly legible and available under an **open licence** that permits commercial distribution of the book.

### L.2.2 ERDA CC‑BY CJK (Chinese, Japanese, Korean)

**ERDA CC‑BY CJK**

- **Licence:** CC BY 4.0  
- **Source:** in‑house development of the ERDA project  
- **Use:** supplementary coverage for CJK characters (Chinese, Japanese, Korean)  
- **Legal note:** Attribution required; commercial use permitted.

**Rationale for selection:**  
For multilingual editions (in particular Appendix J) a CJK font is required that is licensed under **CC BY 4.0** and thus consistent with the project’s licensing principles.

### L.2.3 Twemoji Mozilla (emojis)

**Twemoji Mozilla**

- **Version:** 0.6.0  
- **Licence:** CC BY 4.0  
- **Copyright:** © Twitter, Inc. and other contributors  
- **Source:** <https://github.com/mozilla/twemoji-colr>  
- **Distribution:** Ubuntu package `fonts-twemoji`  
- **Legal note:** Attribution required; commercial use permitted.

**Rationale for selection:**  
Emojis are an integral part of the multilingual licence clauses (Appendix J) and of the visual design. Twemoji offers consistent, colourful rendering under an **open licence** without proprietary restrictions.

---

## L.3 Production tools

The ERDA book was created using the following open‑source tools:

### L.3.1 GitBook

- **Role:** basis of the Markdown structure  
- **Licence:** Apache 2.0  
- **Use:** structuring, navigation, HTML export  
- **Source:** <https://www.gitbook.com/>

### L.3.2 Pandoc

- **Version:** 3.6 (November 2024)  
- **Licence:** GPL v2+  
- **Use:** conversion from Markdown to LaTeX/PDF  
- **Source:** <https://pandoc.org/>

**Technical details:**  
Pandoc orchestrates the transformation of the Markdown source files into an intermediate LaTeX format, which is then compiled to the final PDF by LuaLaTeX.

### L.3.3 TeX Live

- **Version:** TeX Live 2025  
- **Licence:** mixed open‑source licences (LaTeX Project Public License, public domain, etc.)  
- **Use:** LaTeX engine for PDF generation  
- **Source:** <https://tug.org/texlive/>

**Technical details:**  
- **Engine:** LuaHBTeX 1.22.0 (TeX Live 2025)  
- **Packages:** scheme-basic + xetex, fontspec, polyglossia, unicode-math, babel-german, enumitem, geometry, xcolor, booktabs, caption, fancyhdr  
- **Installation:** CTAN mirror (install-tl-unx)

### L.3.4 Python toolchain

- **Version:** Python 3.11+  
- **Licence:** Python Software Foundation Licence  
- **Use:** build orchestration, emoji processing, quality assurance  
- **Main modules:**  
  - `workflow_orchestrator.py`: master build process  
  - `publisher.py`: PDF generation  
  - `emoji_utils.py`: emoji detection and font fallback

### L.3.5 Docker

- **Version:** Docker 24.0+  
- **Licence:** Apache 2.0  
- **Use:** reproducible build environment  
- **Images:**  
  - `erda-workflow-tools:latest`: TeX Live 2025, Pandoc 3.6, Python 3.11  
  - `erda-publisher:legacy`: TeX Live 2021/2022 (fallback)

---

## L.4 Production environment

### L.4.1 Build platform

- **Operating system:** Ubuntu 22.04 LTS (Docker container)  
- **Hardware:** generic x86_64 processor  
- **Build time:** ~2–5 minutes (depending on content size)

### L.4.2 Version control

- **System:** Git 2.34+  
- **Repository:** GitHub (`Rob9999/erda-book`)  
- **Branch model:** `main` (stable), `release_candidate` (pre‑release)  
- **CI/CD:** GitHub Actions (automated builds)

### L.4.3 Date and version

- **Build date:** {{BUILD_DATE}} (generated automatically)  
- **Version:** {{VERSION}} (see `CITATION.cff`)  
- **Commit hash:** {{COMMIT_HASH}} (Git reference)

---

## L.5 Quality assurance

The technical quality of the ERDA book is ensured by the following measures:

1. **Automated testing:** the CI/CD pipeline validates build processes.  
2. **Licence compliance:** automated checks for incompatible licences (see `AGENTS.md`).  
3. **Font fallback:** automatic emoji detection and font assignment.  
4. **UTF‑8 validation:** ensuring correct character encoding.  
5. **DCO enforcement:** all contributions are signed (Developer Certificate of Origin).

Details of the content‑related quality assurance can be found in **Appendix K**.

---

## L.6 Acknowledgements

This book would not have been possible without the **open‑source community**. Special thanks go to:

- **Bitstream, Inc.** and the **DejaVu developers** for the excellent font family.  
- **Twitter, Inc.** and **Mozilla** for the Twemoji project.  
- The **TeX Live**, **Pandoc** and **Python** communities.  
- All contributors to the ERDA project who have committed to the **DCO**.

---

## L.7 Further information

- **Complete attribution:** see `ATTRIBUTION.md` in the repository.  
- **Licence details:** see **Appendix J: License & Openness**.  
- **Technical documentation:** see `README.md` and `.github/gitbook_worker/`.  
- **Zenodo archiving:** DOI and concept DOI, see `CITATION.cff`.

---

## L.8 Maintenance note

This colophon is part of the **attribution hierarchy** of the ERDA project:

- **`ATTRIBUTION.md`** (repository) = primary source (machine‑readable)  
- **Appendix L** (this document) = reader‑friendly presentation (PDF)  
- **Appendix J** = licensing philosophy and legal framework

**For any changes to fonts, emojis or production tools:**

1. Update `ATTRIBUTION.md` in the repository (new table row).  
2. Update this colophon (section L.2 Typography / L.3 Tools).  
3. Review `content/anhang-j-lizenz---offenheit.md` (licence matrix J.2).

For details, see `AGENTS.md` → “Attribution‑Hierarchy”.

---

**End of the colophon.**  
This document is part of the ERDA book and is licensed under **CC BY‑SA 4.0** (see Appendix J).
