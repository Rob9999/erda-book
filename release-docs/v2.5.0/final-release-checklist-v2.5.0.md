# Final-Release-Checkliste v2.5.0 (Draft)

**Release:** v2.5.0  
**Release name:** Democratic Knowledge  
**Stand:** 2026-05-05
**Status:** Draft, noch nicht freigegeben  
**Arbeitsrolle:** Redakteur:in, mit Zuarbeit Writer, Editor, Lektor, Native gb-en Translator und Publisher

---

## Zweck

Diese Checkliste beschreibt die verbindlichen Gates für die finale Freigabe von v2.5.0. Sie ersetzt keine redaktionelle Entscheidung; sie macht sichtbar, welche Prüfungen vor Tag, Release und Veröffentlichung abgeschlossen oder bewusst als Restrisiko dokumentiert sein müssen.

Ein Final-Release darf erst gesetzt werden, wenn alle Muss-Gates geschlossen sind oder der/die Redakteur:in eine begründete Ausnahme im Zertifizierungsprotokoll dokumentiert.

---

## Gate 0: Release-Identität

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| Finales Releasedatum festgelegt | ja | offen | README, book.json, CFF, Release Docs |
| Version final auf `v2.5.0` gesetzt, nicht `v2.5.0-rc1` | ja | offen | README, CFF, `.zenodo.json`, Release Notes |
| Release name final festgelegt | ja | offen | `Democratic Knowledge` oder dokumentierte Änderung |
| Channel-/Branch-Aussage final konsistent | ja | offen | README, Release Docs |
| `release_candidate` vor Merge/Tag sauber und synchron | ja | offen | `git status --short --branch` |

---

## Gate 1: Metadaten und technische Konsistenz

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| README-`As of`, `de/book.json` und `en/book.json` konsistent | ja | erledigt im RC-Arbeitsstand | 2026-05-05 in Root-README, `de/book.json`, `en/book.json` |
| `de/CITATION.cff`, `en/CITATION.cff`, Root-`CITATION.cff` konsistent | ja | offen | CFF-Dateien |
| `.zenodo.json` final, nicht mehr Release Candidate | ja | offen | `.zenodo.json` |
| Release Notes und Release History widerspruchsfrei | ja | offen | `release-docs/` |
| Content-Frontmatter nutzt `content_lang`, keine Content-Keys `lang`, `language`, `lang-version` | ja | offen | Content-Gate / Script-Ausgabe |
| Restliches Rollen-/Tooling-Wording auf `content_lang` geprüft | ja | offen | insbesondere `worker-roles.md` |
| `git diff --check` ohne Whitespace-Fehler | ja | offen | Terminalausgabe |

---

## Gate 2: Referenz- und Quellenprüfung

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| `gitbook_worker.tools.quality.link_audit` getestet | ja | erledigt im P.2-Scope | `source-link-check-civitas-v2.5.0.md` |
| `gitbook_worker.tools.quality.sources` getestet | ja | erledigt im P.2-Scope | `source-link-check-civitas-v2.5.0.md` |
| `gitbook_worker.tools.quality.ai_references` mindestens im `--dry-run` geprüft | bedingt | dokumentiert mit Restrisiko | AI-Berichte nur Suchhilfe; manuelle Pruefung massgeblich |
| Externe Links und lokale Medien geprüft | ja | offen | Link-Audit-Report |
| Quellenabschnitte extrahiert und redaktionell stichproben-/risikobasiert geprüft | ja | offen | Sources-Report |
| Heikle Zahlen, Zeitangaben und geopolitische Aussagen gegen offizielle/verlässliche Quellen geprüft | ja | offen | Redaktionsnotiz |
| AI-Vorschläge nur nach menschlicher Prüfung übernommen | ja | erledigt im Prioritaetsscope | `source-review-v2.5-priority-references-2026-05-05.md` |

---

