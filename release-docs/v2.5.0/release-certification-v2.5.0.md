# Zertifizierungsprotokoll v2.5.0 (Draft)

**Release:** v2.5.0  
**Release name:** Democratic Knowledge  
**Stand:** 2026-05-05
**Status:** Draft, nicht freigegeben  
**Zuständige Rolle:** Redakteur:in  
**Mitwirkende Rollen:** Writer, Editor, Lektor, Native gb-en Translator, Publisher

---

## 1. Zertifizierungsentscheidung

| Feld | Eintrag |
|---|---|
| Entscheidung | offen |
| Entscheidung am | offen |
| Entscheidung durch Rolle | Redakteur:in |
| Freigabeumfang | offen |
| Restrisiken akzeptiert | offen |
| Tag-Freigabe `v2.5.0` | offen |

Kurzbegründung:

> Draft. Die finale Begründung wird nach Abschluss der Release-Gates eingetragen.

---

## 2. Release-Identität und Metadaten

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Version final `v2.5.0` | offen | | |
| Releasedatum konsistent | offen | | |
| README, book.json, CFF, Zenodo synchron | offen | | |
| Release Notes final | offen | | |
| Release History final | offen | | |
| Channel-/Branch-Aussage konsistent | offen | | |

---

## 3. Technische Gates

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Git-Status sauber und synchron | offen | | |
| `git diff --check` sauber | offen | | |
| Frontmatter-Gate DE/EN bestanden | offen | | |
| Keine Content-Keys `lang`, `language`, `lang-version` | offen | | |
| Rollen-/Tooling-Dokumentation auf `content_lang` geprüft | offen | | |

---

## 4. Quality-Tools des gitbook_worker

| Tool | Testmodus | Ergebnis | Brauchbarkeit | Nachweis |
|---|---|---|---|---|
| `gitbook_worker.tools.quality.link_audit` | CIVITAS P.2 DE/EN | bestanden im P.2-Scope | geeignet als technischer Gate-Hinweis, mit 403-Gegenpruefung | `source-link-check-civitas-v2.5.0.md` |
| `gitbook_worker.tools.quality.sources` | DE/EN Quellenexport | bestanden im P.2-Scope | geeignet zur Quelleninventur, nicht als inhaltliche Wahrheit | `source-link-check-civitas-v2.5.0.md` |
| `gitbook_worker.tools.quality.ai_references` | lokaler Test / Wrapper | nur Hinweischarakter | nicht autoritativ; 429, Kontextgrenzen und Fehlbewertungen dokumentiert | `source-delta-since-v2.0.0-v2.5.0.md`, `source-review-v2.5-priority-references-2026-05-05.md` |
| `gitbook_worker.tools.quality.staatenprofil_links` | nicht final im v2.5-A6/A7-Scope | offen | Backlog fuer vollstaendige Staatenprofil-Aktualitaet | `source-delta-since-v2.0.0-v2.5.0.md` |

Bewertung:

Bewertung: Die fuer CIVITAS und die v2.5-Prioritaetsreferenzen eingesetzten Tools sind als technische Hilfen dokumentiert. AI-gestuetzte Ergebnisse wurden nicht als Quellenwahrheit uebernommen; entscheidend war die manuelle Pruefung gegen DOI, Originalseiten, offizielle EU-/Eurostat-Quellen und bibliografische Plausibilitaet.

---

## 5. Quellen- und Referenzaktualität

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Quellenabschnitte DE extrahiert | erledigt im CIVITAS-P.2-Scope | `source-link-check-civitas-v2.5.0.md` | Gesamtbuch bleibt Final-Gate. |
| Quellenabschnitte EN extrahiert | erledigt im CIVITAS-P.2-Scope | `source-link-check-civitas-v2.5.0.md` | Gesamtbuch bleibt Final-Gate. |
| Externe Links geprüft | erledigt fuer P.2 und v2.5-Prioritaetsreferenzen | `source-review-v2.5-priority-references-2026-05-05.md` | Keine bekannte 404-Referenz im geaenderten Scope. |
| Lokale Bilder/Medien geprüft | technisch offen | | Nicht Teil der A5-Prioritaetsquellenpruefung. |
| Risikobehaftete Zahlen/Aussagen geprüft | erledigt im Prioritaetsscope | `source-review-v2.5-priority-references-2026-05-05.md` | Kapitel 13.8 wurde mit offiziellen EU-/Eurostat-Quellen nachgeschaerft. |
| Offene Quellenfragen dokumentiert | erledigt fuer v2.5-Prioritaetsscope | `source-delta-since-v2.0.0-v2.5.0.md` | Vollstaendige Staatenprofil-Aktualitaet bleibt v2.6/backlog. |

