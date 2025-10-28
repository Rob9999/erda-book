# Workflow Tool Suite

This package houses the automation code that backs the repository's GitHub
Actions workflows.  The modules are organised as a standalone Python project
and can also be executed locally for debugging or to reproduce CI behaviour.

The tooling falls into three groups:

* **Workflow orchestration** – glue code that reads `publish.yml`, evaluates
  automation profiles and executes the appropriate helper scripts.
* **Publishing utilities** – scripts that build PDFs, update GitBook artefacts
  and manage manifest flags.
* **Developer helpers** – generic runners and Docker utilities that make it
  easier to execute the toolchain on contributor machines.

All entry points rely on the shared logging helpers in `logging_config.py`,
which configure structured INFO-level logging and optionally mirror output into
`.github/logs/` when running inside Actions.

## Quick start

* Run the consolidated workflow locally:
  ```bash
  python -m tools.workflow_orchestrator --help
  python -m tools.workflow_orchestrator --profile default --dry-run
  ```
  Profiles are read from the repository `publish.yml`.  Each profile provides
  the list of steps to execute (`check_if_to_publish`, `converter`,
  `publisher`, …) and optional Docker settings.

* Execute the legacy publishing pipeline without the orchestrator:
  ```bash
  python .github/tools/publishing/pipeline.py --manifest publish.yml
  ```
  This script shells out to the helper modules described below, matching the
  behaviour of the historical GitHub Actions configuration.

* Convert CSV assets into Markdown tables and charts:
  ```bash
  python -m tools.converter.convert_assets --manifest publish.yml
  ```

## Module overview

### `workflow_orchestrator/`

The orchestrator mirrors the GitHub workflow chain and is the preferred entry
point for automated runs:

* `orchestrator.py` resolves command-line arguments into an
  `OrchestratorConfig` by reading `publish.yml`, expanding profile templates and
  deriving runtime options such as repository visibility.  It then invokes the
  configured steps in order while exporting a consistent environment for
  subprocesses.
* Available steps include:
  * `check_if_to_publish` – run `publishing/set_publish_flag.py` to compute which
    manifest entries changed between two Git SHAs and should be rebuilt.
  * `ensure_readme` – create placeholder `readme.md` files for directories that
    would otherwise break GitBook navigation.
  * `update_citation` – keep `docs/public/publish/citation.cff` in sync with the
    current date.
  * `converter` – call `publishing/dump_publish.py` followed by the CSV asset
    converter to refresh derived tables and charts.
  * `engineering-document-formatter` – ensure Markdown engineering documents
    carry the expected YAML front matter.
  * `publisher` – delegate to `publishing/pipeline.py` for the heavy lifting.
* `__main__.py` exposes `python -m tools.workflow_orchestrator` as the CLI
  entry point.

### `publishing/`

This package implements the selective publishing flow used by the Actions job:

* `pipeline.py` orchestrates the end-to-end run.  It resolves the manifest,
  optionally toggles publish flags, normalises GitBook assets via
  `gitbook_style.py`, and forwards custom options to the PDF publisher.  Each
  helper is executed as a subprocess to ensure identical CLI behaviour inside
  GitHub Actions and local runs.
* `publisher.py` reads the manifest entries flagged for publishing and renders
  PDFs.  It combines Markdown sources, applies optional landscape helpers,
  injects fonts and LaTeX macros, honours per-entry asset directories from
  `publish.yml` when constructing Pandoc's resource path so images stay
  available, runs Pandoc and resets build flags through `reset_publish_flag.py`
  when successful.
* `gitbook_style.py` contains two subcommands: `rename`, which applies GitBook
  naming conventions, and `summary`, which rebuilds `SUMMARY.md` from
  `book.json`.  Both support running with or without Git metadata.
* `preprocess_md.py`, `markdown_combiner.py` and `table_pdf.py` provide the PDF
  pre-processing pipeline, handling wide tables, landscape sections and paper
  size escalation.