## Gate 3: Inhaltliche Prüfung DE

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| DE als Quelle der Wahrheit final gelesen | ja | offen | Review-Protokoll |
| Neue v2.5-Inhalte in Kapitelstruktur und SUMMARY konsistent | ja | offen | DE SUMMARY / Content |
| Querverweise auf Anhang M, Anhang P.1, Anhang P.2 und v2.5-Begriffe geprüft | ja | offen | Review-Protokoll |
| Mini-Wording-Set und Glossar konsistent | ja | offen | Anhang I / Anhang K |
| Ethik-vor-Strategie-Pass auf unbeabsichtigte Schärfen geprüft | ja | offen | Redakteur-Notiz |
| Keine offenen Arbeitsmarker in Release-relevanten Inhalten | ja | offen | Link-Audit / manuelle Suche |

---

## Gate 4: EN-Übersetzungsprüfung

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| Rolle `Native gb-en Translator` für Review-Arbeit dokumentiert | ja | offen | Zertifizierungsprotokoll |
| EN-Dateien md-für-md gegen DE-Quelle geprüft | abhängig vom Releaseziel | offen | Translation-Review-Report |
| Britisches Englisch, Terminologie und Ton konsistent | abhängig vom Releaseziel | offen | Review-Notizen |
| Keine inhaltlichen Erfindungen oder Bedeutungsverschiebungen | ja | offen | Review-Notizen |
| EN-Statuslage transparent dokumentiert (`draft`, `in-review`, `approved`) | ja | offen | Statusauswertung |
| Falls EN nicht vollständig freigegeben ist: Release Notes benennen den Status klar | ja | offen | Release Notes / Zertifizierung |

---

## Gate 5: Build und Artefakte

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| DE-Publish-Lauf erfolgreich | ja | erledigt im RC-Arbeitsstand | Orchestrator 2026-05-05: `converter=ok`, `publisher=ok` |
| EN-Publish-Lauf erfolgreich | ja | erledigt mit gitbook_worker 2.4.0 | `.venv`-Lauf 2026-05-05: `converter=ok`, `publisher=ok`; Titelseite zeigt Datum und Version |
| PDF-Fonts geprüft: DejaVu, Twemoji Mozilla, ERDA CC-BY CJK | ja | erledigt im v2.5.0-Scope | DejaVu/Twemoji/ERDACCbyCJK-Regular eingebettet; ERDA CC-BY CJK deckt die multilingualen Lizenzbeschreibungen ab, weitere Glyphen bei Bedarf ueber gitbook_worker-Lieferant |
| Generierte Markdown-Artefakte plausibel | ja | erledigt im Stichprobenscope | Kapitel 6, P.2, Kapitel 13.8, Titeldatum geprueft |
| Lokale Sichtprüfung der PDFs abgeschlossen | ja | technisch stichprobengeprueft | `pdfinfo`, `pdftotext`, `pdffonts`, gerenderte EN-Titelseite; volle Publisher-Sichtpruefung offen |
| Build erzeugt keine stillschweigenden Metadatenänderungen | ja | erledigt im RC-Arbeitsstand | Datumswechsel auf 2026-05-05 bewusst in README/book.json nachgezogen |

---

## Gate 6: Zertifizierung, Freeze und Tag

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| Zertifizierungsprotokoll ausgefüllt | ja | erledigt fuer A4-A7 / Draft bleibt offen | `release-certification-v2.5.0.md` |
| Content-Freeze erklärt | ja | offen | Statusdatei / Zertifizierung |
| Nur Release-Fixes nach Freeze zugelassen | ja | offen | Git-Historie / Notiz |
| Redakteur-Finalreview dokumentiert | ja | offen | Zertifizierungsprotokoll |
| Publisher-Buildfreigabe dokumentiert | ja | offen | Zertifizierungsprotokoll |
| Finaler Tag `v2.5.0` erst nach geschlossenem Gate gesetzt | ja | offen | Git-Tag / Release |

---

## Offene Klärungen vor Final

- Soll v2.5.0 zweisprachig vollständig freigegeben werden, oder wird DE final und EN mit transparentem Review-/Draft-Status ausgeliefert?
- Wird `Democratic Knowledge` finaler Release name oder bleibt es als Codename des Release Candidate dokumentiert?
- Welche Quellen gelten für die Aktualitätsprüfung als primär verbindlich, insbesondere bei EU-, NATO-, Ukraine- und Sicherheitszahlen?
- Wird das AI-Referenztool aktiv mit API-Zugang genutzt oder nur als optionaler, dokumentierter Dry-Run bewertet?
