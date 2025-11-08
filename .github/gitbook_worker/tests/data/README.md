# Test Data

Sample markdown and CSV files used for integration and converter tests.

## Publishing Test Scenarios

Dieses Verzeichnis enthält isolierte Testdaten für verschiedene Publishing-Szenarien.

### `scenario-1-single-gitbook/`
**Single GitBook mit book.json**

Testet:
- Korrekte Auswertung von `book.json` (insbesondere `root: content/`)
- Einlesen von `SUMMARY.md` aus dem korrekten `root`-Verzeichnis
- Kombination mehrerer Markdown-Dateien gemäß SUMMARY
- LaTeX-Sonderzeichen im Titel und Content (& % $ # _ { } \)
- Emoji-Rendering (Standard und Flaggen)
- CJK-Font-Fallback

Dateien:
- `book.json` - GitBook-Konfiguration mit `root: content/`
- `publish.yml` - Publisher-Manifest mit `use_book_json: true`
- `content/SUMMARY.md` - Inhaltsverzeichnis
- `content/README.md` - Einführung
- `content/chapter-*.md` - Kapitel mit verschiedenen Markdown-Features

Erwartetes Ergebnis:
- ✅ Erfolgreicher PDF-Build
- ✅ Nur Dateien aus `content/` werden einbezogen
- ✅ Keine YAML-Parse-Fehler
- ✅ Keine LaTeX-Fehler bei Sonderzeichen

---

### `scenario-2-multi-gitbook/`
**Mehrere GitBooks in einem Repository**

Testet:
- Zwei separate GitBook-Projekte (project-a, project-b)
- Jedes Projekt mit eigener `book.json` und `content/`
- Array von Dokumenten in `publish.yml`
- Separate PDF-Generierung pro Projekt
- Keine Vermischung der Inhalte

Dateien:
- `publish.yml` - Manifest mit 2 Dokumenten
- `project-a/book.json` + `content/` - Backend-fokussiertes GitBook
- `project-b/book.json` + `content/` - Frontend-fokussiertes GitBook

Erwartetes Ergebnis:
- ✅ Zwei separate PDFs (`test-project-a.pdf`, `test-project-b.pdf`)
- ✅ Jedes PDF enthält nur eigene Inhalte
- ✅ Korrekte Titel aus jeweiliger `book.json`
- ✅ Exit Code 0

---

### Weitere Szenarien (geplant)

- `scenario-3-single-file/` - Einzelne Markdown-Datei ohne GitBook-Struktur
- `scenario-4-folder-without-gitbook/` - Ordner ohne `book.json` (Fallback-Modus)
