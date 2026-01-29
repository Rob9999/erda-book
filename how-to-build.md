# How to build (DE/EN) – local + Docker

This document is the **single source of truth** for build commands.
It is aligned with `.vscode/launch.json` (configs: *Orchestrator (local) - German/English* and *Orchestrator (ERDA Smart Worker)*).

## Outputs

- German PDF: `de/publish/das-erda-buch.pdf`
- English PDF: `en/publish/the-erda-book.pdf`

## Prerequisites

- Python (recommended: 3.11.x)
- Docker Desktop / Docker Engine (only for Docker-based builds)

> Important: Use the repository virtual environment (`.venv`) when running the orchestrator.
> Using a global Python can accidentally pick up unrelated tooling and fail in non-obvious ways.

### Environment variables (same as VS Code launch configs)

The VS Code launch configs set these for reproducible UTF-8 behaviour:

- `PYTHONIOENCODING=utf-8`
- `PYTHONUTF8=1`
- `PYTHONNOUSERSITE=1`

You normally do not need to set them manually, but if you run from a terminal and see encoding/path oddities, set them for that session.

## VS Code (recommended)

Use **Run and Debug** and pick one of:

- `Orchestrator (local) - German`
- `Orchestrator (local) - English`
- `Orchestrator (ERDA Smart Worker)` (Docker-based)
- `Orchestrator (ERDA Smart Worker - fresh rebuild)` (Docker-based, forces rebuild)

These configurations already set `cwd`, `env`, and `args` correctly.

---

## Local build (Windows)

### 1) Create venv + install deps

PowerShell:

```powershell
Set-Location -Path "<YOUR_REPO_ROOT>"

# optional but recommended (mirrors .vscode/launch.json)
$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
$env:PYTHONNOUSERSITE = "1"

# create venv if missing
if (-not (Test-Path ".\.venv\Scripts\python.exe")) { py -3.11 -m venv .venv }
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `py -3.11` is not available, use `py -3` (and ensure it resolves to Python 3.11+).

### 2) Build German (local profile)

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root "$PWD" --manifest "de/publish.yml" --profile local --content-config "content.yaml" --lang de
```

### 3) Build English (local profile)

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root "$PWD" --manifest "en/publish.yml" --profile local --content-config "content.yaml" --lang en
```

---

## Local build (Linux)

### 1) Create venv + install deps

```bash
cd /path/to/ERDA
python3.11 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
```

### 2) Build German (local profile)

```bash
./.venv/bin/python -m gitbook_worker.tools.workflow_orchestrator run --root "$(pwd)" --manifest "de/publish.yml" --profile local --content-config "content.yaml" --lang de
```

### 3) Build English (local profile)

```bash
./.venv/bin/python -m gitbook_worker.tools.workflow_orchestrator run --root "$(pwd)" --manifest "en/publish.yml" --profile local --content-config "content.yaml" --lang en
```

---

## Local build (macOS)

Same as Linux.

If you installed Python via Homebrew, you may have `python3.11` available; otherwise use `python3` if it points to 3.11.

---

## Docker-based build (DE/EN)

Docker builds run the orchestrator via `gitbook_worker.tools.docker.run_docker`.
This matches the VS Code config **Orchestrator (ERDA Smart Worker)**.

### 1) Prerequisites

- Docker is running
- You have a working Python environment with `gitbook_worker` installed (use `.venv`)

### 2) Build German (default profile, Docker)

```bash
./.venv/bin/python -m gitbook_worker.tools.docker.run_docker orchestrator --profile default --use-dynamic --manifest de/publish.yml --lang de
```

Windows PowerShell equivalent:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.docker.run_docker orchestrator --profile default --use-dynamic --manifest de/publish.yml --lang de
```

### 3) Build English (default profile, Docker)

```bash
./.venv/bin/python -m gitbook_worker.tools.docker.run_docker orchestrator --profile default --use-dynamic --manifest en/publish.yml --lang en
```

Windows PowerShell equivalent:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.docker.run_docker orchestrator --profile default --use-dynamic --manifest en/publish.yml --lang en
```

### 4) Fresh rebuild (Docker)

Use this if Docker caches got stale:

```bash
./.venv/bin/python -m gitbook_worker.tools.docker.run_docker orchestrator --profile default --use-dynamic --manifest de/publish.yml --lang de --rebuild --no-cache
```

Windows PowerShell equivalent:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.docker.run_docker orchestrator --profile default --use-dynamic --manifest de/publish.yml --lang de --rebuild --no-cache
```

---

## Troubleshooting

### “It works in VS Code, but fails in the terminal”

Most commonly: terminal uses the wrong Python.

- Expected (from `.vscode/launch.json`): `.venv/Scripts/python.exe` (Windows) or `./.venv/bin/python` (Linux/macOS)
- Avoid: `C:\Python311\python.exe` or any other global Python

### Where do outputs go?

See the `out_dir` in `de/publish.yml` / `en/publish.yml`:

- DE: `de/publish/das-erda-buch.pdf`
- EN: `en/publish/the-erda-book.pdf`
