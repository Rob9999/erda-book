# ERDA Backlog

**Zweck:** Arbeitsliste fuer offene Aufgaben, die nicht zwingend in v2.5 abgeschlossen werden muessen, aber fuer Release-Qualitaet, Quellenpflege und kommende Versionen sichtbar bleiben sollen.

## V2.5 - offen oder optional

| Prioritaet | Aufgabe | Naechster Schritt | Status |
|---|---|---|---|
| P1 | Quellen-Delta seit v2.0.0 abarbeiten | Pruefliste in `release-docs/v2.5.0/source-delta-since-v2.0.0-v2.5.0.md` verwenden | offen |
| P1 | Anhang P.1 Anti-Game-Over kurz pruefen | DOI, APA-Zitation, Lizenzlink und interne Querverweise technisch pruefen | offen |
| P1 | Kapitel 13.8 Energiesouveraenitaet pruefen | Aktuelle Programme, Zahlen, Zeitraeume und Roadmap-Aussagen quellenkritisch lesen | offen |
| P1 | Kapitel 6 CIVITAS Abschlusscheck | Quellenstaerke, interne P.2-Links und Review-/Governance-Wording redaktionell pruefen | offen |
| P1 | A6 Publish-Artefakte | DE/EN Publish Markdown und PDF bewusst neu erzeugen, erst nach Metadaten-Sync | offen |
| P1 | A7 Zertifizierungsprotokoll | `release-certification-v2.5.0.md` final durchgehen, keine stillen Freigaben setzen | offen |
| P1 | A8 Final Release Gate | Rollen-/Redaktionsfreigabe, README/book.json/CFF/Zenodo/Release Notes konsistent pruefen | offen |
| P2 | Gemini/AI-Referenzlauf DE | Nur im Dry-Run ueber `scripts/quality/ai_references_throttled.py`; priorisierte Dateiliste und Reports nach `tmp/gitbook-worker-ai-v2.5.0/` | vorbereitet |
| P2 | EN-Uebersetzungsreview | EN-Status, Source-Fidelity und britisches Englisch fuer neue v2.5-Inhalte pruefen | offen |
| P2 | CIVITAS P.2 deutsche Volluebersetzung | Optional klaeren, ob spaeter eine vollstaendige deutsche Uebersetzung statt deutscher Einordnung gewuenscht ist | offen |

## Spaeter / v2.6+

| Prioritaet | Aufgabe | Hinweis | Status |
|---|---|---|---|
| P1 | Gesamtbuch-Quellenaktualitaet | Vollstaendige Quelleninventare DE/EN aus `sources` risikobasiert pruefen; Staatenprofile priorisieren | offen |
| P1 | Staatenprofile Link-/Aktualitaetsaudit | Viele bestehende Quellenzeilen liegen in geaenderten Dateien, aber nicht zwingend als neue v2.5-Links | offen |
| P2 | AI-Referenzworkflow haerten | Provider, Datenschutz, Prompt-Verhalten, Rate Limits und Nicht-Dry-Run-Regeln dokumentieren | offen |
| P2 | Zugriffsdaten aktualisieren | Nach echter Quellenpruefung Zugriffsdaten bewusst aktualisieren, nicht automatisch | offen |
| P2 | Quellenreport als Release-Artefakt modellieren | Entscheiden, welche `tmp`-Reports dauerhaft in `release-docs/` zusammengefasst werden | offen |
| P3 | Desktop-Materialien kuratieren | Desktop-Papers und Misc-Dokumente nach Buchbezug, DOI-Status und Integrationsbedarf ordnen | offen |
| P3 | Terminologie- und Glossar-Sweep | Neue Begriffe aus v2.5/v2.6 konsistent in DE/EN Glossar und Summary sichtbar machen | offen |

## Arbeitsregeln

- Keine finale Freigabe oder `approved`-Status ohne zuständige Rolle nach `worker-roles.md`.
- `tmp/`-Reports sind Rohdaten; dauerhafte Entscheidungen gehoeren nach `release-docs/`.
- API-Keys nie committen und nicht in Chat-/Report-Ausgaben aufnehmen.
- AI-Ergebnisse sind Hinweise, keine Quellenwahrheit; redaktionelle Entscheidung bleibt erforderlich.
