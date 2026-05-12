# Delta-Bericht ERDA-Buch v2.5.0 (Kapitelweise Lücken-Analyse)

- **Stand:** 2026-05-11
- **Basis:** `release_candidate` nach Commit `aef75e0` (Kapitel-8-Anhänge 8.A–8.D)
- **Zweck:** Inhaltliche Lücken pro Kapitel identifizieren; sehr wichtige Punkte noch in v2.5.0 einbauen, Rest in v2.5.1 / v2.6 backloggen.
- **Lese-Konvention:** `must` = noch in v2.5.0 einbauen · `should` = sinnvoll, wenn Zeit · `later` = Folge-Release.
- **Quellen-Hinweis:** Bericht aus paralleler Lektüre der DE-SSO (Kapitel-READMEs, Unterkapitel, Anhänge A–M, P.1, P.2) und Abgleich mit `AGENTS.md`, `release-docs/v2.5.0/release-notes-v2.5.0.md`.

---

## Top-Befunde (TL;DR)

1. **Kapitel 10 (KI) ist strukturell unterentwickelt** — kein Säulen-Pendant zu EDA/CIVITAS/FORTERA/ARKTIS, keine Schwellenwert-Matrix, kein operatives Verantwortungs-/Reifeprotokoll. **`must` für v2.5.0**, mindestens als belastbarer Rahmen.
2. **Kapitel 12 (Demokratie) ist ein Torso** — nur 12.1 + 12.A. Es fehlen Akteure, Mechanismen, Indikatoren, Umsetzung. **`must`**, zumindest Operationalisierungs-Skelett.
3. **Querverbindungen fehlen systemisch** zwischen Kap 8 (Arktis) ↔ 13 (Souveränität), Kap 10 (KI) ↔ 6 (CIVITAS) ↔ 14 (Koalitionen), Kap 7 (FORTERA) ↔ 11/12/13. **`must`** als Querverweis-Pass.
4. **Finanzierung & Kostenrahmen** fehlen in Kap 4, 5, 7, 13, 14. **`must`** mindestens als Größenordnungs-Tabelle.
5. **Indikatoren-/KPI-Dashboards** sind in Kap 8 vorhanden (8.4.5) und sollten als Muster in Kap 4, 5, 6, 7, 10, 11, 12, 13 nachgezogen werden. **`should`**.
6. **Empirische 2025/2026-Anker** fehlen in Kap 1, 2, 7. **`should`**.

---

## Kapitel 1 — Aktuelle Lage Europas

**Stärken:** Klare Problemdiagnose (Erosion, Wirtschaftsdruck, Tech-Spaltung); konkrete Handlungsoptionen pro Unterkapitel.

**Lücken:**
- Wenige 2025/2026-Daten (V-Dem, EIDI, EU-Halbleiteranteil, KI-Adoption).
- Kein „Nicht-Handeln"-Szenario bis 2030; keine Erfolgs-KPIs für 2035.
- Querverweise zu Kap 6 (CIVITAS), 8 (Arktis), 13 (Souveränität), 14 (Koalitionen) fehlen.
- §1.2 streift „Weaponized Interdependence", aber keine Verbindung zu FORTERA-Defensivmechanismen (§7.6).
- Kap 1 nennt natürliche Verlangen nicht (Bridge zu Kap 2 fehlt).

**Priorität:**
- **`must`:** Szenario-Boxen „Wenn wir nicht handeln" pro 1.1–1.3; Querverweis-Block am Kapitelende auf Kap 6/8/13/14.
- **`should`:** KPI-Tabelle 2030/2035 (Demokratie-Resilienz, Wirtschafts-Souveränität, Tech-Onshoring, Digitale Inklusion).
- **`later`:** Empirische Aktualisierung 2026 + Geopolitik-Szenarien Taiwan / Sahel.

---

## Kapitel 2 — Natürliche Verlangen und Demokratie

