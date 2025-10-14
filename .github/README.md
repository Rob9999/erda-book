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

Follow `python-project-structure-guide.md` and `.github/agents.md` when modifying or extending this project.
