# Anhang-M-Beurteilung: CIVITAS P.2 und Kapitel 6

**Stand:** 2026-05-04  
**Rolle:** Redakteur:in  
**Bezugscommit:** `362c0d5 docs: integrate civitas paper and deepen chapter six`  
**Maßstab:** `de/content/anhang-m-massstab-messbare-buchprojektentscheidungen-und-release-kriterien.md`  
**Status:** Redakteur-Beurteilung mit Handlungsanweisungen, keine Finalfreigabe

---

## 1. Kurzurteil

Die CIVITAS-Integration ist nach Anhang M **inhaltlich tragfähig und releasefähig als Release-Candidate-Bestandteil**. Für ein finales v2.5.0-Release ist sie **erfüllt mit Restrisiko**, nicht automatisch final freigegeben.

Der wichtigste Befund: Die Umsetzung macht CIVITAS wesentlich konkreter, ohne das Buchkapitel mit dem vollständigen Paper zu überladen. Kapitel 6 bleibt lesbar, Anhang P.2 übernimmt die zitierfähige Tiefenfassung. Das entspricht der Logik von Anhang M: pfadfindend arbeiten, aber Status, Quelle, Roadmap und Restrisiken sichtbar machen.

---

## 2. M-Gates für CIVITAS

| Gate | Beurteilung | Nachweis | Konsequenz |
|---|---|---|---|
| M-G1 Statusklarheit | erfüllt | Kapitel 6 kennzeichnet CIVITAS als erste operative Schicht und als Roadmap, nicht als fertiges System. | Kein Content-Blocker. |
| M-G2 Quellenintegrität | erfüllt mit Restrisiko | P.2 enthält Quellenapparat und DOI; Kapitel 6 verdichtet daraus das Konzept. | P.2-Quellen in finaler Quellenprüfung risikobasiert stichproben. |
| M-G3 Baseline-Transparenz | nicht zentral, ausreichend | CIVITAS arbeitet vor allem als Konzept/Roadmap; KPIs und Phasen sind Zielindikatoren, keine behaupteten Ist-Daten. | KPI-/Roadmap-Sprache nicht als empirische Wirkung darstellen. |
| M-G4 Rollen- und Freigabelogik | erfüllt mit Restrisiko | EN-Dateien tragen `status: draft`; P.2 ist als veröffentlichtes Paper markiert. | EN nicht stillschweigend auf `approved` setzen. |
| M-G5 Paper-Compliance | erfüllt | P.2 enthält DOI, APA-Zitation, Autor, Version, Datum, Lizenz und Quellenpfad. | P.2 kann in Anhang P bleiben. |
| M-G6 Übersetzungssynchronität | erfüllt mit transparentem Restrisiko | DE/EN sind synchron angelegt; deutsches Buch nutzt deutschen Wrapper plus englisches Original. | Vollständige deutsche Paper-Übersetzung als Backlog, nicht als v2.5-Blocker. |
| M-G7 Release-Ehrlichkeit | teilweise erfüllt | Status- und Release-Dokumente benennen CIVITAS P.2; finale Zertifizierung ist noch offen. | Zertifizierungsprotokoll muss die Restrisiken explizit aufnehmen. |

---

## 3. Spezifische Handlungsanweisungen

### A1 - CIVITAS-Integration redaktionell akzeptieren

**Anweisung:** Kapitel 6 und Anhang P.2 bleiben Bestandteil von v2.5.0. Keine Rücknahme, keine Verschiebung aus dem Release, solange die unten genannten Prüfungen keine harten Fehler finden.

**Begründung:** Die Integration erfüllt die Anhang-M-Logik: Buchkapitel als verdichtete Architektur, Anhang P.2 als Paper mit DOI und Quellenapparat.

### A2 - P.2 nicht stillschweigend als deutsche Vollübersetzung behandeln

**Anweisung:** In Zertifizierung und Release Notes ausdrücklich festhalten: Die deutsche Buchfassung enthält deutsches Vorblatt, deutsche Einordnung und den veröffentlichten englischen Originaltext. Eine vollständige deutsche Paper-Übersetzung bleibt Backlog für eine spätere Version.

**Release-Wertung:** Kein v2.5-Blocker, wenn transparent dokumentiert.

### A3 - Auffälligen Original-Heading bewusst behandeln

**Befund:** Der Abschnittstitel `### 17.2 Discussion Its value lies...` kam bereits aus dem Desktop-Original und wurde zunächst in P.2 übernommen.

**Anweisung:** Als offensichtlichen Markdown-/Layoutfehler typografisch normalisieren, ohne Inhalt, Reihenfolge oder Zitierkern des Papers zu ändern. Die Korrektur muss in allen repo-internen CIVITAS-Kopien synchron erfolgen:

1. `desktop/papers/civitas/content/civitas_public_v1_0_zenodo.md`
2. `desktop/papers/civitas/publish/civitas-public-v1.0-zenodo.md`
3. `de/content/anhang-p-papers/p.2-civitas-public-building-a-european-digital-agora.md`
4. `en/content/appendix-p-papers/p.2-civitas-public-building-a-european-digital-agora.md`

**Umsetzung:** Für v2.5.0 wurde die Überschrift zu `### 17.2 Discussion` getrennt und der folgende Satz als normaler Absatz gesetzt. Das ist eine typografische Normalisierung, keine inhaltliche Paper-Änderung.

### A4 - Rechtsaussagen nur als Anforderungen, nicht als Rechtsgutachten führen

