# B.2. Schema für ERDA-Staatenprofile (v5, technisches Muster-Template)

_**Technisches Muster-Template für ERDA-Staatenprofile (v5)**_

> **Redaktioneller Hinweis:** Dieser Abschnitt dokumentiert bewusst ein technisches Muster-Template. Platzhalter markieren Felder, die in konkreten Länderprofilen zu ersetzen sind. Die Frontmatter-Felder bleiben aus Gründen der Tool-Kompatibilität in technischer Notation.

### 1. 🌍 ERDA-Staatenprofil – technisches Muster-Template (v5, 2026)

```markup
---
description: "Staat: {{country-code}}, Datum: {{YYYY-MM-dd}}, verantwortliche Redaktion: {{author}}, rechtlich verantwortliche Stelle: {{official}}"
country: "{{country-code}}"
date: "{{YYYY-MM-dd}}"
author: "{{author}}"
legal_responsible: "{{official}}"
layout: "ERDA-State-Profile-v5"
version: "1.0"
---

# {{country-code}} - Staatenprofil {{Land}}


## 1. Überblick (Meta)

* Offizieller Name:
* Geografische Lage (Kontinent, Region):
* Bevölkerung (Stand 2025):
* Regierungsform & Verfassungsstatus (Stand 2025):
* ERDA-Status \[assoziiert | Mitglied | Beitrittskandidat | souveräner Partner]:
* Zukünftige Rolle im ERDA-Netzwerk (z.B. Arktisknoten, Bildungsnation, Cyberhub, Kulturvermittler):

## 2. Demografie & Gesellschaft

* Bevölkerung Prognose (2050 / 2075):
* Altersstruktur (Medianalter, Jugendanteil %, Altenquotient):
* Urbanisierungsgrad (%):
* Durchschnittliche Bildung (Schuljahre, Hochschulquote %, MINT-Fächer %):
* Lebenserwartung (Jahre):
* Migrationssaldo pro Jahr (Durchschnitt 2025–2075):
* Soziale Kohäsion (Zufriedenheitsindex \[0–10], Demokratievertrauen \[%]):

## 3. Wirtschaft & Innovation

* Bruttoinlandsprodukt (BIP real, heute / 2050 / 2075 in Mrd. EUR):
* BIP pro Kopf (EUR):
* Top-3 Schlüsselindustrien:
* Anteil Automatisierung & Digitalisierung (heute / 2050 in %):
* Forschungs- und Innovationsquote (% des BIP):
* Patente pro Jahr (Trend, Durchschnitt):
* Mitglied in FORTERA-Handelsallianzen \[Ja | Nein]:
* Mitglied im Democracy Trade Network \[Ja | Nein]:
* Nutzung von EHAM+ (Handelsabwehr) \[0–10]:

### 3.1 Infrastrukturautarkie

* Produktionssouveränität in strategischen Sektoren:
  * Energie \[☑ | ☐]
  * IT/Cloud \[☑ | ☐]
  * Verteidigung \[☑ | ☐]
  * Ernährung \[☑ | ☐]
  * Satellitenkommunikation (IRIS²) \[☑ | ☐]
  * Quantentechnologie \[☑ | ☐]
  * Autonome Logistiksysteme \[☑ | ☐]

## 4. Ressourcenprofil

### Natürliche Ressourcen

* Landfläche (km²):
* Meeresfläche (falls relevant, km²):
* Strategische Rohstoffe (z.B. Lithium, Seltene Erden, Wasser):
* Erneuerbare Energiepotenziale (Solar, Wind, Geothermie, Wasser):
* Anteil Biodiversität & Schutzgebiete (% der Fläche):
* Nachhaltigkeitskennzahlen (CO₂-Ausstoß pro Kopf, Recyclingquote, Materialverbrauch pro Kopf):

### Soziale Ressourcen

* Ehrenamt & Gemeinschaftskultur (Index \[0–10]):
* CIVITAS-Partizipationsindex \[0–10]:
* Gesundheitssystem (Zugänglichkeit \[0–10], Prävention \[0–10]):

### Politische Ressourcen

* Verfassungsbindung \[Ja | Nein]:
* Direkte Demokratieinstrumente \[Vorhanden | Teilweise | Nicht vorhanden]:
* Demokratiequalitätsindex (Freedom House oder vergleichbar \[0–100]):
* Bürgerpartizipationsquote (lokal/national) \[%]:
* Rechtstaatlichkeitsindex \[0–10]:
* Internationale Vertrauenswerte \[0–10]:

## 5. Sicherheit & Strategische Rolle (EDA)

* Militärisches Potenzial:
  * DSN-geeignet \[☑ | ☐]
  * Cyberkommando \[☑ | ☐]
  * Frühwarnsystem \[☑ | ☐]
* Verteidigungsausgaben (% des BIP):
* Rolle im Arctic/Nordmeer/Atlantik-Raum (Beschreibung, optional):
* Rolle im Mitteleuropa/Osteuropa/Westeuropa-Raum (Beschreibung, optional):
* Rolle im Südeuropa/Afrika/Asien-Raum (Beschreibung, optional):
* Rolle im Globalen/Solar Alliance-Raum (Beschreibung, optional):
* Zivile Resilienzprogramme \[Vorhanden | Teilweise | Nicht vorhanden]:
* Drohnen-/Raumfahrt-/KI-Kapazitäten \[Vorhanden | Teilweise | Nicht vorhanden]:

### 5.1 Arktisstrategie & Planetare Verantwortung (optional für Arktis-Staaten)

* Integration in EDA-DSN Nordmeer \[Ja | Nein]:
* Beteiligung am Arctic Resilience Observatory \[Ja | Nein]:
* Umsetzung Arctic Democracy Mining Act \[Ja | Nein]:
* Partnerschaften mit indigenen Gemeinschaften \[Ja | Nein]:

## 6. Kulturelle Identität & Soft Power

* Sprachen / Indigene Kulturen:
* UNESCO-Welterbe / Kulturstätten (Anzahl):
* Kreativwirtschaft (Stärke in Musik, Film, Design \[0–10]):
* Internationale Sichtbarkeit (Olympische Spiele, Nobelpreise, etc.):
* Rolle der Kultur als Vermittlungsfaktor in Demokratienetzwerken \[0–10]:

## 7. Entwicklungspfad (2025–2075)

### Szenario-Entwicklung

* Status 2025 (kurze Lageeinschätzung):
* Best Case 2050/2075 (optimistische Ziele & Vorteile):
* Base Case 2050/2075 (realistische Entwicklung):
* Worst Case 2050/2075 (potenzielle Risiken, kritische Entwicklungen & proaktive Lösungsansätze):

### Rolle in der ERDA-Vision 2075

* Beitrag zur Post-Knappheitsökonomischen Ordnung:
* Demokratische Resilienz (sozial, kulturell, ökologisch):
* Exemplarische Wirkung auf andere Staaten / Regionen:

## 8. Narrative & Anwerbewirkung

* Kernbotschaft (Beispiel-Platzhalter): „{{Land}} zeigt, dass ...“
* Beispiele für starke, wirkungsvolle Narrative und Einladungen:
* Selbstwirksamkeit: (Wie gestalten Bürger:innen mit?)
* Zukunftswürde: (Was verleiht Identität & Stolz?)
* Einladung an andere Staaten & Bürger:innen: (Welches Signal sendet das Profil?)

## 9. Kennzahlenübersicht (Kurzform)

| Indikator                             | 2025 | 2050 | 2075 | EU-Durchschnitt 2024 (Benchmark) |
| ------------------------------------- | ---- | ---- | ---- | -------------------------------- |
| BIP (Mrd. EUR)                        |      |      |      |                                  |
| Bevölkerung                           |      |      |      |                                  |
| Anteil Erneuerbare Energien (%)       |      |      |      |                                  |
| Lebenserwartung (Jahre)               |      |      |      |                                  |
| Bildungsquote (%)                     |      |      |      |                                  |
| KI-Kapazität [0–10]                   |      |      |      |                                  |
| Zivilgesellschaftlicher Index [0–10]  |      |      |      |                                  |
Hinweise: (n/b) - N/B nicht belegt (warum?), (p) - Prognose (wer?)

## 10. Kurzfassung: „{{Land}} auf einen Blick“ (Muster)

Kurze, emotional ansprechende Zusammenfassung der wichtigsten Punkte, Stärken und Besonderheiten für breites Publikum.

## 11. Quellen & Modellierungen

### 11.1 ℹ️ Allgemeines

* **Statistik:** Unterscheidung zwischen nationalen (Statistisches Bundesamt) und internationalen (Eurostat, Weltbank) Datenquellen; Basisjahr 2020 für alle Projektionen.
* **Modellannahmen zur Wirtschaftsentwicklung:** Annahmen zu BIP-Wachstum (2,0 % p.a.), Inflation (1,5 % p.a.), demografische Veränderungen (Statistisches Bundesamt, Bevölkerungsvorausschätzung 2030).
* **Energiepotenziale:** Nutzung von IEA (2024) und Fraunhofer ISE (2023) Studien mit definierten Ausbaupfaden bis 2050.
* **Innovation & Bildung:** Indikatoren wie Forschungsquote (3 % des BIP) und Bildungsausgaben (OECD-Daten) als Treiber in den Projektionen.
* **Demokratie & Rechtsstaatlichkeit:** Ranking-Werte (Freedom House, Rule of Law Index, Bertelsmann Stiftung).
* **Nachhaltigkeits- und Ressourcenindikatoren:** Ecological Footprint (Global Footprint Network), SDG-Indikatoren (UN), Materialeffizienz (IEA).

### 11.2 📎 Verwendete Quellen & Verweise
(DIN ISO 690:2013-10!)
Beispiel Corporate Author
1. Statistisches Bundesamt. 2023. "Bevölkerungsvorausschätzung bis 2060". Wiesbaden: Destatis. \[online] verfügbar unter: [https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/_inhalt.html](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/_inhalt.html) (Letzter Zugriff am 2025-06-09).

Beispiel Zeitschriftenartikel
2. Müller, Anna; Schmidt, Peter. 2022. „Auswirkungen des demografischen Wandels auf die Wirtschaft“, *Journal für Wirtschaftsprognosen*, 15(2), S. 45–62.

Beispiel Datenbank/Website
3. International Energy Agency. 2024. *World Energy Outlook 2024*. \[online] verfügbar unter: [https://www.iea.org/reports/world-energy-outlook-2024](https://www.iea.org/reports/world-energy-outlook-2024) (Letzter Zugriff am 2025-06-09).

### 11.3 🛠️ Modellierungen & Annahmen

(Muster mit Beispieldaten)
1. Wirtschaftliche Projektionen 2050–2075
* Basisjahr: 2020; Parameter: BIP-Wachstum 2,0 % p.a., Inflation 1,5 % p.a., Demografie s. 11.1.
* Quellen: Eurostat, Weltbank.

(Muster mit Beispieldaten)
2. KI-Kapazitäten
* Annahme: Rechenleistung verdoppelt sich alle 3 Jahre.
* Quelle: \[konkrete Fachquelle gemäß Themenbereich ergänzen, z. B. Eurostat, IEA oder nationale Statistik].

(Muster mit Beispieldaten)
3. Infrastrukturautarkie
* Ziel: 80 % erneuerbare Energieversorgung regional autark.
* Datenbasis: Fraunhofer ISE, GIS-Modellierung.

(Muster mit Beispieldaten)
4. Demokratie- und Beteiligungswerte
* Indikatoren: Freedom House Score, CIVICUS Monitor.
* Basiswert 2020; Annahme: jährliche Verbesserung um 0,5 Punkte.

(Muster mit Beispieldaten)
5. Energiepotenziale
* Szenarien: moderat vs. ambitioniert.
* Potenzial Solar PV: 150 GWp (moderat), 300 GWp (ambitioniert).
* Quellen: BMWi, IEA.


## 12. 🤝 Mitwirkung willkommen
Dieses Profil basiert auf öffentlich zugänglichen und modellierten Daten. Vertreter:innen des jeweiligen Landes sowie interessierte Fachstellen sind herzlich eingeladen, eigene Perspektiven, Ergänzungen und Aktualisierungen beizutragen – für ein gemeinsames Bild einer resilienten und demokratischen Zukunft Europas.

### 12.1 Letzte inhaltlich verantwortliche Ansprechpartner
Autor: ERDA Buch Redaktion
Kontakt: ERDA Buch Redaktion
Letzte Änderung: 2026-01-08
```

