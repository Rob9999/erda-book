# gitbook_worker Quality-Tool-Bewertung v2.5.0 (Draft)

**Stand:** 2026-05-03  
**Status:** Draft, vorläufig bewertet
**Arbeitsrolle:** Redakteur:in / Publisher-Vorprüfung

---

## Zweck

Diese Notiz bewertet die vorhandenen `gitbook_worker.tools.quality`-Funktionen für die finale v2.5.0-Freigabe. Die Tools sind als Prüf- und Assistenzwerkzeuge zu behandeln. Sie ersetzen keine redaktionelle Freigabe.

Nach neu festgelegter Arbeitsregel werden weitere `gitbook_worker`-Runs erst nach gesichertem Worktree ausgeführt.

---

## Getestete Tools

| Tool | Teststand | Ergebnis | Vorläufige Bewertung |
|---|---|---|---|
| `sources` | DE/EN Content-Bäume | erfolgreich | brauchbar für Quelleninventar und Review-Vorbereitung |
| `link_audit` | Release-Dokumente, DE-Sample-Datei, DE-Strukturcheck ohne HTTP | erfolgreich, aber teils sehr laut | brauchbar; globale Duplicate-Heading-Ergebnisse brauchen Filterung |
| `ai_references` | lokaler Mock-Endpunkt, `--dry-run`, DE-Sample-Datei | erfolgreich | technisch brauchbar, aber nur begrenzt und mit menschlicher Abnahme einsetzen |
| `staatenprofil_links` | DE Content-Baum | erfolgreich, 176 Reportzeilen | brauchbar als Spezialscan, aber 403/404/ERR müssen redaktionell bewertet werden |

---

## Quellenextraktion

Ausgeführt:

```powershell
C:/Python311/python.exe -m gitbook_worker.tools.quality.sources --root de/content -o tmp/gitbook-worker-quality-v2.5.0/sources-de.csv --language de --max-level 6
C:/Python311/python.exe -m gitbook_worker.tools.quality.sources --root en/content -o tmp/gitbook-worker-quality-v2.5.0/sources-en.csv --language en --max-level 6
```

Ergebnis:

| Sprache | Gefundene Markdown-Dateien | CSV-Zeilen |
|---|---:|---:|
| DE | 318 | 1226 |
| EN | 318 | 1128 |

Bewertung:

- Für das Release brauchbar als Quelleninventar.
- Sehr hilfreich, um riskante oder veraltete Quellenbereiche redaktionell zu priorisieren.
- Die Differenz DE/EN sollte nicht automatisch als Fehler gelten, aber für den Übersetzungsreview sichtbar bleiben.
- Das Tool prüft nicht selbst, ob eine Quelle aktuell oder fachlich geeignet ist.

---

## Link- und Struktur-Audit

Ausgeführt auf den Release-Dokumenten:

```powershell
C:/Python311/python.exe -m gitbook_worker.tools.quality.link_audit --root release-docs/v2.5.0 --http-report tmp/gitbook-worker-quality-v2.5.0/link-audit-release-docs.csv --timeout 5 --no-progress --check-images --check-duplicate-headings --check-citations --list-todos
```

Ergebnis nach Bereinigung der Checklistenformulierung:

| Prüfung | Ergebnis |
|---|---|
| HTTP-Links | 0 broken, 0 valid links im getesteten Bereich |
| Bilder/Medien | 0 Issues |
| Doppelte Überschriften | 0 Duplicates |
| Zitationslücken | 0 Dateien mit Lücken |
| Arbeitsmarker | 0 Einträge |

Bewertung:

- Für Release-Dokumente gut brauchbar.
- Die Arbeitsmarker-Suche ist rein textbasiert und markiert auch erklärende Vorkommen der Wörter, wenn sie ausgeschrieben werden. Checklisten sollten deshalb neutrale Begriffe wie `Arbeitsmarker` verwenden.
- Für den gesamten Content-Baum kann der Lauf deutlich umfangreicher sein und sollte nach Commit-Sicherung separat erfolgen.

Ausgeführt auf einer DE-Sample-Datei mit Quellen:

```powershell
C:/Python311/python.exe -m gitbook_worker.tools.quality.link_audit de/content/1.-aktuelle-lage-europas-herausforderungen-und-chancen/1.1-demokratische-erosion-und-geopolitische-fragmentierung.md --http-report tmp/gitbook-worker-quality-v2.5.0/link-audit-de-sample.csv --timeout 5 --no-progress --check-images --check-duplicate-headings --check-citations --list-todos
```

Ergebnis:

| Prüfung | Ergebnis |
|---|---|
| HTTP-Links | 0 broken, 2 valid links |
| Bilder/Medien | 0 Issues |
| Doppelte Überschriften | 0 Duplicates |
| Zitationslücken | 0 Dateien mit Lücken |
| Arbeitsmarker | 0 Einträge |

Ausgeführt auf `de/content` ohne externe HTTP-Abfragen:

```powershell
C:/Python311/python.exe -m gitbook_worker.tools.quality.link_audit --root de/content --no-progress --check-duplicate-headings --check-citations --list-todos
```

