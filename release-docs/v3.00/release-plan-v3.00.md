# ERDA Book - Release v3.00 Plan

**Status:** v3.00-Vorbereitung auf `release_candidate`; Content- und Metadaten-Sync umgesetzt; Final-Gates offen  
**Letzte Aktualisierung:** 2026-06-25

---

## Scope

Release 3.00 fokussiert auf zwei Arbeitsachsen: die demokratische Integrationsarchitektur des ERDA-Buches und die redaktionelle Reifung des Gesamtwerks. Inhaltlicher Kern ist das 4+1-Ring-System als pragmatisches Modell zwischen geopolitischer Partnerschaft, schrittweiser Integration und voller Mitgliedschaft. Redaktioneller Kern ist die Umsetzung der v2.5-Evaluation in klare Arbeitsgates.

### Kernthemen

1. **4+1-Ring-System**
   Kapitel 4.2.3 erhaelt ein neues Unterkapitel zur Integration ohne Wartesaal: globale demokratische Partner, demokratischer Beitrittsring, domaenenbasierter Mitgliedschaftsring, volle EU-/ERDA-Mitgliedschaft und freiwilliger tiefer verfassungsdemokratischer Kern.

2. **Interne Vernetzung**
   Das Modell wird mit Anhang A/B, Kapitel 5 EDA, Kapitel 6 CIVITAS, Kapitel 7 FORTERA, Kapitel 13 strategische Souveraenitaet sowie Kapitel 14 und Annex 14.F Membership Tiers verbunden.

3. **Release- und Metadatensynchronisation**
   README, `de/book.json`, `en/book.json`, `de/publish.yml`, `en/publish.yml`, CFF-Dateien, `.zenodo.json` und Release-Dokumentation werden auf v3.00 / 2026-06-25 gestellt.

4. **Redaktionelle Reifeagenda**
   Die v2.5-Evaluation wird in einen bereinigten Redaktionsleitfaden ueberfuehrt. Dieser definiert Zielklarheit, Evidenzlabels, Quellen- und Faktenaudit, PDF-Accessibility, Metadatenkonsistenz, Stilkontrolle und Publikationsarchitektur als v3.00-Arbeitsgegenstand.

### Nicht Teil dieses RC-Schritts

- Kein finaler Publish-Build.
- Keine Publisher-Freigabe.
- Kein Git-Tag.
- Keine Behauptung einer final freigegebenen englischen Uebersetzung; die EN-Fassung bleibt `in-review`.

---

## Meilensteine

| # | Meilenstein | Status |
|---|---|---|
| 1 | 4+1-Unterkapitel in DE erstellen und intern vernetzen | erledigt |
| 2 | EN-Synchronfassung erstellen und als `in-review` markieren | erledigt |
| 3 | Versions- und Datumsmetadaten auf v3.00 / 2026-06-25 setzen | erledigt |
| 4 | Release-Docs-Ordner `release-docs/v3.00/` anlegen | erledigt |
| 5 | Release History und Release-Index aktualisieren | erledigt |
| 6 | Basis-Konsistenzcheck der Release-Metadaten | erledigt |
| 7 | v2.5-Evaluation in Redaktionsleitfaden v3.00 ueberfuehren | erledigt |
| 8 | Redaktionsgates fuer Zielklarheit, Evidenzstatus, Quellen, Accessibility und Stil abarbeiten | offen |
| 9 | Final Review, Publish-Build und Publisher-Freigabe | offen |
| 10 | Main-Merge und Tag `v3.00` | offen |

---

## Deliverables

- Neues Unterkapitel 4.2.3.6 zum 4+1-Ring-System (DE).
- Englische Synchronfassung in Kapitel 4.2.3 (EN, `status: in-review`).
- Aktualisierte Quellen- und Kapitelverweise in 4.2.3.
- Bereinigter Redaktionsleitfaden aus der v2.5-Evaluation in `desktop/misc/`.
- Synchronisierte v3.00-Metadaten in README, book.json, publish.yml, CFF und Zenodo-Metadaten.
- Release-Dokumentation in `release-docs/v3.00/`.

---

## Arbeitsstroeme und Aufgaben

- [x] Inhaltliche Einbettung in Kapitel 4.2.3 statt eigener Anhang als Primaerloesung.
- [x] Interne Links zu bestehenden Buchthemen setzen.
- [x] DE/EN-Synchronisation nachziehen.
- [x] EN-Status auf `in-review` setzen.
- [x] README-Releaseabschnitte auf v3.00 aktualisieren.
- [x] CFF-Abstracts an den v3.00-Scope anpassen.
- [x] `.zenodo.json` auf v3.00-Beschreibung und Keywords aktualisieren.
- [x] v2.5-Evaluation in Redaktionsleitfaden v3.00 ueberfuehren.
- [x] Release-Metadaten per Basischeck pruefen.
- [ ] Zielgruppe, Gattung und Nutzungsszenario redaktionell klaeren.
- [ ] Evidenzlabel-System definieren und pilotieren.
- [ ] Quellen- und Faktenaudit fuer tragende Claims planen.
- [ ] Accessibility-Gate fuer den naechsten Publish-Build definieren.
- [ ] Stil- und Registerpass als Redaktionsauftrag planen.
- [ ] Publish-Artefakte nach Final-Freeze regenerieren.
- [ ] Final Review, Publisher-Freigabe und Tag dokumentieren.
