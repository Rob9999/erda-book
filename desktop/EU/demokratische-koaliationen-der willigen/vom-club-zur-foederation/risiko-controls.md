**Risiko-Controls**
Unten ist ein **Risiko-Control-Katalog** (Kontrollmechanismen) für deine föderale „European Defense Alliance → Föderation“-Architektur. Ich strukturiere es so, dass jedes Risiko **(a)** einen klaren **Trigger/Indikator**, **(b)** **präventive Controls**, **(c)** **detektive Controls** (Frühwarnung), **(d)** **reaktive Controls** (Sanktion/Recovery) und **(e)** **NoGo-Schwellen** hat.

---

## 1) Risiko-Controls als Master-Tabelle

| Risikofeld                              | Typische Failure Mode                                                         | Prävention (Prevent)                                                             | Detektion (Detect)                                                  | Reaktion (Respond)                                                     | NoGo-Schwelle                                            |
| --------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------- |
| **State Capture / Korruption**          | Ministerien/Behörden werden parteilich „übernommen“; Geld fließt in Netzwerke | strikte Transparenz (Lobby/Spenden), unabhängige Ernennungen, Procurement-Regeln | Audit, Forensik, Whistleblower-Schutz, Vermögensregister            | Mittelstopp, Amtsenthebung, Strafverfolgung, Stimmrechts-Suspendierung | systemische Korruption ohne effektive Strafverfolgung    |
| **Demokratie-Erosion**                  | Einschränkung Medien/NGOs, Wahlmanipulation                                   | Grundrechts-Charta, Wahlstandards, Medienpluralismus-Schutz                      | Wahlbeobachtung, Medien-Monitoring (transparent), Gerichtsreporting | Vertragsverletzungsverfahren, Rechte-Suspendierung, Neuwahl-Trigger    | Unfreie Wahlen / verfassungswidrige Notstände            |
| **Notstandsmissbrauch (Angstimperium)** | Notstand wird Dauerzustand, Grundrechte erodieren                             | enge Notstandsgründe, Sunset, Doppelmehrheit, Auto-Gerichtsreview                | öffentliche Notstandsberichte, Ombudsmann, Opposition-Inquiry       | automatisch auslaufen, gerichtliche Aufhebung, Entschädigung           | Notstand > X Tage ohne Doppelmehrheit + Gericht          |
| **Veto-/Blockade-Erpressung**           | Einzelstaat blockiert, um Zugeständnisse zu erzwingen                         | keine Einstimmigkeit im Kernclub; opt-in ohne veto                               | KPI: Entscheidungszeiten, Blockade-Logs                             | Bypass-Mechanismus, Ausschluss aus Programmen                          | Einstimmigkeit wird zur Norm                             |
| **Infiltration/Spionage/Influence Ops** | Leaks, Agentennetzwerke, politische Bestechung                                | Sicherheitsüberprüfung, Geheimschutz, Foreign-Agent-Transparenz                  | Counterintelligence, Anomalie-Detektion, Geldflüsse                 | Zugriffsentzug, Strafverfolgung, „clean rooms“, Sanktionen             | wiederholte systemische Leaks ohne Konsequenz            |
| **Militärische Fehlsteuerung**          | unklare Befehlskette; Einsätze ohne Mandat                                    | klare C2-Kette; Parlamentsmandat; Rules of Engagement                            | Einsatzberichte, unabhängige IG-Inspektion                          | Einsatzstopp, Verantwortlichkeit, Mandatsanpassung                     | Operationen ohne demokratische Rückbindung               |
| **Rüstungs-/Beschaffungsversagen**      | Kostenexplosion, Korruption, Lieferausfälle                                   | Standardisierung, Rahmenverträge, dual sourcing, offtake                         | Earned-Value, Lieferkettenmonitoring, QA-Audits                     | Vertragsstrafen, Neuvergabe, Notfallbeschaffung                        | wiederholte systemische Lieferausfälle                   |
| **Industrie-/Lieferkettenerpressung**   | Abhängigkeit von Autokratien bei Chips/Minerals/Energie                       | Diversifizierung, Stockpiles, friend-shoring                                     | Abhängigkeitsindex, Stress-Tests                                    | Notfallsubstitution, Exportkontrollen, Investitionsschutz              | Single point of failure in kritischen Gütern             |
| **Finanz-/Transfer-Konflikte**          | Nord/Süd-Spaltung, Moral Hazard                                               | klare Fiskalregeln, mission-based debt, Audit                                    | Schulden-/Defizitmonitoring, Frühwarnrat                            | Konditionalität, automatische Korrekturen                              | dauerhafte Transfers ohne Legitimation/Regeln            |
| **Gericht/Justiz-Politisierung**        | Parteijustiz, selektive Strafverfolgung                                       | unabhängige Richterräte, Ernennungsquoren                                        | Statistik zu Verfahrensdauer/Urteilsanomalien                       | internationale Richterpanel, Suspendierung                             | nachweisliche politische Steuerung                       |
| **Informations-/Zensurrisiko**          | „Anti-Desinfo“ wird Zensur                                                    | Transparenzpflichten, gerichtsfeste Standards, keine Inhaltssteuerung            | Beschwerdekanäle, Gerichts-Review                                   | Aufhebung, Entschädigung, Behördenreform                               | staatliche Inhaltskontrolle ohne Gericht                 |
| **Daten-/Überwachungsrisiko**           | Zentralisierte Profile, Missbrauch                                            | privacy-by-design, Datensparsamkeit, getrennte Schlüssel                         | Logs, unabhängige Datenschutzaufsicht                               | Löschung, Sanktionen, Strafverfahren                                   | Massenüberwachung ohne richterliche Kontrolle            |
| **Krisenkoordination scheitert**        | Behördenchaos, Doppelzuständigkeit                                            | klare Kompetenzmatrix, gemeinsame Übungen                                        | After-Action-Reviews, KPI Reaktionszeit                             | Reform, Personalwechsel, Prozesse                                      | wiederholtes Chaos ohne Lernkurve                        |
| **Sezession/Legitimitätsbruch**         | „Zwangsföderation“-Narrativ, Austrittsdrohungen                               | Exit-Regeln, Subsidiarität, Bürgerbeteiligung                                    | Umfragen/Legitimitätsindex, Konfliktmonitoring                      | Mediationsrat, Kompetenz-Backtransfer                                  | dauerhafte Mehrheit gegen Föderation ohne Dialogmechanik |

---

## 2) Konkrete „Controls“ als Bausteine (die man in Verträge schreibt)

### A) Anti-Capture & Anti-Korruption

| Control                        | Was genau                                                      | Warum es wirkt             |
| ------------------------------ | -------------------------------------------------------------- | -------------------------- |
| **Procurement Integrity Unit** | zentrale Vergabe-Forensik, Blacklist, Ausschreibungs-Standards | stoppt Rüstungs-Korruption |
| **Lobby-/Spenden-Transparenz** | Echtzeit-Register, Obergrenzen, Herkunftsnachweis              | reduziert Kaufbarkeit      |
| **Asset Recovery Office**      | Vermögenseinfrierung/Abschöpfung + internationale Kooperation  | macht Korruption teuer     |
| **Whistleblower Safe Channel** | anonym, gerichtsfest, Schutz vor Repressalien                  | erhöht Aufdeckungsrate     |

### B) Demokratie-/Oppositionsschutz

| Control                               | Was genau                                          | NoGo verhindert   |
| ------------------------------------- | -------------------------------------------------- | ----------------- |
| **Oppositionsrechte verfassungsfest** | Untersuchungsausschuss/Normenkontrolle/Aktenzugang | Exekutivdominanz  |
| **Unabhängiger Rechnungshof**         | Budgetprüfung, Wirkungskontrolle                   | Schattenhaushalte |
| **Medienpluralismus-Guard**           | Kartell-/Transparenzregeln, Schutz vor Übernahmen  | Gleichschaltung   |

### C) Notstands-Controls („Angstimperium“-Bremse)

| Control                      | Was genau                                | Warum es stabil ist            |
| ---------------------------- | ---------------------------------------- | ------------------------------ |
| **Sunset-by-default**        | alles läuft automatisch aus              | Notstand wird nicht Normalität |
| **Doppelmehrheit + Gericht** | Unterhaus+Oberhaus + automatische Review | verhindert Machtballung        |
| **Grundrechts-Kernschutz**   | unantastbare Kernrechte                  | rote Linien bleiben rot        |
| **Post-mortem Pflicht**      | Bericht + Untersuchung möglich           | Lernfähigkeit erzwingt         |

### D) Sicherheits- & Infiltrationsschutz

| Control                             | Was genau                                           | Wirkung                           |
| ----------------------------------- | --------------------------------------------------- | --------------------------------- |
| **Harmonisiertes Clearance-System** | gemeinsame Standards/Rezertifizierung               | reduziert Leaks                   |
| **Foreign Influence Transparency**  | Offenlegung politischer/finanzieller Einflusskanäle | trocknet verdeckte Netzwerke aus  |
| **Counterintelligence Board**       | Multi-State Board + parlamentarische Oversight      | verhindert Geheimdienst-Wildwuchs |

### E) Militärische Kontrolle & Kriegsverhinderung durch Regeln

| Control                       | Was genau                                  | Wirkung                                    |
| ----------------------------- | ------------------------------------------ | ------------------------------------------ |
| **War Powers Act**            | Einsatz nur mit Mandat (Ausnahme: 72h)     | demokratische Kette fix                    |
| **Rules of Engagement Codex** | rechtsstaatliche RoE, Schulung, Monitoring | senkt Eskalations-/Kriegsverbrechensrisiko |
| **Inspector General Defense** | unabhängige Inspektion/Whistleblower       | interne Kontrolle                          |

### F) Finanzielle Stabilität ohne Transferkrieg

| Control                              | Was genau                                    | Wirkung                   |
| ------------------------------------ | -------------------------------------------- | ------------------------- |
| **Mission-based Budget**             | Föderalhaushalt nur für definierte Missionen | begrenzt Zentralstaat     |
| **Automatic Stabilizers mit Deckel** | Krisenhilfe, aber begrenzt und regelgebunden | verhindert Dauertransfers |
| **Audit + Konditionalität**          | Auszahlung nur bei Standards                 | verhindert Moral Hazard   |

---

## 3) Frühwarnsystem: „Resilience Dashboard“ (wenn du’s messen willst)