Ergebnis:

| Prüfung | Ergebnis |
|---|---|
| Doppelte Überschriften | 1317 Treffer |
| Zitationslücken | 1 Datei mit Lücke |
| Arbeitsmarker | 0 Einträge |

Bewertung des DE-Strukturchecks:

- Die Zitationslücke ist potentiell prüfenswert: `de/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/staatenprofil-deutschland-de.md`, fehlende Nummer 15.
- Die Duplicate-Heading-Zahl ist in dieser Form nicht release-blockierend, weil viele Treffer aus bewusst wiederholten Staatenprofil- und Executive-Compendium-Strukturen entstehen.
- Für einen echten Release-Gate-Einsatz sollte der Duplicate-Heading-Check entweder auf einzelne Publikationsabschnitte begrenzt oder um erlaubte Template-Überschriften gefiltert werden.

---

## Staatenprofil-Linkprüfung

Ausgeführt:

```powershell
C:/Python311/python.exe -m gitbook_worker.tools.quality.staatenprofil_links --root de/content --output tmp/gitbook-worker-quality-v2.5.0/staatenprofil-links-de.csv
```

Ergebnis:

| Report | Wert |
|---|---:|
| Reportzeilen | 176 |

Beispiele aus dem Report enthalten `403 Forbidden`, `404 Not Found` und `ERR` bei externen Staatenprofil-Links.

Bewertung:

- Für Anhang-B-/Staatenprofil-Qualität brauchbar.
- `403` ist nicht automatisch ein inhaltlich kaputter Link, weil manche Anbieter HEAD/automatisierte Requests blocken.
- `404` und dauerhafte `ERR`-Treffer sind für die Referenzaktualität deutlich relevanter.
- Für v2.5.0 sollte mindestens eine priorisierte Prüfung der `404`/dauerhaften `ERR`-Fälle erfolgen.

---

## AI-Referenzprüfung

Festgestellt vor dem Test:

- CLI vorhanden: `python -m gitbook_worker.tools.quality.ai_references`
- Unterstützt `--dry-run` und JSON-Report.
- Standardprovider ist OpenAI-kompatibel; ohne API-Key sind echte Requests voraussichtlich nicht nutzbar.
- Das Tool kann Dateien über `SUMMARY.md`, Manifest oder explizite `--files` entdecken.
- Es kann bei erfolgreicher Antwort Quellenzeilen ändern, sofern nicht `--dry-run` gesetzt ist.

Vorläufige Bewertung:

- Nur mit `--dry-run` für Release-Review einsetzen.
- Nur auf ausgewählten Dateien oder Quellen-Samples testen, nicht blind auf dem gesamten Buch.
- Keine Inhalte an externe Dienste senden, bevor Datenschutz, API-Ziel und Prompt-Verhalten bewusst freigegeben sind.
- AI-Ergebnisse sind Hinweise, keine redaktionelle Wahrheit.

Ausgeführt mit lokalem Mock-Endpunkt, ohne externe API und mit `--dry-run`:

```powershell
C:/Python311/python.exe -m gitbook_worker.tools.quality.ai_references --root . --files de/content/1.-aktuelle-lage-europas-herausforderungen-und-chancen/1.1-demokratische-erosion-und-geopolitische-fragmentierung.md --language de --ai-provider local --ai-url http://127.0.0.1:8765 --json-report tmp/gitbook-worker-quality-v2.5.0/ai-references-mock-de-sample.json --dry-run --no-progress
```

Ergebnis:

| Prüfung | Ergebnis |
|---|---:|
| Referenzaufgaben | 2 |
| Erfolgreich validiert | 2 |
| Reparaturen | 0 |
| Fehlgeschlagen | 0 |

Bewertung des Mock-Tests:

- CLI, Discovery über explizite Datei, JSON-Report und `--dry-run` funktionieren.
- Der Test validiert die Toolkette, aber nicht die faktische Qualität eines echten AI-Providers.
- Das Tool kann im Nicht-Dry-Run Dateien verändern; für Releasezwecke ist `--dry-run` deshalb Pflicht, solange keine separate Freigabe vorliegt.

Offen bleibt:

- Optionaler echter Dry-Run nur nach ausdrücklicher Entscheidung zu API/Provider.

---

## Vorläufiges Fazit

Die alten Quality-Tools sind nicht veraltet im Sinne von unbrauchbar. `sources`, `link_audit`, `staatenprofil_links` und die technische `ai_references`-Pipeline liefern verwertbare Signale. Für v2.5.0 sollte die belastbare Linie lauten:

1. `sources` erzeugt das Quelleninventar.
2. `link_audit` prüft technische Link-/Medien-/Strukturprobleme.
3. `staatenprofil_links` priorisiert externe Linkprobleme in den Staatenprofilen.
4. `ai_references` darf nur optional, begrenzt und im `--dry-run` laufen.
5. Die endgültige Quellenaktualität entscheidet die Redaktion anhand der Berichte.
