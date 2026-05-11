# Final-Release-Checkliste v2.5.0

**Release:** v2.5.0  
**Release name:** Democratic Knowledge  
**Stand:** 2026-05-11
**Status:** Final-Gate-Stand nach gitbook_worker 2.9.1 dokumentiert; Tag-/Publisher-Freigabe noch offen
**Arbeitsrolle:** Redakteur:in, mit Zuarbeit Writer, Editor, Lektor, Native gb-en Translator und Publisher

---

## Zweck

Diese Checkliste beschreibt die verbindlichen Gates für die finale Freigabe von v2.5.0. Sie ersetzt keine redaktionelle Entscheidung; sie macht sichtbar, welche Prüfungen vor Tag, Release und Veröffentlichung abgeschlossen oder bewusst als Restrisiko dokumentiert sein müssen.

Ein Final-Release darf erst gesetzt werden, wenn alle Muss-Gates geschlossen sind oder der/die Redakteur:in eine begründete Ausnahme im Zertifizierungsprotokoll dokumentiert.

---

## Gate 0: Release-Identität

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| Finales Releasedatum festgelegt | ja | erledigt | 2026-05-05 in README, book.json, CFF, Release Docs |
| Version final auf `v2.5.0` gesetzt, nicht `v2.5.0-rc1` | ja | erledigt | README, CFF, `.zenodo.json`, Release Notes, publish.yml |
| Release name final festgelegt | ja | erledigt | `Democratic Knowledge` |
| Channel-/Branch-Aussage final konsistent | ja | erledigt mit Hinweis | README: finale v2.5.0-Vorbereitung auf `release_candidate`; stabiler Kanal nach Merge/Tag: `main` |
| `release_candidate` vor Merge/Tag sauber und synchron | ja | erledigt mit Hinweis | 2026-05-05: sauberer Arbeitsbaum vor Edits, Branch `release_candidate` ahead 13 |

---

## Gate 1: Metadaten und technische Konsistenz

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| README-`As of`, `de/book.json` und `en/book.json` konsistent | ja | erledigt im RC-Arbeitsstand | 2026-05-05 in Root-README, `de/book.json`, `en/book.json` |
| `de/CITATION.cff`, `en/CITATION.cff`, Root-`CITATION.cff` konsistent | ja | erledigt | Version 2.5.0, `date-released: 2026-05-05` |
| `.zenodo.json` final, nicht mehr Release Candidate | ja | erledigt | Version 2.5.0, stabile Releasebeschreibung |
| Release Notes und Release History widerspruchsfrei | ja | erledigt | `release-docs/v2.5.0/`, `release-docs/Releases.md` |
| Content-Frontmatter nutzt `content_lang`, keine Content-Keys `lang`, `language`, `lang-version` | ja | erledigt | `Select-String '^(lang|language|lang-version):'` ohne Treffer |
| Restliches Rollen-/Tooling-Wording auf `content_lang` geprüft | ja | erledigt | Versionierungscheckliste und Release-Dokumentation aktualisiert |
| `git diff --check` ohne Whitespace-Fehler | ja | erledigt | 2026-05-05: keine Ausgabe / keine Whitespace-Fehler |

---

## Gate 2: Referenz- und Quellenprüfung

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| `gitbook_worker.tools.quality.link_audit` getestet | ja | erledigt | P.2-Scope und v2.5-Finalscope; siehe `source-link-check-civitas-v2.5.0.md`, `source-review-final-gate-2026-05-05.md` |
| `gitbook_worker.tools.quality.sources` getestet | ja | erledigt | P.2-Scope und v2.5-Finalscope |
| `gitbook_worker.tools.quality.ai_references` mindestens im `--dry-run` geprüft | bedingt | erledigt | Finalscope-Dry-run: 35 validiert, 0 failed, 0 rate-limited |
| Externe Links und lokale Medien geprüft | ja | erledigt im Finalscope | Link-Audit: 0 broken, 2 good DOI-links, 0 image issues |
| Quellenabschnitte extrahiert und redaktionell stichproben-/risikobasiert geprüft | ja | erledigt im Finalscope | Sources-Export + manuelle Webprüfung |
| Heikle Zahlen, Zeitangaben und geopolitische Aussagen gegen offizielle/verlässliche Quellen geprüft | ja | erledigt im Finalscope | EU-Solar, Social Climate Fund, Eurostat, Gas Storage und Zenodo-DOIs manuell bestätigt |
| AI-Vorschläge nur nach menschlicher Prüfung übernommen | ja | erledigt im Prioritaetsscope | `source-review-v2.5-priority-references-2026-05-05.md` |

