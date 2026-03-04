# ERDA Book

[![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Version](https://img.shields.io/badge/version-v2.0.0-green.svg)](https://github.com/Rob9999/erda-book/releases/tag/v2.0.0)

**Current version:** v2.0.0  
**As of (date):** 2026-03-01  
**Channel:** release_candidate (pre-release)  
**Codename / Release name:** Human AI Democrazy

**Multi-language democratic resilience framework**  
🇩🇪 Deutsche Fassung: [`de/`](de/publish/das-erda-buch.pdf)  
🇬🇧 English version: [`en/`](en/publish/the-erda-book.pdf)

**Sprungmarken / Jump links:** 🇩🇪 [Deutsch](#de) | 🇬🇧 [English](#en)

- 🇩🇪 [Deutsch](#de)
  - [Was ist das ERDA Buch?](#de-was-ist)
  - [Aktuelles Release (v2.0.0)](#de-release)
  - [Lizenz](#de-lizenz)
  - [Zitierung](#de-zitierung)
  - [Attribution und Lizenzierung](#de-attribution)
  - [Schriftarten-Design](#de-fonts)
  - [Tooling & Build](#de-tooling)
- 🇬🇧 [English](#en)
  - [What is the ERDA Book?](#en-what-is)
  - [Current release (v2.0.0)](#en-release)
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
### Aktuelles Release (v2.0.0) – 1. März 2026

> Dieses Release transformiert das ERDA-Buch von einem konzeptionellen Entwurf zu einem umfassenden Governance-Rahmenwerk mit konkreter Vertrags- und Bündnisarchitektur.

Erweiterung von **9 auf 14 Kapitel** mit über 200 Seiten neuem Inhalt:

| Kap. | Thema | Highlights |
|---|---|---|
| **10** | KI-Governance | Ko-Evolutions-Index (KEI) als demokratisches Frühwarninstrument |
| **11** | Bürger-Konzept | Adaptiver Pflichtdienst, demografischer Imperativ |
| **12** | Demokratie-Konzept | Sieben Transformationsregeln sozialer Demokratie |
| **13** | Strategische Souveränität | Werkzeugkoffer gegen Selbstabschreckung (Luftverteidigung, Attrition, Hybridabwehr) |
| **14** | Koalitionen der Willigen | EDDRC-Club-Architektur, Stufenmodell Tier 0–9, Verfassungsskizze (Art. 1–30), 6 Vertragsanlagen mit 155 Artikeln |

Weitere Neuerungen:
- ⚔️ **Zaluzhnyi-Integration:** Kill-Zonen, transparenter Gefechtsraum, Drohnenkrieg – Erkenntnisse aus dem russisch-ukrainischen Krieg (6 Kapitel)
- 📖 **D.5 Strategiepapier:** Russlands Verhandlungstaktik als Kriegsinstrument und europäische Gegenstrategien
- 📊 **Glossar:** 30 Begriffe (19 bestehend + 11 neu)
- 🌐 **Vollständige DE↔EN-Synchronisation** aller neuen Kapitel

Details: [`release-docs/v2.0.0/`](release-docs/v2.0.0/)

### Beiträge und Qualität

Das ERDA-Buch versteht sich als **lebendiges Dokument demokratischer Resilienz** – es lebt von der fachkundigen Mitwirkung aus Zivilgesellschaft, Wissenschaft, Politik und Praxis. Beiträge sind daher nicht nur willkommen, sondern ausdrücklich erwünscht.

**Redaktionelle Leitlinien:**

- **Qualitätsanspruch:** Jeder Beitrag sollte den analytischen Maßstäben des Projekts gerecht werden – sachlich fundiert, quellentransparent und konstruktiv im Sinne demokratischer Handlungsfähigkeit.
- **Verbindliche Regeln:** Bitte die Richtlinien in [`AGENTS.md`](AGENTS.md) beachten – insbesondere DCO-Sign-off, Lizenz- und Attributionspflichten sowie die DE↔EN-Synchronisation bei inhaltlichen Änderungen.
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
### Current release (v2.0.0) – 1 March 2026

> This release transforms the ERDA book from a conceptual draft into a comprehensive governance framework with a concrete treaty and alliance architecture.

Expansion from **9 to 14 chapters** with over 200 pages of new content:

| Ch. | Topic | Highlights |
|---|---|---|
| **10** | AI Governance | Co-evolution Index (KEI) as a democratic early-warning instrument |
| **11** | Citizen Concept | Adaptive duty service, demographic imperative |
| **12** | Democracy Concept | Seven transformation rules of social democracy |
| **13** | Strategic Sovereignty | Toolbox against self-deterrence (air defence, attrition, hybrid defence) |
| **14** | Coalitions of the Willing | EDDRC club architecture, tier model Tier 0–9, constitutional sketch (Art. 1–30), 6 treaty annexes with 155 articles |

Further additions:
- ⚔️ **Zaluzhnyi integration:** Kill zones, transparent battlespace, drone warfare – insights from the Russo-Ukrainian war (6 chapters)
- 📖 **D.5 Strategy paper:** Russia’s negotiation tactics as an instrument of war and European counter-strategies
- 📊 **Glossary:** 30 terms (19 existing + 11 new)
- 🌐 **Full DE↔EN synchronisation** of all new chapters

Details: [`release-docs/v2.0.0/`](release-docs/v2.0.0/)

### Contributions and quality

The ERDA Book sees itself as a **living document of democratic resilience** – it thrives on expert contributions from civil society, academia, policy-making, and practice. Contributions are therefore not merely welcome but actively encouraged.

**Editorial guidelines:**

- **Quality standards:** Every contribution should meet the project's analytical expectations – well-founded, source-transparent, and constructive in the service of democratic agency.
- **Binding rules:** Please observe the guidelines in [`AGENTS.md`](AGENTS.md) – in particular DCO sign-off, licensing and attribution duties, and DE↔EN synchronisation for content changes.
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
