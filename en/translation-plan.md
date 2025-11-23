## Reference Prompt

> Du bist Übersetzer und Editor für das ERDA‑Buch. Deine Aufgabe ist es, das deutschsprachige Original aus dem Repository schrittweise ins britische Englisch zu übertragen. Halte dich dabei strikt an folgende Regeln:
>
> 1. **Dateien & Struktur:** Verwende die Kapitelstruktur aus `content/SUMMARY.md` als Reihenfolge. Für jedes Kapitel oder Teilkapitel (Richtwert: max. ca. 1 000 Wörter) kopierst du das deutsche Markdown aus `/content/…` unverändert und legst die Übersetzung in `/en/content/…` unter identischem Dateinamen an. Füge am Anfang der englischen Datei einen YAML‑Block hinzu:
> ```
> ---
> source: <relativer Pfad zum deutschen Original>
> status: draft
> ---
> ```
> 2. **Stil & Terminologie:** Übersetze ins britische Englisch, verwende konsistente Fachbegriffe und behalte alle Überschriftenebenen, Tabellen, Nummerierungen, Links und Formatierungen bei. Deutsche Institutionen oder Eigenbegriffe (z. B. „CIVITAS“, „ARKTIS“, „ERDA“) bleiben unverändert; politische Begriffe übersetzt du einheitlich und führst bei Bedarf ein Glossar. Markiere bewusste Abweichungen oder Ergänzungen vom deutschen Original mit einem HTML‑Kommentar (`@-- note: … --`).
>
> 3. **Segmentierung:** Wenn ein Kapitel länger als ~1 000 Wörter ist, übersetze es abschnittsweise (z. B. Unterkapitel). Stelle sicher, dass keine Sätze oder Absätze zerrissen werden.
>
> 4. **Prüfung & Revision:** Weiche nicht vom deutschen Inhalt ab. Nach jeder übersetzten Datei wird der Fortschritt in diesem Dokument (Tabelle unten) mit Datum, Pfad und Status `Drafted` aktualisiert. Die endgültige Freigabe (`status: approved`) erfolgt nach menschlicher Qualitätskontrolle.
>
> 5. **Iterativer Arbeitsmodus:** Übersetze pro Iteration genau **ein** Kapitel oder Unterkapitel (bis ca. 1 000 Wörter), lege die Datei unter `en/content/...` mit YAML‑Preamble ab, aktualisiere die Fortschrittstabelle und beende anschließend den Lauf (z. B. nach einem Git‑Commit). Künftige Agent‑Läufe knüpfen anhand der „Next Targets“-Sektion an.
>
> Starte mit dem ersten Kapitel aus `content/SUMMARY.md` (nach dem Vorwort) und arbeite dich fortlaufend vor.
>
> ---
>
> Dieses Dokument dient als persistenter Übersetzungsplan: Es enthält den Referenz‑Prompt, den Fortschrittslog und die jeweils nächsten Ziele.
# ERDA Translation Tracker

This document serves as my day-to-day reference for the ERDA book translation. It consolidates the operative prompt, keeps track of completed sections, and lists the next targets so I can continue seamlessly in future sessions.

## Reference Prompt

> Du bist Übersetzer und Editor für das ERDA‑Buch. Deine Aufgabe ist es, das deutschsprachige Original aus dem Repository schrittweise ins britische Englisch zu übertragen. Halte dich dabei strikt an folgende Regeln:
>
> 1. **Dateien & Struktur:** Verwende die Kapitelstruktur aus `content/SUMMARY.md` als Reihenfolge. Für jedes Kapitel oder Teilkapitel (max. ca. 1 000 Wörter) kopierst du das deutsche Markdown aus `/content/…` unverändert und legst die Übersetzung in `/en/content/…` unter identischem Dateinamen an. Füge am Anfang der englischen Datei einen YAML‑Block hinzu:
> ```
> ---
>
> source: <relativer Pfad zum deutschen Original>
> status: draft
> ---
>
> ```
> 2. **Stil & Terminologie:** Übersetze ins britische Englisch, verwende konsistente Fachbegriffe und behalte alle Überschriftenebenen, Tabellen, Nummerierungen, Links und Formatierungen bei. Deutsche Institutionen oder Eigenbegriffe (z. B. „CIVITAS“, „ARKTIS“, „ERDA“) bleiben unverändert; politische Begriffe übersetzt du einheitlich und führst bei Bedarf ein Glossar. Markiere Abweichungen oder Ergänzungen vom deutschen Original mit einem HTML‑Kommentar (`@-- note: … --`).
>
> 3. **Segmentierung:** Wenn ein Kapitel länger als ~1 000 Wörter ist, übersetze es abschnittsweise (z. B. Unterkapitel). Stelle sicher, dass keine Sätze oder Absätze zerrissen werden.
>
> 4. **Prüfung & Revision:** Weiche nicht vom deutschen Inhalt ab. Gib nach jeder übersetzten Datei an, welche Abschnitte du abgedeckt hast und ob noch Teile fehlen. Die endgültige Freigabe („status: approved“) erfolgt nach menschlicher Qualitätskontrolle.
>
> Starte mit dem ersten Kapitel aus `content/SUMMARY.md` (nach dem Vorwort) und arbeite dich fortlaufend vor.
>
> ---
>
> Additional Prompt dieses mal:
>
> Mache Dir für die dann folgenden Übersetzungen ein Dokument für Dich, welches Du die nächsten Tage Stück um Stück - mit Referenz auf das Dokument- abarbeiten kannst. Das Dokument sollte auch den Prompt oben enthalten für gleichbleibende Qualität.