---

## Gate 3: Inhaltliche Prüfung DE

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| DE als Quelle der Wahrheit final gelesen | ja | erfüllt mit Restrisiko | `redaktioneller-durchgang-de-v2.5.0.md`, Finalscope-Prüfung 2026-05-05 |
| Neue v2.5-Inhalte in Kapitelstruktur und SUMMARY konsistent | ja | erledigt | DE SUMMARY enthält 13.8, Anhang M, Anhang P.1/P.2 |
| Querverweise auf Anhang M, Anhang P.1, Anhang P.2 und v2.5-Begriffe geprüft | ja | erledigt im Finalscope | SUMMARY, Kapitel 6, P-Anhang und Release Notes |
| Mini-Wording-Set und Glossar konsistent | ja | erfüllt mit Restrisiko | Keine neue Blockade; Feinschliff bleibt v2.6-/Backlog-Thema |
| Ethik-vor-Strategie-Pass auf unbeabsichtigte Schärfen geprüft | ja | erfüllt mit Restrisiko | Direkte strategische Sprache bleibt bewusst; Rechts-/Konformitätsclaims für CIVITAS separat A4-geprüft |
| Keine offenen Arbeitsmarker in Release-relevanten Inhalten | ja | erledigt | DE `TODO/FIXME/TBD`-Treffer waren spanisches Wort `Todo`, keine Arbeitsmarker; Link-Audit Finalscope: 0 TODOs |

---

## Gate 4: EN-Übersetzungsprüfung

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| Rolle `Native gb-en Translator` für Review-Arbeit dokumentiert | ja | erledigt als Restrisiko | Keine native finale Vollfreigabe dokumentiert |
| EN-Dateien md-für-md gegen DE-Quelle geprüft | abhängig vom Releaseziel | nicht Releaseziel v2.5.0 | EN wird synchronisiert, aber als Draft/Review ausgeliefert |
| Britisches Englisch, Terminologie und Ton konsistent | abhängig vom Releaseziel | erfüllt im Stichprobenscope | Vollständiges Native-gb-en-Lektorat bleibt Folgeauftrag |
| Keine inhaltlichen Erfindungen oder Bedeutungsverschiebungen | ja | erfüllt im v2.5-Synchronisationsscope | Keine bekannte Bedeutungsverschiebung in P.1/P.2/Kapitel 6/13.8; Vollprüfung offen |
| EN-Statuslage transparent dokumentiert (`draft`, `in-review`, `approved`) | ja | erledigt | Statusauswertung 2026-05-05: 18 approved, 263 draft, 40 in-review |
| Falls EN nicht vollständig freigegeben ist: Release Notes benennen den Status klar | ja | erledigt | Release Notes DE/EN: EN synchron, Draft/Review; keine native finale Vollfreigabe |

---

