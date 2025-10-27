# Tooling Migration Review

## Executive summary

- The standalone workflow suite under `.github/tools` already provides a structured orchestration layer, selective publishing pipeline, and developer helpers that are ready for reuse by GitHub Actions and local contributors.【F:.github/tools/README.md†L1-L156】【F:.github/tools/workflow_orchestrator/orchestrator.py†L1-L134】
- The legacy `tools/gitbook-worker` package duplicates many of those responsibilities, carries packaging quirks (hyphenated module name) and mixes unrelated CLIs, which prevents it from being imported cleanly in CI and makes maintenance costly.【F:tools/gitbook-worker/src/gitbook-worker/__init__.py†L12-L103】【F:tools/gitbook-worker/src/gitbook-worker/__main__.py†L36-L200】
- Migrating the unique capabilities (AI-assisted reference repair, source extraction, link checks) into dedicated subpackages inside `.github/tools` lets the Actions workflows depend on a single toolbox while retiring the root-level project.

## Findings

### `.github/tools` workflow suite

- The README documents three coherent pillars—workflow orchestration, publishing utilities, and developer helpers—along with clear entry points (`python -m tools.workflow_orchestrator`, `publishing/pipeline.py`, CSV converter).【F:.github/tools/README.md†L7-L114】
- `workflow_orchestrator/orchestrator.py` resolves `publish.yml` profiles, composes steps such as `check_if_to_publish`, `converter`, and `publisher`, and standardises environment setup, so new functionality only needs to implement another step script.【F:.github/tools/workflow_orchestrator/orchestrator.py†L1-L134】
- Helper modules already cover Docker lifecycle management and subprocess execution (`utils/docker_runner.py`, `utils/run.py`) in a cross-platform, well-logged manner, which we can leverage instead of maintaining parallel code paths.【F:.github/tools/utils/docker_runner.py†L1-L120】【F:.github/tools/utils/run.py†L9-L29】
- The publishing package owns Pandoc orchestration, Markdown preprocessing, GitBook summary maintenance, and manifest flag handling, so we should reuse these primitives rather than rebuild them elsewhere.【F:.github/tools/publishing/publisher.py†L1-L198】【F:.github/tools/publishing/preprocess_md.py†L1-L200】

### `tools/gitbook-worker` package

- The package directory is named `gitbook-worker`, forcing a compatibility shim that injects `gitbook_worker.src.gitbook_worker` into `sys.modules` to satisfy imports, a pattern that breaks packaging conventions and triggered the earlier `ModuleNotFoundError` in CI.【F:tools/gitbook-worker/src/gitbook-worker/__init__.py†L12-L103】
- The monolithic CLI (`__main__.py`) couples cloning, Docker invocation, PDF generation, linting, AI-powered citation repair, link checking, readability reports, and spellchecking behind dozens of flags, making the code hard to test or reuse piecemeal.【F:tools/gitbook-worker/src/gitbook-worker/__main__.py†L36-L200】
- Utility modules implement their own subprocess runner, Docker checks, and Pandoc command builders even though richer implementations already exist in `.github/tools`, leading to drift and duplicated bug fixes.【F:tools/gitbook-worker/src/gitbook-worker/utils.py†L25-L107】【F:tools/gitbook-worker/src/gitbook-worker/docker_tools.py†L11-L94】【F:tools/gitbook-worker/src/gitbook-worker/pandoc_utils.py†L7-L107】
- Several features are still valuable—AI-backed citation validation (`ai_tools.py`), structured source extraction (`source_extract.py`), HTTP/image link scanning (`linkcheck.py`), and Git repo cloning helpers (`repo.py`)—but they live in the legacy package and are inaccessible to the Actions tooling today.【F:tools/gitbook-worker/src/gitbook-worker/ai_tools.py†L17-L198】【F:tools/gitbook-worker/src/gitbook-worker/source_extract.py†L1-L120】【F:tools/gitbook-worker/src/gitbook-worker/linkcheck.py†L8-L93】【F:tools/gitbook-worker/src/gitbook-worker/repo.py†L22-L71】

## Migration proposal

1. **Create a `.github/tools/quality` package.**
   - Port `source_extract.py` and `linkcheck.py` into focused modules (e.g. `quality/sources.py`, `quality/link_audit.py`) that rely on `tools.logging_config` and `utils.run` for consistent logging/output.【F:tools/gitbook-worker/src/gitbook-worker/source_extract.py†L1-L120】【F:tools/gitbook-worker/src/gitbook-worker/linkcheck.py†L8-L93】【F:.github/tools/utils/run.py†L9-L29】
   - Reimplement the CLI as small entry points (`python -m tools.quality.link_audit`) so the workflow orchestrator can call them as dedicated steps.

2. **Move AI-assisted reference tooling.**
   - Translate `ai_tools.py` into `.github/tools/quality/ai_references.py`, keeping the JSON parsing, retry handling, and prompt schema logic while swapping to repository-wide logging helpers and environment configuration.【F:tools/gitbook-worker/src/gitbook-worker/ai_tools.py†L17-L198】【F:.github/tools/logging_config.py†L1-L80】
   - Add orchestrator support for an optional `ai-reference-check` step that feeds manifest-selected Markdown files into the new module, allowing CI opt-in without touching legacy code paths.【F:.github/tools/workflow_orchestrator/orchestrator.py†L29-L125】

3. **Consolidate repository and Docker helpers.**
   - Merge `repo.clone_or_update_repo` into a new `.github/tools/utils/git.py`, expressed in terms of `subprocess.run` wrappers already present, so Git interactions live next to Docker and Python workspace helpers.【F:tools/gitbook-worker/src/gitbook-worker/repo.py†L22-L71】【F:.github/tools/utils/run.py†L9-L29】
   - Replace `docker_tools.ensure_docker_image/ensure_docker_desktop` with thin adapters over `utils/docker_runner.py`, eliminating duplicated platform checks while keeping the capability to pre-build images when needed.【F:tools/gitbook-worker/src/gitbook-worker/docker_tools.py†L11-L94】【F:.github/tools/utils/docker_runner.py†L1-L120】

4. **Retire duplicate Pandoc glue.**
   - Remove `pandoc_utils.py` after migrating any missing switches into `publishing/publisher.py` or `publishing/preprocess_md.py`, ensuring all PDF builds flow through the maintained pipeline and its Lua filters/assets.【F:tools/gitbook-worker/src/gitbook-worker/pandoc_utils.py†L7-L107】【F:.github/tools/publishing/publisher.py†L34-L198】【F:.github/tools/publishing/preprocess_md.py†L1-L200】
   - For functions such as `wrap_wide_tables`, either reuse the existing preprocessing step or expose a focused helper under `publishing` if additional behaviour is required.【F:tools/gitbook-worker/src/gitbook-worker/utils.py†L175-L200】【F:.github/tools/publishing/preprocess_md.py†L1-L200】

5. **Plan the shutdown of `tools/gitbook-worker`.**
   - Once the above modules are migrated and wired into the orchestrator, delete the legacy package, keep only lightweight wrappers (e.g. CLI stubs) if external automation still imports `gitbook_worker`, and update the repository documentation to mark the root-level `tools/` folder as deprecated.【F:tools/gitbook-worker/src/gitbook-worker/__init__.py†L12-L103】【F:.github/tools/README.md†L147-L156】
   - Add regression tests inside `.github/tests` for the new quality modules to mirror the existing coverage pattern for publishing helpers.【F:.github/tests/README.md†L1-L72】

This approach lets GitHub Actions ignore the root `tools/` tree, keeps publishing and Docker topics within the already mature workflow suite, and focuses future maintenance on a single Python project.
