# Zertifizierungsprotokoll v2.5.0 (Draft)

**Release:** v2.5.0  
**Release name:** Democratic Knowledge  
**Stand:** 2026-05-03  
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
| `gitbook_worker.tools.quality.link_audit` | offen | offen | offen | |
| `gitbook_worker.tools.quality.sources` | offen | offen | offen | |
| `gitbook_worker.tools.quality.ai_references` | offen | offen | offen | |
| `gitbook_worker.tools.quality.staatenprofil_links` | offen | offen | offen | |

Bewertung:

> Draft. Die Tools werden zunächst praktisch getestet. AI-gestützte Ergebnisse gelten nur als Hinweis und benötigen redaktionelle Prüfung.

---

## 5. Quellen- und Referenzaktualität

| Prüfung | Ergebnis | Nachweis | Bemerkung |
|---|---|---|---|
| Quellenabschnitte DE extrahiert | offen | | |
| Quellenabschnitte EN extrahiert | offen | | |
| Externe Links geprüft | offen | | |
| Lokale Bilder/Medien geprüft | offen | | |
| Risikobehaftete Zahlen/Aussagen geprüft | offen | | |
| Offene Quellenfragen dokumentiert | offen | | |

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
| DE Publish Markdown | offen | | |
| DE PDF | offen | | |
| EN Publish Markdown | offen | | |
| EN PDF | offen | | |
| PDF-Fonts: DejaVu | offen | | |
| PDF-Fonts: Twemoji Mozilla | offen | | |
| PDF-Fonts: ERDA CC-BY CJK | offen | | |
| Sichtprüfung DE PDF | offen | | |
| Sichtprüfung EN PDF | offen | | |

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
