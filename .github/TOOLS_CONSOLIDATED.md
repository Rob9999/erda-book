# .github — Tools: consolidated guide and review

This consolidated document gathers the essential usage, development notes and a short code-review summary for the automation and publishing tools living under `.github/tools`.

## Purpose

Provide a single entry point for contributors and CI authors that documents:

- how to set up and run the tools locally (cross-platform),
- what the main components do (quick map),
- test and Docker guidance, and
- short code-review findings and recommended actions.

## Quick start (Windows PowerShell and macOS/Linux)

1. Create and activate a virtual environment inside `.github`:

Windows PowerShell

```powershell
cd .github
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

macOS / Linux

```bash
cd .github
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

2. Run tests locally:

```bash
cd .github
pytest -q
```

3. Run the orchestrator CLI (preferred entry point):

```bash
python -m tools.workflow_orchestrator --help
python -m tools.workflow_orchestrator --profile default --dry-run
```

Notes

- Install pinned dependencies via `pyproject.toml`/`requirements.txt` inside `.github`.
- Prefer `python -m` invocations to ensure the correct environment is used.

## Module map (short)

- `workflow_orchestrator`: preferred high-level runner that reads `publish.yml` and executes configured steps (check_if_to_publish, converter, publisher, ...).
- `publishing`: PDF builder, manifest flag management, and pipeline orchestration (`pipeline.py`, `publisher.py`, `gitbook_style.py`, `dump_publish.py`).
- `converter`: CSV -> Markdown/PNG conversion helpers.
- `quality`: QA tools that audit sources and links and provide AI-assisted reference repair.
- `emoji`: emoji scanning and font reporting utilities.
- `support`: small helpers for debugging (appendix inspector, etc.).
- `utils`: reusable helpers (docker runner, venv bootstrap, run wrapper, logging).
- `docker`: Dockerfiles used for CI images.

## Tests & CI

- Unit tests: `.github/tests/` — run with `pytest` inside the `.github` venv.
- Docker integration: build `.github/tools/docker/Dockerfile` and run tests in the container when you need a hermetic environment.
- Workflows exist in `.github/workflows/` and call the orchestrator or the publishing helper scripts as needed.

## Recommended commands (Windows PowerShell friendly)

Activate venv and run a smoke test:

```powershell
cd .github; .\.venv\Scripts\Activate.ps1; pytest -q
```

Build the Docker image used in CI (if Docker installed):

```powershell
docker build -f .github/tools/docker/Dockerfile -t erda-workflow-tools .
```

## Code review — summary (findings and recommended actions)

Key observations found while reviewing the `.github` documentation and layout:

1. Documentation overlap and fragmentation
   - Multiple README files cover overlapping information (e.g. quick start, module maps, Docker). This is safe but makes it hard to find the authoritative instruction.
   - Recommendation: keep per-module READMEs for module-specific details and use this consolidated file as the canonical quick-start and contributor guide. Add a single "See consolidated docs" pointer to each module README.

2. Inconsistent setup instructions
   - Some files use `python -m pip install -e .` while others mention `requirements.txt` or `pyproject.toml` without a canonical order.
   - Recommendation: standardise the Quick Start to prefer `pyproject.toml` + editable install for local development and include a small `./.github/setup-dev.sh` / `setup-dev.ps1` script for reproducible setup.

3. Platform-specific commands are scattered
   - PowerShell and Bash instructions sometimes appear in different files. Consolidate platform-specific blocks and clearly label them.

4. Project-specific names and secrets
   - Some docs reference an older project name and a PAT secret (`SPHERE_SPACE_STATION_EARTH_ONE_AND_BEYOND`) which may be confusing in this repo.
   - Recommendation: replace project-specific names and secret names with generic examples or document where repo-specific values must be substituted.

5. Small code hygiene items
   - `tools/__init__.py` is effectively empty. Consider adding a minimal module docstring or explicit exports, or leave as-is if intentionally blank.
   - Several READMEs are minimal; where complex CLIs exist (for example `publisher.py`), consider adding usage examples and the most common flags in the module README.

6. Testing & CI
   - Tests reference different docker images and python versions; pin recommended CI images in the consolidated doc and keep the `pytest` invocation consistent.

## Low-risk follow-ups (I can implement these if you want)

1. Add a small `./.github/setup-dev.ps1` and `setup-dev.sh` to automate venv creation and editable install.
2. Insert a one-line pointer at top of each per-module README pointing to this consolidated document.
3. Replace any hard-coded project secrets in workflow docs with placeholders and a short note where to configure them.

## Where I placed this file

`./.github/TOOLS_CONSOLIDATED.md` — this is the canonical consolidated guide. I added a shallow pointer to it at the top of `./.github/tools/README.md` so module readers find the unified guide quickly.

---

If you'd like, I can now apply the low-risk follow-ups (add setup scripts and add pointers to each module README). Which of these should I do next? Or shall I also update the workflow files to use placeholder secret names? 
