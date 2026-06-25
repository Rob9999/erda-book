# ERDA Book

[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Version](https://img.shields.io/badge/version-v3.00-brightgreen.svg)](https://github.com/Rob9999/erda-book/releases/tag/v3.00)

**Current version:** v3.00
**As of (date):** 2026-06-25
**Channel:** release_candidate (v3.00 preparation; stable channel after merge/tag: main)
**Codename / Release name:** Democratic Integration

**Multi-language democratic resilience framework**
🇩🇪 Deutsche Fassung: [`de/`](de/publish/das-erda-buch.pdf)
🇬🇧 English version: [`en/`](en/publish/the-erda-book.pdf)

**Sprungmarken / Jump links:** 🇩🇪 [Deutsch](#de) | 🇬🇧 [English](#en)

- 🇩🇪 [Deutsch](#de)
  - [Was ist das ERDA Buch?](#de-was-ist)
   - [Aktuelles Release (v3.00)](#de-release)
  - [Lizenz](#de-lizenz)
  - [Zitierung](#de-zitierung)
  - [Attribution und Lizenzierung](#de-attribution)
  - [Schriftarten-Design](#de-fonts)
  - [Tooling & Build](#de-tooling)
- 🇬🇧 [English](#en)
  - [What is the ERDA Book?](#en-what-is)
   - [Current release (v3.00)](#en-release)
  - [Licence](#en-licence)
  - [Citation](#en-citation)
  - [Attribution and licensing](#en-attribution)
  - [Font design](#en-fonts)
  - [Tooling & build](#en-tooling)

---

<a id="de"></a>
## 🇩🇪 Deutsch

<a id="de-was-ist"></a>
### Was ist das ERDA Buch?

Das **ERDA Buch** ist ein Open-Access-Buchprojekt zur **demokratischen Resilienz**, zur **strategischen Handlungsfähigkeit Europas** und zur **Governance moderner Technologien** (insbesondere KI, digitale Partizipation, Sicherheit).

Es verbindet dabei:

- eine langfristige **Roadmap** (2025–2075)
- institutionelle **Architekturvorschläge** (z. B. CIVITAS, FORTERA, EDA)
- konkrete **Governance-Leitplanken** (z. B. KI-Ebenenmodell, rote Linien)
- einen Schwerpunkt auf **evolutiv stabilen** Mechanismen (Anreize, Pflichten/Rechte, Transparenz, Kontrollfähigkeit)

### Für wen ist das gedacht?

- **Entscheidungsträger:innen** (Politik, Verwaltung, Institutionen, Think Tanks)
- **Zivilgesellschaft** (Beteiligungsformate, Transparenz, demokratische Kultur)
- **Forschung & Bildung** (Begriffsarbeit, Modelle, Szenarien)
- **Technologie- und Sicherheits-Communities** (Umsetzungsideen, Redlines, Auditierbarkeit)

### Wie ist das Repository aufgebaut?

- `de/` enthält die **deutsche Originalfassung** (Source of Truth).
- `en/` enthält die **englische Übersetzung** (Draft/Review-Status je Kapitel).
- In `*/content/` liegen die GitBook-Markdown-Quellen; in `*/publish/` die generierten Artefakte (MD/PDF).

### Wie liest man das Buch am schnellsten?

1. Starte mit den **Kapitel-Executive-Summaries** (wo vorhanden) für den Überblick.
2. Nutze die Kapitel als modulare Bausteine (Institutionen, Sektoren, Konzepte).
3. Lies Detailabschnitte dort, wo du Entscheidungen vorbereiten oder Regeln definieren willst (z. B. KI-Governance).

### Wofür steht „evolutiv stabil“ in diesem Kontext?

Gemeint sind Modelle, die langfristig funktionieren, weil sie **Anreize**, **Kontrollmechanismen** und **gesellschaftliche Tragfähigkeit** zusammendenken – statt nur Idealbilder zu formulieren.

<a id="de-release"></a>
### Aktuelles Release (v3.00) – 25. Juni 2026

> Dieses Release präzisiert die demokratische Integrationsarchitektur des ERDA-Buches durch das 4+1-Ring-System: globale demokratische Partner, demokratischer Beitrittspfad, domänenbasierte Mitgliedschaft, volle EU-/ERDA-Mitgliedschaft und ein freiwilliger tiefer verfassungsdemokratischer Kern.

**Neue Inhalte:**
- **4+1-Ring-System in §4.2.3:** neues Unterkapitel zur demokratischen Integration ohne Wartesaal.
- **Interne Vernetzung:** Verweise auf Anhang A/B, EDA, CIVITAS, FORTERA, strategische Souveränität und Annex 14.F Membership Tiers.
- **Release-Candidate-Metadaten:** README, `book.json`, `publish.yml`, CFF-Dateien und `.zenodo.json` auf v3.00 / 2026-06-25 synchronisiert.

Details: [`release-docs/v3.00/`](release-docs/v3.00/)

<details>
<summary>Vorheriges Release: v2.5.0 - 12. Mai 2026</summary>

> Dieses Release vertiefte die normativen Grundlagen des ERDA-Buches. Im Zentrum stand das „Demokratische Wissen" als Leitfaden für demokratische Handlungsfähigkeit.

Weitere Schwerpunkte:
- **CIVITAS Public / Anhang P.2:** veröffentlichtes Working Paper zur europäischen digitalen Agora; Kapitel 6 wurde als operative CIVITAS-Architektur vertieft.
- **Anhang M / Anhang P:** messbarer Buchprojektmaßstab und Paper-Anhänge mit DOI-/APA-Pflicht für veröffentlichte ERDA-Papers.
- **Kapitel 8 und §10.2.1:** ARKTIS-Konsolidierung sowie Demokratie der Mündigen als Verantwortungsrahmen für Menschen, KI und mögliche weitere mündige Wesen.
- **Redaktionelle Qualitätsoffensive:** README, Rollenmodell, Frontmatter und Release-Gates wurden weiter professionalisiert.

Details: [`release-docs/v2.5.0/`](release-docs/v2.5.0/)

</details>

### Beiträge und Qualität

Das ERDA-Buch versteht sich als **lebendiges Dokument demokratischer Resilienz** – es lebt von der fachkundigen Mitwirkung aus Zivilgesellschaft, Wissenschaft, Politik und Praxis. Beiträge sind daher nicht nur willkommen, sondern ausdrücklich erwünscht.

**Redaktionelle Leitlinien:**

- **Qualitätsanspruch:** Jeder Beitrag sollte den analytischen Maßstäben des Projekts gerecht werden – sachlich fundiert, quellentransparent und konstruktiv im Sinne demokratischer Handlungsfähigkeit.
- **Verbindliche Regeln:** Bitte die Richtlinien in [`AGENTS.md`](AGENTS.md) beachten – insbesondere DCO-Sign-off, Lizenz- und Attributionspflichten sowie die DE↔EN-Synchronisation bei inhaltlichen Änderungen.
- **Rollen & Verantwortlichkeiten:** Writer, Editor, Lektor, Redakteur und Publisher sind in [`worker-roles.md`](worker-roles.md) mit Rechten, Pflichten und Freigabegrenzen definiert.
- **Peer-Review-Prinzip:** Inhaltliche Änderungen durchlaufen ein Review, um Konsistenz, fachliche Korrektheit und Übersetzungssynchronität sicherzustellen.

> **Rechtlicher Hinweis:** Alle Inhalte werden „as is" und ohne Gewähr bereitgestellt. Das ERDA-Buch stellt keine Rechts-, Steuer- oder sonstige professionelle Beratung dar.

<a id="de-lizenz"></a>
### Lizenz

| Inhaltsart | Lizenz | Datei |
|---|---|---|
| Texte, Grafiken, Diagramme | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | [`LICENSE`](LICENSE) |
| Code, Build-Skripte, Toolchain | [MIT](https://opensource.org/licenses/MIT) | [`LICENSE-CODE`](LICENSE-CODE) |
| Schriften (eigene) | CC BY 4.0 / MIT (Dual) | [`LICENSE-FONTS`](LICENSE-FONTS) |

<a id="de-zitierung"></a>
### Zitierung

Dieses Projekt kann über die Datei [`CITATION.cff`](CITATION.cff) zitiert werden. GitHub erkennt dieses Format automatisch und bietet unter dem Menüpunkt **„Cite this repository“** einen BibTeX- und APA-Export an.

<a id="de-attribution"></a>
### 📜 Attribution und Lizenzierung

Dieses Projekt verwendet ein **Drei-Ebenen-System** für Transparenz und Rechtssicherheit:

### Attribution-Hierarchie

1. **`ATTRIBUTION.md`** (Repository) — **Primärquelle** für Compliance
   - Maschinenlesbare Tabelle aller Drittinhalte (Fonts, Emojis, Assets)
   - Wird von CI/CD-Tools geprüft
   - **Zielgruppe:** Entwickler, Maintainer, Rechtsprüfung

2. **`de/content/anhang-l-kolophon.md`** / **`en/content/appendix-l-colophon.md`** (PDF-Buch) — **Leserfreundlich**
   - Narrative Font-Attribution für PDF-Leser
   - Produktionsdetails (TeX Live, Pandoc, Build-Umgebung)
   - **Zielgruppe:** Buchleser ohne Repo-Zugriff

3. **`de/content/anhang-j-lizenz---offenheit.md`** / **`en/content/appendix-j-license-and-openness.md`** (Konzept) — **Lizenzphilosophie**
   - Rechtliche Rahmenbedingungen und Share-Alike-Prinzip
   - **Zielgruppe:** Rechtsinteressierte, KI-Trainer, Remix-Projekte

### ⚠️ Wichtig: Bei Änderungen an Fonts/Emojis/Assets

**Alle drei Ebenen aktualisieren:**
1. ✅ `ATTRIBUTION.md` → Neue Zeile in Tabelle
2. ✅ `de/content/anhang-l-kolophon.md` / `en/content/appendix-l-colophon.md` → Abschnitt L.2 Typografie
3. ✅ `de/content/anhang-j-lizenz---offenheit.md` / `en/content/appendix-j-license-and-openness.md` → Lizenzmatrix prüfen
4. ✅ Commit mit `Signed-off-by:` (DCO)

Details siehe [`AGENTS.md`](AGENTS.md) → "Attribution-Hierarchie".

---

<a id="de-fonts"></a>
### Schriftarten-Design

### PDF-Generierung
Bei der PDF-Generierung werden **keine** zusätzlichen System-Emoji-Schriftarten aus externen Paketen eingebunden, um das Design konsistent mit der Markenidentität zu halten. Die Schriftarten können in der `publish.yml` über die `pdf_options` konfiguriert werden:

```yaml
pdf_options:
  emoji_color: true
  main_font: "DejaVu Serif"  # Hauptschriftart für Fließtext
  sans_font: "DejaVu Sans"   # Serifenlose Schriftart für Überschriften
  mono_font: "DejaVu Mono"   # Monospace-Schriftart für Code
```

Diese Konfiguration stellt sicher, dass das Dokumentendesign den Vorgaben entspricht.

<a id="de-tooling"></a>
### Tooling & Build

Das Build-Tooling (`gitbook_worker`) wird extern gepflegt und von hier bezogen:

- https://github.com/Rob9999/gitbook-worker

Dieses Repository verwendet ein **gepinntes, vendortes Paket-Artefakt** (siehe `requirements.txt`) sowie repo-lokale Konfiguration (z. B. `de/publish.yml`, `en/publish.yml`, `content.yaml`).

Ablageort des vendorten Artefakts (aktuelles Muster): `packages/gitbook-worker/*.tar.gz`

Eine Schritt-für-Schritt-Anleitung zur lokalen PDF-Erzeugung findet sich in [`how-to-build.md`](how-to-build.md).

---

<a id="en"></a>
## 🇬🇧 English

<a id="en-what-is"></a>
### What is the ERDA Book?

The **ERDA Book** is an open-access book project on **democratic resilience**, **Europe’s strategic capacity to act**, and the **governance of modern technologies** (especially AI, digital participation, and security).

It combines:

- a long-term **roadmap** (2025–2075)
- institutional **architecture proposals** (e.g. CIVITAS, FORTERA, EDA)
- concrete **governance guardrails** (e.g. AI level model, red lines)
- a focus on **evolutionarily stable** mechanisms (incentives, duties/rights, transparency, controllability)

### Who is this for?

- **Decision-makers** (policy, administration, institutions, think tanks)
- **Civil society** (participation formats, transparency, democratic culture)
- **Research & education** (conceptual work, models, scenarios)
- **Technology & security communities** (implementation ideas, red lines, auditability)

### How is this repository structured?

- `de/` contains the **German original** (source of truth).
- `en/` contains the **English translation** (draft/review status per chapter).
- `*/content/` holds the GitBook Markdown sources; `*/publish/` holds generated artifacts (MD/PDF).

### How to read it quickly

1. Start with chapter **executive summaries** (where available) for orientation.
2. Use chapters as modular building blocks (institutions, sectors, concepts).
3. Read the detailed sections where you need to define rules or prepare decisions (e.g. AI governance).

### What does “evolutionarily stable” mean here?

It refers to models that remain viable long-term because they align **incentives**, **control mechanisms**, and **social sustainability**, instead of only describing ideals.

<a id="en-release"></a>
### Current release (v3.00) – 25 June 2026

> This release specifies the ERDA Book's democratic integration architecture through the 4+1 ring system: global democratic partners, a democratic accession path, domain-based membership, full EU/ERDA membership and a voluntary deeper constitutional-democratic core.

**New content:**
- **4+1 ring system in §4.2.3:** new subsection on democratic integration without a waiting room.
- **Internal linking:** references to Appendix A/B, EDA, CIVITAS, FORTERA, strategic sovereignty and Annex 14.F Membership Tiers.
- **Release-candidate metadata:** README, `book.json`, `publish.yml`, CFF files and `.zenodo.json` synchronised to v3.00 / 2026-06-25.

Details: [`release-docs/v3.00/`](release-docs/v3.00/)

<details>
<summary>Previous release: v2.5.0 - 12 May 2026</summary>

> This release deepened the normative foundations of the ERDA Book. At its centre was "Democratic Knowledge" as a guide for democratic agency.

Further priorities:
- **CIVITAS Public / Appendix P.2:** published working paper on a European digital agora; Chapter 6 was deepened as an operational CIVITAS architecture.
- **Appendix M / Appendix P:** measurable book-project yardstick and paper appendices with DOI/APA requirements for published ERDA papers.
- **Chapter 8 and §10.2.1:** ARKTIS consolidation and Democracy of the Mature as a responsibility frame for humans, AI and possible future mature beings.
- **Editorial quality initiative:** README, roles model, front matter and release gates were professionalised further.

Details: [`release-docs/v2.5.0/`](release-docs/v2.5.0/)

</details>

### Contributions and quality

The ERDA Book sees itself as a **living document of democratic resilience** – it thrives on expert contributions from civil society, academia, policy-making, and practice. Contributions are therefore not merely welcome but actively encouraged.

**Editorial guidelines:**

- **Quality standards:** Every contribution should meet the project's analytical expectations – well-founded, source-transparent, and constructive in the service of democratic agency.
- **Binding rules:** Please observe the guidelines in [`AGENTS.md`](AGENTS.md) – in particular DCO sign-off, licensing and attribution duties, and DE↔EN synchronisation for content changes.
- **Roles & responsibilities:** Writer, Editor, Lektor, Redakteur and Publisher are defined in [`worker-roles.md`](worker-roles.md), including rights, duties and approval boundaries.
- **Peer-review principle:** Content changes undergo review to ensure consistency, factual accuracy, and translation synchronisation.

> **Legal notice:** All content is provided "as is" and without warranty. The ERDA Book does not constitute legal, tax, or any other form of professional advice.

<a id="en-licence"></a>
### Licence

| Content type | Licence | File |
|---|---|---|
| Text, graphics, diagrams | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | [`LICENSE`](LICENSE) |
| Code, build scripts, toolchain | [MIT](https://opensource.org/licenses/MIT) | [`LICENSE-CODE`](LICENSE-CODE) |
| Fonts (own) | CC BY 4.0 / MIT (dual) | [`LICENSE-FONTS`](LICENSE-FONTS) |

<a id="en-citation"></a>
### Citation

This project can be cited via the [`CITATION.cff`](CITATION.cff) file. GitHub recognises this format automatically and offers BibTeX and APA export under **“Cite this repository”**.

<a id="en-attribution"></a>
### 📜 Attribution and licensing

This project uses a **three-layer system** for transparency and legal robustness:

### Attribution hierarchy

1. **`ATTRIBUTION.md`** (repository level) — **Primary source** for compliance
   - Machine-readable table of all third-party content (fonts, emojis, assets)
   - Checked by CI/CD tools
   - **Audience:** Developers, maintainers, legal review

2. **`de/content/anhang-l-kolophon.md`** / **`en/content/appendix-l-colophon.md`** (PDF book) — **Reader-friendly**
   - Narrative font attribution for PDF readers
   - Production details (TeX Live, Pandoc, build environment)
   - **Audience:** Book readers without repo access

3. **`de/content/anhang-j-lizenz---offenheit.md`** / **`en/content/appendix-j-license-and-openness.md`** (concept) — **Licence philosophy**
   - Legal framework and share-alike principle
   - **Audience:** Legal professionals, AI trainers, remix projects

### ⚠️ Important: When changing fonts/emojis/assets

**Update all three layers:**
1. ✅ `ATTRIBUTION.md` → New row in table
2. ✅ `de/content/anhang-l-kolophon.md` / `en/content/appendix-l-colophon.md` → Section L.2 Typography
3. ✅ `de/content/anhang-j-lizenz---offenheit.md` / `en/content/appendix-j-license-and-openness.md` → Check licence matrix
4. ✅ Commit with `Signed-off-by:` (DCO)

Details: see [`AGENTS.md`](AGENTS.md) → “Attribution-Hierarchie”.

<a id="en-fonts"></a>
### Font design

### PDF generation
For PDF generation, **no** additional system-emoji fonts from external packages are pulled in, keeping the design consistent with the brand identity. Fonts can be configured in `publish.yml` via `pdf_options`:

```yaml
pdf_options:
  emoji_color: true
  main_font: "DejaVu Serif"  # Main body font
  sans_font: "DejaVu Sans"   # Sans-serif font for headings
  mono_font: "DejaVu Mono"   # Monospace font for code
```

This configuration ensures the document design matches the project guidelines.

<a id="en-tooling"></a>
### Tooling & build

The build tooling (`gitbook_worker`) is maintained externally and delivered from:

- https://github.com/Rob9999/gitbook-worker

This repository uses a **pinned, vendored package artifact** (see `requirements.txt`) and repo-local configuration (e.g. `de/publish.yml`, `en/publish.yml`, `content.yaml`).

Vendored artifact location (current pattern): `packages/gitbook-worker/*.tar.gz`

A step-by-step guide for local PDF generation can be found in [`how-to-build.md`](how-to-build.md).
