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

## Next Targets

1. `content/1.-aktuelle-lage-europas-herausforderungen-und-chancen/1.2-wirtschaftlicher-druck-und-globale-systemkonkurrenz.md`
2. `content/1.-aktuelle-lage-europas-herausforderungen-und-chancen/1.3-technologische-transformation-und-soziale-spaltung.md`
3. `content/1.-aktuelle-lage-europas-herausforderungen-und-chancen/1.4-chancen-im-wandel.md`

I will continue following the order in `content/SUMMARY.md`, updating this tracker after each translated file.

### Chapter 1 Checklist

| Section | Status  | Notes |
| ------- | ------- | ----- |
| 1.1 Demokratische Erosion und geopolitische Fragmentierung | Drafted | Delivered 2025-02-14 with YAML preamble. |
| 1.2 Wirtschaftlicher Druck und globale Systemkonkurrenz | Queued  | Next immediate translation task. |
| 1.3 Technologische Transformation und soziale Spaltung | Queued  | Translate right after 1.2 to keep thematic flow. |
| 1.4 Chancen im Wandel | Backlog | Prep materials while handling earlier subsections. |
| 1.5 Der strategische Imperativ | Backlog | Begin once Chapter 1 subsections 1.1–1.4 are approved. |

