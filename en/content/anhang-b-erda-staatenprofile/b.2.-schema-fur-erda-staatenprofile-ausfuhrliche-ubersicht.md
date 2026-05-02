---
content_id: erda.book.anhang.b.erda.staatenprofile.b.2.schema.fur.erda.staatenprofile.ausfuhrliche.ubersicht
lang: en
source: de/content/anhang-b-erda-staatenprofile/b.2.-schema-fur-erda-staatenprofile-ausfuhrliche-ubersicht.md
status: draft
---

# B.2 ERDA State Profile Template (v5, Technical Sample)

_**Technical sample template for ERDA state profiles (v5)**_

> **Editorial note:** This section deliberately documents a technical sample template. Placeholders mark fields that must be replaced in concrete country profiles. The front-matter keys remain technical so that the template stays compatible with repository files and tooling.

### 1. 🌍 ERDA State Profile – Technical sample template (v5, 2026)

```markup
---
description: "State: {{country-code}}, Date: {{YYYY-MM-dd}}, Responsible Author: {{author}}, if from official or institute: Legal Responsible [Author, Institute, Government]: {{official}}"
country: "{{country-code}}"
date: "{{YYYY-MM-dd}}"
author: "{{author}}"
legal_responsible: "{{official}}"
layout: "ERDA-State-Profile-v5"
version: "1.0"
---

# {{country-code}} – State Profile {{Country}}


## 1. Overview (meta)

* Official name:
* Geographical location (continent, region):
* Population (as of 2025):
* System of government & constitutional status (as of 2025):
* ERDA status [associate | member | accession candidate | sovereign partner]:
* Future role in the ERDA network (e.g. Arctic hub, education nation, cyber hub, cultural mediator):

## 2. Demography & society

* Population projections (2050 / 2075):
* Age structure (median age, youth share %, old-age dependency ratio):
* Urbanisation rate (%):
* Average education (school years, higher-education rate %, STEM subjects %):
* Life expectancy (years):
* Net migration per year (average 2025–2075):
* Social cohesion (satisfaction index [0–10], trust in democracy [%]):

## 3. Economy & innovation

* Gross domestic product (real GDP, today / 2050 / 2075 in bn EUR):
* GDP per capita (EUR):
* Top-3 key industries:
* Share of automation & digitalisation (today / 2050 in %):
* Research and innovation quota (% of GDP):
* Patents per year (trend, average):
* Member of FORTERA trade alliances [Yes | No]:
* Member of the Democracy Trade Network [Yes | No]:
* Use of EHAM+ (trade defence) [0–10]:

### 3.1 Infrastructure autonomy

* Production sovereignty in strategic sectors:
  * Energy [☑ | ☐]
  * IT/cloud [☑ | ☐]
  * Defence [☑ | ☐]
  * Food [☑ | ☐]
  * Satellite communication (IRIS²) [☑ | ☐]
  * Quantum technology [☑ | ☐]
  * Autonomous logistics systems [☑ | ☐]

## 4. Resource profile

### Natural resources

* Land area (km²):
* Sea area (if relevant, km²):
* Strategic raw materials (e.g. lithium, rare earths, water):
* Renewable energy potentials (solar, wind, geothermal, hydro):
* Share of biodiversity & protected areas (% of territory):
* Sustainability indicators (CO₂ emissions per capita, recycling rate, material consumption per capita):

### Social resources

* Volunteering & community culture (index [0–10]):
* CIVITAS participation index [0–10]:
* Health system (accessibility [0–10], prevention [0–10]):

### Political resources

* Constitutional adherence [Yes | No]:
* Instruments of direct democracy [available | partial | not available]:
* Democracy quality index (Freedom House or similar [0–100]):
* Citizen participation rate (local/national) [%]:
* Rule-of-law index [0–10]:
* International trust values [0–10]:

## 5. Security & strategic role (EDA)

* Military potential:
  * DSN-capable [☑ | ☐]
  * Cyber command [☑ | ☐]
  * Early-warning system [☑ | ☐]
* Defence expenditure (% of GDP):
* Role in the Arctic/North Sea/Atlantic area (description, optional):
* Role in the Central/Eastern/Western Europe area (description, optional):
* Role in the Southern Europe/Africa/Asia area (description, optional):
* Role in the global/Solar Alliance area (description, optional):
* Civil resilience programmes [available | partial | not available]:
* Drone/space/AI capacities [available | partial | not available]:

### 5.1 Arctic strategy & planetary responsibility (optional for Arctic states)

* Integration into EDA DSN North Sea [Yes | No]:
* Participation in the Arctic Resilience Observatory [Yes | No]:
* Implementation of the Arctic Democracy Mining Act [Yes | No]:
* Partnerships with indigenous communities [Yes | No]:

## 6. Cultural identity & soft power

* Languages / indigenous cultures:
* UNESCO World Heritage / cultural sites (number):
* Creative industries (strength in music, film, design [0–10]):
* International visibility (Olympics, Nobel prizes, etc.):
* Role of culture as a mediation factor in democratic networks [0–10]:

## 7. Development path (2025–2075)

### Scenario development

* Status 2025 (short assessment):
* Best case 2050/2075 (optimistic goals & advantages):
* Base case 2050/2075 (realistic development):
* Worst case 2050/2075 (potential risks, critical developments & proactive responses):

### Role in the ERDA Vision 2075

* Contribution to a post-scarcity economic order:
* Democratic resilience (social, cultural, ecological):
* Exemplary impact on other states/regions:

## 8. Narrative & attractiveness

* Core message (sample placeholder): "{{Country}} shows that ..."
* Examples of strong, effective narratives and invitations:
* Self-efficacy: (How do citizens help shape outcomes?)
* Future dignity: (What provides identity & pride?)
* Invitation to other states & citizens: (What signal does the profile send?)

## 9. Key indicators (short form)

| Indicator                            | 2025 | 2050 | 2075 | EU average 2024 (benchmark) |
| ------------------------------------ | ---- | ---- | ---- | --------------------------- |
| GDP (bn EUR)                         |      |      |      |                             |
| Population                           |      |      |      |                             |
| Share of renewable energy (%)        |      |      |      |                             |
| Life expectancy (years)              |      |      |      |                             |
| Education rate (%)                   |      |      |      |                             |
| AI capacity [0–10]                   |      |      |      |                             |
| Civil-society index [0–10]           |      |      |      |                             |
Notes: (n/b) – not available (why?); (p) – projection (by whom?).

## 10. Snapshot: "{{Country}} at a glance" (sample)

A short, emotionally engaging summary of the key points, strengths and distinctive features for a broad audience.

## 11. Sources & modelling

### 11.1 ℹ️ General

* **Statistics:** distinguish between national (statistics offices) and international (Eurostat, World Bank) data sources; base year 2020 for all projections.
* **Modelling assumptions for economic development:** GDP growth (2.0% p.a.), inflation (1.5% p.a.), demographic change (national population projections 2030).
* **Energy potentials:** use IEA (2024) and Fraunhofer ISE (2023) studies with defined expansion pathways to 2050.
* **Innovation & education:** indicators such as research quota (3% of GDP) and education spending (OECD data) as drivers in the projections.
* **Democracy & rule of law:** ranking values (Freedom House, Rule of Law Index, Bertelsmann Stiftung).
* **Sustainability & resource indicators:** ecological footprint (Global Footprint Network), SDG indicators (UN), material efficiency (IEA).

### 11.2 📎 Sources & references
(DIN ISO 690:2013-10!)
Example corporate author
1. Federal Statistical Office. 2023. "Population projection to 2060". Wiesbaden: Destatis. [online] available at: <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Bevoelkerungsvorausberechnung/_inhalt.html> (last accessed 2025-06-09).

Example journal article
2. Müller, Anna; Schmidt, Peter. 2022. "Impacts of demographic change on the economy", *Journal für Wirtschaftsprognosen*, 15(2), pp. 45–62.

Example database/website
3. International Energy Agency. 2024. *World Energy Outlook 2024*. [online] available at: <https://www.iea.org/reports/world-energy-outlook-2024> (last accessed 2025-06-09).

### 11.3 🛠️ Modelling & assumptions

(Sample with example data)
1. Economic projections 2050–2075
* Base year: 2020; parameters: GDP growth 2.0% p.a., inflation 1.5% p.a., demographics cf. 11.1.
* Sources: Eurostat, World Bank.

(Sample with example data)
2. AI capacities
* Assumption: computing power doubles every three years.
* Source: [add a concrete specialist source relevant to the topic, e.g. Eurostat, IEA or a national statistics office].

(Sample with example data)
3. Infrastructure autonomy
* Goal: 80% renewable energy supply generated domestically.
* Data basis: Fraunhofer ISE, GIS modelling.

(Sample with example data)
4. Democracy and participation values
* Indicators: Freedom House score, CIVICUS Monitor.
* Base value 2020; assumption: annual improvement by 0.5 points.

(Sample with example data)
5. Energy potentials
* Scenarios: moderate vs. ambitious.
* Solar PV potential: 150 GWp (moderate), 300 GWp (ambitious).
* Sources: BMWK, IEA.

## 12. 🤝 Participation welcome
This profile is based on publicly accessible and modelled data. Representatives of the respective country and interested specialist bodies are warmly invited to contribute their own perspectives, additions and updates – to build a shared picture of a resilient and democratic future for Europe.

### 12.1 Last responsible points of contact
Author: ERDA Book editorial team
Contact: ERDA Book editorial team
Last update: 2026-01-08
```

**Note on technical notation:** The metadata keys `country`, `date`, `author`, `legal_responsible`, `layout` and `version` intentionally remain technical so that this sample can be reused directly in the repository.

#### 2. Formatting, completion & collaboration notes

* **Link formatting:** use `[Title](URL)` for online sources and `[Title](./path-to-file.md)` for internal references.
* **In-text links:** feel free to add clickable links for online readers. Add a footnote reference for **each in-text link**, e.g. `[Title](URL)[1]`, with the corresponding citation in the sources section.
* **Group sources:** arrange citations in the sources section by topic – e.g. "Demography", "Economy" or "Security".
* **Citation rules:** follow the **DIN ISO 690:2013-10** guidelines consistently.
* **Hypothetical sources:** clearly label any hypothetical or model-based references with the addition **"(hypothetical)"**.
* **Invitation to contribute:** states and research institutions are **warmly invited** to submit their own profiles based on this template or add to existing ones.
* **Note:** this profile serves **as a fair and appealing self-portrayal of each country**. It considers both potential and realistic challenges. Only in justified exceptional cases ("no one else will do it") should a profile be created, altered or deleted without the respective country’s official mandate.
