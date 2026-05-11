---
version: 1.0.0
date: 2026-05-11
status: technical-package-ready-with-erda-warnings
target_release: "gitbook_worker v2.9.1 Abnahmefix"
review_role: Redakteur:in
source_package: "packages/gitbook-worker/gitbook_worker-2.9.1-py3-none-any.whl"
source_archive: "packages/gitbook-worker/gitbook_worker-2.9.1.tar.gz"
source_docs: "packages/gitbook-worker/gitbook-worker-v2.9.1-customer-acceptance-redacted-2026-05-11.zip"
history:
  - "1.0.0: 2026-05-11 - Technische ERDA-Lieferpruefung fuer gitbook_worker v2.9.1 Abnahmefix dokumentiert."
---

# Lieferreview: gitbook_worker v2.9.1 Abnahmefix

## Kurzentscheidung

Die Nachlieferung `gitbook_worker 2.9.1` ist aus ERDA-Sicht **technisch
abnahmefaehig fuer die Repo-Integration**.

Der zentrale offene Punkt aus 2.9.0 ist behoben: Die bisherigen
`pdf.text.replacement_glyph`-Fails werden nicht mehr als harter
Font-/Glyphenfehler klassifiziert, sondern als
`pdf.text.extraction_replacement`-Warnung fuer Textlayer, Accessibility und
Copy/Paste. Diese Einstufung passt zur visuellen Stichprobe, unter anderem zur
gedruckten DE-Seite 73, auf der die Symbole sichtbar intakt erscheinen, aber
`pypdf` im Textlayer Replacement-Zeichen extrahiert.

ERDA ist damit nicht automatisch final release-freigegeben. Die Quality-Gates
stehen jedoch nicht mehr auf `failed`, sondern auf `passed_with_warnings`. Die
verbleibenden Warnungen sind redaktionell zu priorisieren oder als Restrisiko
zu dokumentieren.

## Lieferumfang geprueft

| Nachweis | Ergebnis |
|---|---|
| Wheel | `packages/gitbook-worker/gitbook_worker-2.9.1-py3-none-any.whl` vorhanden und lokal installierbar |
| Tarball | `packages/gitbook-worker/gitbook_worker-2.9.1.tar.gz` vorhanden |
| Installierte Version | `gitbook-worker 2.9.1` in `.venv` verifiziert |
| Acceptance-ZIP | `packages/gitbook-worker/gitbook-worker-v2.9.1-customer-acceptance-redacted-2026-05-11.zip` vorhanden |
| Acceptance-Doku | README, redaktierte Markdown-Zusammenfassung und redaktierte JSON-Zusammenfassung enthalten |
| Datenschutzgrenze | ZIP enthaelt nur aggregierte Evidenz, keine Kunden-PDFs, Rohtexte, Logs, CSV/SARIF/HTML oder Snapshots |

## Lieferanten-Abnahmenachweis

Die redaktierte Kundenabnahme nennt fuer `v2.9.1 "Abnahmefix"`:

| Status | Blocked | Fail | Warn | Info |
|---|---:|---:|---:|---:|
| `passed_with_warnings` | 0 | 0 | 43 | 7 |

Wichtige Lieferantennotiz: Textlayer-Replacement-Signale bleiben sichtbar, sind
aber als Extraktions-/Accessibility-Warnung eingestuft, nicht als visueller
Fontfehler.

## Publisher-Kompatibilitaet

Nach Installation von `gitbook-worker 2.9.1` wurden die lokalen Publisher-Stufen
fuer DE und EN erfolgreich ausgefuehrt.

| Artefakt | Seiten | Dateigroesse nach Rebuild | Ergebnis |
|---|---:|---:|---|
| `de/publish/das-erda-buch.pdf` | 868 | 4355269 bytes | Build erfolgreich |
| `en/publish/the-erda-book.pdf` | 830 | 4374034 bytes | Build erfolgreich |

Die deutsche Seitenzahl bleibt stabil. Die englische PDF liegt nach dem
2.9.1-Rebuild bei 830 Seiten und muss in den finalen Release-Metadaten bewusst
nachgezogen werden, sofern dort noch 829 Seiten dokumentiert sind.

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

Ergebnis mit `gitbook-worker 2.9.1`:

