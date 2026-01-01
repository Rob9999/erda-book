# Release-Zertifizierungsprotokoll v1.0.2

**Zeitstempel:** 2026-01-01  
**Release-Version:** v1.0.2  
**Projektname:** ERDA-Buch  
**Branch:** release_candidate  
**Zertifizierer:** GitHub Copilot (automatisiert)  
**Status:** 🔄 Entwurf (Pruefungen stehen aus)

---

## Executive Summary (kurz)
- Inhalt: EN-Strukturfehler behoben (Kapitel 3 korrekt eingeordnet), fehlendes Kapitel 3.7 uebersetzt, Appendix-J-Heading angepasst.
- Release-Docs: DE und EN Kurzbeschreibungen ergaenzt.
- Noch offen: PDF-Build/CI fuer 1.0.2, erneute Lizenz- und Attribution-Pruefung, Tagging/Zenodo.

---

## 1. Lizenz-Compliance
- **Texte/Grafiken/Diagramme:** CC BY-SA 4.0 (unveraendert)
- **Code/Toolchain/Skripte:** MIT (unveraendert)
- **Fonts:** CC BY 4.0 oder MIT (dual) (unveraendert)
- **Emojis:** Twemoji (CC BY 4.0) (unveraendert)
- **Check:** Delta zu 1.0.1 minimal; erneute Pruefung von `ATTRIBUTION.md` und Appendix J empfohlen.

## 2. Inhalte & Struktur
- EN `SUMMARY.md` aktualisiert (Kapitel 3 zwischen 2 und 4)
- EN Kapitel 3.7 hinzugefuegt
- EN Kapitel-README fuer Kapitel 3 hinzugefuegt (GitBook-Baum korrekt)
- Appendix-J Heading korrigiert

## 3. Build & QA (offen)
- PDF-Build fuer 1.0.2 ausstehend (orchestrator, EN/DE) mit `.venv`
- CI-Workflows fuer 1.0.2 noch nicht erneut gelaufen
- Docker-Build nicht erneut geprueft (erwartet unveraendert)

## 4. Metadaten
- `.zenodo.json`, `CITATION.cff`, `publish.yml` nicht angepasst; Pruefung auf Versionsstand empfohlen (Tag folgt nach Build)

## 5. Release-Schritte (to-do)
1) Orchestrator laufen lassen (EN/DE) und PDFs erzeugen
2) CI-Workflows gruene Durchlaeufe sicherstellen
3) Abschlusspruefung Lizenz/Attribution (Delta zu 1.0.1 minimal)
4) Tag `v1.0.2` setzen, Zenodo Upload

---

**Hinweis:** Dieses Protokoll ist ein Entwurf bis die offenen Pruefungen abgeschlossen sind.
