# Das ERDA Buch – Release v1.0.1

**Datum:** 2025-11-05  
**Tag:** `v1.0.1`  
**Autor:** Robert Alexander Massinger (mit ChatGPT/OpenAI)

---

## 📋 Zusammenfassung

Version 1.0.1 ist eine **technisch überarbeitete Ausgabe** des ERDA-Buches. Der Fokus liegt auf verbesserter Typografie, konsistenter Schriftverwendung und optimiertem Layout für das PDF. Gleichzeitig wurde die **Reproduzierbarkeit** durch vollständige Build-Dokumentation sichergestellt.

---

## ✨ Änderungen

### Technische Verbesserungen
- **Konsistente Schriften**: Einheitliche Verwendung der `erda-ccby-cjk` Font-Familie (CC BY 4.0 / MIT Dual-Lizenz) im gesamten Dokument
- **Optimierte Typografie**: Verbesserte Abstände, Zeilenumbrüche und Seitenlayouts für bessere Lesbarkeit
- **Saubere Inhaltsverzeichnisse**: Korrekte Kapitel-Hierarchie und Seitennummerierung in PDF-Bookmarks
- **Kleinere Layout-Korrekturen**: Behebung von Formatierungsinkonsistenzen in Tabellen, Listen und Code-Blöcken

### Reproduzierbarkeit & Build-Setup
- **Vollständige Quellen**: Alle GitBook-Markdown-Dateien im `content/` Verzeichnis
- **Build-Dokumentation**: `publish.yml` beschreibt den kompletten PDF-Build-Prozess
- **Metadaten harmonisiert**: `CITATION.cff`, `.zenodo.json` und `ATTRIBUTION.md` aufeinander abgestimmt
- **Font-Lizenzen geklärt**: Dual-Lizenzierung (CC BY 4.0 / MIT) für eigenentwickelte Fonts dokumentiert

### Lizenz & Attribution
- **Lizenzmatrix präzisiert**:
  - Texte, Grafiken, Diagramme: **CC BY-SA 4.0**
  - Code, Toolchain, Skripte: **MIT**
  - Eigenentwickelte Fonts: **CC BY 4.0** oder **MIT** (Dual-Lizenz)
  - Emojis (Twemoji): **CC BY 4.0**
- **Anhang J erweitert**: Mehrsprachige Lizenzklauseln (DE, EN, ES, FR, und viele weitere)
- **ATTRIBUTION.md aktualisiert**: Vollständige Nachweise aller verwendeten Assets

---

## 📦 Dateien in diesem Release

### Haupt-PDF
- `publish/das-erda-buch.pdf` – Finales, druckfertiges PDF (technisch überarbeitet)

### Quellen & Metadaten
- `publish/das-erda-buch.md` – Kombinierter Markdown-Quelltext
- `CITATION.cff` – Zitationsmetadaten (CFF 1.2.0 Format)
- `.zenodo.json` – Zenodo-Archivierungsmetadaten
- `ATTRIBUTION.md` – Vollständige Lizenz- und Quellennachweise

### Build-System
- `publish.yml` – Build-Manifest (Workflow-Definition)
- `book.json` – GitBook-Konfiguration
- `build-pdf.ps1` – PowerShell-Build-Skript

---

## 📜 Lizenzierung

Dieses Werk verwendet eine **differenzierte Lizenzmatrix**:

| Kategorie | Lizenz | Erläuterung |
|-----------|--------|-------------|
| **Texte, Grafiken, Diagramme** | CC BY-SA 4.0 | Freie Nutzung mit Namensnennung, Bearbeitungen unter gleicher Lizenz |
| **Code, Toolchain, Skripte** | MIT | Maximale Flexibilität, auch kommerzielle Nutzung |
| **Eigenentwickelte Fonts** | CC BY 4.0 oder MIT | Dual-Lizenz nach Wahl des Nutzers |
| **Emojis (Twemoji)** | CC BY 4.0 | Namensnennung erforderlich |

**Vollständige Details:** siehe `content/anhang-j-lizenz-and-offenheit.md` und `ATTRIBUTION.md`

---

## 🔗 Links

