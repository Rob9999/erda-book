# Quellen-Delta seit v2.0.0 - Pruefliste v2.5.0

**Datum:** 2026-05-05
**Baseline:** `v2.0.0`  
**Vergleich:** `v2.0.0..35e0c8b`  
**Status:** Arbeits- und Pruefliste; Finalscope-Gate separat abgeschlossen in `source-review-final-gate-2026-05-05.md`

## Kurzbefund

Der reine Dateidiff seit `v2.0.0` ist zu breit fuer eine sinnvolle manuelle Quellenpruefung, weil viele Dateien durch Frontmatter-, Synchronisations- und Release-Arbeiten beruehrt wurden. Die tatsaechliche v2.5-Pruefliste sollte deshalb aus neuen Inhalten, neuen URL-/DOI-Zeilen und v2.5-Schwerpunktbereichen gebildet werden.

| Messpunkt | Ergebnis |
|---|---:|
| Content-Dateien im Diff | 644 |
| Neu angelegt | 12 |
| Geaendert | 630 |
| Umbenannt | 2 |
| Neu hinzugefuegte Link-/Quellenmarker-Zeilen | 82 |
| Davon echte neue URL-/DOI-Zeilen | 38 |
| Neu hinzugefuegte Ueberschriften | 307 |

Temporäre Rohdaten liegen unter `tmp/delta-added-links-since-v2.0.0.csv`, `tmp/delta-added-headings-since-v2.0.0.csv` und `tmp/delta-links-since-v2.0.0.csv`. Diese Dateien sind Arbeitsartefakte und sollen nicht als Release-Dokumentation committed werden.

## Neu angelegte Content-Dateien

| Bereich | DE | EN | Pruefhinweis |
|---|---|---|---|
| Reformpfad-Grafik | `de/content/.gitbook/assets/erda-reformpfad-2025-2035.svg` | `en/content/.gitbook/assets/erda-reform-path-2025-2035.svg` | Herkunft/Attribution pruefen; XML-Namespace ist kein Quellenlink. |
| Kapitel 13.8 Energiesouveraenitaet | `de/content/13.-strategische-souveranitat-werkzeugkoffer-fur-demokratische-sicherheit/13.8-energiesouveranitat-strategie-und-roadmap-2026-2029.md` | `en/content/13.-strategische-souveranitat-werkzeugkoffer-fur-demokratische-sicherheit/13.8-energiesouveranitat-strategie-und-roadmap-2026-2029.md` | Hohe Aktualitaetsrelevanz; Zahlen, Programme, Roadmap-Daten und politische Bezuege redaktionell pruefen. |
| Anhang M / Appendix M | `de/content/anhang-m-massstab-messbare-buchprojektentscheidungen-und-release-kriterien.md` | `en/content/appendix-m-measure-measurable-book-project-decisions-and-release-criteria.md` | Normativer Qualitaetsrahmen; Quellenbegriffe und Paper-Compliance-Logik pruefen. |
| Anhang P / Appendix P README | `de/content/anhang-p-papers/README.md` | `en/content/appendix-p-papers/README.md` | Navigation, DOI-/APA-Pflichten und interne Links pruefen. |
| Paper P.1 Anti-Game-Over | `de/content/anhang-p-papers/p.1-kindheit-erwachsenwerden-und-das-anti-game-over-prinzip.md` | `en/content/appendix-p-papers/p.1-childhood-adulthood-and-the-anti-game-over-principle.md` | DOI, APA-Zitation, Lizenzrahmen und Querverweise pruefen. |
| Paper P.2 CIVITAS Public | `de/content/anhang-p-papers/p.2-civitas-public-building-a-european-digital-agora.md` | `en/content/appendix-p-papers/p.2-civitas-public-building-a-european-digital-agora.md` | A5-Pruefung erledigt; siehe `source-link-check-civitas-v2.5.0.md`. |

Die zwei Umbenennungen betreffen die englischen Anhaenge J und L:

- `en/content/anhang-j-lizenz---offenheit.md` -> `en/content/appendix-j-license-and-openness.md`
- `en/content/anhang-l-kolophon.md` -> `en/content/appendix-l-colophon.md`