| Prefix | Status | Blocked | Fail | Warn | Info |
|---|---|---:|---:|---:|---:|
| `de-release` | `passed_with_warnings` | 0 | 0 | 43 | 7 |
| `en-release` | `passed_with_warnings` | 0 | 0 | 45 | 7 |
| `project-release` | `passed_with_warnings` | 0 | 0 | 88 | 8 |

Die lokalen Artefakte liegen unter `logs/quality/` und bleiben bewusst ignoriert:

- `de-release-editorial-acceptance.md/json/html`
- `en-release-editorial-acceptance.md/json/html`
- `project-release-editorial-acceptance.md/json/html`
- korrespondierende Metrics-, CSV- und SARIF-Dateien

## Abhilfe gegen 2.9.0-Fail

| 2.9.0 | 2.9.1 |
|---|---|
| `pdf.text.replacement_glyph` als `fail` in Kategorie `pdf.fonts` | `pdf.text.extraction_replacement` als `warn` in Kategorie `pdf.text` |
| Evidenz nur als Gesamtzahl | Evidenz mit Seitenhinweisen, z. B. `p1=24, p2=12, ...` |
| Heilung: Fontkonfiguration und LaTeX-Logs pruefen | Heilung: visuelle Stichprobe, Poppler/pypdf-Extraktion und echte Missing-character-Signale trennen |
| Moeglicher Eindruck eines visuellen Massenfehlers | Klare Einordnung als Textlayer-/Accessibility-/Copy-Paste-Risiko ohne Sichtbefund |

Aktuelle ERDA-Befunde:

| Regel | Artefakt | Severity | Evidenz |
|---|---|---|---|
| `pdf.text.extraction_replacement` | `de/publish/das-erda-buch.pdf` | warn | 9317 text extraction replacement signal(s), mit Seitenhinweisen |
| `pdf.text.extraction_replacement` | `en/publish/the-erda-book.pdf` | warn | 9062 text extraction replacement signal(s), mit Seitenhinweisen |

## Warnungsbild ERDA

Die Projekt-Warnungen verteilen sich im 2.9.1-Lauf wie folgt:

| Gruppe | Anzahl | Severity | Einordnung |
|---|---:|---|---|
| `markdown.long_token` | 71 | warn | Lange Links, HTML-Fragmente oder technische Tokens; Layoutrelevanz stichprobenartig pruefen |
| `markdown.review_marker` | 10 | warn | Offene redaktionelle Marker oder vom Tool erkannte Review-Signale priorisieren |
| `pdf.text.extraction_replacement` | 2 | warn | Textlayer-/Accessibility-Risiko, kein visueller Fontblocker ohne Sichtbefund |
| `publish.summary.orphaned_markdown` | 2 | warn | `de/README.md` und `en/README.md` ausserhalb der Publish-SUMMARY bewusst einordnen |
| `metadata.version_mismatch` | 2 | warn | Manifest-/Markdown-Metadaten bewusst pruefen |
| `pdf.text.empty_pages` | 1 | warn | Einzelne textleere PDF-Seite sichtbar pruefen |
| `pdf.toc.outline_without_markdown_heading` | 5 | info | TOC-/Heading-Abgleich beobachten |
| `pdf.text.script_sample` | 2 | info | Skriptstichproben sichtbar |
| `references.ai.tasks_detected` | 1 | info | AI-Referenzsignal als Hinweis, keine Quellenwahrheit |

## Entscheidung fuer ERDA

| Ebene | Entscheidung |
|---|---|
| Technische Paketuebergabe | annehmbar |
| Repo-Integration der Version | annehmbar, wenn Worker-Pins auf 2.9.1 zeigen |
| ERDA-Quality-Gate | `passed_with_warnings`, keine harten Befunde |
| ERDA-Releasefreigabe | noch manuell zu entscheiden; Warnungen und Release-Metadaten nachziehen |
| Publisher-Freigabe | nach Sichtpruefung, Warnungspriorisierung und finaler Metadatenkonsistenz moeglich |

## Naechste Schritte

1. Worker-Pins in `requirements.txt` und `.github/workflows/orchestrator.yml`
   auf 2.9.1 committen.
2. Finaldocs und Release-Metadaten auf neue PDF-Groessen und EN-Seitenzahl 830
   pruefen.
3. Die 88 Projektwarnungen priorisieren oder als bewusstes Restrisiko
   dokumentieren.
4. Vor Tag/Publisher-Freigabe einen finalen Quality-Lauf mit dokumentierter
   manueller Entscheidung und ggf. akzeptierten Restrisiken ausfuehren.