# Zertifizierungsprotokoll v2.5.0

**Release:** v2.5.0  
**Release name:** Democratic Knowledge  
**Stand:** 2026-05-12
**Status:** Final-Gate-Stand nach gitbook_worker 2.9.2 dokumentiert; Tag-/Publisher-Freigabe noch offen
**Zuständige Rolle:** Redakteur:in  
**Mitwirkende Rollen:** Writer, Editor, Lektor, Native gb-en Translator, Publisher

---

## 1. Zertifizierungsentscheidung

| Feld | Eintrag |
|---|---|
| Entscheidung | Release-Identität, DE-Quellstand und v2.5-Finalscope-Quellenprüfung vorbereitet; keine Tag-Freigabe ohne Publisher-Endcheck |
| Entscheidung am | 2026-05-12 |
| Entscheidung durch Rolle | Redakteur:in |
| Freigabeumfang | DE als Quelle der Wahrheit; EN synchronisiert mit Draft/Review-Transparenz; v2.5-Finalscope Quellen/Links |
| Restrisiken akzeptiert | EN ohne native finale Vollfreigabe; Staatenprofil-Gesamtaktualität v2.6/backlog; Publisher-Sichtprüfung offen |
| Tag-Freigabe `v2.5.0` | offen |

Kurzbegründung:

> v2.5.0 ist metadaten-, quellen- und buildbezogen auf den finalen Release vorbereitet. Eine finale Veröffentlichung/Tag-Freigabe wird erst nach Abschluss von Worktree-Endcheck unmittelbar vor Commit/Tag und Publisher-Sichtprüfung ausgesprochen.

---

## 2. Release-Identität und Metadaten

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Version final `v2.5.0` | erledigt | README, CFF, publish.yml, `.zenodo.json`, Release Notes | `v2.5.0-rc1` entfernt aus primärer Release-Identität. |
| Releasedatum konsistent | erledigt | README, `de/book.json`, `en/book.json`, CFF, `.zenodo.json`, Release Docs | 2026-05-12. |
| README, book.json, CFF, Zenodo synchron | erledigt | Root-/DE-/EN-CFF, `.zenodo.json` | Zenodo-Beschreibung final ohne Release-Candidate-Status. |
| Release Notes final | erledigt | DE/EN Release Notes | EN-Status transparent als Draft/Review. |
| Release History final | erledigt | `release-docs/Releases.md` | v2.5.0-Eintrag auf 2026-05-12 aktualisiert. |
| Channel-/Branch-Aussage konsistent | erledigt mit Hinweis | README, v2.5 Release Docs | Vorbereitung auf `release_candidate`; stabiler Kanal nach Merge/Tag: `main`. |

---

## 3. Technische Gates

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Git-Status sauber und synchron | offen bis Endcheck | `git status --short --branch` | Vor Edits sauber, Branch `release_candidate` ahead 13. Nach Abschluss erneut prüfen. |
| `git diff --check` sauber | erledigt | Terminalausgabe 2026-05-12 | Keine Ausgabe / keine Whitespace-Fehler. |
| Frontmatter-Gate DE/EN bestanden | erledigt | `Select-String '^(lang|language|lang-version):'` | Keine verbotenen Content-Sprachkeys gefunden. |
| Keine Content-Keys `lang`, `language`, `lang-version` | erledigt | Terminalausgabe | `content_lang` bleibt zulässiger Schlüssel. |
| Rollen-/Tooling-Dokumentation auf `content_lang` geprüft | erledigt | Release-Versionierungscheckliste, Gate-Dokumente | Keine neue Babel/Pandoc-Sprachmetadatengefahr im Content dokumentiert. |

---

## 4. Quality-Tools des gitbook_worker

