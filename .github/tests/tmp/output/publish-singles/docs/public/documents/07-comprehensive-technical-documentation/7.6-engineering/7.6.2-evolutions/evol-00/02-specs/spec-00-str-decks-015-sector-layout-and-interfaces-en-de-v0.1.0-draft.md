---
id: spec-00-str-decks-015-0001
title: DECK 015 sector layout and interfaces
version: 0.1.0
state: draft
evolution: EVOL-00
discipline: STR
system: DECKS
system_id: '015'
seq: '0001'
owner: structure-architecture
reviewers:
- safety-reactor
- operations-test
source_of_truth: true
supersedes: []
superseded_by: []
rfc_links: []
adr_links: []
cr_links: []
date: 2025-08-16
lang: en-de
history:
- date: 2025-09-03
  change: Spin law updated to 1 g @ DECK012; g-levels adjusted
geometry:
- paperwidth=210mm
- paperheight=297mm
- left=15mm
- right=15mm
- top=15mm
- bottom=15mm
header-includes:
- \usepackage{calc}
- \usepackage{enumitem}
- \setlistdepth{20}
- \usepackage{longtable}
- \usepackage{ltablex}
- \usepackage{booktabs}
- \usepackage{array}
- \keepXColumns
- \setlength\LTleft{0pt}
- \setlength\LTright{0pt}
---


# SPEC-00-STR-DECKS-015-sector-layout-and-interfaces-EN-DE-v0.1.0-DRAFT

**Project:** Sphere Space Station – Earth ONE (Ø 127.00 m)
**Evolution:** EVOL-00 • **Spin Law:** 1 g at r = 52.00 m (DECK 012) → ω = 0.43430 s⁻¹ ≈ 4.147 rpm
**Document Status:** DRAFT v0.1.0 • **Date:** 2025-08-16

---

## 0. Summary / Kurzfassung (EN/DE)

**EN:** DECK 015 is the **tank farm & thermal buffer deck** with secondary/tertiary loops, inert and oxidizer gas systems, and the cryogenic interface to hull-mounted pods. High g (~1.14–1.21 g) supports **phase settling** and hydrostatic stability; strict EX-zoning and radial relief ensure safety.

**DE:** DECK 015 ist das **Tank- & Thermik-Deck** mit Sekundär/Tertiär-Kühlkreisen, Inert- und Oxidatorgas-Systemen sowie der Kryo-Schnittstelle zu hüllenmontierten Pods. Die hohe g-Last (~1,14–1,21 g) begünstigt **Phasen-Settling** und hydrostatische Stabilität; strenge **EX-Zonierung** und **radiale Entlastung** sichern den Betrieb.

---

## 1. Scope & Purpose / Zweck und Geltung

- **EN:** Sector layout, interfaces, safety zoning, and OPS constraints for DECK 015 (tanks/thermal, gases, cryo interface).  
- **DE:** Sektor-Layout, Schnittstellen, Sicherheitszonen und OPS-Grenzen für DECK 015 (Tanks/Thermik, Gase, Kryo-Interface).

**Dependencies / Abhängigkeiten:** Global Geometry & Gravitation SPEC (EVOL-00), DECK 014 spec, station-wide EX-class rules & ICD.

---

## 2. Geometry & Environment / Geometrie & Umgebung

- **Radial band / Radialband:** **59.50–63.00 m** (Δr = 3.50 m)  
- **g-levels (ceiling→mid→floor):** **1.144 g → 1.178 g → 1.212 g**
- **Windows:** none / **Fenster:** keine (technical deck)

---

## 3. Sectorization & Access / Sektorierung & Zugänge

- **Sectors / Sektoren (12 × 30°):** A…L  
- **Radial bulkheads / Radiale Schotts:** at sector borders; **PT-A/PT-B** per criticality.  
- **Shafts / Schächte:** **HL-0/90/180/270**; **PAX** at ±22.5°, 67.5° …; **UTIL** dual rings.  
- **Relief / Entlastung:** **VENT** to space; **BOP** panels at designated sectors.

---

## 4. Sector Allocation (Functional) / Sektor-Belegung (Funktional)

