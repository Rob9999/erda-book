# Anhang L: Kolophon

## L.1 Über dieses Kolophon

Dieses Kolophon dokumentiert die **technischen und typografischen Details** der Produktion des ERDA-Buches. Es dient der **Transparenz** und erfüllt die **Attributionspflichten** für verwendete Schriftarten, Werkzeuge und Ressourcen. Alle hier aufgeführten Komponenten sind unter **offenen oder kompatiblen Lizenzen** verfügbar und wurden gemäß den in **Anhang J** definierten Lizenzgrundsätzen ausgewählt.

---

## L.2 Typografie und Schriftarten

Das ERDA-Buch verwendet folgende Schriftfamilien:

### L.2.1 DejaVu-Schriftfamilie

**DejaVu Serif** (Haupttext), **DejaVu Sans** (Überschriften, UI-Elemente), **DejaVu Sans Mono** (Code-Blöcke)

- **Version:** 2.37
- **Lizenz:** Bitstream Vera License + Public Domain (für DejaVu-Änderungen)
- **Copyright:** © 2003 Bitstream, Inc. (Bitstream Vera Basis); DejaVu-Änderungen gemeinfrei
- **Quelle:** [dejavu-fonts.github.io](https://dejavu-fonts.github.io/)
- **Distribution:** Ubuntu-Paket `fonts-dejavu-core`
- **Rechtlicher Hinweis:** Die Schriftdateien dürfen nicht separat verkauft werden. Die Einbettung in Dokumente (einschließlich PDF) ist uneingeschränkt erlaubt.

**Begründung der Wahl:**  
Die DejaVu-Familie bietet exzellente **Unicode-Abdeckung** für europäische Sprachen, mathematische Symbole und Sonderzeichen. Die Schriften sind technisch ausgereift, lesbar und unter einer **offenen Lizenz** verfügbar, die die kommerzielle Distribution des Buches ermöglicht.

### L.2.2 ERDA CC-BY CJK (Chinesisch, Japanisch, Koreanisch)

**ERDA CC-BY CJK**

- **Lizenz:** CC BY 4.0
- **Quelle:** Eigenentwicklung des ERDA-Projekts
- **Verwendung:** Ergänzung für CJK-Zeichen (Chinesisch, Japanisch, Koreanisch)
- **Rechtlicher Hinweis:** Namensnennung erforderlich; kommerzielle Nutzung erlaubt.

**Begründung der Wahl:**  
Für mehrsprachige Ausgaben (insbesondere Anhang J) wird eine CJK-Schrift benötigt, die unter **CC BY 4.0** lizenziert ist und konsistent mit den Lizenzgrundsätzen des Projekts bleibt.

### L.2.3 Twemoji Mozilla (Emojis)

**Twemoji Mozilla**

- **Version:** 0.6.0
- **Lizenz:** CC BY 4.0
- **Copyright:** © Twitter, Inc. und andere Mitwirkende
- **Quelle:** [github.com/mozilla/twemoji-colr](https://github.com/mozilla/twemoji-colr)
- **Distribution:** Ubuntu-Paket `fonts-twemoji`
- **Rechtlicher Hinweis:** Namensnennung erforderlich; kommerzielle Nutzung erlaubt.

**Begründung der Wahl:**  
Emojis sind integrale Bestandteile der mehrsprachigen Lizenzklauseln (Anhang J) und der visuellen Gestaltung. Twemoji bietet konsistente, farbige Darstellung unter einer **offenen Lizenz** ohne proprietäre Einschränkungen.

---

## L.3 Produktionswerkzeuge

Das ERDA-Buch wurde mit folgenden Open-Source-Werkzeugen erstellt:

### L.3.1 GitBook

- **Version:** Basis der Markdown-Struktur
- **Lizenz:** Apache 2.0
- **Verwendung:** Strukturierung, Navigation, HTML-Export
- **Quelle:** [gitbook.com](https://www.gitbook.com/)

### L.3.2 Pandoc

- **Version:** 3.6 (November 2024)
- **Lizenz:** GPL v2+
- **Verwendung:** Konvertierung von Markdown zu LaTeX/PDF
- **Quelle:** [pandoc.org](https://pandoc.org/)

**Technische Details:**  
Pandoc orchestriert die Transformation der Markdown-Quelldateien in ein LaTeX-Zwischenformat, das anschließend von LuaLaTeX in das finale PDF kompiliert wird.

### L.3.3 TeX Live

- **Version:** TeX Live 2025
- **Lizenz:** Gemischte Open-Source-Lizenzen (LaTeX Project Public License, Public Domain, u. a.)
- **Verwendung:** LaTeX-Engine für PDF-Generierung
- **Quelle:** [tug.org/texlive](https://tug.org/texlive/)

**Technische Details:**  
- **Engine:** LuaHBTeX 1.22.0 (TeX Live 2025)
- **Packages:** scheme-basic + xetex, fontspec, polyglossia, unicode-math, babel-german, enumitem, geometry, xcolor, booktabs, caption, fancyhdr
- **Installation:** CTAN-Mirror (install-tl-unx)

### L.3.4 Python-Toolchain

- **Version:** Python 3.11+
- **Lizenz:** Python Software Foundation License
- **Verwendung:** Build-Orchestrierung, Emoji-Verarbeitung, Qualitätssicherung
- **Hauptmodule:**
  - `workflow_orchestrator.py`: Master-Build-Prozess
  - `publisher.py`: PDF-Generierung
  - `emoji_utils.py`: Emoji-Erkennung und Font-Fallback

### L.3.5 Docker

- **Version:** Docker 24.0+
- **Lizenz:** Apache 2.0
- **Verwendung:** Reproduzierbare Build-Umgebung
- **Images:**
  - `erda-workflow-tools:latest`: TeX Live 2025, Pandoc 3.6, Python 3.11
  - `erda-publisher:legacy`: TeX Live 2021/2022 (Fallback)

---

## L.4 Produktionsumgebung

### L.4.1 Build-Plattform

- **Betriebssystem:** Ubuntu 22.04 LTS (Docker-Container)
- **Hardware:** Generischer x86_64-Prozessor
- **Build-Zeit:** ~2–5 Minuten (abhängig von Content-Größe)

### L.4.2 Versionskontrolle

- **System:** Git 2.34+
- **Repository:** GitHub (`Rob9999/erda-book`)
- **Branch-Modell:** `main` (stabil), `release_candidate` (Pre-Release)
- **CI/CD:** GitHub Actions (automatisierte Builds)

### L.4.3 Datum und Version

- **Build-Datum:** {{BUILD_DATE}} (automatisch generiert)
- **Version:** {{VERSION}} (siehe `CITATION.cff`)
- **Commit-Hash:** {{COMMIT_HASH}} (Git-Referenz)

---

## L.5 Qualitätssicherung

Die technische Qualität des ERDA-Buches wird durch folgende Maßnahmen sichergestellt:

1. **Automated Testing:** CI/CD-Pipeline validiert Build-Prozesse
2. **Lizenz-Compliance:** Automatisierte Prüfung auf inkompatible Lizenzen (siehe `AGENTS.md`)
3. **Font-Fallback:** Automatische Emoji-Erkennung und Font-Zuweisung
4. **UTF-8-Validierung:** Sicherstellung korrekter Zeichenkodierung
5. **DCO-Enforcement:** Alle Beiträge signiert (Developer Certificate of Origin)

Details zur inhaltlichen Qualitätssicherung finden sich in **Anhang K**.

---

## L.6 Danksagungen

Dieses Buch wäre ohne die **Open-Source-Community** nicht möglich gewesen. Besonderer Dank gilt:

- **Bitstream, Inc.** und den **DejaVu-Entwicklern** für die exzellente Schriftfamilie
- **Twitter, Inc.** und **Mozilla** für das Twemoji-Projekt
- Den **TeX Live**-, **Pandoc**- und **Python**-Communities
- Allen Beitragenden des ERDA-Projekts, die sich dem **DCO** verpflichtet haben

---

## L.7 Weiterführende Informationen

- **Vollständige Attribution:** Siehe `ATTRIBUTION.md` im Repository
- **Lizenzdetails:** Siehe **Anhang J: Lizenz & Offenheit**
- **Technische Dokumentation:** Siehe `README.md` und `.github/gitbook_worker/`
- **Zenodo-Archivierung:** DOI und Concept-DOI siehe `CITATION.cff`

---

## L.8 Hinweis zur Pflege dieses Kolophons

Dieses Kolophon ist Teil der **Attribution-Hierarchie** des ERDA-Projekts:

- **`ATTRIBUTION.md`** (Repository) = Primärquelle (maschinenlesbar)
- **Anhang L** (dieses Dokument) = Leserfreundliche Aufbereitung (PDF)
- **Anhang J** = Lizenzphilosophie und rechtliche Rahmenbedingungen

**Bei Änderungen an Fonts, Emojis oder Produktionswerkzeugen:**
1. `ATTRIBUTION.md` im Repository aktualisieren (neue Tabellenzeile)
2. Dieses Kolophon aktualisieren (Abschnitt L.2 Typografie / L.3 Werkzeuge)
3. `content/anhang-j-lizenz-and-offenheit.md` prüfen (Lizenzmatrix J.2)

Details siehe `AGENTS.md` → "Attribution-Hierarchie".

---

**Ende des Kolophons.**  
Dieses Dokument ist Teil des ERDA-Buches und unterliegt der **CC BY-SA 4.0**-Lizenz (siehe Anhang J).
