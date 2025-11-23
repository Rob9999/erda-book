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
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/README.md | Drafted | Introduced Extended Partnership section heading in English with source link. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/al-staatenprofil-albanien.md | Drafted | Albania profile translated with YAML metadata and scenario indicators preserved. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/am-staatenprofil-armenien.md | Drafted | Armenia profile translated with governance, scenario, and indicator tables mirrored. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/ba-staatenprofil-bosnien-herzegowina.md | Drafted | Bosnia and Herzegovina profile translated with scenario narrative and resource overview. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/ch-staatenprofil-schweiz.md | Drafted | Switzerland profile translated retaining infrastructure autonomy and indicator set. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/cy-staatenprofil-zypern.md | Drafted | Cyprus profile translated with Mediterranean energy focus and YAML metadata. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/ge-staatenprofil-georgien.md | Drafted | Georgia profile translated preserving Black Sea narrative and indicator table. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/hu-staatenprofil-ungarn.md | Drafted | Hungary profile translated with logistics-corridor storyline and metrics. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/il-staatenprofil-israel.md | Drafted | Israel profile translated with tech-partner narrative and defence metrics. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/md-staatenprofil-moldau.md | Drafted | Moldova profile translated with agrarian-to-digital storyline and indicator table. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/me-staatenprofil-montenegro.md | Drafted | Montenegro profile translated; Adriatic sustainability narrative preserved. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/mk-staatenprofil-nord-mazedonien.md | Drafted | North Macedonia profile translated with Balkan bridge-state storyline. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/mt-staatenprofil-malta.md | Drafted | Malta profile translated highlighting Mediterranean cyber-maritime role. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/no-staatenprofil-norwegen.md | Drafted | Norway profile translated focusing on Arctic energy hub role. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/rs-staatenprofil-serbien.md | Drafted | Serbia profile translated covering Balkan logistics and reform themes. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/tr-staatenprofil-tuerkei.md | Drafted | Türkiye profile translated with Eurasian energy-logistics focus. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/ua-staatenprofil-ukraine.md | Drafted | Ukraine profile translated emphasising reconstruction and security role. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/uk-staatenprofil-vereinigtes-koenigreich.md | Drafted | United Kingdom profile translated focusing on finance and maritime security roles. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.4.-staatenprofile-eu-erda-erweiterte-partnerschaft/xk-staatenprofil-kosovo.md | Drafted | Kosovo profile translated highlighting digital-partner and stability narrative. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/README.md | Drafted | Introduced Global Associates overview with reference to concentric-circle architecture. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/au-staatenprofil-australien.md | Drafted | Australia profile translated with Indo-Pacific resource-tech focus. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/ca-staatenprofil-kanada.md | Drafted | Canada profile translated highlighting Arctic connector narrative. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/cl-staatenprofil-chile.md | Drafted | Chile profile translated with lithium-copper sustainability storyline. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/cr-staatenprofil-costa-rica.md | Drafted | Costa Rica profile translated emphasising sustainable tourism diplomacy. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/in-staatenprofil-indien.md | Drafted | India profile translated with digital-hub and demographic scale storyline. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/jp-staatenprofil-japan.md | Drafted | Japan profile translated highlighting tech leadership and demographic adaptation. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/kr-staatenprofil-sued-korea.md | Drafted | South Korea profile translated emphasising semiconductor hub and democratic resilience. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/na-staatenprofil-namibia.md | Drafted | Namibia profile translated covering renewable potential and Walvis Bay logistics role. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/nz-staatenprofil-neuseeland.md | Drafted | New Zealand profile translated with Pacific green-economy focus. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/sn-staatenprofil-senegal.md | Drafted | Senegal profile translated spotlighting West African bridge role and renewables. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/tn-staatenprofil-tunesien.md | Drafted | Tunisia profile translated with Mediterranean solar-hub storyline. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/tw-staatenprofil-taiwan.md | Drafted | Taiwan profile translated highlighting semiconductor leadership and civic resilience. |
| 2025-11-23 | en/content/anhang-b-erda-staatenprofile/b.5.-staatenprofile-erda-globale-assoziierte/uy-staatenprofil-uruguay.md | Drafted | Uruguay profile translated; emphasised Mercosur bridge role and sustainability focus. |

## Remaining chapters (not yet translated)

**B.4 – EU/ERDA Extended Partnership**

- None – section completed; proceed with B.5 targets.

**B.5 – ERDA Global Associates**

- None – section completed for current scope.