## Gate 5: Build und Artefakte

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| DE-Publish-Lauf erfolgreich | ja | erledigt finaler RC-Artefaktstand | Orchestrator 2026-05-11 mit gitbook_worker 2.9.1 nach Kapitel-8-Anhangserweiterung (8.A–8.D) und §10.2.1: `converter=ok`, `publisher=ok`; PDF 880 Seiten, 4.410.294 Bytes |
| EN-Publish-Lauf erfolgreich | ja | erledigt finaler RC-Artefaktstand | Orchestrator 2026-05-11 mit gitbook_worker 2.9.1 nach Kapitel-8-Anhangserweiterung (8.A–8.D) und §10.2.1: `converter=ok`, `publisher=ok`; PDF 837 Seiten, 4.423.739 Bytes |
| PDF-Fonts geprüft: DejaVu, Twemoji Mozilla, ERDA CC-BY CJK | ja | erledigt im v2.5.0-Scope mit 2.9.1-Warnungen | DejaVu/Twemoji/ERDACCbyCJK-Regular eingebettet; Textlayer-Replacement-Signale sind seit 2.9.1 Warnung, kein harter Fontblocker ohne Sichtbefund |
| `editorial-quality` Release-Profil bestanden | ja | erledigt mit Warnungen | 2.9.1-Lauf nach Kapitel-8-Konsolidierung: DE `passed_with_warnings` 0/0/41/7, EN `passed_with_warnings` 0/0/43/7, Project `passed_with_warnings` 0/0/84/8 |
| Markdown/PDF-Layout-Scan durchgeführt | ja | ersetzt durch 2.9.1-Qualitaetsdossier plus historische Scans | `gitbook-worker-2.9.1-delivery-review-v2.5.0.md`; alte Layoutscans bleiben Referenz fuer Restbefunde |
| Generierte Markdown-Artefakte plausibel | ja | erledigt im Stichprobenscope | Kapitel 6, P.2, Kapitel 13.8, Titeldatum und 2.9.1-Rebuild geprueft |
| Lokale Sichtprüfung der PDFs abgeschlossen | ja | technisch stichprobengeprueft mit Warnungen | `editorial-quality`, `pdftotext`/`pypdf`-Stichproben, Sichtpruefung Seite 73; volle Publisher-Sichtpruefung bleibt Final-Gate |
| Build erzeugt keine stillschweigenden Metadatenänderungen | ja | erledigt im RC-Arbeitsstand | Datumsstand 2026-05-11 bewusst in README/book.json/CFF/Zenodo synchronisiert |

---

## Gate 6: Zertifizierung, Freeze und Tag

| Prüfschritt | Muss | Status | Nachweis / Datei |
|---|---:|---|---|
| Zertifizierungsprotokoll ausgefüllt | ja | erledigt fuer A4-A7 / Tag-Freigabe offen | `release-certification-v2.5.0.md` |
| Content-Freeze erklärt | ja | erledigt | `release-certification-v2.5.0.md` |
| Nur Release-Fixes nach Freeze zugelassen | ja | erledigt | `release-certification-v2.5.0.md` |
| Redakteur-Finalreview dokumentiert | ja | erledigt | `redaktioneller-durchgang-de-v2.5.0.md`, Zertifizierungsprotokoll |
| Publisher-Buildfreigabe dokumentiert | ja | offen | Zertifizierungsprotokoll |
| Finaler Tag `v2.5.0` erst nach geschlossenem Gate gesetzt | ja | offen | Git-Tag / Release |

---

## Final geklärte Punkte / verbleibende Freigabe

- v2.5.0 wird mit finalem Release name `Democratic Knowledge` geführt.
- DE ist die Quelle der Wahrheit; EN wird synchronisiert, aber ohne native finale Vollfreigabe als Draft/Review ausgeliefert.
- Für den v2.5-Finalscope gelten DOI/Zenodo, offizielle EU-/Eurostat-Quellen und primäre Rechts-/Programmquellen als maßgeblich.
- Das AI-Referenztool wurde als `--dry-run`/Precheck genutzt; keine AI-Aussage wird ohne manuelle Prüfung übernommen.
- Offen bleiben vor Tag/Release: Publisher-Sichtprüfung der 2.9.1-PDFs, finaler Worktree-Endcheck unmittelbar vor Commit/Tag, bewusste Einordnung der 84 Projektwarnungen und Tag-Freigabe.
