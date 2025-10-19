# GitHub Tools

Utility scripts used by the repository's workflows.

This directory groups helper scripts, such as publishing utilities.

## Orchestrator

- `workflow_orchestrator/` – CLI module that ties together the legacy helper
  scripts. Use `python -m tools.workflow_orchestrator --help` for the available
  options. Profiles are read from the repository `publish.yml`.

## Modules

- `table_pdf.py` – export tables to PDF and pick the next larger paper size (A4→A1) when needed.
