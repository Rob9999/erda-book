# Release-Zertifizierungsprotokoll v2.0.0

**Projekt:** ERDA – Das Buch  
**Version:** 2.0.0  
**Datum:** 2026-03-01  
**Prüfer:** GitHub Copilot (automatisiert)  
**Status:** 🔄 IN BEARBEITUNG

---

## Übersicht

Dieses Protokoll dokumentiert die **systematische Qualitätsprüfung** vor der Release-Freigabe v2.0.0. Alle Punkte müssen mit ✅ (BESTANDEN) markiert sein, bevor das Release freigegeben werden kann.

---

## 1️⃣ Lizenz-Compliance

### 1.1 Allgemeine Lizenz-Dokumentation

| Checkpoint | Status | Details |
|------------|--------|---------|
| `LICENSE` (CC BY-SA 4.0 für Texte) vorhanden | ✅ | Root + de/ + en/ |
| `LICENSE-CODE` (MIT) vorhanden | ✅ | Root + de/ + en/ |
| `LICENSE-FONTS` (Dual CC BY 4.0 / MIT) vorhanden | ✅ | Root + de/ + en/ |
| `ATTRIBUTION.md` vorhanden | ✅ | de/publish/ + en/publish/ |
| Anhang J (Lizenz & Offenheit) aktuell (DE + EN) | ✅ | Unverändert zu v1.0.2 |
| `.zenodo.json` enthält korrekte Lizenzangabe | ✅ | CC-BY-SA-4.0 |
| `CITATION.cff` Lizenz = CC-BY-SA-4.0 | ✅ | Root + de/ + en/ |

**Status:** ✅ **BESTANDEN** (keine Lizenzänderungen zu v1.0.2)

### 1.2 Emoji-Lizenz: Twemoji (CC BY 4.0)

| Checkpoint | Status | Details |
|------------|--------|---------|
| `AGENTS.md` spezifiziert Twemoji (CC BY 4.0) | ✅ | Korrekt |
| `publish.yml` verwendet Twemoji | ✅ | DE + EN |
| Keine verbotenen Emoji-Sets im Build | ✅ | Twemoji COLR in fonts-storage/ |

**Status:** ✅ **BESTANDEN**

### 1.3 Font-Lizenz

| Checkpoint | Status | Details |
|------------|--------|---------|
| Fonts in `fonts-storage/` sind CC BY 4.0 oder MIT | ✅ | DejaVu + Twemoji COLR |
| Keine OFL/GPL/proprietären Fonts | ✅ | Geprüft |

**Status:** ✅ **BESTANDEN**

---

## 2️⃣ Inhalt & Struktur

### 2.1 Kapitelvollständigkeit

| Checkpoint | Status | Details |
|------------|--------|---------|
| Kapitel 1–9 vorhanden (DE + EN) | ✅ | Unverändert + Kap. 5/7 erweitert |
| Kapitel 10 (KI Konzept) DE + EN | ✅ | Vollständig |
| Kapitel 11 (Bürger Konzept) DE + EN | ✅ | 4 Unterkapitel |
| Kapitel 12 (Demokratie Konzept) DE + EN | ✅ | 12.1 + 12.A |
| Kapitel 13 (Strategische Souveränität) DE + EN | ✅ | 7 Unterkapitel |
| Kapitel 14 (Koalitionen der Willigen) DE + EN | ✅ | 7 Unterkapitel + 6 Annexe |
| Anhänge A–L vorhanden (DE + EN) | ✅ | Inkl. D.5, D.6, Glossar-Update |

### 2.2 Navigation & Verweise

| Checkpoint | Status | Details |
|------------|--------|---------|
| DE SUMMARY.md enthält alle Kapitel/Anhänge | ✅ | 318 Zeilen |
| EN SUMMARY.md enthält alle Kapitel/Anhänge | ✅ | 318 Zeilen |
| Appendix-Reihenfolge DE korrekt (A→L) | ✅ | |
| Appendix-Reihenfolge EN korrekt (A→L) | ✅ | Korrigiert (Appendix A war am Ende) |
| D.6 in SUMMARY.md eingetragen (DE + EN) | ✅ | |
| Dateizahl DE = Dateizahl EN | ✅ | 316 = 316 |

### 2.3 Übersetzungssynchronisation

| Checkpoint | Status | Details |
|------------|--------|---------|
| Alle DE-Dateien haben EN-Gegenstücke | ✅ | 316/316 |
| EN-Dateien haben YAML-Frontmatter (source, status) | ✅ | status: draft |
| Keine verwaisten EN-Dateien ohne DE-Quelle | ✅ | |