| Index                | Misst                               | Alarm, wenn…               | Typische Reaktion           |
| -------------------- | ----------------------------------- | -------------------------- | --------------------------- |
| Rule-of-law Index    | Justiz-/Medien-/Wahlqualität        | Trendbruch über 2 Quartale | Konditionalität + Verfahren |
| Capture Risk Index   | Korruption, Vergabeanomalien        | Cluster/Netzwerkhinweise   | Forensik, Blacklist         |
| Decision Speed Index | Handlungsfähigkeit                  | Blockadezeiten steigen     | Governance-Update           |
| Defence Output Index | Munitions-/Systemoutput             | Output < Plan              | Notfallvergabe, Surge       |
| Influence Ops Index  | Desinfo/Leaks/Geldflüsse            | wiederholte Peaks          | Counterintel + Sanktionen   |
| Notstand Abuse Index | Notstandsdauer/Grundrechtseingriffe | wiederholte Verlängerungen | Gericht/Parlament bremst    |

---

## 4) „Hard NoGo“-Liste (rote Linien als Verfassungs-/Vertragsklauseln)

1. **Unfreie Wahlen / systematische Wahlmanipulation**
2. **Politische Kontrolle der Gerichte**
3. **Dauer-Notstand ohne Sunset + Doppelmehrheit + Gericht**
4. **Einsatz militärischer Gewalt ohne demokratische Mandatskette**
5. **Systemische Korruption ohne effektive Strafverfolgung**
6. **Staatliche Inhaltskontrolle (Zensur) ohne gerichtsfestes Verfahren**
7. **Single-point-of-failure Abhängigkeiten in kritischer Sicherheit/Industrie ohne Plan zur Schließung**

---

**Vertragsanlage**:
**„Annex A: Risk Controls & Enforcement“** (mit klaren Artikeln, Schwellen, Sanktionen, Suspendierungs- und Exit-Prozess) – oder als **RACI-Matrix** (wer ist Responsible/Accountable/Consulted/Informed je Control).

## Annex A: Risk Controls & Enforcement (Vertragsanlage – Artikel, Schwellen, Sanktionen, Suspendierung, Exit)

**Annex A – Zweck und Status**

1. Dieser Annex ist integraler Bestandteil des Vertrages und für alle Mitglieder verbindlich.
2. Er definiert verbindliche **Risk Controls**, **Schwellen**, **Enforcement-Maßnahmen**, **Suspendierungs-** und **Exit-Prozesse**.
3. Bei Konflikt mit sonstigen Bestimmungen gilt dieser Annex für sämtliche Fragen der Compliance, Integrität, Notstandskontrolle und Mitgliedschaftsdurchsetzung vorrangig, soweit Grundrechte und Ewigkeitskern nicht verletzt werden.

---

# Teil I – Definitionen und Indikatoren

### Art. A1 – Begriffsbestimmungen

1. **Schwerer Verstoß** liegt vor, wenn ein Mitgliedstaat oder ein Cluborgan eine **NoGo-Schwelle** nach Art. A6 überschreitet.
2. **Systemischer Verstoß** liegt vor, wenn ein Risikoereignis nach Art. A2 über **zwei Prüfzyklen** fortbesteht oder mehrere Kontrollbereiche gleichzeitig betroffen sind.
3. **Trigger** sind messbare Ereignisse/Indikatoren, die eine Pflichtprüfung oder vorläufige Maßnahmen auslösen.

### Art. A2 – Risk-Control-Domänen (verbindliche Bereiche)

a) Rule-of-law & Demokratie-Integrität
b) Anti-Korruption & Procurement Integrity
c) Informationssicherheit, Leaks, Infiltration/Influence Operations
d) Sanktionsvollzug & Anti-Evasion
e) Notstandsregime & Grundrechtsbindung
f) Militärische Mandats- und Einsatzkontrolle
g) Finanz- und Budgetintegrität (Mission-based Budget)
h) Daten- und Datenschutzintegrität (keine Massenüberwachung)
i) Resilienz kritischer Infrastruktur (Single-Point-of-Failure)

### Art. A3 – Prüfzyklen und Auditpflicht

1. **Quartalsprüfung**: Compliance-Status je Domäne (Kurzbericht).
2. **Jahresprüfung**: Vollprüfung inklusive Forensik (bei Auffälligkeiten).
3. Jeder Bericht enthält: Indikatorstand, Abweichungen, Maßnahmenplan, Fristen.

### Art. A4 – Beweisstandard

1. Für vorläufige Maßnahmen genügt **plausible Evidenz** (“reasonable grounds”).
2. Für Suspendierung/Vollmaßnahmen ist **überwiegende Wahrscheinlichkeit** (“balance of probabilities”) erforderlich.
3. Für endgültigen Ausschluss aus Programmen und Vertragsstatus ist ein **bindender Beschluss** nach Art. A12–A14 sowie eine **DRT-Überprüfbarkeit** erforderlich.

### Art. A5 – Zuständige Stellen

1. **ACI** (Audit Court/Inspectorate): Audit, Forensik, KPI-Prüfung.
2. **CRP** (Constitution & Rule-of-Law Panel): Rule-of-law/Notstand/Grundrechte-Compliance.
3. **PIA/Integrity Unit**: Procurement-/Korruptionskontrollen, Blacklist, Step-in.
4. **OCB/Security Board**: Geheimschutz, Clearance, Leak- und Infiltrationslage.
5. **DRT**: bindende Streitbeilegung und Rechtsschutz.

---

# Teil II – NoGo-Schwellen (rote Linien)

### Art. A6 – NoGo-Schwellen (automatische Eskalation)

Ein Mitglied überschreitet eine NoGo-Schwelle, wenn mindestens einer der folgenden Tatbestände vorliegt:

1. **Unfreie Wahlen** oder systematische Wahlmanipulation auf Mitgliedsebene oder Föderationsebene (nach CRP-Feststellung).
2. **Politisierte Justiz**: nachweisliche Regierungssteuerung zentraler Gerichte/Staatsanwaltschaften oder systematische Missachtung höchstrichterlicher Entscheidungen.
3. **Dauer-Notstand**: Notstand > 14 Tage ohne Doppelmehrheit + obligatorische gerichtliche Prüfung oder wiederholte Verlängerungen ohne Sunset-Compliance.
4. **Militärischer Einsatz ohne Mandat** jenseits der 72h-Sofortreaktionsregel oder wesentliche Mandatsüberschreitung.
5. **Systemische Korruption/State Capture**: wiederholte, schwere Vergabe- und Interessenkonfliktverstöße ohne wirksame Strafverfolgung.
6. **Sanktionsumgehung als Politik**: behördlich geduldete oder geförderte Umgehung in kritischen Kategorien (CRP/ACI-Feststellung).
7. **Schwere Leaks/Infiltration**: wiederholter, nicht behobener Abfluss klassifizierter Informationen (Security Board Feststellung).
8. **Massenüberwachung** ohne richterliche Grundlage/zweckgebundene Begrenzung oder systematische Missachtung Datenschutzaufsicht.

**Rechtsfolge:** automatische Einleitung des Verfahrens nach Art. A10 (Emergency Review) binnen 48 Stunden.

---

# Teil III – Maßnahmenkatalog (Sanktionen, Step-in, Remediation)

### Art. A7 – Stufen der Durchsetzung

Maßnahmen sind abgestuft und verhältnismäßig:

**Stufe 0 (Hinweis & Plan):** formaler Compliance-Hinweis, Maßnahmenplan, Frist.
**Stufe 1 (Konditionalität):** Auszahlung/Program Zugriff nur gegen Nachweis konkreter Schritte.
**Stufe 2 (Vorläufige Suspendierung):** temporärer Stimmrechts- oder Zugriffsverlust, Geheimzugriff entzogen.
**Stufe 3 (Voll-Suspendierung):** Entzug Stimmrecht + Program Access + operative Beteiligung.
**Stufe 4 (Programmausschluss/Contract Step-in):** Beschaffung wird übernommen, Verträge neu vergeben, Blacklisting.
**Stufe 5 (Status-Downgrade oder Vertragsbeendigung nach Art. A16):** geordnete Trennung/Exit.

### Art. A8 – Procurement Integrity (Sofortrechte)

1. Bei schwerem Vergabeverdacht hat die Integrity Unit **Step-in Rights**: Vergabestopp, Sonderaudit, Neuvergabe.
2. Blacklisting von Firmen bei Beneficial-Ownership-Verstößen, Korruption, Sanktionsbruch.
3. Pflicht zu Dual-Sourcing bei kritischen Gütern; Single Supplier nur mit begründetem Ausnahmebeschluss und Sunset.

### Art. A9 – Finanzmaßnahmen

1. Bei Stufe 1–3 können **Mittel eingefroren** werden (programm- oder vollständig), ausgenommen:
   a) Zahlungen zur Erfüllung bereits gelieferter, unstreitiger Leistungen
   b) Mittel, die unmittelbar der Sicherheit des Clubs dienen (nach ACI/CoM-Entscheid)
2. Rückforderungen bei missbräuchlicher Mittelverwendung sind zwingend.

---

# Teil IV – Verfahren: Trigger → Prüfung → Entscheidung → Rechtsschutz

### Art. A10 – Emergency Review (48h-Verfahren)

1. Bei NoGo-Triggern nach Art. A6 ist binnen 48 Stunden ein Emergency Review einzuleiten.
2. CRP/ACI/Security Board legen binnen 7 Tagen eine Erstbewertung vor.
3. Der Executive Board kann bis zur Entscheidung vorläufige Maßnahmen (max. 14 Tage) anordnen.

### Art. A11 – Ordentliches Compliance-Verfahren

1. Einleitung durch ACI/CRP/OCB oder auf Antrag der POA-Minderheit (z. B. 25%).
2. Anhörung des betroffenen Mitglieds; Aktenzugang für POA im Geheimschutzrahmen.
3. Beschlussfassung nach Art. A12.

### Art. A12 – Beschlussfassung (Mehrheiten)

1. **Stufe 0–1:** CoM qualifizierte Mehrheit (z. B. 60% Mitglieder + 70% Beiträge).
2. **Stufe 2 (vorläufig):** CoM 2/3 der Stimmen oder automatisch bei CRP-Notstandsfeststellung.
3. **Stufe 3–4:** CoM 2/3 + zwingendes CRP/ACI-Gutachten.
4. **Stufe 5 (Statusbeendigung):** CoM 3/4 + DRT-Bestätigung der Verfahrens- und Beweisstandards.

### Art. A13 – Rechtsschutz (DRT)

1. Das betroffene Mitglied kann binnen 14 Tagen DRT-Review beantragen.
2. DRT prüft: Zuständigkeit, Verfahren, Beweisstandard, Verhältnismäßigkeit, Grundrechtsbindung.
3. DRT kann Maßnahmen bestätigen, abändern oder aufheben.
4. Vorläufige Maßnahmen bleiben bis zur DRT-Entscheidung in Kraft, höchstens 30 Tage, außer DRT ordnet anderes an.

### Art. A14 – Remediation-Plan (Rückkehr)

1. Jede Suspendierung enthält zwingend einen Remediation-Plan mit messbaren Meilensteinen.
2. Rückkehrrechte: nach ACI/CRP-Positivbericht + CoM-Mehrheit (mind. 60%/70%).
3. Wiederholungsfall binnen 24 Monaten → automatische Eskalation um eine Stufe.