| Tool | Testmodus | Ergebnis | Brauchbarkeit | Nachweis |
|---|---|---|---|---|
| `gitbook_worker.tools.quality.link_audit` | CIVITAS P.2 DE/EN + v2.5-Finalscope | bestanden | geeignet als technischer Gate-Hinweis, mit manueller Gegenpruefung | `source-link-check-civitas-v2.5.0.md`, `source-review-final-gate-2026-05-05.md` |
| `gitbook_worker.tools.quality.sources` | DE/EN Quellenexport + v2.5-Finalscope | bestanden | geeignet zur Quelleninventur, nicht als inhaltliche Wahrheit | `source-link-check-civitas-v2.5.0.md`, `source-review-final-gate-2026-05-05.md` |
| `gitbook_worker.tools.quality.ai_references` | `--dry-run --precheck-only` v2.5-Finalscope | 35 validiert, 0 failed, 0 rate-limited | nicht autoritativ; AI bleibt Suchhilfe, Precheck und manuelle Quellenpruefung massgeblich | `source-review-final-gate-2026-05-05.md` |
| `gitbook_worker.tools.quality.staatenprofil_links` | nicht final im v2.5-A6/A7-Scope | offen | Backlog fuer vollstaendige Staatenprofil-Aktualitaet | `source-delta-since-v2.0.0-v2.5.0.md` |
| `gitbook_worker.tools.quality.editorial_metrics` / `editorial_acceptance` | 2.9.2 `release`-Profil fuer DE, EN und Project | `passed_with_warnings`, 0 blocked, 0 fail | geeignet als finales technisches Quality-Dossier; Warnungen brauchen redaktionelle Entscheidung, ersetzen keine Freigabe | `gitbook-worker-2.9.2-delivery-review-v2.5.0.md` |

Bewertung: Die fuer CIVITAS, die v2.5-Prioritaetsreferenzen und den Finalscope eingesetzten Tools sind als technische Hilfen dokumentiert. AI-gestuetzte Ergebnisse wurden nicht als Quellenwahrheit uebernommen; entscheidend war die manuelle Pruefung gegen DOI, Originalseiten, offizielle EU-/Eurostat-Quellen und bibliografische Plausibilitaet. Der Qualitaetskompass-Lauf mit gitbook_worker 2.9.2 fuehrt den frueheren 2.9.0-Blocker `pdf.text.replacement_glyph` weiterhin als `pdf.text.extraction_replacement`-Warnung.

---

## 5. Quellen- und Referenzaktualität

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Quellenabschnitte DE extrahiert | erledigt im P.2- und Finalscope | `source-link-check-civitas-v2.5.0.md`, `source-review-final-gate-2026-05-05.md` | Gesamtbuch bleibt v2.6-/Backlog-Thema. |
| Quellenabschnitte EN extrahiert | erledigt im P.2-Scope | `source-link-check-civitas-v2.5.0.md` | EN bleibt Draft/Review; keine native Vollfreigabe. |
| Externe Links geprüft | erledigt fuer P.2, Prioritaetsreferenzen und Finalscope | `source-review-v2.5-priority-references-2026-05-05.md`, `source-review-final-gate-2026-05-05.md` | Keine bekannte 404-Referenz im geaenderten Scope. |
| Buch-interne Markdown-Referenzen geprüft | erledigt | Lokaler Markdown-Linkcheck 2026-05-12 | DE/EN Content: 560 lokale Markdown-Links geprueft, 9 Template-Platzhalter bewusst ignoriert, 0 fehlende Ziele. |
| Lokale Bilder/Medien geprüft | erledigt im Finalscope | `source-review-final-gate-2026-05-05.md` | Link-Audit: 0 image issues im geprueften Scope. |
| Risikobehaftete Zahlen/Aussagen geprüft | erledigt im Finalscope | `source-review-final-gate-2026-05-05.md` | EU-Solar, Social Climate Fund, Eurostat, Gas Storage und Zenodo-DOIs manuell bestaetigt. |
| Offene Quellenfragen dokumentiert | erledigt fuer v2.5-Finalscope | `source-delta-since-v2.0.0-v2.5.0.md`, `source-review-final-gate-2026-05-05.md` | Vollstaendige Staatenprofil-Aktualitaet bleibt v2.6/backlog. |

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
| DE-Haupttext final geprüft | erfüllt mit Restrisiko | `redaktioneller-durchgang-de-v2.5.0.md`, Finalscope-Pruefung 2026-05-05 | DE ist Quelle der Wahrheit; historische/umfangreiche Backlog-Themen bleiben dokumentiert. |
| Neue v2.5-Inhalte integriert und plausibel | erledigt | SUMMARY, Kapitel 6, Kapitel 13.8, Anhang M, Anhang P.1/P.2 | Struktur in DE SUMMARY sichtbar. |
| Querverweise und SUMMARY geprüft | erledigt | `de/content/SUMMARY.md` | 13.8, Anhang M, Anhang P.1/P.2 vorhanden. |
| Glossar und Mini-Wording-Set konsistent | erfüllt mit Restrisiko | Anhang I/K, Release-Dokumentation | Kein Releaseblocker; Feinschliff bleibt Folgeauftrag. |
| Ethik-vor-Strategie-Pass redaktionell abgenommen | erfüllt mit Restrisiko | Zertifizierung A4/A7, Release Notes | Direkte strategische Sprache bleibt bewusst, Rechtsclaims bleiben Anforderungs-/Zielrahmen. |
| Keine offenen Arbeitsmarker in Release-Inhalten | erledigt | DE `TODO/FIXME/TBD`-Suche, Link-Audit | `Todo`-Treffer sind spanisches Wort, keine Arbeitsmarker. |

