# gitbook_worker Quality-Tool-Bewertung v2.5.0 (Draft)

**Stand:** 2026-05-03  
**Status:** Draft, unvollständig  
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
| `link_audit` | `release-docs/v2.5.0` | erfolgreich | brauchbar für Links, Medien, doppelte Überschriften, Zitationslücken und Arbeitsmarker; einfache Heuristik beachten |
| `ai_references` | `--help` und Code-/CLI-Prüfung; Mock-Test vorbereitet, nicht abgeschlossen | offen | potentiell brauchbar, aber nur mit `--dry-run`, Datenschutz-/API-Prüfung und menschlicher Abnahme |
| `staatenprofil_links` | `--help` | CLI vorhanden | nur relevant, falls Staatenprofil-Dateien im Scope sind |

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

---

## AI-Referenzprüfung

Festgestellt:

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

Offen:

- Lokaler Mock-Dry-Run der CLI nach Commit-Sicherung.
- Optionaler echter Dry-Run nur nach ausdrücklicher Entscheidung zu API/Provider.

---

## Vorläufiges Fazit

Die alten Quality-Tools sind nicht veraltet im Sinne von unbrauchbar. `sources` und `link_audit` liefern bereits jetzt verwertbare Release-Gates. `ai_references` ist technisch interessant, aber für v2.5.0 nur vorsichtig als Assistenzwerkzeug geeignet. Für die finale Freigabe sollte die belastbare Linie lauten:

1. `sources` erzeugt das Quelleninventar.
2. `link_audit` prüft technische Link-/Medien-/Strukturprobleme.
3. `ai_references` darf nur optional, begrenzt und im `--dry-run` laufen.
4. Die endgültige Quellenaktualität entscheidet die Redaktion anhand der Berichte.