---

# Teil V – Spezifische Controls nach Domäne (Trigger & Standardmaßnahmen)

### Art. A15 – Domänenspezifische Trigger (Kurzliste)

1. **Rule-of-law:** Eingriff in Richterernennung/Entlassung, Nichtbefolgung höchstrichterlicher Urteile, Medienübernahme.
2. **Notstand:** Verlängerung ohne Doppelmehrheit/Sunset, Maßnahmen ohne Grundrechtsfolgenabschätzung.
3. **Leak/Infiltration:** 2+ schwere Leak-Events in 12 Monaten ohne Abstellung.
4. **Sanctions/Evasion:** statistisch signifikante Umgehungsströme + behördliche Untätigkeit.
5. **Procurement:** Vergaben ohne Wettbewerb/Begründung in kritischen Kategorien; Interessenkonflikte ohne Offenlegung.
6. **Finance:** Schattenhaushalte, Zweckentfremdung, Audit-Blockade.
7. **Data/Privacy:** zentrale Profilbildung ohne richterliche Grundlage; fehlende Löschpflichten.

**Standardmaßnahmen:** Stufe 1 (Konditionalität) bis Stufe 3 (Suspendierung) je nach Schwere.

---

# Teil VI – Exit/Beendigung & Abwicklung

### Art. A16 – Geordnete Vertragsbeendigung (Status-Downgrade/Exit)

1. **Exit des Mitglieds:** Kündigungsfrist 12–24 Monate; Abwicklungsplan binnen 60 Tagen.
2. **Exit durch Club (Stufe 5):** nur nach wiederholter NoGo-Überschreitung oder verweigerter Remediation.
3. Abwicklung umfasst:
   a) Abrechnung gemeinsamer Assets nach Formel (Anteil Beiträge vs. Nutzung)
   b) Rückgabe/Weiterbetrieb sensibler Systeme unter Geheimschutz
   c) Fortgeltung von Verschwiegenheits- und Exportkontrollpflichten (mind. 10 Jahre)
   d) Schutz individueller Rechtspositionen (Verträge, Ansprüche) bis Ablauf

### Art. A17 – No-Hostage-Klausel

1. Kein Mitglied kann Exit/Abwicklung eines anderen blockieren.
2. Streit über Abwicklungswerte entscheidet DRT binnen 90 Tagen verbindlich.

### Art. A18 – Öffentliche Rechenschaft

1. Alle Enforcement-Entscheidungen sind zu begründen und in einem Transparenzbericht zu dokumentieren (mit Geheimschutz-Ausnahmen).
2. KPI: Decision-Speed, Defence Output, Audit Findings, Remediation Success Rate.

---

# RACI-Matrix (optional, als Annex A-2 oder separat)

Wenn du zusätzlich die **RACI-Matrix** willst, hier eine sofort nutzbare Version als Ergänzung:

| Control-Domäne         | Responsible (R)                 | Accountable (A)                               | Consulted (C)            | Informed (I)                |
| ---------------------- | ------------------------------- | --------------------------------------------- | ------------------------ | --------------------------- |
| Rule-of-law Monitoring | CRP                             | Council of Members                            | POA, DRT                 | alle Mitglieder             |
| Notstand-Compliance    | CRP                             | CoM (Verlängerung)                            | POA, Ombud               | Öffentlichkeit (wo möglich) |
| Procurement Integrity  | Integrity Unit / PIA            | Executive Board                               | ACI, POA                 | CoM                         |
| Budget Audit & KPI     | ACI                             | POA (Kontrollberichte) / CoM (Budgetfreigabe) | EB, PIA                  | alle Mitglieder             |
| Leak/Infosec           | Security Board/OCB              | CoM                                           | POA Geheimschutzpanel    | betroffene Programme        |
| Sanctions Enforcement  | EB + Außenministeriumskonferenz | CoM                                           | ACI, Justiznetzwerk      | POA                         |
| Influence Transparency | Bürger/CIVITAS-Behörde          | CoM                                           | Datenschutzaufsicht, POA | Öffentlichkeit              |
| Suspension Procedure   | EB (vorläufig)                  | CoM                                           | CRP/ACI/DRT              | POA                         |
| Exit/Abwicklung        | EB Abwicklungsstelle            | CoM                                           | ACI, DRT                 | alle Mitglieder             |

---


* **Annex B: Procurement Code** (Vergabeverfahren, Dual Sourcing, Blacklist, Step-in)
* **Annex C: Interop & Certification** (STANAG-Äquivalent, Audit-Tests, Upgrade-Regeln T1→T2)

## Annex B: Procurement Code (Vertragsanlage – Vergabe, Standards, Dual Sourcing, Integrity, Step-in)

**Annex B – Zweck und Status**

1. Dieser Annex ist integraler Bestandteil des Vertrages und für alle Mitglieder sowie alle durch den Club beauftragten Auftragnehmer verbindlich.
2. Er regelt **gemeinsame Beschaffung**, **Standardisierung**, **Integritätsanforderungen**, **Lieferkettenresilienz** sowie **Kontroll- und Eingriffsrechte (Step-in)**.
3. Abweichungen sind nur zulässig, wenn dieser Annex eine **Ausnahme** ausdrücklich vorsieht und die Ausnahme dokumentiert, befristet und auditierbar ist.

---

# Teil I – Grundprinzipien

### Art. B1 – Grundsätze der Beschaffung

1. Beschaffung erfolgt nach den Grundsätzen: **Wettbewerb**, **Transparenz**, **Nichtdiskriminierung**, **Wirtschaftlichkeit**, **Sicherheitsgeeignetheit**, **Interoperabilität**, **Resilienz**.
2. „Buy-national“-Vorgaben sind unzulässig, soweit sie den Clubzielen widersprechen; zulässig sind **Sicherheits- und Resilienzanforderungen**, die faktisch qualifizierte Anbieter begünstigen können.

### Art. B2 – Programm- und Missionsbindung

1. Jede Beschaffung ist einem **Programm** und einer **Mission** zuzuordnen (z. B. Ammo, Air Defence, EW, ISR, Cyber, Stockpiles).
2. Beschaffungen ohne Programmcodierung sind unzulässig, außer bei Notfallbeschaffung nach Art. B18.

### Art. B3 – Standardisierungspflicht

1. Für kritische Kategorien gelten **Club-Standards** (Annex C Interop & Certification).
2. Systeme ohne Zertifizierung dürfen nicht in gemeinsame Pools/Stockpiles eingebracht werden, außer nach Ausnahme nach Art. B17.

---

# Teil II – Governance und Rollen

### Art. B4 – Zuständige Stellen

1. **PIA (Procurement & Industrial Agency)** führt gemeinsame Vergaben durch.
2. **Integrity Unit** prüft Interessenkonflikte, Beneficial Ownership, Sanktions-Compliance und führt Forensik.
3. **ACI** (Audit Court/Inspectorate) prüft Rechtmäßigkeit, Wirtschaftlichkeit, KPI.
4. **Program Boards** (Pay-to-play) definieren Bedarfe, Mengen, Zeitpläne und Abnahmebedingungen.

### Art. B5 – RACI (Kurz)

1. Responsible: PIA (Vergabe), Integrity Unit (Integrität), Program Boards (Anforderungen).
2. Accountable: Executive Board (Durchführung), Council of Members (Programmfreigaben).
3. Consulted: OCB (Interop), CRP (Rule-of-law bei Sanktionen), ACI (Audit).
4. Informed: POA (Kontrollberichte), Mitglieder nach Geheimschutzregeln.

---

# Teil III – Vergabeverfahren

### Art. B6 – Vergabearten

Zulässige Verfahren:

1. **Offenes Verfahren** (Standard)
2. **Nichtoffenes Verfahren** (bei sicherheitsrelevanter Vorqualifikation)
3. **Verhandlungsverfahren** (nur bei hochkomplexen Systemen, begründet)
4. **Rahmenvertrag** (für Serienbedarfe, mehrjährig)
5. **Notfallbeschaffung** (Art. B18, eng begrenzt)

### Art. B7 – Ausschreibung und Transparenz

1. Ausschreibungen enthalten mindestens: Leistungsbeschreibung, Standards, Lieferplan, Qualitätskriterien, KPI, Abnahme, Vertragsstrafen, Export-/Sanktionsklauseln.
2. Wesentliche Vergabeunterlagen werden veröffentlicht, soweit Sicherheitsinteressen nicht entgegenstehen; in diesem Fall erfolgt Veröffentlichung in **geschwärzter** Form plus Audit-Zugang.

### Art. B8 – Eignungs- und Zuschlagskriterien

1. Eignung: technische Leistungsfähigkeit, Sicherheitszuverlässigkeit, Qualitätsmanagement, Kapazität.
2. Zuschlag: **Best Value** (Preis + Lieferzeit + Qualität + Resilienz + Wartbarkeit + Skalierbarkeit).
3. Preis allein darf nicht ausschlaggebend sein, wenn Sicherheits-/Resilienzanforderungen betroffen sind.

### Art. B9 – Vorqualifikation (Security & Quality)

1. Für kritische Kategorien ist Vorqualifikation zwingend (z. B. Air Defence, C2, Crypto, Munition, ISR).
2. Vorqualifikation umfasst: Geheimschutzfähigkeit, Lieferketten-Transparenz, Exportkontroll-Compliance.

---

# Teil IV – Integrity & Compliance (Anti-Korruption / Anti-Capture)

### Art. B10 – Beneficial Ownership und Interessenkonflikte

1. Bieter müssen **wirtschaftlich Berechtigte** offenlegen (bis zur natürlichen Person).
2. Interessenkonflikte sind vor Angebotsabgabe offenzulegen; Verstöße führen zur Ausschlussfähigkeit.

### Art. B11 – Anti-Korruptionsklausel

1. Korruption, Kickbacks, verbotene Zuwendungen sind Nulltoleranz-Verstöße.
2. Nachweis führt zu: Vertragskündigung, Schadenersatz, Blacklisting (Art. B15), Strafanzeige.

### Art. B12 – Sanktions- und Exportkontrollklauseln

1. Bieter/Unterauftragnehmer dürfen nicht sanktioniert sein oder Sanktionen umgehen.
2. Kritische Komponenten aus Hochrisikostaaten sind nur zulässig, wenn explizit genehmigt und mitigiert.

### Art. B13 – Audit- und Zugriffsrechte

1. PIA/ACI/Integrity Unit erhalten Audit-Zugang zu relevanten Unterlagen und Lieferketteninformationen.
2. Verweigerung gilt als schwerer Verstoß (Annex A) und kann zum Ausschluss führen.

### Art. B14 – Whistleblower-Mechanismus

