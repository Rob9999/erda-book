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
| 2025-11-23 | 6. Das CIVITAS Konzept (README)                                      | Drafted | Executive summary for CIVITAS digital democracy translated.  |
| 2025-11-23 | 6.1 Leitidee: Demokratie im digitalen Raum                           | Drafted | Section translated describing CIVITAS as digital agora.      |
| 2025-11-23 | 6.2 Trägerschaft & demokratische Kontrolle                           | Drafted | Governance and oversight structure for CIVITAS translated.   |
| 2025-11-23 | 6.3 Technische Architektur und Datenschutz                           | Drafted | Technical architecture and data-protection framing translated.|
| 2025-11-23 | 6.4 Kernfunktionen von CIVITAS                                       | Drafted | Core functional modules and interfaces translated.           |
| 2025-11-23 | 6.5 Schutzmechanismen & Rechtssicherheit                             | Drafted | Legal safeguards and protection mechanisms translated.       |
| 2025-11-23 | 6.6 Partnerschaften & globale Integration                            | Drafted | Partnership and global integration section translated.       |
| 2025-11-23 | 6.7 Bildung, Jugend & demokratische Partizipation                    | Drafted | Youth, education and participation section translated.       |
| 2025-11-23 | 6.8 Schlussgedanken                                                   | Drafted | CIVITAS concluding reflections and strategic framing.        |
| 2025-11-23 | 7. Das FORTERA Konzept (README)                                       | Drafted | Executive summary for FORTERA economic architecture translated. |
| 2025-11-23 | 7.1 Ausgangslage und strategische Eckpfeiler                          | Drafted | Starting point and strategic cornerstones section translated. |
| 2025-11-23 | 7.2 Ziel des Konzepts                                                 | Drafted | Aim of the FORTERA concept section translated.               |
| 2025-11-23 | 7.3 Produktionssouveränität und strategische Industriepolitik (README) | Drafted | Production sovereignty & strategic industrial policy README translated. |
| 2025-11-23 | 7.3.1 Übersicht: Strategische Produktionsziele Europas (Auszug)       | Drafted | Table of Europe’s strategic production goals translated.      |
| 2025-11-23 | 2. Natürliche Verlangen und ihre Bedeutung für Demokratie und Zivilisation (README) | Drafted | Chapter 2 executive summary/README translated with YAML preamble. |
| 2025-11-23 | 7.3.2 Quantifizierte Szenarien zur Produktionssouveränität im Rahmen von FORTERA | Drafted | Quantified production-sovereignty scenarios translated; YAML preamble added. |
| 2025-11-23 | 7.3.3 Herausforderungen, Risiken und Lösungsansätze              | Drafted | Challenge, risk and solution section translated with YAML preamble. |
| 2025-11-23 | 7.3.4 Übergangskosten und Finanzierungsstrategie                  | Drafted | Transition-cost and financing-strategy section translated; YAML added. |
| 2025-11-23 | 7.3.5 Praktische Maßnahmen- und Meilensteinplanung (2025–2050)    | Drafted | Practical measures and milestones section translated; YAML added. |
| 2025-11-23 | 7.3.6 Erfolgskontrolle und Anpassungsmechanismen                  | Drafted | Success-monitoring and adjustment-mechanisms section translated; YAML added. |
| 2025-11-23 | 7.3.7 Gesamtausblick und Nutzen                                   | Drafted | Overall outlook and benefits section translated; YAML added. |
| 2025-11-23 | 7.4 Aufbau demokratischer Handelsallianzen ("Democracy Trade Network") | Drafted | Section on democratic trade alliances translated; YAML preamble added. |
| 2025-11-23 | 7.5 Transatlantische Partnerschaft neu denken                    | Drafted | Section on rethinking the transatlantic partnership translated; YAML preamble added. |
| 2025-11-23 | 7.6 Defensivmechanismen gegen wirtschaftlichen Nationalismus     | Drafted | Section on defensive mechanisms against economic nationalism translated; YAML preamble added. |
| 2025-11-23 | 7.7 Bürgerbeteiligung & demokratische Wirtschaftskultur          | Drafted | Section on citizen participation and democratic economic culture translated; YAML preamble added. |
| 2025-11-23 | 7.8 Wirtschaftliche Resilienz und ethische Fundierung            | Drafted | Section on economic resilience and ethical foundations translated; YAML preamble added. |
| 2025-11-23 | 7.9 Schlussgedanken                                               | Drafted | Concluding reflections of FORTERA chapter translated; YAML preamble added. |
| 2025-11-23 | 8. Das ARKTIS Konzept (README)                                    | Drafted | ARKTIS chapter executive summary and glossary translated; YAML preamble added. |
| 2025-11-23 | 8.1 ARKTIS Codex – Ethik der arktischen Verantwortung             | Drafted | ARKTIS Codex on ethics of Arctic responsibility translated; YAML preamble added. |
| 2025-11-23 | 8.2 Ausgangslage                                                   | Drafted | ARKTIS section on the initial situation translated; YAML preamble added. |
| 2025-11-23 | 8.3 Leitprinzipien                                                 | Drafted | ARKTIS guiding principles section translated; YAML preamble added. |
| 2025-11-23 | 9. Das SPACE Konzept (README)                                      | Drafted | SPACE chapter executive summary translated; YAML preamble added. |
| 2025-11-23 | 9.1 ERDA Codex für kosmische Verantwortung (README)               | Drafted | README for ERDA Codex for Cosmic Responsibility translated; YAML preamble added. |
| 2025-11-23 | 9.1.1 Präambel                                                    | Drafted | Preamble of ERDA Codex for Cosmic Responsibility translated; YAML preamble added. |
| 2025-11-23 | 9.1.2 Grundsätze (README)                                         | Drafted | Principles section README of ERDA Codex translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.1 Menschenwürde und Rechtsstaatlichkeit gelten auch im All  | Drafted | Principle on human dignity and rule of law in space translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.2 Der Weltraum ist Allmende – kein Privateigentum           | Drafted | Principle on space as commons and non-privatisation translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.3 Keine Militarisierung ohne demokratische Kontrolle         | Drafted | Principle on no militarisation without democratic control translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.4 Technologische Offenheit und Wissensfreiheit               | Drafted | Principle on technological openness and freedom of knowledge translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.5 Nachhaltigkeit über Generationen hinweg                     | Drafted | Principle on intergenerational sustainability of space missions translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.6 Gerechtigkeit für alle Lebensformen                         | Drafted | Principle on justice and development rights for all life forms translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.7 Besucherprinzip für außersolare Intelligenz                | Drafted | Principle on treating extrasolar intelligence as guests under democratic rule-of-law translated; YAML preamble added. |
| 2025-11-23 | 9.1.2.8 Ressourcen gehören den natürlichen Inhabitanten            | Drafted | Principle on shared ownership of solar-system resources by natural inhabitants translated; YAML preamble added. |

