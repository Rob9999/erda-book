---
version: 1.0.0
date: 2026-05-12
status: technical-package-ready-with-erda-warnings
target_release: "gitbook_worker v2.9.2"
review_role: Redakteur:in
source_package: "packages/gitbook-worker/gitbook_worker-2.9.2-py3-none-any.whl"
source_archive: "packages/gitbook-worker/gitbook_worker-2.9.2.tar.gz"
supersedes: "release-docs/v2.5.0/gitbook-worker-2.9.1-delivery-review-v2.5.0.md"
history:
  - "1.0.0: 2026-05-12 - Technische ERDA-Lieferpruefung fuer gitbook_worker v2.9.2 dokumentiert."
  - "1.0.1: 2026-05-12 - Artefaktmetriken und Quality-Zaehler nach ERDA-Buch-Namenspass aktualisiert."
---

# Lieferreview: gitbook_worker v2.9.2

## Kurzentscheidung

Die Nachlieferung `gitbook_worker 2.9.2` ist aus ERDA-Sicht **technisch
abnahmefaehig fuer die Repo-Integration**.

Die Version wurde aus dem vendorten Wheel installiert, die CI-/Workflow-Pins
wurden auf den neuen Tarball umgestellt und die DE/EN-Publish-Artefakte wurden
lokal neu erzeugt. Das integrierte `editorial-quality`-Gate endet weiterhin mit
`passed_with_warnings`, 0 `blocked` und 0 `fail`.

ERDA ist damit nicht automatisch final release-freigegeben. Die verbleibenden
Warnungen sind redaktionell zu priorisieren oder als Restrisiko zu dokumentieren;
die Publisher-Sichtpruefung bleibt vor Tag/Release separat erforderlich.

## Lieferumfang geprueft

| Nachweis | Ergebnis |
|---|---|
| Wheel | `packages/gitbook-worker/gitbook_worker-2.9.2-py3-none-any.whl` vorhanden und lokal installierbar |
| Tarball | `packages/gitbook-worker/gitbook_worker-2.9.2.tar.gz` vorhanden |
| Installierte Version | `gitbook-worker 2.9.2` in `.venv` verifiziert |
| Acceptance-ZIP | kein 2.9.2-Acceptance-ZIP im Repo mitgeliefert; Integration daher anhand Wheel/Tarball, lokaler Installierbarkeit, Publisher-Lauf und `editorial-quality` reproduziert |

## Publisher-Kompatibilitaet

Nach Installation von `gitbook-worker 2.9.2` wurden die lokalen Publisher-Stufen
fuer DE und EN erfolgreich ausgefuehrt.

| Artefakt | Seiten | Dateigroesse nach Rebuild | CreationDate | Ergebnis |
|---|---:|---:|---|---|
| `de/publish/das-erda-buch.pdf` | 858 | 4403173 bytes | `D:20260512130526+02'00'` | Build erfolgreich |
| `en/publish/the-erda-book.pdf` | 826 | 4421247 bytes | `D:20260512125449+02'00'` | Build erfolgreich |

## ERDA-Reproduktionslauf

Ausgefuehrter integrierter Lauf:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run `
  --root C:\RAMProjects\ERDA `
  --manifest en/publish.yml `
  --profile local `
  --content-config content.yaml `
  --lang en `
  --step editorial-quality `
  --quality-profile release `
  --quality-gate `
  --quality-scope configured `
  --silent
```

Ergebnis mit `gitbook-worker 2.9.2`:

| Prefix | Status | Blocked | Fail | Warn | Info |
|---|---|---:|---:|---:|---:|
| `de-release` | `passed_with_warnings` | 0 | 0 | 35 | 7 |
| `en-release` | `passed_with_warnings` | 0 | 0 | 40 | 7 |
| `project-release` | `passed_with_warnings` | 0 | 0 | 75 | 8 |

Die lokalen Artefakte liegen unter `logs/quality/` und bleiben bewusst ignoriert:

- `de-release-editorial-acceptance.md/json/html`
- `en-release-editorial-acceptance.md/json/html`
- `project-release-editorial-acceptance.md/json/html`
- korrespondierende Metrics-, CSV- und SARIF-Dateien

## Warnungsbild ERDA

Die Projekt-Warnungen verteilen sich im 2.9.2-Lauf wie folgt:

| Gruppe | Anzahl | Severity | Einordnung |
|---|---:|---|---|
| `markdown.long_token` | 59 | warn | Lange Links, HTML-Fragmente oder technische Tokens; Layoutrelevanz stichprobenartig pruefen |
| `markdown.review_marker` | 10 | warn | Offene redaktionelle Marker oder vom Tool erkannte Review-Signale priorisieren |
| `metadata.version_mismatch` | 2 | warn | Manifest-/Markdown-Metadaten bewusst pruefen |
| `pdf.text.extraction_replacement` | 2 | warn | Textlayer-/Accessibility-Risiko, kein visueller Fontblocker ohne Sichtbefund |
| `publish.summary.orphaned_markdown` | 2 | warn | `de/README.md` und `en/README.md` ausserhalb der Publish-SUMMARY bewusst einordnen |
| `pdf.toc.outline_without_markdown_heading` | 5 | info | TOC-/Heading-Abgleich beobachten |
| `pdf.text.script_sample` | 2 | info | Skriptstichproben sichtbar |
| `references.ai.tasks_detected` | 1 | info | AI-Referenzsignal als Hinweis, keine Quellenwahrheit |

## Entscheidung fuer ERDA

| Ebene | Entscheidung |
|---|---|
| Technische Paketuebergabe | annehmbar |
| Repo-Integration der Version | annehmbar, wenn Worker-Pins auf 2.9.2 zeigen |
| ERDA-Quality-Gate | `passed_with_warnings`, keine harten Befunde |
| ERDA-Releasefreigabe | noch manuell zu entscheiden; Warnungen und Publisher-Sichtpruefung bleiben offen |
| Publisher-Freigabe | nach Sichtpruefung, Warnungspriorisierung und finaler Metadatenkonsistenz moeglich |

## Naechste Schritte

1. Worker-Pins in `requirements.txt` und `.github/workflows/orchestrator.yml` auf 2.9.2 committen.
2. Finaldocs und Release-Metadaten auf neue PDF-Groessen, Seitenzahlen und Quality-Zaehler pruefen.
3. Die 75 Projektwarnungen priorisieren oder als bewusstes Restrisiko dokumentieren.
4. Vor Tag/Publisher-Freigabe einen finalen Worktree-/Index-Endcheck und die bewusste Tag-Entscheidung ausfuehren.