---

## 7. EN-Übersetzungsprüfung

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Rolle `Native gb-en Translator` angewendet | nicht vollständig | Statusentscheidung 2026-05-05 | Keine native finale Vollfreigabe dokumentiert. |
| EN-Statusauswertung erstellt | erledigt | Terminalauswertung | 18 approved, 263 draft, 40 in-review. |
| EN-Dateien gegen DE-Quelle geprüft | nicht Releaseziel v2.5.0 | Release Notes, Final-Checkliste | EN bleibt synchronisierter Draft/Review-Stand. |
| Britisches Englisch und Terminologie geprüft | stichprobengeprueft | v2.5-Scope | Vollständiges Native-gb-en-Lektorat bleibt Folgeauftrag. |
| Bedeutungs- und Quellenfidelity geprüft | erfüllt im v2.5-Synchronisationsscope | P.1/P.2, Kapitel 6/13.8, Release Notes | Keine bekannte Bedeutungsverschiebung im geprueften Scope. |
| Nicht freigegebene EN-Dateien transparent benannt | erledigt | EN-Statusauswertung, Release Notes | EN wird nicht als final native-approved dargestellt. |

Freigabeaussage EN:

> EN wird in v2.5.0 als synchronisierte Draft-/Review-Fassung ausgeliefert. Die deutsche Fassung bleibt Quelle der Wahrheit. Eine native finale britisch-englische Vollfreigabe ist nicht Bestandteil der v2.5.0-Tag-Freigabe und bleibt Folgeauftrag.

---

## 8. Build- und Artefaktprüfung

| Artefakt / Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| DE Publish Markdown | erzeugt | `de/publish/das-erda-buch.md` | Finaler RC-Artefaktstand 2026-05-12 mit gitbook_worker 2.9.2, Orchestrator: `converter=ok`, `publisher=ok`. |
| DE PDF | erzeugt | `de/publish/das-erda-buch.pdf` | 858 Seiten, 4.403.173 Bytes, CreationDate 2026-05-12 13:05 MESZ. |
| EN Publish Markdown | erzeugt | `en/publish/the-erda-book.md` | Finaler RC-Artefaktstand 2026-05-12 mit gitbook_worker 2.9.2, Orchestrator: `converter=ok`, `publisher=ok`. |
| EN PDF | erzeugt | `en/publish/the-erda-book.pdf` | 826 Seiten, 4.421.247 Bytes, CreationDate 2026-05-12 12:54 MESZ. |
| PDF-Fonts: DejaVu | bestanden | `pdffonts` DE/EN, Qualitaetsdossier | DejaVuSerif, DejaVuSansMono und Varianten eingebettet. |
| PDF-Fonts: Twemoji Mozilla | bestanden mit Textlayer-Warnung | `pdffonts` DE/EN, `editorial-quality` | TwemojiMozilla eingebettet; `pypdf`-Textlayer-Replacements bleiben als Warnung sichtbar, ohne Sichtbefund kein harter Font-/Glyphenfehler. |
| PDF-Fonts: ERDA CC-BY CJK | bestanden im Release-Scope | `pdffonts` / Publisher-Einschaetzung | CJK-Fonts decken den v2.5.0-Scope ab; echte Missing-character-Logsignale bleiben bei Bedarf separat zu pruefen. |
| `editorial-quality` Release-Profil | bestanden mit Warnungen | `logs/quality/*-release-editorial-acceptance.*`, dokumentiert in `gitbook-worker-2.9.2-delivery-review-v2.5.0.md` | DE 0 blocked/0 fail/35 warn/7 info; EN 0/0/40/7; Project 0/0/75/8. |
| Sichtprüfung DE PDF | technisch stichprobengeprueft | Seite 73, `pypdf`-/Textlayer-Abgleich, Quality-Dossier | Symbole sichtbar intakt; Textlayer-Replacements als Accessibility-/Copy-Paste-Warnung eingeordnet. Vollstaendige Publisher-Sichtpruefung bleibt Final-Gate. |
| Sichtprüfung EN PDF | technisch stichprobengeprueft | Quality-Dossier, PDF-Metadaten | Keine harten Quality-Fails; vollstaendige Publisher-Sichtpruefung bleibt Final-Gate. |

