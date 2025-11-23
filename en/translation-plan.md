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
| 2025-11-23 | 4. Das ERDA Gesamtkonzept (README)                               | Drafted | Executive summary and glossary translated; YAML preamble added. |
| 2025-11-23 | 4.1 Vision & Leitprinzip (README)                                | Drafted | Introductory subchapter translated; YAML preamble added. |
| 2025-11-23 | 4.1.1 Mehrsprachige Narrative und kulturelle Identität           | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.1.2 Starke Zivilgesellschaft als Partnerin                     | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.1.3 Institutionelle Balance                                    | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.1.4 Demokratische Kontrolle über KI-Prozesse                   | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.1.5 Interplanetare Verantwortung und evolutionäre Perspektiven  | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.1.6 ERDA im zeitlichen Wandel                                   | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.2 Reformphase 2025–2035 (README)                               | Drafted | Executive summary and key messages translated with YAML preamble. |
| 2025-11-23 | 4.2.1 Umsetzung zentraler Reformempfehlungen                      | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.2.2 Aufbau der Europäischen Verteidigungsallianz (EDA 2.0)     | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.2.3 Erweiterungsstrategie nach dem Modell „Konzentrischer Kreise“ | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.2.4 Einbindung globaler Perspektiven                            | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.2.5 Zivilgesellschaftliche Begleitstruktur                      | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.3 Konsolidierung 2035–2050 (README)                              | Drafted | Executive summary chapter translated with YAML preamble. |
| 2025-11-23 | 4.3.1 Verankerung einer ERDA-Verfassung                            | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.3.2 Demokratie in der Post-Knappheitsökonomie                    | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.3.3 Souveränität durch Technologie & Innovation                   | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.3.4 Globale Gerechtigkeit & Klimasolidarität                     | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.3.5 Resilienz durch Kultur & Bildung                             | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.3.6 Institutionelle Demokratisierung                             | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.4 Transformation 2050–2075 (README)                              | Drafted | Executive summary chapter translated with YAML preamble. |
| 2025-11-23 | 4.4.1 Demokratische Hochtechnologie-Zivilisation                    | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.4.2 Soziale und kulturelle Resilienz                              | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.4.3 Globale Integration auf Grundlage des Rechts                  | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.4.4 Technologie mit Sinn und Verantwortung                         | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.4.5 Post-materialistische Lebensqualität                          | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.4.6 Zukunft als Gemeinschaftsaufgabe                              | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5 Strategische Narrative & öffentliche Kommunikation (README)     | Drafted | Executive summary chapter translated with YAML preamble. |
| 2025-11-23 | 4.5.1 Soziale & emotionale Aspekte                                  | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5.2 Narrative Bausteine (README)                                  | Drafted | Section stub translated and YAML added. |
| 2025-11-23 | 4.5.2.1 Narrativ der Ermächtigung                                   | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5.2.2 Demokratie als schöpferische Kraft                          | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5.2.3 Autonomie ist kein Abbruch – sondern Überlebensstrategie    | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5.2.4 Transatlantische Erneuerung durch Gleichgewicht             | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5.2.5 Globale Einladung                                           | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 4.5.2.6 Erzählung des Mitgestaltens                                 | Drafted | Full subchapter translated including tables, boxes and quiz. |
| 2025-11-23 | 5. Das EDA Konzept (README)                                         | Drafted | Executive summary, glossary and framing translated.          |
| 2025-11-23 | 5.1 Vision und Mission der Europäischen Verteidigungsallianz (EDA)  | Drafted | Section translated including vision and core objectives.     |
| 2025-11-23 | 5.2 Mitgliedschaft und Organisationsstruktur                         | Drafted | Section translated including members, partners and organs.   |
| 2025-11-23 | 5.3 Prinzipien und Verteidigungsdoktrin                              | Drafted | Section translated including key defence principles.         |
| 2025-11-23 | 5.4 Militärische Integration und gemeinsame Standards                | Drafted | Section translated including integration and standards.      |
| 2025-11-23 | 5.5 Globale Koordination und Verantwortung                           | Drafted | Section translated including global coordination aspects.    |
| 2025-11-23 | 5.6 Synergien und Konnektivität                                      | Drafted | Section translated including links to wider ERDA context.    |
| 2025-11-23 | 5.7 Kommandostruktur und operative Souveränität                      | Drafted | Section translated including command and sovereignty design. |
| 2025-11-23 | 5.8 Defense Sovereignty Nodes (DSNs)                                 | Drafted | Section translated including DSN concept and subsections.    |
| 2025-11-23 | 5.9 Unbemannte strategische Systeme und Drohnenkräfte                | Drafted | Full EDF subchapter translated with all components.          |
| 2025-11-23 | 5.10 Nukleare Abschreckung und strategische Autonomie (README)       | Drafted | Section README translated with strategic framing.            |
| 2025-11-23 | 5.10.1 Begründung und Grundsätze                                     | Drafted | Principles and rationale for nuclear deterrence translated.  |
| 2025-11-23 | 5.10.2 Sofortmaßnahmen (2025–2030)                                   | Drafted | Immediate measures for nuclear posture translated.           |
| 2025-11-23 | 5.10.3 Mittelfristige Entwicklung (2030–2040)                        | Drafted | Medium-term development path for deterrence translated.      |
| 2025-11-23 | 5.10.4 Langfristige Vision (2040–2050)                               | Drafted | Long-term ENDD vision and DSN linkage translated.            |
| 2025-11-23 | 5.10.5 Öffentliche Kommunikation und ethische Grundlage              | Drafted | Public communication and ethical framing translated.         |

## Next Targets

I will continue following the order in `content/SUMMARY.md`, updating this tracker after each translated file.

### Chapter 1 Checklist

| Section | Status  | Notes |
| ------- | ------- | ----- |
| 1.1 Demokratische Erosion und geopolitische Fragmentierung | Drafted | Delivered 2025-02-14 with YAML preamble. |
| 1.2 Wirtschaftlicher Druck und globale Systemkonkurrenz | Drafted | Completed 2025-11-19 including interactive elements. |
| 1.3 Technologische Transformation und soziale Spaltung | Drafted | Completed 2025-11-19 with tables and calls to action. |
| 1.4 Chancen im Wandel | Drafted | Completed 2026-11-20 with YAML preamble and full translation. |
| 1.5 Der strategische Imperativ | Drafted | Completed 2025-11-19 with YAML preamble and interactive elements. |