1. Jeder Auftragnehmer muss einen geschützten Kanal bereitstellen.
2. Repressalien sind Vertragsbruch; Sanktionen bis Vertragsauflösung.

### Art. B15 – Blacklisting

1. Blacklisting erfolgt bei schweren Verstößen (Korruption, Sanktionsumgehung, Fälschung, Audit-Blockade).
2. Dauer: 2–10 Jahre, abhängig von Schwere; Wiederaufnahme nur nach nachgewiesener Compliance-Reform.

---

# Teil V – Lieferkettenresilienz und Dual Sourcing

### Art. B16 – Dual Sourcing (Pflicht)

1. Für kritische Kategorien ist **Dual Sourcing** zwingend: mindestens zwei unabhängige Lieferquellen.
2. Unabhängigkeit bedeutet: keine beherrschende gemeinsame Eigentümerstruktur und keine gemeinsame Single-Point-Komponente.

### Art. B17 – Ausnahmen (Single Supplier)

1. Ausnahme nur, wenn:
   a) technische Unverfügbarkeit von Alternativen belegt ist, und
   b) ein Substitutionsplan mit Frist vorliegt, und
   c) CoM die Ausnahme mit qualifizierter Mehrheit beschließt.
2. Jede Ausnahme ist befristet (Sunset) und quartalsweise zu prüfen.

### Art. B18 – Notfallbeschaffung (Emergency Procurement)

1. Nur zulässig bei: akuter Bedrohung, unerwartetem Lieferausfall, krisenbedingtem Surge.
2. Verfahren: verkürzt, aber dokumentationspflichtig; Integrity-Prüfung bleibt zwingend.
3. Notfallbeschaffungen laufen automatisch aus, sobald Normalverfahren wieder möglich ist.

### Art. B19 – Stockpiles und Abnahmegarantien

1. Programme können strategische Lager (Ammo/Ersatzteile) definieren.
2. Abnahmegarantien („offtake“) sind zulässig, sofern KPI/Preisregeln festgelegt sind.

---

# Teil VI – Qualitätsmanagement, Test, Abnahme

### Art. B20 – Qualitätsanforderungen

1. Lieferungen unterliegen Zertifizierung/Tests nach Annex C.
2. Serienproduktion erfordert kontinuierliche Stichprobenprüfungen.

### Art. B21 – Abnahme (Acceptance)

1. Abnahme erfolgt nach: Spezifikation, Testprotokoll, Interop-Zertifikat, Sicherheitsfreigaben.
2. Teilabnahmen sind zulässig, wenn operativ sinnvoll.

### Art. B22 – Garantie, Wartung, Lebenszyklus

1. Verträge enthalten Mindestgarantien, Ersatzteilverfügbarkeit, Wartungsrechte, Dokumentationspflicht.
2. Vendor Lock-in ist zu vermeiden; Schnittstellen müssen dokumentiert sein.

---

# Teil VII – KPI, Vertragsstrafen, Step-in Rights

### Art. B23 – KPI (Pflicht-Katalog)

Mindestens zu messen:

1. Liefermenge vs. Plan
2. Lieferzeit (On-time)
3. Qualitätsquote (Defect Rate)
4. Kostenabweichung
5. Ausfall-/Wartungskennzahlen
6. Lieferkettenrisikoindex (kritische Komponenten)

### Art. B24 – Vertragsstrafen und Remedies

1. Bei KPI-Verfehlen: Vertragsstrafen, Preisreduktionen, Nachlieferpflichten.
2. Wiederholtes KPI-Verfehlen → Eskalation bis Step-in (Art. B25).

### Art. B25 – Step-in Rights (Eingriffsrechte)

1. Bei schwerem oder systemischem Versagen kann PIA:
   a) Produktions-/Lieferpläne übernehmen (mit Auftragnehmerkooperation),
   b) Unterauftragnehmer neu bestimmen,
   c) kritische Teilkomponenten neu sourcen,
   d) Know-how-Übergabe verlangen, soweit vertraglich vereinbart.
2. Step-in ist zu begründen, befristet und auditierbar.

### Art. B26 – Termination (Kündigung)

1. Kündigung bei: Korruption, Sanktionsbruch, Audit-Blockade, wiederholtem Leistungsversagen.
2. Kündigung schließt Schadensersatz und Blacklisting nicht aus.

---

# Teil VIII – Rechtsschutz und Streitbeilegung

### Art. B27 – Bieterrechtsschutz

1. Bieter haben Anspruch auf überprüfbare Vergabeentscheidung innerhalb Geheimschutzgrenzen.
2. Streitigkeiten werden vorrangig durch DRT/Vergabekammer-Mechanismus entschieden; Fristen sind kurz (z. B. 30–60 Tage).

### Art. B28 – Geheimschutz in Verfahren

1. Klassifizierte Details werden in „clean rooms“ geprüft.
2. POA-Geheimschutzpanel erhält Einsicht zu Kontrollzwecken.

---

# Teil IX – Berichterstattung und Transparenz

### Art. B29 – Öffentliche Transparenz (ohne Sicherheitsleck)

1. Jährlicher Bericht: Gesamtausgaben, Programme, KPI-Topline, Blacklist-Anzahl, Audit-Findings.
2. Sicherheitsrelevante Details bleiben klassifiziert; die Existenz der Maßnahme ist zu berichten.

### Art. B30 – Inkrafttreten und Übergang

1. Dieser Annex gilt ab Inkrafttreten des Vertrages.
2. Bestehende Verträge werden binnen 12 Monaten kompatibel gemacht oder ausphasend ersetzt.

---

## Mini-Anhang: Standard-Vertragsklauseln (Copy/Paste-Bausteine)

*(zur direkten Nutzung in Ausschreibungen)*

1. **Integrity Clause** (Korruption/BO/Interessenkonflikte)
2. **Sanctions & Export Control Clause**
3. **Audit Access Clause**
4. **KPI & Penalty Clause**
5. **Step-in Clause**
6. **Whistleblower Protection Clause**
7. **Dual Sourcing Clause**


## Annex C: Interoperability & Certification (Vertragsanlage – Standards, Tests, Zertifikate, Tiers/Upgrades)

**Annex C – Zweck und Status**

1. Dieser Annex ist integraler Bestandteil des Vertrages und für alle Mitglieder, Cluborgane und Auftragnehmer verbindlich.
2. Er definiert das verbindliche **Interoperabilitäts- und Zertifizierungsregime** für Systeme, Einheiten, Datenlinks, Ausbildung und operative Verfahren.
3. Ohne gültige Zertifizierung nach diesem Annex gelten Systeme/Einheiten als **nicht club-kompatibel** und dürfen nur unter den Ausnahmen nach Art. C18 genutzt oder in Pools/Stockpiles eingebracht werden.

---

# Teil I – Begriffe, Prinzipien, Geltungsbereich

### Art. C1 – Begriffe

1. **Interop-Standard**: verbindliche technische/operative Spezifikation (Schnittstellen, Datenformate, Protokolle, Verfahren).
2. **Zertifikat**: formale Bestätigung, dass ein System/Verfahren/Einheit die Anforderungen erfüllt.
3. **Baseline**: Mindestanforderung je Kategorie (z. B. C2, Munition, AD, EW, ISR, Cyber).
4. **Waiver**: befristete Ausnahme mit Sunset und Mitigation-Plan.

### Art. C2 – Prinzipien

1. **Open Architecture**: Schnittstellen offen dokumentiert; Vendor Lock-in ist zu minimieren.
2. **Security by Design**: Kryptographie, Schlüsselmanagement und Zugriffskontrolle sind integraler Teil.
3. **Fail-Safe & Degraded Mode**: definierte Betriebsfähigkeit bei Teilausfall.
4. **Auditability**: Nachweisbarkeit durch Tests, Logs, Dokumentation.
5. **Backward Compatibility**: Übergänge für Legacy-Systeme, aber mit Sunset-Pfad.

### Art. C3 – Geltungsbereich

Dieser Annex gilt mindestens für:
a) C2/Kommunikation/Datenlinks
b) Luft-/Raketenabwehr (AD) und Sensor-/Shooter-Integration
c) Munition/Logistik/Ersatzteilpools/Stockpiles
d) EW/Counter-UAS/ISR-Assets
e) Cyber-Tools für Verteidigung/Response
f) Ausbildung, Zertifizierung von Personal/Units
g) Klassifizierung/Informationssicherheit (gemeinsame Stufen)

---

# Teil II – Governance: Standardsetzung, Zertifizierer, Register

### Art. C4 – Standard- und Zertifizierungsorgane

1. **Interop Standards Board (ISB)**: erarbeitet Standards, pflegt Versionen, definiert Testpläne.
2. **Certification Authority (CA)**: erteilt/entziet Zertifikate, führt Audits durch.
3. **Operational Command Board (OCB)**: definiert operative Mindestverfahren (RoE-nahe SOPs, Übungen).
4. **Security Board (SB)**: verantwortet Geheimschutz, Clearance-Profile, Kryptopolitik.

### Art. C5 – Beschluss und Versionierung

1. Standards werden durch das Council of Members (CoM) nach Empfehlung des ISB beschlossen.
2. Jeder Standard hat Version, Gültigkeitsdauer, Migrationsfenster und „End of Life“-Datum.

### Art. C6 – Zertifikatsregister

1. Die CA führt ein **Zertifikatsregister** (klassifiziert/geschwärzt je nach Sensitivität).
2. Program Boards dürfen nur zertifizierte Komponenten für gemeinsame Pools/Programme akzeptieren (Art. C15).

---

# Teil III – Zertifizierungsstufen (Levels)

### Art. C7 – Zertifikatslevels

Es gelten mindestens folgende Levels:

| Level | Name                           | Bedeutung                                         | Typischer Einsatz          |
| ----- | ------------------------------ | ------------------------------------------------- | -------------------------- |
| L0    | Non-Compliant                  | keine Club-Interop                                | rein national, keine Pools |
| L1    | Basic Interop                  | minimale Schnittstellen/Logistik                  | Program Member (T1)        |
| L2    | Operational Interop            | voll interoperabel in gemeinsamen Operationen     | Operational Member (T2)    |
| L3    | High Assurance                 | erhöhte Sicherheit/Resilienz, kritische Missionen | C2/AD/Cyber Kern           |
| L4    | Strategic Assurance (optional) | besondere Sicherheits-/Abschreckungsbereiche      | sensibelste Domänen        |

### Art. C8 – Mapping Tier ↔ Zertifikatsniveau

1. **T1 (Program Member):** mindestens L1 in relevanten Programmkategorien.
2. **T2 (Operational Member):** mindestens L2 für C2/Comms + betroffene Kernsysteme; L3 für kritische Elemente nach CoM-Liste.
3. **T3 (Constitutional Member):** vollständige Compliance in allen zugewiesenen föderalen Feldern; L3 standardmäßig im Kern.

