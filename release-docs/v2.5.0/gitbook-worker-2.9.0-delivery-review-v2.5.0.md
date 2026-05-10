---
version: 1.0.0
date: 2026-05-10
status: technical-package-ready-with-erda-fails
target_release: "gitbook_worker v2.9.0 Qualitaetskompass"
review_role: Redakteur:in
source_package: "packages/gitbook-worker/gitbook_worker-2.9.0-py3-none-any.whl"
source_docs: "tmp/gitbook-worker-v2.9.0-quality-customer-acceptance-2026-05-10.zip"
history:
  - "1.0.0: 2026-05-10 - Technische ERDA-Lieferpruefung fuer gitbook_worker v2.9.0 Qualitaetskompass dokumentiert."
---

# Lieferreview: gitbook_worker v2.9.0 Qualitaetskompass

## Kurzentscheidung

Die Lieferung ist aus ERDA-Sicht **technisch prueffaehig und integrierbar**, aber
noch **nicht release-freigegeben**.

Die gelieferten Paket- und Dokuartefakte schliessen die zuvor offenen
Nachweisfragen deutlich besser als der reine Lieferantenreport. Wheel, Tarball,
Requirements-Matrix, Readiness-Review, Fail-Offenlegung, Warnungsgruppen,
Exit-Code-Nachweis, Datenschutz-/Evidenzpolicy sowie Sample-Quality-Reports
liegen vor. Der lokale ERDA-Reproduktionslauf erzeugt ebenfalls die erwarteten
Dossiers und Artefaktformate.

Die fachliche Freigabe bleibt offen, weil der ERDA-Lauf harte
`pdf.text.replacement_glyph`-Befunde in beiden finalen PDFs meldet und sehr viele
Warnungen sichtbar macht. Das ist kein Lieferblocker fuer die technische
Paketuebergabe, aber ein Release-Gate fuer ERDA.

## Lieferumfang geprueft

| Nachweis | Ergebnis |
|---|---|
| Wheel | `packages/gitbook-worker/gitbook_worker-2.9.0-py3-none-any.whl` vorhanden und lokal installierbar |
| Tarball | `packages/gitbook-worker/gitbook_worker-2.9.0.tar.gz` vorhanden |
| Installierte Version | `gitbook-worker 2.9.0` in `.venv` verifiziert |
| Neue CLIs | `editorial_metrics` und `editorial_acceptance` vorhanden |
| Exit-Code-Hilfe | Codes 45, 46, 47, 48 per `--help-exit-codes` abrufbar |
| Lieferdoku-ZIP | `tmp/gitbook-worker-v2.9.0-quality-customer-acceptance-2026-05-10.zip` vorhanden |
| Doku-Nachweise | Requirements-Matrix, Delivery Evidence, Readiness, Warning Groups, Fail Disclosure, Privacy und Exit-Code Evidence enthalten |
| Sample-Reports | DE-, EN- und Projekt-Dossiers mit JSON, Markdown, CSV, SARIF, HTML, Trend und Snapshot-Index enthalten |

## Publisher-Kompatibilitaet

Nach Installation von `gitbook-worker 2.9.0` wurden die lokalen Publisher-Stufen
fuer DE und EN erfolgreich ausgefuehrt.

| Artefakt | Seiten | Dateigroesse nach Rebuild | Ergebnis |
|---|---:|---:|---|
| `de/publish/das-erda-buch.pdf` | 868 | 4345520 bytes | Build erfolgreich |
| `en/publish/the-erda-book.pdf` | 829 | 4344134 bytes | Build erfolgreich |

Die Seitenzahlen bleiben gegenueber dem 2.8.0-Default-Build stabil. Der deutsche
Publish-Markdown wurde an einer Tabellen-Trennzeile mechanisch normalisiert.

## Lieferanten-Samplelauf

Die mitgelieferte Kundenabnahme-Doku nennt fuer den konfigurierten `release`-Lauf
im Lieferantenrepo:

| Prefix | Status | Blocked | Fail | Warn | Info |
|---|---|---:|---:|---:|---:|
| `de-release` | `failed` | 0 | 1 | 195 | 27 |
| `en-release` | `failed` | 0 | 1 | 172 | 18 |
| `project-release` | `failed` | 0 | 2 | 546 | 30 |

Die beiden harten Befunde sind offen gelegte
`pdf.text.replacement_glyph`-Signale in den Sample-PDFs. Der Lieferant deutet
diese nicht in ein Scheingruen um, sondern behandelt sie als harte Fails mit
Healing-Steps. Das entspricht der ERDA-Anforderung an ehrliche Abnahmedossiers.

## ERDA-Reproduktionslauf

Ausgefuehrter integrierter Lauf:

```powershell
python -m gitbook_worker.tools.workflow_orchestrator run `
  --root . `
  --content-config content.yaml `
  --profile local `
  --step editorial-quality `
  --quality-profile release `
  --quality-scope configured
```

Ergebnis:

| Prefix | Status | Blocked | Fail | Warn | Info |
|---|---|---:|---:|---:|---:|
| `de-release` | `failed` | 0 | 1 | 2063 | 7 |
| `en-release` | `failed` | 0 | 1 | 2102 | 7 |
| `project-release` | `failed` | 0 | 2 | 4296 | 8 |

Erzeugte ERDA-Artefakte liegen lokal unter `logs/quality/`, insbesondere:

- `de-release-editorial-acceptance.md`
- `en-release-editorial-acceptance.md`
- `project-release-editorial-acceptance.md`
- korrespondierende JSON-, CSV-, SARIF-, HTML-, Trend- und Snapshot-Index-Dateien

## Harte ERDA-Befunde

| Regel | Artefakt | Evidenz | Einordnung |
|---|---|---:|---|
| `pdf.text.replacement_glyph` | `de/publish/das-erda-buch.pdf` | 9317 replacement glyph signal(s) | Release-blockierend bis Font/Textlayer visuell und technisch geklaert ist |
| `pdf.text.replacement_glyph` | `en/publish/the-erda-book.pdf` | 9062 replacement glyph signal(s) | Release-blockierend bis Font/Textlayer visuell und technisch geklaert ist |

Diese Befunde koennen reale Font-/Glyphenprobleme anzeigen, koennen aber auch
aus Textlayer- oder Extraktionssignalen entstehen. Fuer ERDA gilt: Solange sie
nicht visuell und technisch eingeordnet sind, bleiben sie ein `fail`.

## Warnungsbild ERDA

Die groessten Warnungsgruppen im Projektlauf sind:

| Gruppe | Anzahl | Einordnung |
|---|---:|---|
| `markdown.heading.duplicate_title` | 2769 | Viele gleiche Abschnittstitel erschweren Review und Querverweise; redaktionell gruppieren statt einzeln lesen |
| `markdown.long_token` | 1257 | Vor allem `content_id`, Quellen-URLs und lange technische Tokens; Layoutrelevanz stichprobenartig pruefen |
| `markdown.review_marker` | 265 | Offene redaktionelle Marker oder vom Tool erkannte Review-Signale; vor finaler Freigabe priorisieren |
| `publish.summary.orphaned_markdown` | 2 | `de/README.md` und `en/README.md` liegen ausserhalb der Publish-SUMMARY |
| `metadata.version_mismatch` | 2 | Manifest-/Markdown-Metadaten muessen bewusst eingeordnet werden |
| `pdf.text.empty_pages` | 1 | Einzelne textleere PDF-Seite sichtbar; visuell pruefen |

## Abgleich gegen ERDA-Ergaenzungen E1-E14

| Bereich | Bewertung |
|---|---|
| E1 Report-Drift und Artefakt-Frische | umgesetzt; PDF-Seiten, Groessen, CreationDate und Reportstatus erscheinen im Dossier |
| E2 Wenigzeiler/Leerseiten | umgesetzt; textarme/leere Seiten werden als PDF-Signale sichtbar |
| E3 Seitenzielkorridore | technisch vorhanden; ERDA-Profilwerte muessen projektseitig gepflegt werden |
| E4 Frontmatter/Uebersetzung | technisch vorhanden; ERDA muss Policy fuer Warnungen und Approved-Schutz scharfziehen |
| E5 Publikationsscope | umgesetzt; Orphaned Markdown wird gefunden |
| E6 PDF-TOC/SUMMARY/Heading | umgesetzt; Outline- und Heading-Signale erscheinen |
| E7 Tabellenstrategie | im Lieferanten-Sample nachgewiesen; im ERDA-Lauf nicht lokal belastet, weil keine `*.table-layout.jsonl`-Reports vorhanden waren |
| E8 PDF-Layout/BBox | modelliert; ERDA sollte bestehende Layoutscans weiter parallel vergleichen |
| E9 Font/Textlayer | umgesetzt und wirksam; die aktuellen ERDA-Fails stammen genau aus diesem Gate |
| E10 Quellen/Rechts/AI-Hinweise | in Lieferdoku vorgesehen; ERDA muss Disclaimer in Dossiers bei Quellenlaeufen weiter pruefen |
| E11 Profile | umgesetzt; `local`, `release` und konfigurierte Scopes funktionieren lokal |
| E12 Manuelle Freigabe/Restrisiko | Dossierabschnitt vorhanden; keine automatische Freigabe gesetzt |
| E13 Stable IDs/Baseline | technisch vorhanden; kein ERDA-Baseline-Report uebergeben |
| E14 Pfad/Datenschutz | Doku vorhanden; echter CLI-Schalter fuer Evidenzstufe ist laut Lieferdoku noch nicht eigenstaendig vorhanden |

## Entscheidung fuer ERDA

| Ebene | Entscheidung |
|---|---|
| Technische Paketuebergabe | annehmbar |
| Repo-Integration der Version | annehmbar, wenn Worker-Pins auf 2.9.0 zeigen |
| ERDA-Releasefreigabe | noch nicht annehmbar |
| Publisher-Freigabe | erst nach Glyphen-/Fontklaerung und Warnungspriorisierung |

## Naechste Schritte

1. Worker-Pins in `requirements.txt` und `.github/workflows/orchestrator.yml`
   vor Commit auf 2.9.0 verifizieren.
2. `pdf.text.replacement_glyph` fuer beide ERDA-PDFs technisch und visuell
   pruefen.
3. Warnungsgruppen aus `logs/quality/project-release-editorial-findings.csv`
   redaktionell priorisieren.
4. ERDA-spezifisches Acceptance-Profil mit Seitenzielkorridor, Fontpolicy,
   Evidenzstufe und Warnungs-Gates nachziehen.
5. Bei finalem Release einen neuen `editorial-quality`-Lauf mit Baseline und ggf.
   akzeptierten Restrisiken ausfuehren.
