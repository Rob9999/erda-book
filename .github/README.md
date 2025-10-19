# .github Project

This directory hosts the automation and publishing toolkit that powers the Sphere Space Station project. It is a standalone Python package (`sphere-space-new-horizons-workflow-tools`) plus GitHub workflow configuration.

## Getting started

```powershell
cd .github
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

On macOS/Linux replace the activation line with `source .venv/bin/activate`.

## Tooling

- Python sources live under `tools/`.
- Tests reside in `tests/` and run with `pytest`.
- GitHub Actions workflow files stay in `workflows/`.
- VS Code picks up the project interpreter via `.vscode/settings.json`.
- Launch configurations are stored in `.vscode/launch.json`; use **Orchestrator (local)** to run the workflow locally.

Follow `python-project-structure-guide.md` and `.github/agents.md` when modifying or extending this project.

## Workflow orchestrator

The entry point `python -m tools.workflow_orchestrator` reads `publish.yml` and
executes the configured steps. Profiles live under `profiles.*` in the
manifest. Examples:

```bash
# Run the full publishing pipeline using the default profile
python -m tools.workflow_orchestrator --profile default --reset-others

# Minimal local run without touching GHCR
python -m tools.workflow_orchestrator --profile local --dry-run
```

The orchestrator keeps the behaviour of the individual helper scripts intact
and only coordinates their execution. Additional command line arguments can be
passed to the publisher via repeated `--publisher-arg` flags.

## Docker images & GHCR

`orchestrator.yml` builds the publishing container and pushes it to the GitHub
Container Registry (`ghcr.io/<owner>/<repo>/publisher`). Private repositories
build the image on-demand inside the workflow without pushing to GHCR. Caching
is configured via the registry-backed Buildx cache.

## Testing

Run `pytest` from within the `.github` directory or trigger the `python-package`
workflow manually via the `workflow_dispatch` trigger. The new orchestrator
module comes with dedicated tests under `tests/workflow_orchestrator/`.