Besonders zu prüfen:

- EU-, NATO-, Ukraine-, Sicherheits- und Finanzierungszahlen
- Jahreszahlen, Datumsangaben und Roadmap-Zeiträume
- Aussagen mit direktem Bezug auf aktuelle Programme, Verträge, Institutionen oder politische Beschlüsse

### 5.1 Teilzertifizierung A5 - CIVITAS P.2

| Feld | Eintrag |
|---|---|
| Prüfdatum | 2026-05-04 |
| Prüfrolle | Redakteur:in |
| Scope | CIVITAS P.2 DE/EN, Referenzen `[1]` bis `[16]`, DOI, Plattform-/Rechtsquellen |
| Toolreports | `tmp/a5-civitas/sources-de.csv`, `tmp/a5-civitas/sources-en.csv`, `tmp/a5-civitas/link-audit-civitas-de.csv`, `tmp/a5-civitas/link-audit-civitas-en.csv` |
| Dauerhafter Report | `release-docs/v2.5.0/source-link-check-civitas-v2.5.0.md` |
| Ergebnis | erfüllt mit dokumentiertem Restrisiko |

**Befund:** `sources` extrahierte DE/EN-Quellenreports. `link_audit` meldete für CIVITAS P.2 DE/EN nach redaktioneller Heading-Normalisierung jeweils 0 broken links, 1 good DOI-link, 0 image issues, 0 duplicate headings, 0 citation gaps und 0 TODOs. Die Referenzen `[1]` bis `[16]` wurden risikobasiert geprüft; DOI- und Weblinks sind verifiziert oder als bibliografische/rechtliche Quellenklasse plausibel dokumentiert.

**Restrisiko:** Einige Anbieter blockieren CLI-Abrufe zeitweise mit `403`; die betroffenen Quellen wurden per `curl`, DOI-Handle-API oder bibliografischer Plausibilität gegengeprüft. Kein A5-Blocker für CIVITAS P.2.

---

## 6. Inhaltliche Prüfung DE

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| DE-Haupttext final geprüft | offen | | |
| Neue v2.5-Inhalte integriert und plausibel | offen | | |
| Querverweise und SUMMARY geprüft | offen | | |
| Glossar und Mini-Wording-Set konsistent | offen | | |
| Ethik-vor-Strategie-Pass redaktionell abgenommen | offen | | |
| Keine offenen Arbeitsmarker in Release-Inhalten | offen | | |

---

## 7. EN-Übersetzungsprüfung

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Rolle `Native gb-en Translator` angewendet | offen | | |
| EN-Statusauswertung erstellt | offen | | |
| EN-Dateien gegen DE-Quelle geprüft | offen | | |
| Britisches Englisch und Terminologie geprüft | offen | | |
| Bedeutungs- und Quellenfidelity geprüft | offen | | |
| Nicht freigegebene EN-Dateien transparent benannt | offen | | |

Freigabeaussage EN:

> offen

---

## 8. Build- und Artefaktprüfung