---

## 9. Freeze-Protokoll

| Feld | Eintrag |
|---|---|
| Content-Freeze erklärt am | 2026-05-05 |
| Freeze erklärt durch Rolle | Redakteur:in |
| Erlaubte Änderungen nach Freeze | nur Release-Fixes, Build-Fixes, Metadatenkorrekturen |
| Änderungen nach Freeze dokumentiert | ja, in diesem Protokoll und den v2.5.0-Release-Dokumenten; zuletzt Kapitel 10 §10.2.1 synchronisiert, HTML-Tabellen in Markdown zurückgeführt, ERDA-Buch-/Buchprojekt-Wording harmonisiert und Buch-interne Referenzen geprüft |
| Freeze aufgehoben? | nein |

---

## 10. Final Review und Publisher-Freigabe

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Redakteur-Finalreview abgeschlossen | erledigt | `redaktioneller-durchgang-de-v2.5.0.md`, dieses Protokoll | DE ist Quelle der Wahrheit; Restrisiken dokumentiert. |
| Publisher-Buildfreigabe abgeschlossen | offen | `gitbook-worker-2.9.2-delivery-review-v2.5.0.md`, Sichtprüfung | 2.9.2-Quality-Gate ohne Fails; Warnungen vor Tag-Freigabe priorisieren oder als Restrisiko dokumentieren. |
| Finaler Worktree geprüft | offen | | |
| Tag `v2.5.0` vorbereitet | offen | | |
| GitHub-/Zenodo-Releasebeschreibung final | vorbereitet | `.zenodo.json`, Release Notes | GitHub-Release selbst noch nicht angelegt/veroeffentlicht. |

Finale Aussage:

> Final-Gate-Stand: redaktionell vorbereitet und technisch mit gitbook_worker 2.9.2 ohne harte Quality-Fails reproduziert, aber keine Tag-/Publisher-Freigabe, solange Publisher-Sichtpruefung, Warnungs-/Restrisikoentscheidung, finaler Worktree/Index-Check und bewusste Tag-Entscheidung offen sind.

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

**Entscheidung:** Für v2.5.0 ist A4 als Release-Check erfüllt mit Restrisiko. CIVITAS wird nicht als rechtlich geprüfte Plattform dargestellt. Vor Finalfreigabe bleiben Publisher-Sichtprüfung, finaler Worktree/Index-Check und bewusste Tag-Freigabe offen. Diese Aussage ist keine Rechtsberatung.

---

## 12. Teilzertifizierung A6 - Build- und Artefaktprüfung

Diese Teilzertifizierung dokumentiert den Arbeitsstand zu A6 aus der Anhang-M-Beurteilung: Publish-Artefakte nach sauberem Inhaltscommit neu erzeugen, technisch pruefen und Diff-/Tooling-Risiken benennen.

| Feld | Eintrag |
|---|---|
| Prüfdatum | 2026-05-12 |
| Prüfrolle | Publisher mit Redakteur:in-Zuarbeit |
| DE Build | `converter=ok`, `publisher=ok`, `editorial-quality=passed_with_warnings` |
| EN Build | `converter=ok`, `publisher=ok`, `editorial-quality=passed_with_warnings` |
| DE PDF | 858 Seiten, 4.403.173 Bytes, CreationDate 2026-05-12 13:05 MESZ |
| EN PDF | 826 Seiten, 4.421.247 Bytes, CreationDate 2026-05-12 12:54 MESZ |
| Fontbefund | DejaVu, TwemojiMozilla und ERDACCbyCJK-Regular in DE/EN eingebettet; Textlayer-Replacements als Warnung, nicht als harter Fontfail |
| Ergebnis | erfuellt mit dokumentierten Warnungen; vendortes gitbook_worker 2.9.2 installiert, DE/EN-Artefakte neu erzeugt und Qualitaetsdossier reproduziert |