## V2.5-Schwerpunktbereiche

Diese Bereiche bilden die aktuelle redaktionelle Quellen- und Linkpruefliste fuer v2.5:

| Prioritaet | Bereich | Grund | Status |
|---|---|---|---|
| P1 | Anhang P.2 / Appendix P.2 CIVITAS Public | 30 neue URL-/DOI-Zeilen in DE+EN, 16 Referenzen, DOI, Plattform-/Rechtsquellen | A5 erledigt mit dokumentiertem Restrisiko. |
| P1 | Anhang P.1 / Appendix P.1 Anti-Game-Over | 6 neue URL-/DOI-Zeilen in DE+EN, DOI/APA/Lizenzrahmen | DOI/Zenodo/Lizenz geprueft; siehe `source-review-v2.5-priority-references-2026-05-05.md`. |
| P1 | Kapitel 13.8 Energiesouveraenitaet | komplett neue DE/EN-Datei, aktueller politischer und strategischer Gegenstand | Quellen ergaenzt und Zahlen korrigiert; siehe `source-review-v2.5-priority-references-2026-05-05.md`. |
| P1 | Kapitel 6 CIVITAS | inhaltlich stark vertieft; 7 neue Quellenmarker, aber keine neuen externen URL-Zeilen | A4 erledigt; inhaltliche Quellenstaerke und interne Referenzen pruefen. |
| P2 | Paragraph 11.3.7 Erziehungsleitbild | neuer Abschnitt aus Desktop-Material, Querverweise auf P.1 | Plausibilitaet, interne Links, EN-Fidelity pruefen. |
| P2 | Paragraph 5.8.4 Mosaik-Prinzip | neuer Abschnitt aus Desktop-Material | Begriffliche Quellenlage und strategische Einordnung pruefen. |
| P2 | Anhang M / Appendix M | neuer Qualitaetsmassstab | Konsistenz mit Zertifizierung und Release-Gates pruefen. |
| P2 | Anhang K/L/E und Attribution-/Quellenverzeichnis-Teile | neue oder erweiterte Quellen-/Attributionslogik | Strategic-Compass-Beispiellink und Twemoji-Version korrigiert; siehe `source-review-v2.5-priority-references-2026-05-05.md`. |
| P3 | Anhang B Staatenprofile | viele bestehende Quellenzeilen in geaenderten Dateien; nicht zwingend neue v2.5-Links | Vollstaendige Aktualitaetspruefung fuer v2.6/backlog vormerken, ausser es gab inhaltliche Einzelupdates. |

## Link-Delta

Die 38 echten neuen URL-/DOI-Zeilen verteilen sich so:

| Datei/Bereich | Neue URL-/DOI-Zeilen | Einordnung |
|---|---:|---|
| `de/content/anhang-p-papers/p.2-civitas-public-building-a-european-digital-agora.md` | 15 | Bereits in A5 geprueft. |
| `en/content/appendix-p-papers/p.2-civitas-public-building-a-european-digital-agora.md` | 15 | Bereits in A5 geprueft. |
| `de/content/anhang-p-papers/p.1-kindheit-erwachsenwerden-und-das-anti-game-over-prinzip.md` | 3 | DOI/Zenodo/Lizenzlink pruefen. |
| `en/content/appendix-p-papers/p.1-childhood-adulthood-and-the-anti-game-over-principle.md` | 3 | DOI/Zenodo/Lizenzlink pruefen. |
| DE/EN Reformpfad-SVG | 2 | XML-Namespace, kein inhaltlicher Quellenlink. |

Weitere 44 Treffer sind Quellen-/DOI-/Referenzmarker ohne neue externe URL. Sie gehoeren trotzdem in die redaktionelle Pruefliste, weil sie Quellenpflichten, Korrekturregeln oder interne Referenzlogik beschreiben.

## Gemini / AI-Referenzpruefung

Geprueft wurden die relevanten Umgebungsvariablen ohne Ausgabe geheimer Werte:

| Variable | Status |
|---|---|
| `AI_REFERENCE_API_KEY` | nicht gesetzt |
| `AI_REFERENCE_PROVIDER` | nicht gesetzt |
| `AI_REFERENCE_URL` | nicht gesetzt |
| `AI_REFERENCE_MODEL` | nicht gesetzt |
| `GEMINI_API_KEY` | nicht gesetzt |
| `GOOGLE_API_KEY` | nicht gesetzt |
| `GOOGLE_GENAI_API_KEY` | nicht gesetzt |

Der installierte `gitbook_worker.tools.quality.ai_references` unterstuetzt `genai` / `google-genai`, verwendet aber fuer den Worker primaer die Variablen `AI_REFERENCE_API_KEY`, `AI_REFERENCE_PROVIDER`, `AI_REFERENCE_URL` und `AI_REFERENCE_MODEL`. Ein echter Gemini-Probelauf wurde deshalb nicht gestartet, weil kein API-Key hinterlegt ist.

Empfohlener DE-Dry-Run, sobald der Key bewusst in der Terminal-Session gesetzt ist:

```powershell
$env:AI_REFERENCE_PROVIDER = "genai"
$env:AI_REFERENCE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent"
$env:AI_REFERENCE_API_KEY = "<nur lokal in dieser Terminal-Session setzen>"
New-Item -ItemType Directory -Force tmp/gitbook-worker-ai-v2.5.0 | Out-Null
C:/Python311/python.exe -m gitbook_worker.tools.quality.ai_references --root . --summary de/content/SUMMARY.md --language de --ai-provider $env:AI_REFERENCE_PROVIDER --ai-url $env:AI_REFERENCE_URL --ai-api-key $env:AI_REFERENCE_API_KEY --json-report tmp/gitbook-worker-ai-v2.5.0/ai-references-de-gemini-dry-run.json --dry-run --no-progress
```

Fuer einen schnelleren Smoke-Test kann statt `--summary de/content/SUMMARY.md` eine explizite `--files`-Liste mit den P1-Dateien aus dieser Pruefliste verwendet werden.

Nach dem ersten Gesamtversuch gilt: Der direkte Worker-Lauf ueber `--summary de/content/SUMMARY.md` erzeugt bei Gemini sehr schnell `429 Too Many Requests`. Fuer weitere Versuche ist deshalb der lokale Throttling-Wrapper zu verwenden, der pro Referenz wartet, 429-Cooldowns setzt, bei wiederholten Rate-Limits abbricht und Reports/Logs sanitisiert:

```powershell
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$asOfDate = Get-Date -Format 'yyyy-MM-dd'
C:/Python311/python.exe scripts/quality/ai_references_throttled.py --root . --files-list tmp/gitbook-worker-ai-v2.5.0/ai-references-de-v2.5-priority-files.txt --language de --include-inline-links --as-of-date $asOfDate --delay-seconds 8 --jitter-seconds 3 --cooldown-on-429-seconds 90 --max-consecutive-429 5 --json-report "tmp/gitbook-worker-ai-v2.5.0/ai-references-de-v2.5-priority-throttled-$stamp.json" --log-file "tmp/gitbook-worker-ai-v2.5.0/ai-references-de-v2.5-priority-throttled-$stamp.log"
```

## Release-Entscheidung

Fuer v2.5 ist die realistische aktuelle Quellenpruefliste nicht das gesamte Buch, sondern:

1. Anhang P.2 CIVITAS Public: erledigt durch A5.
2. Anhang P.1 Anti-Game-Over: DOI-/Lizenz-/APA-Check erledigt; siehe `source-review-final-gate-2026-05-05.md`.
3. Kapitel 13.8 Energiesouveraenitaet: redaktionelle Quellen- und Aktualitaetspruefung im Finalscope erledigt; siehe `source-review-final-gate-2026-05-05.md`.
4. Kapitel 6 CIVITAS: A4 erledigt; Quellenstaerke/Querverweise im Finalscope geprueft, externe Detailquellen liegen primaer in P.2.
5. Paragraph 11.3.7, Paragraph 5.8.4 und Anhang M: Plausibilitaet und interne Einbettung im Finalscope geprueft; EN bleibt Draft/Review.
6. Vollstaendige Staatenprofil- und Gesamtbuch-Aktualitaet: als eigenes v2.6-/Backlog-Thema fuehren.