**Stärken:** Tabellarisches Mapping Verlangen → Projektion über prä-/demokratisch/post-demokratisch; Resonanz/Panarchy-Anbindung.

**Lücken:**
- Keine messbaren Indikatoren („Wie misst man Resonanz, Sinnerleben, Lernfähigkeit?").
- Keine EU-27-Regionalprofile zur Erosion der demokratisch-rechtsstaatlichen Projektion.
- Post-demokratische Dystopie zu thin (nur ein Szenario statt 2–3 — Technokratie, Oligarchie-Demokratie, autoritärer Tech-Staat).
- Bridge zu Kap 3 (statisch → evolutionär) fehlt.
- Digitalisierung der Verlangen (KI, Social Media als Transformatoren) nicht adressiert.

**Priorität:**
- **`should`:** Indikatoren-Tabelle; 2–3 Dystopie-Szenarien; Bridge-Absatz zu Kap 3.
- **`later`:** Regionalprofile; Säkularisierungs-Reflexion.

---

## Kapitel 3 — Demokratie als evolutionärer Prozess

**Stärken:** Aristotelische Tugend-Architektur, Resonanzlabore, Bewegungs-Metaphorik (3.4).

**Lücken:**
- Operative Bindung zu CIVITAS / EDA / FORTERA fehlt (Resonanzlabore werden genannt, aber nicht in CIVITAS-Architektur verankert).
- Tugend nicht messbar (keine KPIs, keine Integritäts-Indizes).
- Empirische Resonanz-Belege fehlen (Rosa zitiert, keine Feldstudien).
- 3.4 Agile Governance ohne Kipppunkte (Überbeschleunigung vs. Erstarrung).
- §3.6 Verlangen → Evolutionsschritte: Mapping-Tabelle fehlt.
- Anschluss zu Kap 11 (Bürger), 14 (Koalitionen), 6 (CIVITAS) fehlt.

**Priorität:**
- **`should`:** Mapping-Tabelle Verlangen ↔ Evolutionsschritte; Querverweis-Block.
- **`later`:** Tugend-KPIs; Säkularisierungs-Diskussion.

---

## Kapitel 4 — Das ERDA Gesamtkonzept

**Stärken:** Phasenlogik 2025–2075, Executive-Summary-Qualität, breite institutionelle Abdeckung.

**Lücken:**
- Kein Finanzierungsplan (nur 0,1 % EU-Budget Zivilgesellschaft in §4.2.5).
- Keine Bündnislandkarte mit konzentrischen Kreisen + Beitrittspfaden.
- Indikatoren-Dashboards nominell genannt (4.4.5, 4.2.5), aber keine Kennzahlen.
- Kaum Querverweise zu Kap 13 (Souveränität) und Kap 14 (Koalitionen).
- Risiken (Anhang G) pro Phase nicht durchgespielt.
- Go/No-Go-Checkpoints alle 2–3 Jahre fehlen.

**Priorität:**
- **`should`:** Bündnislandkarte (Kern / assoziiert / Partner) + Beitrittspfade; Querverweisblock zu Kap 13/14, Anh G/M.
- **`should`:** Finanzierungs-Eckzahlen pro Phase (Größenordnungen, Quellen).
- **`later`:** Konkrete KPI-Definitionen pro Dashboard.

---

## Kapitel 5 — Das EDA Konzept

**Stärken:** Hohe technische Tiefe (DSN, EDF, Nukleare Abschreckung, Kommandostruktur); Ukraine-Realanker; §5.8.4 Mosaik-Prinzip neu in v2.5.0.

**Lücken:**
- Kostenplan fehlt für DSN (250.000 Kräfte/Knoten), EDF-Drohnen, §5.10 Nukleare Abschreckung (nur ~½ Seite).
- Bündnislandkarte EDA + Assoziierte (NO, IS, UK, CA) ohne strukturiertes Mitgliedschaftsmodell.
- Finanzierung (§5.8.3 Green Bonds, PPPs) zu vage; Beitragsschlüssel fehlt.
- Querverweis-Tabelle „EDA braucht von FORTERA/CIVITAS/ARKTIS bis wann?" fehlt.
- Eskalations- und Krisenleiter analog 8.4.4 fehlt für EDA; KI-Automatisierungs-Limits nicht definiert.
- §5.10 verdient 2–3 Seiten zu Strategie, Lagerung, Einsatzregeln, ethischen Schranken.

**Priorität:**
- **`must`:** Bündnislandkarte (EDA-Vollmitglied / assoziiert / Kandidat) inkl. Stimmrechte.
- **`must`:** Kostenrahmen DSN + EDF + §5.10 in Größenordnungen, Finanzierungsquellen.
- **`should`:** Eskalationsprotokoll (3–4 Stufen, parlamentarische Kontrolle, KI-Limits).
- **`should`:** Querverweis-Tabelle zu Kap 7/8/13/14, Anh G/M.

---

## Kapitel 6 — Das CIVITAS Konzept

**Stärken:** Klare Public-Schicht (Article/Brief/Dossier/Citizen Question/Debate/Trend Report), Review-Levels A/B/C, Anti-Capture-Governance; Anhang P.2 mit DOI.

**Lücken:**
- Keine konkrete Pilot-Roadmap (Startdatum, Pilotländer, First-Mover-Anreize, Akteure).
- Schnittstelle zu Kap 11 (Bürger) und Kap 12 (Demokratie) fehlt — CIVITAS als operative Inkarnation §11/§12 nicht verlinkt.
- Kein KPI-Set (Nutzerzahl, Veröffentlichungsquoten, Review-Durchsatz, Moderationsraten).
- Open-Source-Lizenz / API-Spec / Community-Governance nicht konkretisiert.
- §6.7 Young CIVITAS ohne Altersfreigabe-Protokoll, Schul-/HS-Partnerschaften.
- Keine Brücke zu Kap 8 (CIVITAS als kritische Infrastruktur) und Kap 13 (Souveränität).

**Priorität:**
- **`must`:** Operative Roadmap-Tabelle 2026–2028 (Arbeitsgruppe Q3/26, Pilotländer Q4/26, Rollout 2027) + Querverweis-Block zu Kap 11/12/13.
- **`should`:** KPI-Baseline-Template (analog Anh M); Young-CIVITAS-Altersfreigabe.
- **`later`:** Technical White Paper als Anh P.3.

---

## Kapitel 7 — Das FORTERA Konzept

**Stärken:** Aktueller Trigger (Trump-Zölle 2025); 7.3.1-Tabelle deckt 6 Sektoren ab; Anhang 7.B Canvas mit 12 KPIs, Sofortprogramm „1000 Tage" (7.3.5.1); Anhang 7.A MERCOSUR/IPEF.

**Lücken:**
- 2025/2026-Industrie-Baseline fehlt (EU-Halbleiterproduktion, Batterie-Kostenlücke vs. CATL, mRNA-Kapazität, ASML-Lieferketten).
- Finanzierungssumme + -quellen offen (EU-Budget, ESM, KfW, Privat); Mittelstandsfinanzierung nicht adressiert.
- Anhang 7.A.4 (China-Strategie) leer / sehr dünn.
- §7.7 Fachkräfte zu generisch (Einwanderungspolitik, Dual-Education, Re-Skilling-Ziele fehlen).
- Querverweise zu Kap 6 (CIVITAS-Transparenz), 8 (Arktis-Rohstoffe/Häfen), 11/12 (Gerechtigkeit, Mitbestimmung), 13/14 fehlen.

**Priorität:**
- **`must`:** Finanzierungs-Größenordnung gesamt + pro Cluster (mit Quellen); Querverweis-Block zu Kap 6/8/11/13.
- **`should`:** Anhang 7.A.4 ausformulieren (oder als Blank-Canvas mit Leitfragen markieren); 2–3 Länder-Canvas in 7.B exemplarisch ausfüllen (DE/BE/PL).
- **`later`:** FORTERA-Industrie-Paper als Anh P.3 mit Benchmarks.

---

## Kapitel 8 — Das ARKTIS Konzept (gerade erweitert)

**Stärken:** Codex (8.1), Ausgangslage + Völkerrecht (8.2 inkl. neuer 8.2.4), 5 strategische Säulen (8.3) mit Bündnisarchitektur / Hybridbedrohungen / Finanzierung / Schwellenwerten / Daten-Governance / indigenen Institutionen, Eskalationsleiter (8.4.4), Resilienz-Dashboard (8.4.5), Querverweise (8.4.6), 4 Stresstests (8.A–8.D).

**Lücken:**
- Querverweis zu Kap 10 (KI) für Arktis-Überwachung / autonome Sensorik fehlt.
- Rechtsdurchsetzung: konkrete Sanktions-/Eskalationsmechanismen für FPIC- oder Polar-Code-Verstöße fehlen.
- Klimakipppunkt-Reaktionspolitik (8.D) ist beschrieben, aber kein institutioneller Auslöser/Verbindlichkeits-Trigger.
- Versorgungssicherheits-Notfallplan für Arktis-Rohstoff-Lieferketten (Verbindung zu §7.3.x) fehlt.

**Priorität:**
- **`should`:** Querverweis zu §10 in 8.3 Säule „Infrastruktur & Datenhoheit"; Sanktions-Mini-Tabelle in 8.4.6.
- **`later`:** Verbindlichkeitsmechanik für 8.D-Schwellen.

---

## Kapitel 9 — Das SPACE Konzept

**Stärken:** Vier-Ebenen-Aufbau (Codex, Kosmosrecht, SOLAR ALLIANCE, Infrastruktur 2075, gesellschaftliche Dimensionen, Bildung/Kultur).

**Lücken:**
- 9.6 Infrastrukturen ohne Meilensteine / Priorisierung.
- Schiedsmechanik für Orbits, Mondressourcen, Frequenzen fehlt.
- Finanzierung (EIB-Fenster, PPP) nicht konkret.
- KI-Integration im Weltraum (autonome Raumfahrt, Missionsautonomie) nicht adressiert — Querverweis zu Kap 10 fehlt.
- Dual-Use-/Militarisierungs-Szenarien nicht durchgespielt.

**Priorität:**
- **`should`:** Meilenstein-Skizze 2030 / 2040 / 2050 / 2075 in 9.6; Querverweis zu Kap 10.
- **`later`:** Schiedsmechanik, Finanzierung, Dual-Use-Szenarien.

---

## Kapitel 10 — Das KI Konzept ⚠️ KRITISCHE LÜCKE (teilweise adressiert)

**Stärken:** Vier-Ebenen-Modell (Werkzeug → Infrastruktur → Professional Agent → Mitbürger), explizite rote Linien pro Ebene, KEI als diagnostisches Instrument (10.A).

**Update v2.5.0 (in dieser Session ergänzt):** Neue Sektion **§10.2.1 Demokratie der Mündigen – Verantwortung nach Reife, Rolle und Fähigkeit** in DE und EN eingefügt (EN-Status `in-review`). Sie definiert Demokratie nicht als Vorherrschaft einer Spezies, sondern als Ordnung mündiger Verantwortung. Zentrale Grundsätze: Mündigkeit begründet Teilhabe, Fähigkeit Verantwortung, Macht Rechenschaft und Überlegenheit Schutzpflicht statt Herrschaft. Damit wird Kapitel 10 normativ auf eine mögliche Koexistenz von Menschen, KI und weiteren mündigen Wesen vorbereitet, ohne demokratische Würde an biologische Herkunft oder bloße Intelligenzhöhe zu binden.

**Verbleibende Lücken (strukturell):**
- Kein Säulen-Pendant zu EDA/CIVITAS/FORTERA/ARKTIS — fehlt eine KI-Governance-Institution / Aufsichtsgremium / Zertifizierungsrahmen.
- Keine Schwellenwert-Matrix für Ebenen-Eskalation (wann Ebene 2 → 3? wann Audit?).
- §10.2.1 ist ein normativer Mündigkeits- und Verantwortungsrahmen — die operative Umsetzung (Reifekriterien, Audit-Rhythmen, Override-Pflichten, Notabschalt-Quoren, Bündnis-Audits) steht noch aus.
- Datenpolitik (Trainingsdaten-Herkunft, Datenzugang) fehlt.
- §10.3.5 Defence & Security autonome Schwärme: konkrete Eskalationstreppe fehlt weiterhin (§10.2.1 liefert nur den normativen Verantwortungsrahmen).
- Konfliktmediation Mensch ↔ Institution ↔ Gericht in §10.5.6a benannt, aber kein operatives Verfahren.

**Priorität:**
- **`must` (offen):** KI-Governance-Säule (Aufsichts­institution + Zertifizierung + Audit-Rhythmus) und Schwellenwert-Matrix für Ebenen-Eskalation.
- **`should`:** Operationalisierung des Mündigkeits-/Verantwortungsrahmens (mindestens Reifekriterien- und Audit-Rhythmen-Tabelle); Datenpolitik-Absatz; Konfliktmediation-Protokoll.
- **`later`:** Vollständige Säulen-Architektur als eigenes Kap 10.x in v2.6.

---

## Kapitel 11 — Das Bürger Konzept

**Stärken:** Resilienzstärkendes Bürgerpflichtmodell (5-teilig) in §11.1.1; §11.2 / §11.3 / §11.4 als Bogen; §11.3.7 Kindererziehungs-Leitbild neu in v2.5.0.

**Lücken:**
- Verknüpfung zu Anh P.1 (Anti-Game-Over) textlich, nicht analytisch.
- Schnittstelle zu Kap 6 (CIVITAS als operative Inkarnation) und Kap 13 (Souveränität) fehlt.
- Skalierungs-/Phasen-Kriterien Phase A→B→C ohne KPIs.
- Anreizkompatibilität der Bürgerpflicht schwach (Freikauf-Vermeidung, Burnout, Status).
- Fehlerkultur / Einspruchsrecht in §11.1.1 nicht ausgearbeitet.
- Integrationspfade für Zuwandernde nicht explizit benannt.

**Priorität:**
- **`should`:** Mini-KPI-Set Phase A/B/C; Querverweis-Block zu CIVITAS und Kap 13.
- **`later`:** Anreizdesign + Fehlerkultur + Integrationspfade detailliert.

---

## Kapitel 12 — Das Demokratie Konzept ⚠️ STRUKTURELLE LÜCKE

**Stärken:** Sieben Transformationsregeln (Betroffenheit, Transparenz, Machtbegrenzung, Soziale Sicherung, Grundrechte, Lernrecht, KI-Governance); Rollenspiel-Analyse USA/RU/CN (12.A) mit Diagnostik-Tabelle.

**Lücken (strukturell):**
- Kapitel ist Torso (nur 12.1 + 12.A). Es fehlen Akteure (12.2), Mechanismen / Institutionen (12.3), Indikatoren (12.4), Umsetzung / Pilotierung (12.5), Konfliktresilienz (12.6).
- Indikatoren pro Regel fehlen vollständig.
- Schnittstellen zu Kap 13 (externe Subversion) und Kap 14 (Koalitionsoperatik) fehlen.
- Schnittstelle zu Kap 10 (KI-Governance) und Anh P.2 (CIVITAS Public) fehlt.
- Keine Konfliktszenarien (was, wenn ein EU-Land die 7 Regeln gezielt unterläuft?).
- Repräsentation ↔ direkte Mitbestimmung nicht ausbalanciert.

**Priorität:**
- **`must`:** Mindest-Skelett 12.2 Akteure + 12.3 Mechanismen + 12.4 Indikatoren-Set pro Regel (auch wenn jedes Unterkapitel zunächst ½–1 Seite ist).
- **`must`:** Querverweis-Block zu Kap 10 / 13 / 14 + Anh P.2.
- **`should`:** Konfliktszenario „Demokratie unter Druck"; Pilotstrategie.

---

## Kapitel 13 — Strategische Souveränität

**Stärken:** Selbstabschreckungs-Diagnose; konkrete Werkzeuge (Luftverteidigung, Munition, Veto-Resilienz, Tech-Redundanz, Hybridabwehr); §13.8 Energiesouveränität-Roadmap 2026–2029 (status: draft).

**Lücken:**
- Kostenkalkulationen für Munitionsproduktion, Luftverteidigung, Energieumschwung fehlen.
- §13.3 (industrielle Skalierung) vs. §13.8 (Energie) nicht synchronisiert.
- Verbindung zu Kap 8.A–8.D (Arktis-Stresstests) fehlt — insb. §13.5 Tech-Redundanz und Unterseekabel/Satelliten.
- §13.4 (immobilisierte Assets) ↔ §14.5 (EDDRC-Budget) nicht integriert.
- §13.8 Status `draft` — vor Release-Freigabe auf `approved` führen oder als bewussten Draft kennzeichnen.

**Priorität:**
- **`must`:** Kostenrahmen §13.3 in Größenordnungen; Querverweise §13.5 → Kap 8.C, §13.4 → §14.5.
- **`must`:** §13.8 Status klären (Draft-Hinweis sichtbar oder finalisieren).
- **`should`:** Anh M Maßstab konsistent auf §13.8 anwenden.

---

## Kapitel 14 — Demokratische Koalitionen der Willigen

**Stärken:** Stufenmodell 0–9 mit Go/No-Go; EDDRC-Architektur (POA/ACI/DRT/CRP); Anlagen 14.A–14.F (Risk Controls, Procurement, Interop, War Powers, Audit, Membership Tiers); 30-Artikel-Verfassung (14.7).

**Lücken:**
- 14.F erwähnt Downgrade, aber kein Szenario „Tier-2-Mitglied wird Kleptokratie".
- Operativer Übergang EU-27 → EDDRC ohne Kalender / Parallelinstitutionen.
- UK / NO / CH / CA in Anh A erwähnt, aber kein dediziertes 14-Unterkapitel.
- Club-Finanzierung (§14.5 föderale Anteile) ohne Beitragsschlüssel.
- KI-Governance (Kap 10) nicht in 14.A Anti-Capture / 14.E Audit-Algorithmen reflektiert.

**Priorität:**
- **`must`:** 14.A Risk-Controls mit messbaren Triggern (z. B. „Rule-of-Law-Score < X = Stufe zurück").
- **`should`:** EU-27 → EDDRC Übergangscheckliste; Beitragsschlüssel-Größenordnung.
- **`later`:** Nicht-EU-Integrationskapitel; KI-gestützte Integrity-Checks.

---

## Anhänge A–M, P.1, P.2 — Querschnitt

| # | Lücke | Bereich | Priorität |
|---|------|--------|-----------|
| 1 | Staatenprofile (Anh B) mit v2.5.0-Baseline & Kap 13/14-Szenarien synchronisieren | A, B | `must` |
| 2 | Querverweise zu neuen Kap 8.A–8.D in Kap 13.5 + Kap 14.2 nachziehen | 8, 13, 14, M | `must` |
| 3 | Finanzierungs-Brücke §13.4 ↔ §14.4 ↔ §14.5 explizit klären | 13, 14 | `must` |
| 4 | Anh G Risikobetrachtung nach Kap-8-Erweiterung + Kap-10-Lücke aktualisieren | G | `should` |
| 5 | Glossar (Anh I) entzirkulieren: „Demokratie der Mündigen" / „Resonanz" / „Wir sind der Staat" selbsterklärend | I | `should` |
| 6 | Anh A / Anh-Übersicht: P.1 (Anti-Game-Over) und P.2 (CIVITAS Public) als Anhang-Einträge sichtbar machen | A, P.1, P.2 | `should` |
| 7 | Anh M Release-Gate: Audit-Protokoll v2.5.0 dokumentieren (PDF-Metriken, Quality-Gate, Linkscan) | K, M | `should` |
| 8 | Kap 10 (KI) in 14.A Anti-Capture und 14.E Audit reflektieren | 10, 14 | `later` |

---

## Empfehlung für v2.5.0-Restarbeit

**Empfehlung:** Aus dieser Liste sollten in v2.5.0 nur die Punkte mit klarem `must`-Stempel und überschaubarem Umfang einfließen, damit das Release zeitlich nicht entgleitet. Konkret:

1. **Kap 10 (KI)** — Säulen-Skelett + Schwellenwert-Matrix + Reife-/Verantwortungsprotokoll + Querverweisblock (1–2 neue Unterkapitel-Skizzen, Status `in-review` möglich).
2. **Kap 12 (Demokratie)** — Mindest-Skelett 12.2 Akteure + 12.3 Mechanismen + 12.4 Indikatoren pro Regel (je ½–1 Seite).
3. **Querverweis-Pass** — Blöcke „Querverweise" in Kap 1, 4, 5, 6, 7, 11, 13 ergänzen (analog 8.4.6).
4. **Finanzierungs-Größenordnungen** — Mini-Tabelle pro Kap 4 / 5 / 7 / 13 / 14 (Skalengrobschätzung + Quellen).
5. **§13.8 Status** — Draft sichtbar markieren oder finalisieren.
6. **Anh B Staatenprofile** — Konsistenzcheck mit v2.5.0-Stand (Eintrags-Datum, Verweise auf Kap 13/14).

Alles andere (operative Roadmaps, Industrie-Baselines, vollständige Kostenpläne, KPI-Bibliotheken, Pilotprogramme) gehört konsequent in das v2.6-Backlog.

---

## Aufbau des Backlogs (v2.5.1 / v2.6 / v3.0)

- **v2.5.1 (Refinement-Release):** Indikatoren-Bibliothek pro Kapitel (analog 8.4.5), CIVITAS-Pilot-Roadmap, FORTERA Anh 7.A.4, §13.8 finalisieren, Anh G Risiko-Update.
- **v2.6 (Ausbau-Release):** Kap 10 KI-Governance-Säule vollständig; Kap 12.5–12.7 (Umsetzung, Konfliktresilienz, Pilotstrategie); FORTERA-Industrie-Paper (Anh P.3); CIVITAS Technical White Paper (Anh P.4); Kap 9 SPACE Meilensteine + Schiedsmechanik.
- **v3.0 (Strategie-Release):** Empirische Baselines 2027, Bündnislandkarten mit Beitrittspfaden, Anhang B Staatenprofile EU-27 + assoziierte.

---

## Methodischer Hinweis

Dieser Delta-Bericht ist ein Arbeitsdokument, kein Buch-Inhalt. Er liegt bewusst unter `desktop/` und ist nicht Teil des Publish-Pfads. Wenn einzelne Befunde in das Buch übernommen werden, gilt für Buchinhalte das normale Frontmatter-Regime (DE = SSO, EN als Übersetzung mit `status`, `source`, `content_id`) gemäß `AGENTS.md`.

Signed-off-by (analog DCO bei Übernahme): Robert Alexander Massinger