| Artefakt / Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| DE Publish Markdown | erzeugt | `de/publish/das-erda-buch.md` | A6-Lauf 2026-05-05, Orchestrator: `converter=ok`, `publisher=ok`. |
| DE PDF | erzeugt | `de/publish/das-erda-buch.pdf` | `pdfinfo`: 863 Seiten, 4.084.968 Bytes, CreationDate 2026-05-05 13:18 MESZ. |
| EN Publish Markdown | erzeugt | `en/publish/the-erda-book.md` | A6-Rerun 2026-05-05; Markdown enthaelt P.2, Kapitel 6 und Quellenstand 13.8. |
| EN PDF | erzeugt mit Tooling-Restrisiko | `en/publish/the-erda-book.pdf` | `pdfinfo`: 838 Seiten, 4.095.338 Bytes, CreationDate 2026-05-05 13:25 MESZ. Der letzte EN-Orchestrator schrieb das PDF, hing danach jedoch und wurde beendet. |
| PDF-Fonts: DejaVu | bestanden | `pdffonts` DE/EN | DejaVuSerif, DejaVuSansMono und Varianten eingebettet. |
| PDF-Fonts: Twemoji Mozilla | bestanden | `pdffonts` DE/EN | TwemojiMozilla eingebettet. LaTeX meldet weiter einzelne fehlende Emoji-/Symbolzeichen als Warnungen. |
| PDF-Fonts: ERDA CC-BY CJK | offen / nicht ausgeloest | `pdffonts` DE/EN | Kein CJK-Font in den aktuellen PDFs sichtbar; falls CJK-Glyphen releasekritisch sind, separaten CJK-Testlauf nachziehen. |
| Sichtprüfung DE PDF | technisch stichprobengeprueft | `pdftotext`, `pdfinfo` | Titelseite zeigt 2026-05-05 / Version 2.5.0-rc1; vollstaendige Publisher-Sichtpruefung bleibt Final-Gate. |
| Sichtprüfung EN PDF | technisch stichprobengeprueft | `pdftotext`, `pdfinfo` | Titelseite zeigt 2026-05-05 / Version 2.5.0-rc1; vollstaendige Publisher-Sichtpruefung bleibt Final-Gate. |

---

## 9. Freeze-Protokoll

| Feld | Eintrag |
|---|---|
| Content-Freeze erklärt am | offen |
| Freeze erklärt durch Rolle | Redakteur:in |
| Erlaubte Änderungen nach Freeze | nur Release-Fixes, Build-Fixes, Metadatenkorrekturen |
| Änderungen nach Freeze dokumentiert | offen |
| Freeze aufgehoben? | nein / offen |

---

## 10. Final Review und Publisher-Freigabe

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Redakteur-Finalreview abgeschlossen | offen | | |
| Publisher-Buildfreigabe abgeschlossen | offen | | |
| Finaler Worktree geprüft | offen | | |
| Tag `v2.5.0` vorbereitet | offen | | |
| GitHub-/Zenodo-Releasebeschreibung final | offen | | |

Finale Aussage:

> Draft. Keine finale Freigabe, solange die oben genannten Prüfungen offen sind.

---

## 11. Teilzertifizierung A4 - Rechtsformulierungen CIVITAS

Diese Teilzertifizierung betrifft nur die redaktionelle A4-Frage aus der Anhang-M-Beurteilung: Werden DSGVO, Digital Services Act, eIDAS, EMRK/ECHR und Grundrechte als Anforderungen/Zielrahmen dargestellt, statt als bereits juristisch geprüfte Konformität behauptet?

| Feld | Eintrag |
|---|---|
| Prüfdatum | 2026-05-04 |
| Prüfrolle | Redakteur:in |
| Skript | `scripts/quality/legal_claims_scan.py` |
| Scope | Kapitel 6 DE/EN und CIVITAS P.2 DE/EN |
| Report | `release-docs/v2.5.0/legal-claims-scan-civitas-v2.5.0.md` |
| Ergebnis | erfüllt mit dokumentiertem Restrisiko |

**Befund:** Der Scan fand 64 Kandidatenstellen, davon 6 `review-high`-Treffer. Die `review-high`-Treffer liegen im P.2-Papertext bzw. dessen Anhangserklärungen; die neu verdichteten Kapitel-6-Stellen bleiben im Anforderungs-, Roadmap- und Zielrahmen. Die Treffer werden als redaktionell prüfpflichtige Formulierungen dokumentiert, nicht als juristische Zertifizierung.

**Entscheidung:** Für v2.5.0 ist A4 als Release-Check erfüllt mit Restrisiko. CIVITAS wird nicht als rechtlich geprüfte Plattform dargestellt. Vor Finalfreigabe bleiben Build-/Artefaktprüfung, Quellen-/Linkprüfung und Publisher-Freigabe offen. Diese Aussage ist keine Rechtsberatung.

---

## 12. Teilzertifizierung A6 - Build- und Artefaktprüfung

