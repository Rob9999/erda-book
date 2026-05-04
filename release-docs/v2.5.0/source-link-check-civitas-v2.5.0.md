# A5 Quellen- und Linkprüfung: CIVITAS P.2

**Stand:** 2026-05-04  
**Rolle:** Redakteur:in  
**Scope:** CIVITAS P.2 DE/EN, Kapitel-6-Kontext, Referenzen `[1]` bis `[16]`  
**Status:** Teilprüfung abgeschlossen, kein A5-Blocker

---

## 1. Kurzurteil

A5 ist für CIVITAS P.2 **erfüllt mit dokumentiertem Restrisiko**. Die DOI- und Kernlinks sind funktionsfähig oder plausibel verifiziert. Es gibt keine gebrochenen Links im P.2-Paperkopf, keine Zitationslücken, keine TODOs und nach redaktioneller Normalisierung keine Duplicate-Heading-Warnung mehr.

Ein Restrisiko bleibt bewusst dokumentiert: Einzelne Verlags-/Organisationsseiten blockieren CLI- oder Bot-Abrufe zeitweise mit `403`, obwohl DOI- oder Browser-/curl-Nachprüfung die Quelle als plausibel erreichbar bzw. registriert bestätigt. Das ist kein inhaltlicher Blocker, aber ein Hinweis für spätere Link-Audits.

---

## 2. Toolläufe

| Tool | Scope | Ergebnis | Nachweis |
|---|---|---|---|
| `gitbook_worker.tools.quality.sources` | `de/content` | 321 Markdown-Dateien erkannt; Quellenexport erzeugt | `tmp/a5-civitas/sources-de.csv` |
| `gitbook_worker.tools.quality.sources` | `en/content` | 321 Markdown-Dateien erkannt; Quellenexport erzeugt | `tmp/a5-civitas/sources-en.csv` |
| `gitbook_worker.tools.quality.link_audit` | DE P.2 | 0 broken links, 1 good DOI-link, 0 images issues, 0 duplicate headings, 0 citation gaps, 0 TODOs | `tmp/a5-civitas/link-audit-civitas-de.csv` |
| `gitbook_worker.tools.quality.link_audit` | EN P.2 | 0 broken links, 1 good DOI-link, 0 images issues, 0 duplicate headings, 0 citation gaps, 0 TODOs | `tmp/a5-civitas/link-audit-civitas-en.csv` |

Hinweis: Die `tmp/a5-civitas/`-Dateien sind Arbeitsnachweise für den lokalen Check. Der dauerhafte Release-Nachweis ist dieser Bericht.

---

## 3. Redaktionelle Strukturkorrektur aus dem Link-Audit

Der erste `link_audit` fand je eine Duplicate-Heading-Warnung für `A Call to Action`, weil das bibliografische Vorblatt und der veröffentlichte Originaltext denselben Heading-Text nutzten. Das wurde redaktionell normalisiert:

- DE P.2: Wrapper-Heading entfernt, `**Untertitel:** A Call to Action` ergänzt.
- EN P.2: Wrapper-Heading entfernt, `**Subtitle:** A Call to Action` ergänzt.

Danach meldete `link_audit` in DE und EN jeweils `0 duplicate headings`.

---

## 4. Referenzen `[1]` bis `[16]`

| Ref. | Quelle | A5-Bewertung | Bemerkung |
|---:|---|---|---|
| [1] | Eurobarometer 2025, Standard Eurobarometer 103 | plausibel, manuell zu beobachten | Keine URL im Paper; aktuelle Eurobarometer-Angabe bleibt als institutionelle Quellenklasse akzeptiert. |
| [2] | Bail et al. 2018, PNAS, DOI `10.1073/pnas.1804840115` | verifiziert | PowerShell meldete 403, `curl -L -I` mit User-Agent meldete `200 OK`. |
| [3] | EEAS 2025, 3rd FIMI Report | verifiziert | `Invoke-WebRequest -UseBasicParsing` meldete `200 OK`. |
| [4] | Zuboff 2019, Buch | plausibel | Buchquelle ohne URL; bibliografisch ausreichend. |
| [5] | Lewandowsky et al. 2017, DOI `10.1016/j.jarmac.2017.07.008` | verifiziert | `Invoke-WebRequest -UseBasicParsing` meldete `200 OK`. |
| [6] | ERDA Book 2026, DOI `10.5281/zenodo.18827190` | verifiziert | `Invoke-WebRequest -UseBasicParsing` meldete `200 OK`. |
| [7] | Digital Services Act, Regulation (EU) 2022/2065 | plausibel | Official-Journal-Angabe ohne URL; Rechtsquelle eindeutig genug. |
| [8] | Habermas 1989, Buch | plausibel | Buchquelle ohne URL; bibliografisch ausreichend. |
| [9] | Landemore 2020, Buch | plausibel | Buchquelle ohne URL; bibliografisch ausreichend. |
| [10] | Helberger, Pierson & Poell 2018, DOI `10.1080/01972243.2017.1391913` | verifiziert | PowerShell meldete 403, `curl -L -I` mit User-Agent meldete `200 OK`. |
| [11] | Decidim 2024, Website und GitHub | verifiziert | `decidim.org` und `github.com/decidim/decidim` meldeten `200 OK`. |
| [12] | OECD 2020, DOI `10.1787/339306da-en` | verifiziert mit Zugriffshinweis | Zielseite blockte CLI-Abrufe mit 403; DOI-Handle-API meldete `responseCode 1` für `10.1787/339306da-en`. |
| [13] | Arana-Catania et al. 2021, DOI `10.1145/3452118` | verifiziert | PowerShell meldete 403, `curl -L -I` mit User-Agent meldete `200 OK`. |
| [14] | GDPR, Regulation (EU) 2016/679 | plausibel | Official-Journal-Angabe ohne URL; Rechtsquelle eindeutig genug. |
| [15] | DFG 2019, DOI `10.5281/zenodo.3923602` | verifiziert | `Invoke-WebRequest -UseBasicParsing` meldete `200 OK`. |
| [16] | Keller & Tarkowski 2021, Open Future | verifiziert | PowerShell meldete 403, `curl` per GET meldete `200`. |

---

## 5. Release-Entscheidung A5

Für CIVITAS P.2 gibt es nach dieser Prüfung **keinen A5-Blocker**.

Vor Finalfreigabe bleiben allgemeine Release-Gates offen, insbesondere vollständige Build-/Artefaktprüfung und Publisher-Freigabe. Für den CIVITAS-P.2-Quellen- und Linkstand gilt: releasefähig als dokumentierter RC-Stand, mit dem Hinweis, dass einzelne externe Anbieter CLI-Abrufe blocken können und deshalb spätere Link-Audits Browser-/curl- oder DOI-Handle-Gegenprüfungen nutzen sollten.