| Sector | HZ | EN – Primary Function | DE – Primärfunktion | Notes / Hinweise |
|:-----:|:--:|------------------------|---------------------|------------------|
| **A** | 2 | Water buffer / heat-sink | Wasser-Puffer / Heat-Sink | 2× tanks ~150 m³; HX modules |
| **B** | 2 | Water storage (vertical) + N$_2$ blanket | Wasser-Großspeicher (vert.) + N$_2$-Blanket | Level/sampling, dikes |
| **C** | 2 | Borate/LiOH shield solution | Borat/LiOH-Puffer (Schild) | PH stations, containment |
| **D** | 2 | Secondary pump hall | Sekundär-Pumpenhalle | HL-90 access; accumulators |
| **E** | **3** | **Separated O$_2$/N$_2$ banks (EX)** | **Getrennte O$_2$/N$_2$-Bänke (EX)** | **VENT-015-E→Space**; gas headers |
| **F** | **3** | **Cryogenic interface (no storage)** | **Kryo-Schnittstelle (ohne Lager)** | Manifolds → hull pods; VENT |
| **G** | 2 | Water buffer / heat-sink | Wasser-Puffer / Heat-Sink | HL-180 access |
| **H** | **3** | **Inert gas central (N$_2$/Ar)** | **Inertgas-Zentrale (N$_2$/Ar)** | Mixing, sector valves |
| **I** | 2 | Heat-exchanger gallery (S) | Wärmetauscher-Galerie (S) | HX strings to hull headers |
| **J** | 2 | Pump racks (S/W) | Pump-Racks (S/W) | HL-270 access |
| **K** | 2 | Water shield ring | Wasser-Schildring | Ring tank ~250 m³; tie-in 014 |
| **L** | 2 | Inspection & service / decon | Inspektion & Service / Dekon | AL-C airlocks, workshop

**HZ classes:** 1 normal, **2 elevated**, **3 critical (EX/Cryo)**.

---

## 5. Interfaces / Schnittstellen

### 5.1 MECH
- Ring girder raster: **M20** on 015; tank saddles with restrainers; spill containment/dikes.
- **DE:** Ringträger-Raster **M20**; Tanksättel mit Haltern; Auffangwannen/Dämme.

### 5.2 PWR
- **DC-HV backbone** continues from 014 (DC-B1/B2); MCC panels at **D/J** pump nodes; UPS for valve/VENT/BOP actuation.
- **DE:** DC-Rückgrat aus 014; MCC in **D/J**; USV für Ventile/VENT/BOP.

### 5.3 THM
- **Secondary/Tertiary loops:** pump nodes **D/J**; HX galleries **I**; buffer tanks **A/G/K**.
- **DE:** Sekundär/Tertiär-Kreise über **D/J**; HX-Galerien **I**; Puffer **A/G/K**.

### 5.4 COM
- Red/Blue fiber rings; SAFE-bus monitoring for EX/Cryo sectors **E/F/H**.
- **DE:** Red/Blue-Ringe; SAFE-Bus-Überwachung in **E/F/H**.

### 5.5 GAS
- **O$_2$/N$_2$** separated banks (**E**); **N$_2$/Ar** inertization central (**H**); cryo manifolds (**F**) to hull pods.
- **DE:** **O$_2$/N$_2$** getrennt (**E**); **N$_2$/Ar** Inertisierung (**H**); Kryo-Manifolds (**F**).

---

## 6. Safety, Schotts & Relief / Sicherheit, Schotts & Entlastung

- **PT-A/PT-B** doors per HZ; **AL-C** airlocks at service entries.
- **VENT-015-E→Space** dedicated for EX zone; additional sector VENT lines **F/H**; **BOP** at **A/K** for tank overpressure scenarios.
- **DE:** Türen/Schleusen wie oben; **VENT** in EX-Zonen priorisiert; **BOP** hull-nah; keine tangentiale Entlastung.

---

## 7. Operations & Human Factors / Betrieb & HF

- **Exposure:** Category **D** (≤ 4 h) general; **E** (≤ 2 h) in **E/F/H**; slow head movement in high-g work.  
- **Wayfinding:** EX-zone markings, gas color codes, decon routes to **L**.  
- **DE:** Verweilen: **D** allgemein, **E** in **E/F/H**; klare EX-Markierungen; Dekon-Routen nach **L**.

---

## 8. Verification & Acceptance / Verifikation & Abnahme

- **Hydrostatic/Leak** tests on tanks; **N$_2$ blanket** integrity; level/pressure alarms.  
- **Pump N+1** failover, HX capacity tests; **VENT/BOP** functional drills.  
- **EX compliance** (detectors, interlocks) and **cryo line** integrity at **F**.  
- **DE:** Dichtheit, N$_2$-Blanket, Pumpen-Redundanz, VENT/BOP-Tests, EX/Cryo-Nachweise.

---

## 9. ICD & Naming / Bezeichner

- **Shafts:** `HL-0|90|180|270`, `PAX-22.5|…|337.5`  
- **Relief:** `VENT-015-<Sector>`, `BOP-015-<Sector>`  
- **Tanks:** `WTR-015-<Sector>-<Nr>`, **Gas banks:** `GAS-015-E-<O2/N2>-<Bank>`  
- **Cryo:** `CRYO-015-F-<LineID>`

---

## 10. Change Log / Änderungshistorie

- v0.1.0 (2025-08-16): Initial EVOL-00 tank/thermal layout, EX zoning, interfaces, OPS limits.