---
id: ''
title: ADR-00-Final-RPM-Decision-BALL-D127
version: v0.1.0
state: DRAFT
evolution: '00'
discipline: ''
system: []
system_id: []
seq: []
owner: ''
reviewers: []
source_of_truth: false
supersedes: null
superseded_by: null
rfc_links: []
adr_links: []
cr_links: []
date: 2025-09-01
lang: EN
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


#### ADR-00-Final-RPM-Decision-BALL-D127-en-v0.1.0-draft

##### Executive Summary

* **Decision / Entscheidung:** **1 g @ DECK 012** (reference radius $r_\star = 52.0\ \mathrm{m}$).
* **Operational spin / Betriebsdrehzahl:** $\omega = 0.4343\ \mathrm{s^{-1}}$ ⇒ **4.147 rpm** $T = 14.47\ \mathrm{s}$.
* **Volume-weighted g-comfort:**

  * $\text{SLI}_\text{total} = 324{,}592\ \mathrm{m^3\cdot score}$
  * $\text{SLI}_\text{avg} = 0.736$
* **Previous baseline (legacy):** 1g @ DECK 008 → $\omega = 0.508\ \mathrm{s^{-1}}$ ≈ 4.852 rpm → **retired**.
* **Special decks:**

  * **DECK 000** = axial micro-g tunnel (ID ≈ 20 m) → **excluded from SLI**.
  * **DECK 015** = **Tank/Thermal Deck** at $r=63.0\ \mathrm{m}$; included geometrically (optional occupancy $f_{015} < 1$).

---

##### Context & Scope / Kontext & Geltung

Platform: **BALL-D127 "Earth ONE Class"** with internal sphere radius $R = 63.0\ \mathrm{m}$. Deck bands in 3.5 m gross steps. Objective: determine optimal, sustainable, comfortable **1 g reference deck**.

---

##### Methodology / Methodik

###### Geometry / Geometrie

* Tube length:
  $L(r) = 2\sqrt{R^2 - r^2}$
* Net floor radius:
  $r_\text{floor} = r_\text{bis} - 0.5\ \mathrm{m}$
* DECK 015: $r_\text{floor} = 63.0\ \mathrm{m}$ (shell). DECK 000: $r_\text{floor} = 10.0\ \mathrm{m}$.

###### Volumes / Volumina

* Exact annular volume inside sphere:
  $V(r_A,r_B)=\frac{4\pi}{3}\left[(R^2 - r_A^2)^{3/2} - (R^2 - r_B^2)^{3/2}\right]$

* Habitable:
  $r_\text{in} = \max(r_\text{floor}-1.80, r_\text{ceiling})\quad\Rightarrow\quad V_{\ge1.80} = V(r_\text{in}, r_\text{floor})$

* Effectively habitable ($-0.25\ \mathrm{m}$ for installations):
  $r_\text{in}^\star = \max(r_\text{floor}-1.55, r_\text{ceiling})\quad\Rightarrow\quad V_\text{eff} = V(r_\text{in}^\star, r_\text{floor})$

###### Gravitation & Comfort

* Spin law:
  $a(r)=g_0\cdot \frac{r}{r_\star}$
* Comfort function (g only):
  $C(a) = \max\{0,\ 1 - |g - 0.9|/0.9\}$

###### SLI (Sphere Living Comfort Index)

$\text{SLI}_\text{total} = \sum_{d=001}^{015} V_\text{eff}(d) \cdot C(a_d)\quad\text{and}\quad \text{SLI}_\text{avg} = \frac{\text{SLI}_\text{total}}{\sum V_\text{eff}}$

---

##### Alternatives Considered / Optionen

| Scenario      | $r_\star$ [m] |       rpm | Notes                                            |
| ------------- | -------------: | --------: | ------------------------------------------------ |
| 1g @ D008     |           38.0 |     4.852 | Legacy baseline; outer decks >1.1g → retired     |
| 1g @ D009     |           41.5 |     4.642 | Improvement, but still overloads outer decks     |
| 1g @ D010     |           45.0 |     4.458 | Better centering; acceptable fallback            |
| 1g @ D011     |           48.5 |     4.294 | Very good; slightly underloads inner decks       |
| **1g @ D012** |       **52.0** | **4.147** | **Chosen**: optimal banding 009–013 (0.8–1.05 g) |
| 1g @ D013     |           55.5 |     4.014 | Shifts weight outward; inner decks <0.8g         |
| 1g @ D014     |           59.0 |     3.893 | Too outward; comfort drops overall               |
| 1g @ D015     |           63.0 |     3.768 | Not viable; technical/tank deck only             |

---

##### Why DECK 012 is Correct / Warum DECK 012 richtig ist

* **Maximizes comfort-weighted volume** in residential bands (009–013)
* **Moderate rpm** (4.147), stable for operations
* **Minimizes penalty from tech decks** (014–015)
* **SLI remains robust** even with DECK 015 weighted as $f_{015}<1$

---

##### Result Overview / Ergebnis

| Deck | $r_\text{ceiling}$ [m] | $r_\text{floor}$ [m] | $L$ [m] | $V_\text{eff}$ [m³] | $a/g_0$ | $C(a)$ |
| ---- | ----------------------: | --------------------: | -------: | -------------------: | ------: | -----: |
| 009  |                    38.5 |                  41.5 |    100.4 |               38,123 |   0.798 |  0.887 |
| 010  |                    42.0 |                  45.0 |     84.2 |               38,642 |   0.865 |  0.962 |
| 011  |                    45.5 |                  48.5 |     66.1 |               38,220 |   0.933 |  0.964 |
| 012  |                    49.0 |                  52.0 |     45.3 |               36,578 |   1.000 |  0.889 |
| 013  |                    52.5 |                  55.5 |     19.8 |               33,249 |   1.067 |  0.814 |
| 014  |                    56.0 |                  59.0 |    \~0.0 |               27,244 |   1.135 |  0.739 |
| 015  |                    59.5 |                  63.0 |    \~0.0 |               11,222 |   1.212 |  0.654 |

---

##### Consequences / Konsequenzen

* **Occupancy:** People distribution aligned with high SLI zones → 009–013
* **Architecture:** DECK 008 legacy baseline **replaced** with DECK 012 reference
* **Spin rate:** reduced to 4.147 rpm → lower Coriolis, better comfort
* **Docs:** Update SPEC, SRS, ICD; tag CALC; review SAF/HAZ

---

##### Acceptance Criteria

* Full $C_g$ incl. Coriolis/Gradient/rpm yields $SLI_\text{avg} \ge 0.70$
* Operational head–foot $\Delta g$ ≤ 0.10 g in residential decks
* Verified via calc + update configuration baseline

---

##### Attachment

* [Table 1: Evol00 Decks 000 015 R Korr63 Roehrenmodell Exakt Sli](../../../../../08-glossary-partners-institutions-legal-notices-and-overall-appendices/8.4-overall-appendices/8.4.8-appendix-t-tables/table-1-evol00-decks-000-015-r-korr63-roehrenmodell-exakt-sli.md)
