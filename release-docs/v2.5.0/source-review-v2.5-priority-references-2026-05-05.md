# Manuelle Quellenpruefung v2.5 - Prioritaetsreferenzen

**Datum:** 2026-05-05  
**Scope:** v2.5-Prioritaetsdateien aus `tmp/gitbook-worker-ai-v2.5.0/ai-references-de-v2.5-priority-files.txt`, ergaenzt um beim Review gefundene Strategic-Compass-Altverweise.  
**Methode:** technische HTTP-/DOI-Pruefung, gezielte Inhaltspruefung gegen Originalseiten, keine AI-Ergebnisse als Quellenwahrheit.  
**Status:** Freigabe mit Korrekturen; keine bekannte 404-Referenz im geaenderten Scope.

## Kurzbefund

Die priorisierten P.1-/11.3-/Anhang-E-/Anhang-L-Links waren technisch erreichbar, mit einer Ausnahme: der alte EEAS-Kurzlink `eeas.europa.eu/strategic-compass` lieferte 404. Dieser Link wurde in DE/EN Anhang E.7 durch die offizielle EEAS-Seite zum Strategic Compass ersetzt.

Zusaetzlich wurde ein sachlich fraglicher, aber technisch erreichbarer Strategic-Compass-Spiegel (`strategic-compass-european-union[.]com`) in DE/EN 11.1.1 durch die offizielle EEAS-Seite ersetzt. Kapitel 13.8 hatte keine externen Quellen, aber viele aktuelle Energiezahlen; deshalb wurden offizielle EU-/Eurostat-Quellen ergaenzt und nicht belegte bzw. veraltete Einzelzahlen korrigiert oder entschaerft.

## Technische Linkpruefung

| Referenz | Befund | Entscheidung |
|---|---|---|
| National Archives, Roosevelt Four Freedoms | HTTP 200; Inhalt bestaetigt Annual Message vom 6. Januar 1941 und Freedom-from-Fear-Passage | bleibt |
| Britannica, State monopoly on violence | HTTP 200; Inhalt bestaetigt Weber-Bezug und legitimes Gewaltmonopol | bleibt |
| Blavatnik School of Government, Trust and democracy | HTTP 200; Beitrag vom 10. Oktober 2025, Inhalt passt zu Vertrauen als demokratischer Infrastruktur | bleibt |
| DCAF, Parliamentary Oversight of the Security Sector | PDF HTTP 200; DCAF-Publikationsseite HTTP 200, 1. Januar 2003, Herausgeber Hans Born, Philipp Fluri, Anders Johnsson | bleibt; AI-Titelkorrektur verworfen |
| P.1 DOI `10.5281/zenodo.19244929` | DOI HTTP 200; Zenodo-API bestaetigt DOI, Titel, Datum 2026-03-27, Version 1.0.0, Lizenz `cc-by-4.0`, Creator Robert Alexander Massinger | bleibt |
| EEAS Strategic Compass Kurzlink | GET 404 | ersetzt durch offizielle EEAS-Seite |
| Strategic-Compass-Spiegel `strategic-compass-european-union[.]com` | HTTP 200, aber private Cyber-Risk-GmbH-Spiegelseite, nicht primaere EU-Quelle | ersetzt durch offizielle EEAS-Seite |
| DejaVu Fonts | HTTP 200; upstream bestaetigt Version 2.37 und freie Lizenz | bleibt |
| Twemoji Mozilla | GitHub HTTP 200; lokale TTF per SHA-256 identisch mit upstream `twemoji-colr` v0.7.0 | Kolophon von 0.6.0 auf 0.7.0 korrigiert |
| GitBook / Pandoc / TeX Live | HTTP 200; Werkzeugquellen erreichbar | bleibt |

## Kapitel 13.8 Energiesouveraenitaet

Kapitel 13.8 war kein klassischer Linkfehlerfall, sondern ein Quellenstaerke-Fall: Viele konkrete Zahlen und Programme standen ohne externe Quellen im Kapitel. Folgende Korrekturen wurden vorgenommen:

| Stelle | Befund | Korrektur |
|---|---|---|
| Solar-PV 406 GW 2025 | Europaeische Kommission / DG Energy bestaetigt 406 GW fuer 2025 und verweist auf SolarPower Europe | Quelle ergaenzt |
| Social Climate Fund | Offizielle Kommissionsseite bestaetigt Start 2026 und 86,7 Mrd. EUR fuer 2026-2032 | Quelle ergaenzt |
| LNG-/Gaslieferantenanteile | Eurostat-Datenstand Maerz 2026 nennt 2025: USA 56,0% LNG, Norwegen 52,1% gasfoermiges Erdgas | Q3-2025-Werte ersetzt |
| Speicherfuellziel | Regulation (EU) 2025/1733 setzt 90%-Ziel mit Zielkorridor 1. Oktober bis 1. Dezember | alte 1.-November-Formulierung ersetzt |
| Waermepumpen-/Solarthermie-Einzelzahlen | Im Review nicht als belastbarer offizieller Einzelwert nachgewiesen | exakte Zahlen entschaerft |
| Batterie-Booster-Zahl | Im Review nicht belastbar unter offizieller, erreichbarer Quelle nachgewiesen; ein EIB-Kandidatenlink lieferte 404 | durch allgemein belegte EU/EIB-Cleantech-Finanzierungsinstrumente ersetzt |

Verwendete Quellen im Kapitel: REPowerEU, DG Energy Solar energy, EPBD, Social Climate Fund, Eurostat energy imports, DG Energy gas storage, Net-Zero Industry Act, Critical Raw Materials Act und Clean Industrial Deal.

## Offene Hinweise

Kapitel 6 CIVITAS enthaelt im geprueften DE-Scope keine externen URL-/DOI-Zeilen. Die externe Quellenlage fuer CIVITAS P.2 ist separat durch `release-docs/v2.5.0/source-link-check-civitas-v2.5.0.md` geprueft. Fuer Kapitel 6 bleibt redaktionell zu entscheiden, ob explizite Querverweise auf Anhang P.2/DOI innerhalb einzelner Unterkapitel erwuenscht sind.

Die AI-Referenzberichte unter `tmp/` wurden nur als Suchhilfe genutzt. Fehlerhafte AI-Aussagen, insbesondere das Zukunftsjahr-/Zenodo-Problem und der falsche DCAF-Titel, wurden nicht uebernommen.