* `set_publish_flag.py`, `reset_publish_flag.py` and `dump_publish.py` manage
  manifest state for incremental builds.
* `summary_generator.py`, `paper_info.py`, `make_gitbooks.py` and
  `geometry_package_injector.py` host specialised helpers that are reused by
  the pipeline and publisher scripts.
* `_test_appendix_check.py` contains unit tests for appendix handling logic in
  the summary generation.

The `fonts/`, `lua/` and `texmf/` subfolders ship the assets required by Pandoc
and LaTeX when running headless inside CI.

### `converter/`

Utilities that transform CSV inputs referenced by the manifest into user-facing
artefacts:

* `convert_assets.py` discovers `assets/csvs/` folders next to manifest entries,
  converts each CSV into a Markdown table under `assets/tables/`, applies an
  optional template from `docs/public/assets/templates`, and renders charts into
  `assets/diagrams/` when numeric data is present.
* `csv2md_and_chart.py` holds the reusable helpers for rendering Markdown tables
  and matplotlib charts.  They are imported by the converter and exposed for
  ad-hoc use.

### `quality/`

Quality assurance tooling that inspects Markdown sources for regressions:

* `sources.py` extracts "Quellen"/"Sources" sections from Markdown files into a
  CSV report to help maintain bibliographies.  Run it with `python -m
  tools.quality.sources --help` for usage information.
* `link_audit.py` validates external links, image references, heading reuse and
  TODO markers, emitting CSV or log summaries depending on the selected CLI
  flags (`python -m tools.quality.link_audit --help`).
* `ai_references.py` validates and repairs bibliography entries with the help of
  large language models.  It derives the Markdown scope from `SUMMARY.md`,
  submits each reference to the configured AI backend, updates confirmed fixes
  on disk, and emits a structured JSON report for downstream tooling.

  The legacy `tools/gitbook-worker --ai-reference-repair` flag is deprecated;
  use this module instead so that CI workflows and local runs share the same
  implementation and configuration surface.

### `utils/`

Developer-focused helpers that make it easier to execute the workflows on
heterogeneous machines:

* `run.py` wraps `subprocess.run`, standardising logging, error handling and
  environment merging.
* `docker_runner.py` builds (if necessary) and launches Docker containers with a
  bind-mounted workspace, automatically attempting to start Docker Desktop on
  Windows and the daemon on Linux.
* `python_workspace_runner.py` bootstraps a `.venv` for a given workspace,
  installs dependencies via `pip`, `requirements.txt` files or the optional `uv`
  installer, and executes a provided command/module inside that environment.
* `__init__.py` exports convenience imports for the utils package.

### `docker/`

Contains Dockerfiles used by CI jobs.  `Dockerfile.python` provides a base image
with LaTeX tooling, fonts and Pandoc for the publishing pipeline, while the
multi-stage `Dockerfile` is geared towards building and testing the workflow
suite itself.  The accompanying README documents usage patterns.

### Other support modules

* `logging_config.py` initialises the logging stack, writing to
  `.github/logs/workflow.log` inside Actions when the `GH_LOGS_DIR` environment
  variable is available and falling back to stdout/stderr otherwise.  The module
  also offers a `make_specific_logger` context manager for scripts that need
  dedicated log files.
* `requirements.txt` lists the Python dependencies that must be installed inside
  the `.github` virtual environment for the tooling to run.

## Development notes

* Treat `.github` as an isolated Python project.  Install dependencies into the
  local `.venv` and point IDEs at that interpreter.
* Format code with `black` and `isort`, lint with `flake8`, and keep type hints
  up to date.
* When adding new scripts, include docstrings or README updates so their purpose
  is discoverable from this document.
* Whenever you change the behaviour of an existing tool, update the relevant
  function descriptions in this README (or linked documentation) so they remain
  accurate.
