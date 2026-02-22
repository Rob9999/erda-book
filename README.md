# ERDA Book

**Current version:** v2.0.0 - rc 1 
**As of (date):** 2026-02-07  
**Channel:** release_candidate (pre-release)  
**Codename / Release name:** Human AI Democrazy

**Multi-language democratic resilience framework**  
🇩🇪 Deutsche Fassung: [`de/`](de/publish/das-erda-buch.pdf)  
🇬🇧 English version: [`en/`](en/publish/the-erda-book.pdf)

**Sprungmarken / Jump links:** 🇩🇪 [Deutsch](#de) | 🇬🇧 [English](#en)

- 🇩🇪 [Deutsch](#de)
  - [Was ist das ERDA Buch?](#de-was-ist)
  - [Attribution und Lizenzierung](#de-attribution)
  - [Schriftarten-Design](#de-fonts)
  - [Tooling (gitbook_worker)](#de-tooling)
- 🇬🇧 [English](#en)
  - [What is the ERDA Book?](#en-what-is)
  - [Attribution and licensing](#en-attribution)
  - [Font design](#en-fonts)
  - [Tooling (gitbook_worker)](#en-tooling)

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

### Beiträge und Qualität

Beiträge sind willkommen, aber bitte die Regeln in AGENTS.md beachten (DCO Sign-off, Lizenz-/Attribution-Pflichten, DE↔EN Synchronisation bei Inhaltsänderungen).

Hinweis: Inhalte sind „as is“; keine Rechts- oder Fachberatung.

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
### Tooling (gitbook_worker)

Das Build-Tooling (`gitbook_worker`) wird extern gepflegt und von hier bezogen:

- https://github.com/Rob9999/gitbook-worker

Dieses Repository verwendet ein **gepinntes, vendortes Paket-Artefakt** (siehe `requirements.txt`) sowie repo-lokale Konfiguration (z. B. `de/publish.yml`, `en/publish.yml`, `content.yaml`).

Ablageort des vendorten Artefakts (aktuelles Muster): `packages/gitbook-worker/*.tar.gz`

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

### Contributions and quality

Contributions are welcome—please follow the rules in `AGENTS.md` (DCO sign-off, licensing/attribution duties, and DE↔EN synchronization for content changes).

Note: content is provided “as is”; this is not legal or professional advice.

<a id="en-attribution"></a>
### 📜 Attribution and licensing

This project uses a **three-layer system** for transparency and legal robustness:

1. **`ATTRIBUTION.md`** (repository level) — primary machine-readable compliance source.
2. **`de/content/anhang-l-kolophon.md`** / **`en/content/appendix-l-colophon.md`** (PDF level) — reader-friendly colophon and typography attribution.
3. **`de/content/anhang-j-lizenz---offenheit.md`** / **`en/content/appendix-j-license-and-openness.md`** (concept level) — license philosophy and openness.

When changing fonts/emojis/assets, update all three layers and commit with `Signed-off-by:` (DCO).

<a id="en-fonts"></a>
### Font design

For PDF generation, no extra external system-emoji fonts are pulled in. Fonts can be configured in `publish.yml` via `pdf_options`.

<a id="en-tooling"></a>
### Tooling (gitbook_worker)

The build tooling (`gitbook_worker`) is maintained externally and delivered from:

- https://github.com/Rob9999/gitbook-worker

This repository uses a **pinned, vendored package artifact** (see `requirements.txt`) and repo-local configuration (e.g. `de/publish.yml`, `en/publish.yml`, `content.yaml`).

Vendored artifact location (current pattern): `packages/gitbook-worker/*.tar.gz`
