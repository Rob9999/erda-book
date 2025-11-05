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

**Lizenz dieses Release-Dokuments:** CC BY-SA 4.0  
**Copyright:** © 2025 Robert Alexander Massinger
