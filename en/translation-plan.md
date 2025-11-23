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



## Progress Log

| Date       | Section                                                          | Status  | Notes |
| ---------- | ---------------------------------------------------------------- | ------- | ----- |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/pl-staatenprofil-polen.md | Drafted | State profile translated and mirrored with metadata. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/pt-staatenprofil-republik-portugal.md | Drafted | English version created with YAML front matter and source links preserved. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/ro-staatenprofil-rumanien.md | Drafted | Romania profile translated; retained structure and metadata. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/se-staatenprofil-schweden.md | Drafted | Sweden profile translated with Arctic context and YAML metadata. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/si-staatenprofil-slowenien.md | Drafted | Slovenia profile translated; bridge-state narrative maintained. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/sk-staatenprofil-slowakei.md | Drafted | Slovakia profile translated with tech-corridor storyline and YAML preserved. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.3.-staatenprofile-eu-erda-kernlander/staatenprofil-deutschland-de.md | Drafted | Germany profile translated; innovation/technology democracy framing retained. |