**Hinweis zur technischen Notation:** Die Metadatenfelder `country`, `date`, `author`, `legal_responsible`, `layout` und `version` bleiben bewusst technisch formuliert, damit dieses Muster direkt mit den Profil-Dateien im Repository kompatibel bleibt.

#### 2. Formatierungs-, Ausfüll- & Kollaborationshinweise

* **Linkformatierung:** Nutze `[Titel](URL)` für Internetquellen und `[Titel](./pfad-zur-datei.md)` für interne Verweise.
* **Fließtext-Links:** Setze im Fließtext gerne klickbare Links für Online-Leser:innen ein. Ergänze dabei **pro Fließtext-Link** eine Fußnotenreferenz, z. B. `[Titel](URL)[1]`, mit passender Zitation im Quellenabschnitt.
* **Quellen gruppieren:** Ordne die Zitate im Quellenabschnitt thematisch – z. B. unter „Demografie“, „Wirtschaft“ oder „Sicherheit“.
* **Zitierregeln:** Verwende durchgängig die Richtlinien der **DIN ISO 690:2013-10**.
* **Hypothetische Quellen:** Kennzeichne hypothetische oder modellhafte Verweise deutlich mit dem Zusatz **„(hypothetisch)“**.
* **Einladung zur Mitwirkung:** Staaten und Forschungseinrichtungen sind **herzlich eingeladen**, eigene Profile nach diesem Schema beizutragen oder bestehende zu ergänzen.
* **Hinweis:** Dieses Profil dient **als faire und attraktive Selbstdarstellung des jeweiligen Landes**. Es berücksichtigt sowohl Potenziale als auch realistische Herausforderungen. Nur in begründeten Ausnahmefällen („es tut sonst niemand“) sollte ein Profil ohne offizielle Beauftragung durch das jeweilige Land erstellt, verändert oder gelöscht werden.