---

# Teil IV – Test- und Auditkatalog (was geprüft wird)

### Art. C9 – Technische Mindesttests (Kategorieübergreifend)

Jedes System muss (wo anwendbar) nachweisen:

1. **Interface Compliance** (Protokolle, Datenformate, APIs)
2. **Key Management & Crypto** (HSM/Key Rotation, Zugriff)
3. **Latency/Throughput** (Mindestwerte je Kategorie)
4. **Resilience** (Ausfalltests, Redundanz, Degraded Mode)
5. **EMSEC/OPSEC** (Abstrahlung/Leak-Risiken, wo relevant)
6. **Supply Chain Assurance** (Komponentenliste, Herkunft, Firmware)
7. **Logging/Audit Trails** (fälschungssicher, zweckgebunden)

### Art. C10 – Operative Tests (Units/Verfahren)

1. **Joint Exercise Certification**: Teilnahme an Übungen als Zertifizierungsbestandteil.
2. **RoE/SOP Alignment**: Verfahren sind kompatibel und trainiert.
3. **Medical/Logistics Interop**: Verwundetenversorgung, Ersatzteilketten, Munitionsnachschub.

### Art. C11 – Cyber- und Red-Team Tests

1. Für L2+ ist ein **Red-Team-Test** verpflichtend (Scope nach SB).
2. Kritische Systeme (C2, AD, Crypto) benötigen regelmäßige Re-Zertifizierung (Art. C14).

### Art. C12 – Dokumentationspflicht

1. Technische Doku, Schnittstellen, Wartungsprozesse, Konfigurationsmanagement.
2. Fehlende Dokumentation ist ein Zertifizierungshemmnis, außer bei Altbestand (Waiver).

---

# Teil V – Zertifizierungsprozess (Ablauf, Fristen, Re-Zertifizierung)

### Art. C13 – Erteilung

1. Antrag durch Mitglied/Programm oder Hersteller über PIA.
2. CA führt Prüfung (Lab + Feld + Übung) durch.
3. Zertifikat enthält: Level, Scope, Version, Ablaufdatum, Auflagen.

### Art. C14 – Re-Zertifizierung

1. L1: alle 36 Monate oder bei Major-Versionwechsel.
2. L2: alle 24 Monate oder bei Sicherheits-/Schnittstellenänderung.
3. L3/L4: alle 12–18 Monate + verpflichtende Pen-Tests + Supply-Chain-Review.

### Art. C15 – Pool/Stockpile Admission

1. In gemeinsame Pools/Stockpiles dürfen nur Systeme/Komponenten mit gültigem **L2+** (oder CoM-Ausnahme) aufgenommen werden.
2. Munition/Ersatzteile benötigen zusätzlich Kompatibilitäts- und Qualitätsnachweise (Annex B).

---

# Teil VI – Standardfamilien (Minimal-Liste)

### Art. C16 – Standardfamilien

Der ISB pflegt mindestens folgende Standardfamilien:

1. **C2 & Tactical Data Links** (Multi-domain Lagebild)
2. **Air Defence Integration** (Sensor-to-Shooter, Track Management)
3. **Counter-UAS & EW Interfaces**
4. **ISR Data & Metadata** (Formate, Klassifizierung, Dissemination)
5. **Logistics & Stockpile Data** (Teilekataloge, Seriennummern, MHD, Transport)
6. **Cyber Incident Exchange** (IOCs, TTPs, Reporting, Response Playbooks)
7. **Training & Certification Curricula** (Rollenprofile, Skills, Prüfungen)

---

# Teil VII – Waiver/Legacy-Regime (Ausnahmen, Sunset, Mitigation)

### Art. C17 – Legacy-Übergang

1. Legacy-Systeme können befristet als **L1-legacy** zugelassen werden, wenn ein Migrationsplan vorliegt.
2. Migrationsfenster max. 24–48 Monate (CoM kann für kritische Altbestände abweichend beschließen).

### Art. C18 – Waiver (Ausnahmegenehmigung)

1. Waiver nur, wenn:
   a) operative Notwendigkeit besteht,
   b) keine Alternative verfügbar ist,
   c) Mitigation-Plan (z. B. Gateway/Adapter, getrennte Netze) vorliegt.
2. Waiver ist **befristet** (Sunset) und enthält klare Meilensteine.
3. Waiver werden im Register geführt und quartalsweise überprüft.

### Art. C19 – Sicherheitsbedingte Einschränkungen

1. SB kann die Nutzung eines Systems trotz Interop-Level einschränken, wenn eine akute Sicherheitslücke vorliegt.
2. Solche Einschränkungen sind zu begründen und zeitlich zu befristen; Re-Zertifizierung ist auszulösen.

---

# Teil VIII – Durchsetzung (Enforcement) bei Verstößen

### Art. C20 – Konsequenzen bei Non-Compliance

1. Nutzung in Pools/Programmen wird ausgesetzt.
2. Programmzugang kann konditional gemacht werden (Annex A Stufe 1–3).
3. Bei vorsätzlicher Umgehung: Procurement-Sanktionen (Annex B) + Compliance-Verfahren (Annex A).

### Art. C21 – Auditpflicht und Einsicht

1. CA/ACI/SB erhalten Einsicht in Testprotokolle, Logs, Lieferkettendaten (unter Geheimschutz).
2. Audit-Blockade ist schwerer Verstoß (Annex A).

---

# Teil IX – Upgrade-Regeln T1 → T2 (Operative Mitgliedschaft)

### Art. C22 – Upgrade-Voraussetzungen

Ein Mitglied kann von T1 zu T2 upgraden, wenn:

1. C2/Comms mindestens **L2** nachweist,
2. definierte Kernkategorien (CoM-Liste) mindestens **L2/L3** erfüllen,
3. Sicherheitsüberprüfung/Geheimschutz kompatibel ist,
4. eine Joint Exercise Certification in den letzten 18 Monaten erfolgreich abgeschlossen wurde,
5. Audit- und Procurement-Compliance ohne offene schwerwiegende Findings ist.

### Art. C23 – Upgrade-Verfahren

1. Antrag des Mitglieds → Vorprüfung CA/SB/ACI.
2. Empfehlung OCB + Zertifikatsbescheid CA.
3. CoM-Beschluss (2/3) über Upgrade.

### Art. C24 – Downgrade (T2 → T1)

1. Bei systemischer Non-Compliance oder schweren Sicherheitsmängeln kann ein Downgrade erfolgen.
2. Downgrade erfordert: SB/CA-Feststellung + CoM-Mehrheit; DRT-Review möglich.

---

# Teil X – Inkrafttreten und Übergang

### Art. C25 – Inkrafttreten

Dieser Annex tritt mit dem Vertrag in Kraft.

### Art. C26 – Übergangsfristen

1. Innerhalb 6 Monaten: Baseline-Standards (C2, Logistics, Cyber Exchange).
2. Innerhalb 12 Monaten: Erstzertifizierung L1 für Programmbereiche.
3. Innerhalb 24 Monate: L2 für Operational Members in Kernkategorien.

### Art. C27 – Regelmäßige Aktualisierung

ISB veröffentlicht jährlich eine Roadmap; CoM beschließt Updates; POA erhält Kontrollbericht.

---

## Kurz-Anlage: Zertifikats-Template (Minimalinhalt)

* System/Unit ID, Version, Scope
* Level (L1–L4), Gültigkeit, Auflagen
* Testkatalog-Referenzen (C9–C12)
* Interop-Interfaces, Sicherheitsprofil, Key-Management-Mode
* Waiver (falls vorhanden) + Sunset-Datum


## Appendix D: War Powers & Mandates (Vertragsanlage – Mandatsregeln, 72h, Berichte, IG-Defense, Notstandskorridor)

**Appendix D – Zweck und Status**

1. Dieser Appendix ist integraler Bestandteil des Vertrages und für alle Mitglieder und Cluborgane verbindlich.
2. Er regelt die **demokratische Mandatskette** für militärische Operationen, die **72-Stunden-Sofortreaktion**, **Berichtspflichten**, **Kontrollen** sowie die Einhegung von **Notfallbefugnissen**.
3. Jede militärische Handlung im Namen des Clubs bedarf einer **klaren Rechtsgrundlage**, eines **Ziel- und Umfangsrahmens** und ist an die **Grundrechtebindung** gekoppelt.

---

# Teil I – Grundsätze

### Art. D1 – Grundsatz der Mandatspflicht

1. Club-Operationen dürfen nur aufgrund eines **Mandats** erfolgen, das durch die zuständigen demokratischen Organe erteilt wurde, außer bei Sofortreaktion nach Art. D6.
2. Mandate sind **zweckgebunden**, **zeitlich begrenzt** und **überprüfbar**.

### Art. D2 – Verbot aggressiver Kriegführung

1. Angriffskrieg und Gewaltanwendung zur Gebietserweiterung sind ausgeschlossen.
2. Zulässig sind Verteidigung, Beistand im Verteidigungsfall, Schutz kritischer Infrastruktur, Evakuierungs- und Schutzoperationen sowie andere Zwecke, soweit vertraglich und völkerrechtlich gedeckt.

### Art. D3 – Kette der demokratischen Kontrolle

1. **Unterhaus** (oder POA-äquivalentes Mandatsorgan): Mandat, Budgetbindung, Kontrolle.
2. **Oberhaus** (bei definierten Schwellen): Zustimmung bei hochskaligen Einsätzen, Langzeiteinsätzen, verfassungsrelevanter Wirkung.
3. **Regierung/CoM**: operative Führung innerhalb Mandat.
4. **OCB**: militärische Umsetzung; unterliegt Mandats- und Berichtspflichten.
5. **DRT/Verfassungsgericht**: Rechtsschutz und Kontrolle der Mandatsüberschreitung.

---

# Teil II – Operationstypen und Mandatskategorien

### Art. D4 – Kategorien militärischer Maßnahmen

1. **Kategorie 0 (Routine/Readiness):** Übungen, Abschreckungspräsenz, Training, Logistik, Rotationen.
2. **Kategorie 1 (Schutzmaßnahmen):** Schutz kritischer Infrastruktur, Cyber-Defence-Response, Counter-UAS, maritime/luftpolizeiliche Sicherung.
3. **Kategorie 2 (Begrenzte Operation):** zeitlich/örtlich begrenzter Einsatz mit erhöhtem Risiko (z. B. Evakuierung, Sicherungsoperation).
4. **Kategorie 3 (Große Operation/Beistandsfall):** großskalige oder kampfnahe Operationen, Verteidigungsfall, Kriegseintritt.

### Art. D5 – Mandatsschwellen

1. Kategorie 0 erfordert kein Mandat, unterliegt jedoch **Transparenz- und Kontrollpflichten** (Art. D11).
2. Kategorien 1–3 erfordern Mandat; Kategorie 3 erfordert zusätzlich Oberhauszustimmung nach Art. D10, sofern definiert.

