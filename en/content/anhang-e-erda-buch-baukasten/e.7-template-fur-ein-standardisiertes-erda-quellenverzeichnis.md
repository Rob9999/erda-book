---
source: content/anhang-e-erda-buch-baukasten/e.7-template-fur-ein-standardisiertes-erda-quellenverzeichnis.md
status: draft
---

# E.7 🪄 Template for a standardised ERDA source list

🪄 _**E.7 Template for a standardised ERDA source list (v1.0)**_

### 🎯 Objective

This template is aimed at authors, editors, technical editorial/GitBook teams and quality assurance reviewers.
It supports them in creating source and reference lists in a consistent, clear and error-free way, avoiding broken links, and ensuring sources are traceable and verifiable.

Every source tells a story – handle it with care.

### 🛠 Structure

#### 1) Section: 📎 Sources and references used

- **Content:** only verified, existing external sources and internal GitBook references.
- **Formatting:**
  - Numbered list.
  - Title (italic), year, optionally short context.
  - Direct link for internet sources.
  - Relative path for internal GitBook documents.
  - **Example internet source:** _“Strategic Compass for Security and Defence”_ (European Commission, 2022): [https://eeas.europa.eu/strategic-compass](https://eeas.europa.eu/strategic-compass)
  - **Example GitBook reference:** _Appendix: Europe 2.0 – Roadmap for a Livable, Resilient and Leading Union_ (2025): \[../anhang-europa-2.0-fahrplan-fur-eine-lebenswerte-resiliente-und-fuhrende-union.md]
- **Sorting:**
  - First internet sources (official documents, studies, etc.)
  - Then GitBook-internal chapters
  - Within categories, group alphabetically or in a thematically sensible way
- **Tutorial tip:**
  - For internet links: copy the link from the browser.
  - For GitBook references: copy the file path from `SUMMARY.md` and ensure the relative path structure is correct.

#### 2) Section: 🛠️ Future work by the ERDA Institute or constitutional bodies

- **Content:**
  - Planned concepts, platforms, frameworks that still need to be developed.
- **Formatting:**
  - Bullet list.
  - One sentence of description per item.
- **Examples of mock entries:**
  - **ERDA dialogue model:** develop a framework for scalable moderation of cross-border citizen forums (“EU dialogue forums for citizen participation”).
  - **Democracy Lab handbook:** create a guide for participatory workshop methods and coaching modules in local democracy labs.
- **Motivational note:**
  - These modules are part of the overall ERDA concept and invite co-creation.

### 📐 Formatting rules

| Rule category | Details |
| --- | --- |
| **Linking** | Internet links in square brackets, directly clickable. GitBook references relative with full filename. |
| **Text consistency** | Consistent quotation marks (“”). Hyphens instead of underscores in filenames. No spaces or special characters in GitBook filenames. |
| **Transparency** | Clear separation of planned concepts from existing materials. |
| **Error prevention** | Do not allow placeholders or invented sources. Only reference after verification in `SUMMARY.md` or official documents. |

> Advanced tip: for large chapters, consider using a link-check tool or a linting script.

### 🧠 Quality assurance: standard prompts for review

**Before every final approval:**

1. 🔍 **Internet verification:** is the URL valid? (No 404, correct content)
2. 📂 **GitBook verification:** does the path exist in `SUMMARY.md`?
3. 📑 **Content verification:**
   - Does the source actually match the referenced statement?
   - Is it a primary, secondary or tertiary source?
4. 🚦 **Categorisation:** existing source vs. future concept clearly assigned?
5. 📋 **Formal check:** consistent presentation of title, year, link/path.
6. 🛡️ **Final check:** “Does the list avoid giving any impression of fiction or immaturity at any point?”

- **Responsibility:** final source checks lie with the chapter lead author or the assigned QA instance.

### 📋 Review template “Source list for chapter [title]”

- **Chapter:** [insert chapter name]
- **Review date:** [insert date]
- **Reviewer:** [insert name]

#### 🔎 Review steps

| Step | Priority | Status (✔️/❌) | Comment |
| --- | --- | --- | --- |
| All internet links accessible and current? | Must |  |  |
| All GitBook references exist and match `SUMMARY.md`? | Must |  |  |
| Sources match the chapter content precisely? | Must |  |  |
| Correct separation between existing and planned sources? | Must |  |  |
| Consistent layout, no typos, complete data? | Must |  |  |
| Motivational language for future concepts? | Must |  |  |
| Final check (“no impression of fiction”) passed? | Must |  |  |

> **Result:** [approval recommended / rework required]

***

This template can be used flexibly for any ERDA chapter and significantly increases the quality and consistency of the overall work.
For evolutionary quality development, it is recommended to continuously evaluate the results of source checks and derive optimisations of the template from them.