| 2025-11-23 | 9.1.3 Aufbau einer SOLAR ALLIANCE (README)                         | Drafted | Overview section on building a SOLAR ALLIANCE translated; YAML preamble added. |
| 2025-11-23 | 9.1.3.1 Kodifizierung als Kosmosrecht                              | Drafted | Subsection on codifying the principles as cosmos law translated; YAML preamble added. |
| 2025-11-23 | 9.1.3.2 Vorbereitung der Gründung bis 2028                         | Drafted | Subsection on preparing the founding of the SOLAR ALLIANCE by 2028 translated; YAML preamble added. |
| 2025-11-23 | 9.1.4 Kosmisches Seerecht und Ordnung (README)                     | Drafted | README for cosmic law of the sea and order translated; YAML preamble added. |
| 2025-11-23 | 9.1.4.1 Kodifizierung fundamentaler Prinzipien                     | Drafted | Subsection on codifying fundamental principles of cosmic law translated; YAML preamble added. |
| 2025-11-23 | 9.1.5 Schlussformel                                                | Drafted | Closing formula of the ERDA Codex for Cosmic Responsibility translated; YAML preamble added. |
| 2025-11-23 | 9.2 Vom Seerecht zum Kosmosrecht (README)                         | Drafted | Chapter 9.2 README on moving from the law of the sea to cosmos law translated; YAML preamble added. |
| 2025-11-23 | 9.2.1 Natürliche Verlangen im offenen Raum (Meer oder All)        | Drafted | Subsection on natural longings in open space (sea or cosmos) translated; YAML preamble added. |
| 2025-11-23 | 9.2.2 Die prä-demokratische Zivilisation                           | Drafted | Subsection on the pre-democratic civilisation in relation to open space translated; YAML preamble added. |
| 2025-11-23 | 9.2.3 Die gegenwärtige Zivilisation – auch in ihrer demokratischen Reife | Drafted | Subsection on contemporary civilisation, including democratic maturity, and its contradictions in space translated; YAML preamble added. |
| 2025-11-23 | 9.2.4 Überblick – Bisherige Rechtsordnungen im Vergleich           | Drafted | Comparative overview of law of the sea and existing space law translated, including table; YAML preamble added. |
| 2025-11-23 | 9.2.5 Der Entwicklungsbogen zur Solar Alliance                      | Drafted | Subsection on the development arc towards the SOLAR ALLIANCE, including timeline to 2028, translated; YAML preamble added. |
| 2025-11-23 | 9.3 Die Institutionen der SOLAR ALLIANCE (README)                   | Drafted | README for institutions of the SOLAR ALLIANCE translated; YAML preamble added. |
| 2025-11-23 | 9.3.1 Legislative: Das SOLAR PARLAMENT                               | Drafted | Subsection on the SOLAR PARLIAMENT as the legislature of the SOLAR ALLIANCE translated; YAML preamble added. |
| 2025-11-23 | 9.3.2 Exekutive: Der ALLIANZRAT                                      | Drafted | Subsection on the ALLIANCE COUNCIL as the executive leadership of the SOLAR ALLIANCE translated; YAML preamble added. |
| 2025-11-23 | 9.3.3 Judikative: Die Raumrechtskammer                               | Drafted | Subsection on the independent Space Law Chamber as the judiciary of the SOLAR ALLIANCE translated; YAML preamble added. |
| 2025-11-23 | 9.3.4 Sicherheitskräfte: Orbitaler Zivilschutz & Notfallkoordination  | Drafted | Subsection on the SOLAR ALLIANCE security forces for orbital civil protection and emergency coordination translated; YAML preamble added. |
| 2025-11-23 | 9.3.5 Interplanetarer Rat für Lebensrechte                           | Drafted | Subsection on the Interplanetary Council for Rights of Life, covering dignity of life, biospheres and non-human intelligences in space, translated; YAML preamble added. |

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