---

# Teil III – Sofortreaktion (72-Stunden-Regel)

### Art. D6 – Sofortreaktion bei Angriff/akuter Gefahr

1. Bei bewaffnetem Angriff, unmittelbar drohendem Angriff oder massiver Sabotage kritischer Infrastruktur kann die Exekutive eine **Sofortreaktion** anordnen.
2. Sofortreaktion ist auf **minimale notwendige Abwehrmaßnahmen** beschränkt.

### Art. D7 – Fristen und Bestätigung

1. Innerhalb von **24 Stunden** erfolgt Unterrichtung der Kontrollorgane (POA-Notfallpanel/Unterhaus-Ausschüsse).
2. Innerhalb von **72 Stunden** ist die **parlamentarische Bestätigung** einzuholen.
3. Ohne Bestätigung endet die Operation unverzüglich geordnet; Abbruch darf keine zusätzlichen Gefahren erzeugen („safe disengagement“).

### Art. D8 – Dokumentationspflicht Sofortreaktion

1. Jede Sofortreaktion enthält: Lagebegründung, Ziele, Einsatzregeln, Kräfteumfang, erwartete Dauer, Grundrechtsfolgenabschätzung.
2. Die Dokumentation ist klassifiziert, aber kontrollinstanzfähig (clean room).

---

# Teil IV – Mandatsinhalt (Standardform)

### Art. D9 – Mindestinhalt eines Mandats

Jedes Mandat muss enthalten:

1. **Rechtsgrundlage** (Vertrag, Völkerrecht, nationale Rechtsakte)
2. **Zieldefinition** (konkret, messbar)
3. **Einsatzgebiet** (geografisch/operativ)
4. **Kräfteumfang** (Truppen/Assets/Capabilities)
5. **Einsatzregeln (RoE)** und Schutzregeln
6. **Dauer** (Start, Enddatum, Verlängerungsbedingungen)
7. **Budgetrahmen** und Logistikketten
8. **Berichtspflichten** (Art. D11)
9. **Exit-/Termination-Kriterien** (Art. D12)
10. **Grundrechts- und Compliance-Guardrails** (Art. D13)

### Art. D10 – Zusätzliche Zustimmung des Oberhauses (Schwellen)

Oberhauszustimmung ist erforderlich, wenn mindestens eines gilt:

1. Dauer > 90 Tage, oder
2. Kräfteumfang > definierter Schwellenwert (z. B. Brigadeäquivalent / bestimmte AD-Assets), oder
3. erwartete Kampfintensität hoch, oder
4. erhebliche Haushaltswirkung (über festgelegten Prozentanteil des Core/Program Budget).

---

# Teil V – Kontrolle, Berichte, Untersuchung, Rechtsschutz

### Art. D11 – Berichtspflichten (laufend)

1. Wöchentliche Kurzberichte (klassifiziert) an zuständige Ausschüsse/POA-Panel: Lage, Verluste, Zielerreichung, Risiken.
2. Monatlicher KPI-Bericht: Munitionsverbrauch, readiness, Ausfälle, Logistikstatus, Compliance-Fälle.
3. Öffentlicher Topline-Bericht mindestens quartalsweise, soweit sicherheitsverträglich.

### Art. D12 – Verlängerung und Beendigung

1. Verlängerungen erfordern erneute Abstimmung nach denselben Schwellen wie Mandatserteilung.
2. Mandate enthalten **Sunset**: ohne Verlängerung laufen sie automatisch aus.
3. Beendigung ist zwingend, wenn Mandatsziele erreicht sind, die Rechtsgrundlage entfällt oder NoGo-Schwellen berührt werden.

### Art. D13 – Grundrechts- und Compliance-Guardrails

1. Operationen sind an Grundrechte, humanitäres Völkerrecht und Regeln der Verhältnismäßigkeit gebunden.
2. Verboten sind: willkürliche Inhaftierung, kollektive Bestrafung, unkontrollierte autonome Waffeneinsätze ohne definierten menschlichen Verantwortungsrahmen (sofern vereinbart).
3. Jede operationale Datenerhebung ist zweckgebunden, minimiert, löschpflichtig.

### Art. D14 – Inspector General Defense (IG-D)

1. Ein unabhängiger **IG-Defense** prüft Mandats- und RoE-Compliance, Logistik-/Beschaffungskonformität und Whistleblower-Hinweise.
2. IG-D berichtet direkt an POA/Unterhaus-Ausschüsse und kann Sofortprüfungen auslösen.

### Art. D15 – Untersuchungsausschuss

1. Eine parlamentarische Minderheit (z. B. 25%) kann einen Untersuchungsausschuss zu Operationen beantragen.
2. Die Exekutive ist zur Aktenvorlage verpflichtet, innerhalb Geheimschutzregeln.

### Art. D16 – Rechtsschutz und Mandatsklage

1. Mitgliedstaaten, definierte Parlamentsminderheiten, Ombudstellen und Betroffene können beim DRT/Verfassungsgericht Klage erheben wegen:
   a) Kompetenzüberschreitung,
   b) Mandatsverletzung,
   c) Grundrechtsverletzung.
2. Gerichte können einstweilige Anordnungen erlassen, soweit dies operative Sicherheit nicht unverhältnismäßig gefährdet; dann sind milde Mittel anzuordnen.

---

# Teil VI – Command & Control (C2) und Rules of Engagement

### Art. D17 – C2-Klarheit

1. Für jede Operation wird eine klare Befehlskette festgelegt: politische Leitung, operatives Kommando, taktische Führung.
2. Doppelunterstellungen sind zu vermeiden; bei multinationalen Kräften gilt „unity of command“ nach Mandat.

### Art. D18 – Rules of Engagement (RoE)

1. RoE werden mandatsspezifisch festgelegt und vor Einsatzbeginn trainiert.
2. Änderungen an RoE mit wesentlicher Wirkung sind den Kontrollorganen unverzüglich anzuzeigen; bei Mandatsänderung ist erneute Zustimmung erforderlich.

### Art. D19 – Informationsklassifizierung und Sharing

1. Sharing erfolgt nach Need-to-know + Tier-Regeln (Annex C).
2. Bei Leaks/Infiltration kann der Security Board Zugriffe einschränken; dies ist zu begründen und zu befristen.

---

# Teil VII – Notfallkorridor innerhalb von Operationen (eingezäunt)

### Art. D20 – Operativer Notfallkorridor

1. Unvorhersehbare Lageänderungen können kurzfristige Anpassungen erlauben (z. B. Selbstschutz, Evakuierung, Schutz kritischer Infrastruktur).
2. Anpassungen dürfen nicht den Mandatszweck umkehren oder ausweiten („mission creep“).

### Art. D21 – Mission Creep Trigger

Als mission creep gelten insbesondere:

1. Ausweitung in neue Gebiete ohne Mandatsgrundlage,
2. erhebliche Erhöhung des Kräfteumfangs,
3. Wechsel von Schutzoperation zu Offensivoperation.
   **Rechtsfolge:** sofortige Meldung + binnen 7 Tagen Mandatsnachtrag oder Rückführung.

---

# Teil VIII – Integration mit Annex A/B/C (Enforcement & Procurement & Interop)

### Art. D22 – Verknüpfung mit Annex A (Risk Controls)

1. Verstöße in Operationen können Annex-A-Maßnahmen auslösen (Suspendierung, Access-Entzug).
2. NoGo-Schwellen aus Annex A gelten auch in Operationen (z. B. Einsatz ohne Mandat).

### Art. D23 – Verknüpfung mit Annex B (Procurement)

1. Beschaffung für Operationen unterliegt Annex B; Notfallbeschaffung nur nach Art. B18.
2. KPI/Forensik gelten vollumfänglich.

### Art. D24 – Verknüpfung mit Annex C (Interop)

1. Nur zertifizierte Systeme/Units dürfen im Clubkommando geführt werden, außer Waiver.
2. Kommunikation/C2 muss L2/L3 erfüllen je Kategorie.

---

# Teil IX – Inkrafttreten und Übergang

### Art. D25 – Inkrafttreten

Dieser Appendix tritt mit dem Vertrag in Kraft.

### Art. D26 – Übergangsregel

1. Innerhalb 6 Monaten: Standard-Mandatsformat (Art. D9) verbindlich.
2. Innerhalb 12 Monaten: IG-Defense eingerichtet und arbeitsfähig.
3. Innerhalb 18 Monaten: Übungs- und Berichtssysteme vollständig implementiert.

---

## Kurz-Anlage: Mandatsformular (Template, 1 Seite)

* Operationstitel / Kategorie (0–3)
* Rechtsgrundlage
* Ziele (3–5 messbare Punkte)
* Gebiet/Scope
* Kräfte/Assets
* RoE-Kernaussagen
* Dauer + Sunset
* Budgetrahmen
* Reporting-Plan
* Exit-Kriterien
* Grundrechts-/Compliance-Checkliste
* Unterschriften: politisch + parlamentarisch

## Appendix E: Audit & Transparency (Vertragsanlage – Rechnungshof, KPI, Clean-Room, Ombud, Whistleblower)

**Appendix E – Zweck und Status**

1. Dieser Appendix ist integraler Bestandteil des Vertrages und für alle Mitglieder, Cluborgane und Auftragnehmer verbindlich.
2. Er regelt **Audit**, **Transparenz**, **Rechenschaft**, **KPI-Reporting**, **Geheimschutz-Transparenz (Clean Room)** sowie **Ombud- und Whistleblower-Strukturen**.
3. Ziel ist eine Governance, die **handlungsfähig** bleibt, ohne **Korruption, Capture, Schattenhaushalte, Zensur oder Angstimperium** zu ermöglichen.

---

# Teil I – Organe und Unabhängigkeit

### Art. E1 – Audit Court / Inspectorate (ACI)

1. Es wird ein unabhängiger **Audit Court / Inspectorate (ACI)** eingerichtet.
2. ACI prüft Rechtmäßigkeit, Wirtschaftlichkeit, Wirksamkeit und Compliance aller Clubausgaben, Programme und operativen Strukturen.
3. ACI ist funktional unabhängig; Weisungen sind unzulässig.

### Art. E2 – Unabhängige Bestellung und Amtszeit

1. Leitungspersonen von ACI werden durch qualifizierte Mehrheiten bestellt (z. B. 2/3 der POA oder Unterhausäquivalent).
2. Amtszeit ist fest (z. B. 6–8 Jahre), einmalige Wiederwahl nur in Ausnahme; Abberufung nur aus wichtigem Grund durch qualifizierte Mehrheit und gerichtsfest.

### Art. E3 – Parliamentary Oversight Assembly (POA) – Kontrollrechte