**Anweisung:** Kapitel 6 darf DSGVO, Digital Services Act, eIDAS und Grundrechte-Rahmen als maßgebliche Anforderungen nennen. Es darf nicht behaupten, CIVITAS sei bereits rechtlich geprüft oder garantiert konform.

**Aktueller Stand:** Der Check wurde mit `scripts/quality/legal_claims_scan.py` für Kapitel 6 DE/EN und CIVITAS P.2 DE/EN durchgeführt. Der Report liegt unter `release-docs/v2.5.0/legal-claims-scan-civitas-v2.5.0.md`. Ergebnis: erfüllt mit dokumentiertem Restrisiko. Die `review-high`-Treffer liegen im P.2-Papertext bzw. dessen Anhangserklärungen; die neu verdichteten Kapitel-6-Stellen bleiben im Anforderungs-, Roadmap- und Zielrahmen. Dies ist keine Rechtsberatung.

### A5 - Quellen- und Linkprüfung nachziehen

**Anweisung:** Vor Finalfreigabe die Quality-Tools für Quellen und Links erneut ausführen und die CIVITAS-P.2-Referenzen `[1]` bis `[16]` stichprobenartig prüfen, besonders aktuelle 2025/2026-Quellen und Plattform-/Rechtsquellen.

Empfohlene Befehle:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.quality.sources --root de/content -o tmp/gitbook-worker-quality-v2.5.0/sources-de.csv --language de --max-level 6
.\.venv\Scripts\python.exe -m gitbook_worker.tools.quality.sources --root en/content -o tmp/gitbook-worker-quality-v2.5.0/sources-en.csv --language en --max-level 6
.\.venv\Scripts\python.exe -m gitbook_worker.tools.quality.link_audit --root de/content --no-progress --check-duplicate-headings --check-citations --list-todos
.\.venv\Scripts\python.exe -m gitbook_worker.tools.quality.link_audit --root en/content --no-progress --check-duplicate-headings --check-citations --list-todos
```

**Aktueller Stand:** Erledigt für CIVITAS P.2. Der A5-Bericht liegt unter `release-docs/v2.5.0/source-link-check-civitas-v2.5.0.md`. Ergebnis: kein A5-Blocker; DOI im Paperkopf `200 OK`, keine broken links, keine Zitationslücken, keine TODOs, nach Normalisierung keine Duplicate-Heading-Warnung. Einzelne externe Anbieter blockieren CLI-Abrufe mit `403`; diese Fälle wurden per `curl`, DOI-Handle-API oder bibliografischer Quellenklasse gegengeprüft.

**Release-Wertung:** Für CIVITAS P.2 erfüllt mit dokumentiertem Restrisiko. Allgemeine Release-Quellen- und Build-Gates bleiben davon unberührt.

### A6 - Publish-Artefakte nach sauberem Commit neu erzeugen und prüfen

**Anweisung:** Da die CIVITAS-Integration jetzt committed ist, dürfen die Publish-Läufe erfolgen oder vorhandene Läufe als Nachweis dokumentiert werden. Danach `git status --short --branch` prüfen.

Empfohlene Befehle:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root "$PWD" --manifest "de/publish.yml" --profile local --content-config "content.yaml" --lang de
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root "$PWD" --manifest "en/publish.yml" --profile local --content-config "content.yaml" --lang en
git status --short --branch
```

**Anweisung bei Diff:** Wenn Publish-Artefakte geändert werden, separaten Build-Commit erstellen, zum Beispiel `build: refresh v2.5 publish artifacts`.

### A7 - Zertifizierungsprotokoll konkret ergänzen

**Anweisung:** In `release-docs/v2.5.0/release-certification-v2.5.0.md` vor Finalfreigabe mindestens diese Einträge ergänzen:

- P.2 Paper-Compliance: DOI, APA, Version, Datum, Lizenz, Originalsprache geprüft.
- Kapitel 6: CIVITAS als Roadmap/Architektur, nicht als fertiges System bewertet.
- EN-Status: draft bleibt sichtbar, sofern kein Native-gb-en-Review erfolgt.
- Restrisiko: englisches Original in deutscher Buchfassung bewusst akzeptiert.
- Hinweis: auffälliger Original-Heading 17.2 wurde als typografische Normalisierung in allen repo-internen CIVITAS-Kopien korrigiert.
- Quality-Tool-Ergebnisse: Link-Audit, Sources-Export, ggf. AI-References-Dry-Run.

### A8 - Finalfreigabe erst nach Gate 5 und Gate 6

**Anweisung:** CIVITAS darf redaktionell als v2.5-Inhalt gelten. Der Release `v2.5.0` darf aber erst final getaggt werden, wenn Build-/Artefaktprüfung, Zertifizierungsprotokoll und Publisher-Freigabe geschlossen sind.

---

## 4. Entscheidungsvorschlag

**Redakteur-Vorschlag:** CIVITAS P.2 und Kapitel 6 bleiben im Release. Für v2.5.0 wird keine vollständige deutsche Paper-Übersetzung verlangt. Die offene Arbeit wandert in Zertifizierung, Quellenprüfung, Build-Nachweis und optionalen Erratum-Backlog.

**Release-Entscheidung nach Anhang M:** Erfüllt mit dokumentiertem Restrisiko. Finalfreigabe möglich, sobald die oben genannten Handlungsanweisungen A5 bis A8 abgearbeitet und im Zertifizierungsprotokoll nachgewiesen sind.