Diese Teilzertifizierung dokumentiert den Arbeitsstand zu A6 aus der Anhang-M-Beurteilung: Publish-Artefakte nach sauberem Inhaltscommit neu erzeugen, technisch pruefen und Diff-/Tooling-Risiken benennen.

| Feld | Eintrag |
|---|---|
| Prüfdatum | 2026-05-05 |
| Prüfrolle | Publisher mit Redakteur:in-Zuarbeit |
| DE Build | `converter=ok`, `publisher=ok` |
| EN Build | Markdown und PDF erzeugt; letzter Orchestrator-Rerun hing nach PDF-Erzeugung |
| DE PDF | 863 Seiten, 4.084.968 Bytes, CreationDate 2026-05-05 13:18 MESZ |
| EN PDF | 838 Seiten, 4.095.338 Bytes, CreationDate 2026-05-05 13:25 MESZ |
| Fontbefund | DejaVu und TwemojiMozilla eingebettet; CJK-Font im aktuellen PDF nicht ausgeloest |
| Ergebnis | erfuellt mit Tooling-Restrisiko |

**Befund:** Die Publish-Artefakte wurden nach der P.2-Formatbereinigung und der Metadaten-Synchronisation auf 2026-05-05 neu erzeugt. Die Titelseiten der PDFs weisen `2026-05-05 - Version 2.5.0-rc1` aus. `pdffonts` bestaetigt eingebettete DejaVu- und TwemojiMozilla-Fonts. Der EN-Rerun erzeugte ein aktuelles PDF, gab aber nach der PDF-Erzeugung nicht sauber an den Orchestrator zurueck; der Prozess wurde manuell beendet.

**Entscheidung:** A6 ist fuer den aktuellen RC-Artefaktstand arbeitsfaehig dokumentiert, aber nicht als finale Publisher-Freigabe zu verstehen. Vor A8 bleiben der finale Worktree-/Index-Check, eine bewusste Publisher-Sichtpruefung und die Entscheidung zum EN-Orchestrator-Restrisiko offen.

---

## 13. Teilzertifizierung A7 - Zertifizierungsprotokoll CIVITAS / v2.5

Diese Teilzertifizierung konkretisiert die A7-Anweisung: P.2-Compliance, Kapitel-6-Status, EN-Status, Restrisiken und Quality-Nachweise muessen im Zertifizierungsprotokoll sichtbar sein.

| Prüfpunkt | Ergebnis | Nachweis / Bemerkung |
|---|---|---|
| P.2 Paper-Compliance | erfüllt | DOI `10.5281/zenodo.19443256`, Version 1.0, Datum 2026-04-06, Lizenz CC BY 4.0, APA-Zitation und Originalsprache Englisch sind in DE/EN P.2 sichtbar. |
| Kapitel 6 Status | erfüllt mit Restrisiko | Kapitel 6 wird als CIVITAS-Roadmap und demokratische Architektur gefuehrt, nicht als fertig implementiertes System. |
| Deutsche P.2-Fassung | transparent | Deutsches Vorblatt, deutsche Einordnung und englischer Originaltext; keine stillschweigende Volluebersetzung. |
| EN-Status | transparent offen | EN-Content bleibt `status: draft`, sofern kein Native-gb-en-Finalreview dokumentiert ist. |
| Original-Heading 17.2 | erledigt | Repo-interne CIVITAS-Kopien sind normalisiert; keine Duplicate-Heading-Warnung im P.2-A5-Scope. |
| Quellen-/Linkpruefung | erfüllt im Prioritaetsscope | A5 P.2 plus manueller v2.5-Prioritaetsreview vom 2026-05-05. |
| Quality-Tool-Ergebnisse | dokumentiert | Link-Audit, Sources-Export, AI-Referenztool als nicht-autoritativer Hinweis und A4-Rechtsscanner sind im Protokoll verankert. |

**Entscheidung:** A7 ist als Zertifizierungsdokumentation fuer CIVITAS P.2, Kapitel 6 und die v2.5-Prioritaetsreferenzen erfuellt. Das Gesamtprotokoll bleibt Draft, weil A8, finale Publisher-Freigabe, vollstaendige EN-Freigabe und finale Release-Identitaet noch nicht geschlossen sind.