1. POA besitzt umfassende Kontrollrechte, einschließlich Anhörungen, Aktenzugang, Untersuchungen.
2. Oppositionsrechte sind verfassungsfest; eine Minderheit (z. B. 25%) kann Untersuchungen und Sonderaudits beantragen.

### Art. E4 – Ombudsinstitution

1. Eine unabhängige **Ombudsinstitution** wird eingerichtet.
2. Ombud schützt Bürgerrechte, prüft Beschwerden gegen Cluborgane, und hat Eskalations- und Klagerechte nach Art. E16.

---

# Teil II – Audit-Rechte, Zugriff, Prüfarten

### Art. E5 – Prüfmandat (Scope)

ACI prüft insbesondere:

1. Core Budget, Program Budgets, Contingency Fund
2. Beschaffung/PIA inkl. Annex B Integrity
3. Zertifizierung/Interop (Annex C) soweit budget-/compliance-relevant
4. Operationen/Mandate (Appendix D) soweit rechts- und budgetrelevant
5. Sanktionsvollzug/Anti-Evasion (rechtlich und effektivitätsbezogen)

### Art. E6 – Zugang und Mitwirkungspflichten

1. Cluborgane und Auftragnehmer müssen ACI sämtliche relevanten Informationen zugänglich machen.
2. Audit-Blockade oder Täuschung gilt als schwerer Verstoß (Annex A).

### Art. E7 – Auditarten

1. **Regelprüfung** (jährlich)
2. **Sonderaudit** (bei Triggern)
3. **Forensisches Audit** (bei Korruptions-/Capture-Verdacht)
4. **Wirksamkeitsprüfung** (Outcome/KPI)
5. **IT-/Cyber-Audit** (Logs, Zugriffe, Supply Chain) nach Geheimschutzregeln

### Art. E8 – Clean-Room Verfahren

1. Für klassifizierte Informationen gelten **Clean-Room-Verfahren**: gesicherte Räume, kontrollierte Endgeräte, Protokollierung.
2. POA-Geheimschutzpanel erhält Einsicht; Veröffentlichung erfolgt nur als geschwärzte Topline.

---

# Teil III – KPI-Framework (Messbarkeit statt Symbolpolitik)

### Art. E9 – KPI-Pflicht

Jedes Programm und jede wesentliche Struktur hat verpflichtende KPI:

1. Output (z. B. Stückzahlen, Liefertermine)
2. Readiness (Einsatzbereitschaft, Ausfallraten)
3. Kosten (Plan/Ist, Cost growth)
4. Qualität (Defect rates, Abnahmequote)
5. Resilienz (Dual sourcing, single-point-of-failure index)
6. Compliance (Audit findings, remediation time)
7. Decision Speed (Durchlaufzeiten für Beschlüsse/Notfälle)

### Art. E10 – KPI-Dashboard & Veröffentlichungslogik

1. Ein **KPI-Dashboard** wird quartalsweise aktualisiert.
2. Es gibt drei Sichtstufen:
   a) **öffentlich (Topline)**,
   b) **parlamentarisch (detailliert)**,
   c) **klassifiziert (clean room)**.
3. Sicherheitsrelevante Details dürfen geschützt werden; die Existenz und der Umfang der Maßnahme sind dennoch zu berichten, soweit möglich.

### Art. E11 – Schwellen und automatische Review-Trigger

1. KPI-Schwellen werden pro Programm festgelegt (z. B. „Output < 85% Plan über 2 Quartale“).
2. Bei Triggern ist ein Sonderaudit verpflichtend und ein Remediation-Plan innerhalb 30 Tagen vorzulegen.

---

# Teil IV – Transparenz, Register, Interessenkonflikte

### Art. E12 – Transparenzregister (Minimum)

1. Lobbyregister (Meetings, Themen, Auftraggeber)
2. Vergaberegister (Ausschreibungen, Zuschläge, Ausnahmen)
3. Spenden-/Zuwendungs- und Interessenkonfliktregister für Schlüsselpersonen
4. Blacklist-/Integrity-Register (geschützt, aber kontrollierbar)

### Art. E13 – Interessenkonflikte und Cooling-Off

1. Schlüsselpersonen in EB/PIA/ACI/CA/SB unterliegen Offenlegungspflichten.
2. Cooling-off-Regeln (z. B. 24–36 Monate) für Wechsel in betroffene Industrien.

### Art. E14 – Schattenhaushalte verboten

1. Alle Ausgaben müssen im Core/Program/Contingency Budget abgebildet sein.
2. Zweckentfremdung ist schwerer Verstoß (Annex A).

---

# Teil V – Whistleblower und Schutzsystem

### Art. E15 – Whistleblower-Kanäle

1. Cluborgane und Auftragnehmer richten geschützte Kanäle ein (anonym möglich).
2. Meldungen können an Ombud oder ACI gerichtet werden.

### Art. E16 – Schutz vor Repressalien

1. Repressalien sind Vertragsbruch.
2. Verstöße führen zu Sanktionen: Vertragsstrafen, Kündigung, Blacklisting, disziplinarische Maßnahmen.

### Art. E17 – Untersuchungspflicht

1. ACI/Ombud müssen Meldungen binnen 14 Tagen prüfen (Eingangsbestätigung + Scope).
2. Bei glaubhafter Substanz ist eine forensische Prüfung einzuleiten.

---

# Teil VI – Öffentlichkeitsberichte und demokratische Rechenschaft

### Art. E18 – Jahresbericht (öffentlich)

1. ACI veröffentlicht jährlich einen Bericht mit: Budgettopline, KPI-Trends, Audit Findings, Remediation-Status, Integrity-Statistik.
2. Klassifizierte Inhalte werden geschwärzt; die Gründe sind zu benennen.

### Art. E19 – Quartalsberichte (parlamentarisch)

1. Detaillierte Quartalsberichte an POA/Unterhaus-Ausschüsse.
2. Enthalten: Programmstatus, Risikoindex, Trigger, Maßnahmen, Abweichungen.

### Art. E20 – Hearing-Pflichten

1. EB/PIA/OCB müssen auf Verlangen in Anhörungen erscheinen.
2. Nicht-Erscheinen ohne wichtigen Grund ist schwerer Verstoß.

---

# Teil VII – Enforcement-Verknüpfung (Annex A/B/C/D)

### Art. E21 – Compliance-Eskalation

1. Audit Findings werden nach Schwere klassifiziert: Minor/Major/Critical.
2. Critical Findings lösen automatisch Annex-A-Verfahren aus (Stufe 1–3 je nach Risiko).

### Art. E22 – Remediation-Plan Pflicht

1. Für Major/Critical Findings ist binnen 30 Tagen ein Remediation-Plan vorzulegen.
2. Bei Verzug oder Scheitern: automatische Eskalation um eine Stufe.

### Art. E23 – Procurement & Interop

1. Beschaffungsprüfungen referenzieren Annex B.
2. Interop- und Zertifizierungsrelevante Findings referenzieren Annex C (z. B. Waiver-Missbrauch).

### Art. E24 – Operationen & Mandate

1. Mandats- und RoE-Compliance-Findings referenzieren Appendix D.
2. Einsatz ohne Mandat jenseits 72h ist NoGo (Annex A).

---

# Teil VIII – Rechtsschutz und Klagerechte

### Art. E25 – Klagerechte

Klagebefugt sind:

1. Mitgliedstaaten (Kompetenz-/Budgetstreit)
2. Parlamentsminderheit (z. B. 25%)
3. Ombudsinstitution
4. Betroffene Bürger/Organisationen (bei Grundrechts-/Datenschutzverletzung)

### Art. E26 – Streitbeilegung

1. DRT entscheidet verbindlich über Streitigkeiten, einschließlich Auditzugang, Transparenzpflichten und Sanktionen.
2. Eilverfahren ist möglich (z. B. 14–30 Tage), wenn irreversible Schäden drohen.

---

# Teil IX – Inkrafttreten und Übergang

### Art. E27 – Inkrafttreten

Dieser Appendix tritt mit dem Vertrag in Kraft.

### Art. E28 – Übergangsfristen

1. ACI, Ombud und Clean-Room-Struktur binnen 6 Monaten operational.
2. KPI-Dashboard binnen 9 Monaten, erste Quartalsberichte binnen 12 Monaten.
3. Registerpflichten binnen 6–12 Monaten (nach Sicherheitsklassifizierung gestaffelt).

---

## Kurz-Anlage: Klassifizierung der Audit Findings

* **Minor:** geringe Abweichung, keine Systemwirkung → Remediation ≤ 90 Tage
* **Major:** systemrelevant, Risiko erhöht → Remediation ≤ 60 Tage + Sonderaudit möglich
* **Critical:** NoGo-nah oder systemisch → sofortige Eskalation Annex A, vorläufige Maßnahmen möglich



## Appendix F: Membership Tiers & Upgrade/Downgrade (Vertragsanlage – Rechte/Pflichten, Stimmrechte, Eintritt/Exit, EU-Docking)

**Appendix F – Zweck und Status**

1. Dieser Appendix ist integraler Bestandteil des Vertrages und für alle Mitglieder, Cluborgane und Auftragnehmer verbindlich.
2. Er definiert die **Mitgliedschaftsstufen (T0–T3)**, deren **Rechte und Pflichten**, **Stimm- und Zugriffsrechte**, das **Upgrade/Downgrade-Regime**, sowie **Eintritt, Exit und EU-Docking**.
3. Grundprinzipien: **Pay-to-play**, **keine Vetofalle**, **graduelle Integration**, **gerichtsfeste Durchsetzung**.

---

# Teil I – Mitgliedschaftsstufen (Tiers)

### Art. F1 – Überblick Tiers

Die Mitgliedschaftsstufen sind:

| Tier | Bezeichnung           | Kurzprofil                                                                                         |
| ---- | --------------------- | -------------------------------------------------------------------------------------------------- |
| T0   | Observer (Beobachter) | Vorbereitung, Transparenz/Info-Security Minimum, kein Stimmrecht                                   |
| T1   | Program Member        | Teilnahme an Programmen (Beschaffung/Standards), Pay-to-play Stimmrecht                            |
| T2   | Operational Member    | Operative Integration (C2, Pools/Stockpiles, Übungen), höhere Sicherheits- und Interop-Pflichten   |
| T3   | Constitutional Member | Vollintegration in den „föderalen Pfad“ (falls vereinbart), höchste Rule-of-law/War-Powers Bindung |

### Art. F2 – Grundsatz der Graduierung

1. Rechte wachsen proportional zu Pflichten und überprüfbarer Compliance.
2. Niemand erwirbt durch Beitritt automatisch Rechte außerhalb seines Tiers.

---

# Teil II – Rechte und Pflichten je Tier

### Art. F3 – T0 (Observer)

**Rechte:**

1. Teilnahme an Sitzungen als Beobachter (ohne Abstimmung).
2. Zugang zu nicht-klassifizierten Programminformationen und Roadmaps.