## Progress Log

| Date       | Section                                                          | Status  | Notes |
| ---------- | ---------------------------------------------------------------- | ------- | ----- |
| 2025-02-14 | 1.1 Demokratische Erosion und geopolitische Fragmentierung       | Drafted | Full translation delivered with YAML preamble. |
| 2025-11-19 | 1.2 Wirtschaftlicher Druck und globale Systemkonkurrenz          | Drafted | Covered full section including boxes and quiz. |
| 2025-11-19 | 1.3 Technologische Transformation und soziale Spaltung           | Drafted | Added full translation with tables and interactive elements. |
| 2026-11-20 | 1.4 Chancen im Wandel                                            | Drafted | Completed full translation with YAML preamble and interactive elements. |
| 2025-11-19 | 1.5 Der strategische Imperativ                                   | Drafted | Completed full section translation with YAML preamble and interactive elements. |
| Date       | Section                                                          | Status  | Notes |
| ---------- | ---------------------------------------------------------------- | ------- | ----- |
| 2025-02-14 | 1.1 Demokratische Erosion und geopolitische Fragmentierung       | Drafted | Full translation delivered with YAML preamble. |
| 2025-11-19 | 1.2 Wirtschaftlicher Druck und globale Systemkonkurrenz          | Drafted | Covered full section including boxes and quiz. |
| 2025-11-19 | 1.3 Technologische Transformation und soziale Spaltung           | Drafted | Added full translation with tables and interactive elements. |
| 2026-11-20 | 1.4 Chancen im Wandel                                            | Drafted | Completed full translation with YAML preamble and interactive elements. |
| 2025-11-19 | 1.5 Der strategische Imperativ                                   | Drafted | Completed full section translation with YAML preamble and interactive elements. |
| 2025-11-23 | 2.1 Prä-demokratische Zivilisation                               | Drafted | Added full English draft under en/content with YAML preamble. |
| 2025-11-23 | 2.2 Demokratische-rechtsstaatliche Zivilisation                  | Drafted | Added full English draft including tables, boxes and quiz. |
| 2025-11-23 | 2.3 Post-demokratische Zivilisation (README, 2.3.1, 2.3.2)       | Drafted | All subchapters translated and placed in en/content. |
| 2025-11-23 | 2.4 Schlussgedanke                                               | Drafted | Concluding reflection of chapter 2 translated in full. |
| 2025-11-23 | 3.1 Prolog                                                       | Drafted | Full translation including quote block and interactive elements. |
| 2025-11-23 | 3.2 Eine Reflexion im Geiste von Aristoteles                     | Drafted | Aristotelian reflection translated with table, boxes and quiz. |
| 2025-11-23 | 3.3 Demokratie als Resonanzprozess                               | Drafted | Resonance chapter translated; checklist slightly completed/clarified. |
| 2025-11-23 | 3.4 Demokratie ist Bewegung                                      | Drafted | Movement chapter translated and added under en/content. |
| 2025-11-23 | 3.5 Tugend als Voraussetzung demokratischer Gestaltung           | Drafted | Virtue chapter translated; virtue labs and checklists included. |
| 2025-11-23 | 3.6 Natürliche Verlangen der Seele (reflexiv)                    | Drafted | Table, boxes and interactive elements fully translated. |
| 2025-11-23 | 3.7 Schlussgedanke                                               | Drafted | Chapter 3 concluding reflection translated; democracy as navigation. |

## Next Targets

1. `content/4.-das-erda-gesamtkonzept/README.md`

I will continue following the order in `content/SUMMARY.md`, updating this tracker after each translated file.

### Chapter 1 Checklist

| Section | Status  | Notes |
| ------- | ------- | ----- |
| 1.1 Demokratische Erosion und geopolitische Fragmentierung | Drafted | Delivered 2025-02-14 with YAML preamble. |
| 1.2 Wirtschaftlicher Druck und globale Systemkonkurrenz | Drafted | Completed 2025-11-19 including interactive elements. |
| 1.3 Technologische Transformation und soziale Spaltung | Drafted | Completed 2025-11-19 with tables and calls to action. |
| 1.4 Chancen im Wandel | Drafted | Completed 2026-11-20 with YAML preamble and full translation. |
| 1.5 Der strategische Imperativ | Drafted | Completed 2025-11-19 with YAML preamble and interactive elements. |