- **GitHub Repository**: https://github.com/Rob9999/erda-book
- **Zenodo Archiv**: [wird nach Release-Veröffentlichung automatisch erstellt]
- **Lizenz-Dokumentation**: [Anhang J](https://github.com/Rob9999/erda-book/blob/main/content/anhang-j-lizenz-and-offenheit.md)
- **Attribution**: [ATTRIBUTION.md](https://github.com/Rob9999/erda-book/blob/main/publish/ATTRIBUTION.md)

---

## 🙏 Mitwirkende

- **Robert Alexander Massinger** (Autor, München, Deutschland)
- **ChatGPT (OpenAI)** (KI-Assistent: Strukturierung, Lektorat, Ausarbeitung)

---

## 📌 Hinweise für Nutzer

### Zitierung
Bitte verwenden Sie die `CITATION.cff` für korrekte Literaturverweise. Beispiel (BibTeX):

```bibtex
@book{Massinger2025ERDA,
  title     = {ERDA – unsere demokratische Evolution: Strategie, Ethik und Zukunft Europas},
  author    = {Massinger, Robert Alexander},
  year      = {2025},
  publisher = {ERDA Institut (in Gründung)},
  note      = {Mit Beiträgen von ChatGPT (OpenAI)},
  url       = {https://github.com/Rob9999/erda-book},
  version   = {1.0.1}
}
```

### Bearbeitungen
- **Texte**: Bearbeitungen müssen unter **CC BY-SA 4.0** weitergegeben werden
- **Code**: Frei verwendbar unter **MIT** (Copyright-Hinweis beibehalten)
- **Fonts**: Wahl zwischen **CC BY 4.0** oder **MIT** (Markenname geschützt)

### Zenodo-Archivierung
Dieses Release wird automatisch auf Zenodo archiviert und erhält einen **dauerhaften DOI**. Der **Concept-DOI** verweist immer auf die neueste Version.

---

## 🐛 Bekannte Einschränkungen

- PDF-Erzeugung erfordert spezifische GitBook-Version (siehe `package.json`)
- Build-Prozess aktuell nur für Windows (PowerShell) getestet
- CJK-Font-Support begrenzt auf dokumentierte Zeichen (siehe Font-README)

---

## 🔜 Nächste Schritte

- Community-Feedback sammeln und einarbeiten
- Mehrsprachige Ausgaben (EN, FR, ES) vorbereiten
- Interaktive Web-Version mit GitBook publizieren
- ERDA-Institut formell gründen

---

## 🔧 Patch-Notizen — 2025-11-13 (CI & Build-Fixes)

Diese Release-Notes wurden am 2025-11-13 erweitert, um die jüngsten technischen Korrekturen und CI-/Build-Verbesserungen zu dokumentieren. Die Änderungen betreffen vor allem die PDF-Build-Pipeline, Docker-Images, LaTeX-Toolchain und die GitHub Actions Workflows.

Wesentliche Fixes (Kurzfassung):

- Docker / Build
  - Migration zu `Dockerfile.dynamic` für den Publisher-Build. Das neue Dockerfile installiert eine schlanke, reproduzierbare TeX-Live-Umgebung und richtet Fonts dynamisch ein.
  - Stabiler CTAN-Mirror verwendet: `https://ftp.tu-chemnitz.de/pub/tex/systems/texlive/tlnet/` (reduziert Mirror-bedingte Installationsfehler).
  - Zusätzliche LaTeX-Pakete ergänzt, die für die PDF-Erzeugung benötigt werden: `luatexbase`, `selnolig` (zusätzlich zu den zuvor ausgewählten ~25 Paketen).

- LaTeX / Pandoc
  - Pandoc-Workaround: Die CLI-Option `-V mainfontfallback=...` ist in Pandoc 3.6+ fehlerhaft. Daher wurde die manuelle LaTeX-Fallback-Implementierung aktiviert (statisch, robust).
  - Titel-Rendering: `\\AtBeginDocument{\\maketitle}` wird nun in der generierten LaTeX-Header-Datei gesetzt, damit der Buchtitel zuverlässig im PDF erscheint.
  - LaTeX-Escaping-Bug behoben: Rohstring-Fehler `r"\\&"` → korrigiert zu `"\\&"`, wodurch `&` in Titel/Metadaten korrekt als `\\&` escaped wird.

- Workflows & CI
  - `.github/workflows/test.yml` und `.github/workflows/orchestrator.yml` angepasst, damit CI dieselbe, getestete Umgebung verwendet (`Dockerfile.dynamic`) und nicht mehr die alte, unvollständige Docker-Konfiguration.
  - `test.yml` Verbesserungen:
    - Einheitliche Emoji-Fonts installiert (Twemoji Mozilla) für Konsistenz zwischen Umgebungen
    - `pytest` Flags für bessere Fehlerausgaben (`--tb=short`) und bessere Test-Isolierung (Marker für langsame Tests)
    - Verifikation der Fonts robuster gemacht (SIGPIPE-Problem mit `grep -q` behoben)
  - `orchestrator.yml` Anpassungen:
    - Build/Push konfiguriert auf `Dockerfile.dynamic` (GHCR-Images enthalten jetzt die Fixes)

- Tests & Validierung
  - Lokale und Container-geführte Tests:
    - Unit-Tests: 147 passed, 7 skipped
    - Integration-Tests: 6 passed, 4 skipped
  - PDF-Erzeugung lokal und in Docker validiert (CJK, Emojis, Titel, Tabellen)

- Commits / Audit
  - Relevante Commits dieser Änderung (lokale Historie):
    - 9720e01 — fix: Add missing LaTeX packages and stable CTAN mirror for reliable CI builds
    - fe28777 — fix: Resolve SIGPIPE error in font verification check
    - 5910bea — ci: Migrate workflows to Dockerfile.dynamic and improve test isolation
    - db6dc05 — fix: Correct LaTeX escaping and update tests for manual fallback
    - 11324c8 — fix: Force manual LaTeX fallback for Pandoc 3.6+ font handling

Hinweis: Diese Notizen dokumentieren rein technische Änderungen an der Build-/CI-Infrastruktur und enthalten keine redaktionellen Änderungen am Buchtext selbst.

---

**Lizenz dieses Release-Dokuments:** CC BY-SA 4.0  
**Copyright:** © 2025 Robert Alexander Massinger