**Pflichten:**

1. Unterzeichnung des Geheimschutz-Minimums (Security Board Baseline).
2. Transparenz- und Audit-Vorbereitung (ACI Pre-Assessment).
3. Roadmap zur Erfüllung T1-Kriterien.

### Art. F4 – T1 (Program Member)

**Rechte:**

1. Teilnahme an Program Boards und Program Budgets (Pay-to-play).
2. Stimmrecht in Programmentscheidungen, an denen es finanziell/operativ teilnimmt.
3. Zugang zu Standards und Zertifizierungsprozess (Annex C).

**Pflichten:**

1. Pay-to-play Beiträge je Programm; Mindestbeitrag für Core-Strukturen nach Vertrag.
2. Erfüllung L1-Zertifizierung in relevanten Programmkategorien (Annex C).
3. Vollzug von Sanktions- und Exportkontrollklauseln in Programmlieferketten (Annex B).
4. Akzeptanz von Audit- und Integrity-Regeln (Appendix E, Annex A/B).

### Art. F5 – T2 (Operational Member)

**Zusätzliche Rechte:**

1. Teilnahme an gemeinsamer C2-Architektur und operativen Pools/Stockpiles.
2. Teilnahme an OCB-Strukturen und Einsatzvorbereitung (nicht automatisch Einsatz).
3. Zugriff auf klassifizierte Lagebilder gemäß Clearance-Profil.

**Zusätzliche Pflichten:**

1. L2-Interop für C2/Comms sowie Kernkategorien nach CoM-Liste; L3 für kritische Bereiche (Annex C).
2. Teilnahme an Joint Exercises (Zertifizierungsbestandteil).
3. Voll kompatibles Clearance- und Geheimschutzsystem; Leak-Response-Protokolle.
4. War-Powers & Mandate Bindung für Club-Operationen (Appendix D).
5. Mindestbeitrag zu gemeinsamen Stockpiles und Logistikpools (Program-Pflichtmodule).

### Art. F6 – T3 (Constitutional Member)

**Zusätzliche Rechte:**

1. Vollständige Mitwirkung in verfassungs-/kompetenzrelevanten Entscheidungen (sofern eingerichtet).
2. Voller Zugriff auf föderale Instrumente in definierten Kernkompetenzen.

**Zusätzliche Pflichten:**

1. Vollbindung an Rule-of-law/Grundrechte/Notstandsregime auf föderalem Niveau.
2. Verfassungs- und Parlamentskontrollstandards gemäß Art. 1–30 Verfassungsskizze (oder Äquivalent).
3. Strengste Compliance- und Transparenzpflichten, einschließlich Cooling-off Regeln.

---

# Teil III – Stimmrechte und Entscheidungslogik (keine Vetofalle)

### Art. F7 – Council of Members (CoM) – Stimmrecht

1. Stimmberechtigt sind T1–T3 Mitglieder; T0 ist nicht stimmberechtigt.
2. **Double Majority** gilt für Kernentscheidungen (z. B. 60% Mitglieder + 70% Beitragsanteile).
3. Kein Mitglied besitzt ein Vetorecht, außer bei ausdrücklich vereinbarten Verfassungsfragen (T3).

### Art. F8 – Program Voting (Pay-to-play)

1. Stimmrecht in Programmentscheidungen besitzt nur, wer:
   a) am Programm teilnimmt und
   b) seinen Beitrag fristgerecht geleistet hat.
2. Stimmgewicht im Programm ist proportional zu Beitragsanteil, gedeckelt (z. B. max. 25%) zur Anti-Dominanz.

### Art. F9 – Sicherheitsentscheidungen

1. Sicherheitskritische Entscheidungen (Zugriff auf klassifizierte Systeme, Downgrade wegen Leaks) können durch Security Board Empfehlung beschleunigt werden.
2. Beschlüsse unterliegen DRT-Review und sind befristet, falls sie Grundrechte berühren.

---

# Teil IV – Eintritt, Aufnahme, Upgrade

### Art. F10 – Eintrittsvoraussetzungen (Minimum)

Für T1-Aufnahme sind mindestens erforderlich:

1. Rule-of-law Baseline (CRP positiv)
2. Audit-Fähigkeit (ACI Pre-Assessment positiv)
3. Geheimschutz-Minimum (SB Baseline)
4. Zustimmung zu Annex A–C und Appendix D–E (vertragliche Bindung)

### Art. F11 – Aufnahmeverfahren (T0 → T1)

1. Antrag + Unterlagen → ACI/CRP/SB Vorprüfung.
2. Anhörung im CoM; optional POA Hearing.
3. Aufnahmebeschluss CoM nach Double Majority.

### Art. F12 – Upgrade (T1 → T2)

1. Voraussetzungen:
   a) L2 (C2/Comms) + L2/L3 Kernkategorien (Annex C)
   b) Joint Exercise Certification in den letzten 18 Monaten
   c) keine offenen Critical Audit Findings (Appendix E)
   d) Security Clearance kompatibel, Leak-Response getestet
2. Verfahren: CA/SB/ACI Empfehlung → OCB Empfehlung → CoM 2/3 Beschluss.

### Art. F13 – Upgrade (T2 → T3)

1. Voraussetzungen: vollständige Rule-of-law/Grundrechts-/Notstandsbindung; demokratische Kette in nationaler Umsetzung kompatibel.
2. Verfahren: CRP positives Gutachten + POA Zustimmung + CoM 2/3 + nationale Ratifikation (sofern vorgesehen).

---

# Teil V – Downgrade, Suspendierung, Wiedereinsetzung

### Art. F14 – Downgrade (T2 → T1; T1 → T0)

1. Downgrade ist zulässig bei systemischer Non-Compliance, schweren Leaks, wiederholter Sanktionsumgehung oder Audit-Blockade.
2. Downgrade erfolgt nach Annex A (Stufen 2–4) und ist DRT-reviewbar.
3. Downgrade darf Sicherheits- und Geheimschutzmaßnahmen sofort auslösen (SB).

### Art. F15 – Suspendierung (Zugriffs-/Stimmrechte)

1. Suspendierung kann sich beziehen auf:
   a) Stimmrechte (CoM/Programm)
   b) Programmzugang (Beschaffung, Pools)
   c) operative Teilnahme (OCB, C2)
   d) klassifizierte Informationszugriffe
2. Kriterien und Verfahren richten sich nach Annex A; bei NoGo-Schwellen ist Emergency Review verpflichtend.

### Art. F16 – Wiedereinsetzung / Reinstatement

1. Reinstatement nur nach Remediation-Plan und positiver ACI/CRP/SB Bewertung.
2. CoM entscheidet mit qualifizierter Mehrheit (mind. 60%/70%).
3. Wiederholungsfall innerhalb 24 Monate → automatische Eskalation.

---

# Teil VI – Exit und Abwicklung (geordnet, No-Hostage)

### Art. F17 – Freiwilliger Exit

1. Kündigungsfrist 12–24 Monate.
2. Abwicklungsplan binnen 60 Tagen: Asset-Abrechnung, laufende Verträge, Geheimschutz.
3. Austritt entbindet nicht von fortbestehenden Geheimschutz- und Exportkontrollpflichten.

### Art. F18 – Unfreiwilliger Exit / Statusbeendigung

1. Nur nach wiederholter NoGo-Überschreitung oder verweigerter Remediation (Annex A Stufe 5).
2. CoM 3/4 + DRT Bestätigung; Abwicklung wie F17.

### Art. F19 – No-Hostage-Klausel

1. Kein Mitglied kann Exit/Abwicklung eines anderen blockieren.
2. Streitwerte entscheidet DRT binnen 90 Tagen verbindlich.

---

# Teil VII – Assoziierte Mitglieder („Democratic friends“)

### Art. F20 – Assoziierte Mitgliedschaft

1. Nicht-EU-Demokratien können als T1/T2 assoziiert beitreten, sofern:
   a) Geheimschutz kompatibel ist,
   b) Pay-to-play Beiträge geleistet werden,
   c) Rule-of-law Baseline erfüllt ist,
   d) Exportkontroll-/Sanktionsvollzug kompatibel ist.
2. Assoziierte Mitglieder erhalten keine Rechte in EU-internen Kompetenzfeldern, soweit EU-Recht dies begrenzt.

### Art. F21 – Begrenzungen für Assoziierte

1. Stimmrechte können auf Programmentscheidungen beschränkt werden.
2. Zugriff auf klassifizierte Daten ist tier- und clearance-gebunden.

---

# Teil VIII – EU-Docking / Integration Clause (Variante 1 und 2 kompatibel)

### Art. F22 – Docking to EU Framework

1. Der Club verpflichtet sich, EU-Instrumente (z. B. EDF/EDA/PESCO) zu nutzen, sobald dies rechtlich und politisch möglich ist.
2. Doppelstrukturen werden abgebaut, sobald EU-Strukturen gleichwertige Funktion übernehmen („Sunset on Duplication“).

### Art. F23 – Transposition Protocol

1. Standards, Beschaffungsregeln und Compliance-Mechanismen können als EU-Rechtsakte übernommen werden, sofern EU-Mehrheiten dies ermöglichen.
2. Das CoM beschließt einen Transpositionsplan; ACI prüft Kontinuität; POA überwacht.

### Art. F24 – Compatibility Clause

1. Nichts in diesem Vertrag verpflichtet Mitglieder zu Handlungen, die zwingendem EU-Recht widersprechen.
2. Im Konfliktfall sind Anpassungsprotokolle zu verhandeln; operative Sicherheitsfähigkeit bleibt durch intergouvernementale Teile gewahrt, soweit zulässig.

---

# Teil IX – Inkrafttreten und Übergang

### Art. F25 – Inkrafttreten

Dieser Appendix tritt mit dem Vertrag in Kraft.

### Art. F26 – Übergangsfristen

1. Tiersystem operational binnen 3 Monaten.
2. Erstes Zertifizierungsregister (Annex C) binnen 6 Monaten.
3. Erste vollständige Tier-Reviews binnen 12 Monaten (ACI/CRP/SB).

---

## Kurz-Anlage: „Tier Rights/Pflichten“-Checkliste (1 Seite)

* **T0:** Security Baseline + Audit readiness
* **T1:** Pay-to-play + L1 + Procurement/Integrity + Audit
* **T2:** L2/L3 + Joint exercise + C2/Stockpiles + War Powers compliance
* **T3:** volle verfassungs-/grundrechts-/notstandsbindung + höchste Transparenz

Wenn du willst, kann ich dir jetzt aus Annex A–C und Appendix D–F ein **komplettes Vertragsdokument in Markdown** zusammensetzen (mit Inhaltsverzeichnis, Definitionsteil, Querverweisen, konsistenten Begriffen), so dass du es direkt in euer ERDA-/GitBook-Repo übernehmen kannst.