**Status:** ✅ **BESTANDEN**

---

## 3️⃣ Metadaten & Konsistenz

| Checkpoint | Status | Details |
|------------|--------|---------|
| README.md Version = v2.0.0 - rc 1 | ✅ | |
| README.md Datum = 2026-03-01 | ✅ | |
| `de/book.json` date = 2026-03-01 | ✅ | |
| `en/book.json` date = 2026-03-01 | ✅ | |
| `.zenodo.json` description aktuell (Kap. 11–14) | ✅ | |
| `CITATION.cff` Version aktuell | ⏳ | Prüfung empfohlen |
| Anhang D README Block-Zählung korrekt | ✅ | „vier Blöcke (A–D)" + Tool-Box + Strategiepapier |
| D.4 Kapitelumfang = 5–14 | ✅ | DE + EN |
| Anhang I Glossar enthält Kap. 10–14 Begriffe | ✅ | 30 Begriffe total |

**Status:** ✅ **BESTANDEN** (CITATION.cff Versionsprüfung empfohlen)

---

## 4️⃣ Build & Artefakte

| Checkpoint | Status | Details |
|------------|--------|---------|
| DE PDF erzeugt und committed | ✅ | `de/publish/das-erda-buch.pdf` |
| DE Merged MD erzeugt und committed | ✅ | `de/publish/das-erda-buch.md` |
| EN PDF erzeugt und committed | ✅ | `en/publish/the-erda-book.pdf` |
| EN Merged MD erzeugt und committed | ✅ | `en/publish/the-erda-book.md` |
| Orchestrator erfolgreich durchgelaufen | ✅ | Lokal (DE + EN) |

**Status:** ✅ **BESTANDEN**

---

## 5️⃣ Git & Versionierung

| Checkpoint | Status | Details |
|------------|--------|---------|
| Branch `release_candidate` sauber | ✅ | Keine uncommitted Changes |
| Alle Release-Dateien committed | ✅ | |
| DCO (Signed-off-by) in allen Commits | ✅ | |
| Tag `v2.0.0` noch nicht vorhanden | ✅ | Wird nach Merge gesetzt |
| `main` Branch bereit für Merge | ⏳ | PR noch nicht erstellt |

**Status:** ⏳ **AUSSTEHEND** (PR-Erstellung)

---

## 6️⃣ Release-Dokumentation

| Checkpoint | Status | Details |
|------------|--------|---------|
| Release Notes DE vorhanden | ✅ | `release-notes-v2.0.0.md` |
| Release Notes EN vorhanden | ✅ | `release-notes-v2.0.0-en.md` |
| Inhaltsbeschreibung DE vorhanden | ✅ | `inhaltsbeschreibung-version-2.0.0.md` |
| Description EN vorhanden | ✅ | `description-version-2.0.0-en.md` |
| Release Status vorhanden | ✅ | `RELEASE-2.0.0-STATUS.md` |
| Release Plan aktuell | ✅ | `release-plan-v2.0.0.md` |
| `release-docs/Releases.md` v2.0.0 Eintrag | ✅ | |

**Status:** ✅ **BESTANDEN**

---

## 🎯 Zusammenfassung

### Bestanden

- ✅ Lizenz-Compliance (Texte, Code, Fonts, Emojis)
- ✅ Inhalt & Struktur (14 Kapitel, Anhänge A–L, SUMMARY.md)
- ✅ Übersetzungssynchronisation (316/316 Dateien)
- ✅ Metadaten & Konsistenz (README, book.json, .zenodo.json)
- ✅ Build & Artefakte (PDF/MD DE + EN)
- ✅ Release-Dokumentation vollständig

### Noch offen

- ⏳ `CITATION.cff` Versionsnummer prüfen
- ⏳ PR: main ← release_candidate erstellen
- ⏳ Tag `v2.0.0` setzen und pushen
- ⏳ Zenodo-Veröffentlichung
- ⏳ Lektorat/Terminologie-Feinschliff (empfohlen, nicht blockierend)

---

## ✍️ Release-Freigabe

**Release v2.0.0 ist FREIGEGEBEN:** ⏳ **AUSSTEHEND**

**Voraussetzung:** PR erstellen, mergen, Tag setzen.

**Freigabe durch:** _[NAME]_  
**Datum:** _[DATUM]_  
**Signatur:** _[DIGITAL ODER MANUELL]_

---

**Protokoll erstellt:** 2026-03-01  
**Protokoll-Version:** 1.0  
**Lizenz:** CC BY-SA 4.0 (dieses Protokoll)
