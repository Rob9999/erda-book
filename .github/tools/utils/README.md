# Shared Utilities

Reusable helpers for subprocess execution, Docker orchestration and virtual
environment management.

## Modules

| Module | Description |
| --- | --- |
| `run.py` | Wrapper around `subprocess.run` that standardises logging, environment merging and error handling. |
| `docker_runner.py` | Builds (if necessary) and runs Docker containers with a bind-mounted workspace. Attempts to start Docker Desktop on Windows or the daemon on Linux. |
| `docker.py` | Helper functions used by the runner to build images and manage bind mounts. |
| `python_workspace_runner.py` | Creates a `.venv` inside a target workspace, installs dependencies via `pip`, `requirements.txt` files or `uv`, and executes a command/module inside that environment. |
| `git.py` | Utilities for resolving repository metadata (e.g. the current commit) when running inside CI. |

## Usage examples

Run a command with logging and strict error handling:

```python
from tools.utils import run

run(["pytest", "-q"], cwd=".github", check=True)
```

Execute a script inside a temporary virtual environment:

```bash
python -m tools.utils.python_workspace_runner \
  --workspace .github \
  --module tools.workflow_orchestrator \
  -- --profile default --dry-run
```

## Development notes

* Prefer pathlib paths when extending these utilities.
* Update callers in `workflow_orchestrator` if function signatures change.
* Document new subcommands here so other modules can adopt them quickly.