**Befund:** Die Publish-Artefakte wurden nach Integration des gitbook_worker-2.9.2-Pakets, nach der redaktionellen Kapitel-8-Konsolidierung und nach der §10.2.1-Synchronisierung neu erzeugt. DE- und EN-Orchestrator liefen erfolgreich durch. Der integrierte `editorial-quality`-Lauf im `release`-Profil erzeugte fuer DE, EN und Project jeweils `passed_with_warnings` mit 0 `blocked` und 0 `fail`. Die frueheren `pdf.text.replacement_glyph`-Fails aus 2.9.0 bleiben als `pdf.text.extraction_replacement`-Warnungen mit Seitenhinweisen klassifiziert. Das entspricht der visuellen Stichprobe: Die Symbole sind in der PDF sichtbar intakt, waehrend `pypdf` im Textlayer Replacement-Zeichen extrahiert. Der lokale Windows-Lauf benoetigte weiterhin einen repo-lokalen `LOCALAPPDATA`-Buildkontext, damit Font-Caches und Altstubs nicht in den PDF-Build eingreifen.

**Entscheidung:** Das fruehere harte Glyphen-/Font-Gate aus 2.9.0 wird fuer v2.5.0 durch gitbook_worker 2.9.2 weiterhin als geschlossen bewertet. A6 ist fuer den aktuellen v2.5.0-Artefaktstand technisch erfuellt, aber nicht als finale Publisher-Freigabe zu verstehen. Vor A8 bleiben der finale Worktree-/Index-Check, die bewusste Publisher-Sichtpruefung, die Einordnung der 75 Projektwarnungen und die Tag-Entscheidung offen. Fuer spaetere Releases bleibt der Hinweis bestehen, PDF-Laeufe nicht parallel gegen dieselben Ausgabepfade zu starten.

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

**Entscheidung:** A7 ist als Zertifizierungsdokumentation fuer CIVITAS P.2, Kapitel 6 und die v2.5-Prioritaetsreferenzen erfuellt. Das Gesamtprotokoll bleibt ohne Tag-Freigabe, weil A8, finale Publisher-Freigabe und vollstaendige EN-Freigabe noch nicht geschlossen sind.

---

## 14. Teilzertifizierung A7b - ERDA-Buch-Namenspass und interne Referenzen

Diese Teilzertifizierung dokumentiert den redaktionellen Namens- und Referenzpass fuer v2.5.0: Das Buch selbst wird als ERDA-Buch bzw. The ERDA Book gefuehrt, waehrend Prozess-/Werkstattbezug als ERDA-Buchprojekt bzw. ERDA Book project gefuehrt wird.

| Feld | Eintrag |
|---|---|
| Prüfdatum | 2026-05-12 |
| Prüfrolle | Redakteur:in |
| Scope | DE/EN Content, insbesondere Quellenlisten, Kapitel 14, Anhang E, Lizenz/Kolophon und Staatenprofil-Metadaten |
| Versions-/Jahresstand | Buchinterne Quellenlabels auf ERDA-Buch / The ERDA Book (2026); Modulbezug 12.A auf v2.5.0 aktualisiert |
| Interne Referenzprüfung | 560 lokale Markdown-Links geprüft; 9 explizite Template-Platzhalter ignoriert; 0 fehlende Ziele |
| Ergebnis | erfüllt |

**Befund:** Veraltete Labels wie `ERDA-Projekt (2025/2026)`, `ERDA Buch (2025)`, `ERDA-Anbindung` und `ERDA Buch Redaktion` wurden im Content-Scope auf die v2.5.0-Hausform gebracht. Ein fehlerhafter Buch-internen Pfad zu Anhang B.2 wurde korrigiert. Die anschliessende lokale Markdown-Linkpruefung meldete keine fehlenden Ziele im DE/EN-Content.
