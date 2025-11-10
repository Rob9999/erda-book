# Docker Workflow Image

Dockerfiles used to reproduce the CI environment for
`.github/gitbook_worker/tools`.

## Images

* `Dockerfile` – multi-stage build that installs the tool suite along with the
  test dependencies.  Use it to run pytest in a hermetic environment.
* `Dockerfile.python` – base image with LaTeX tooling, fonts and Pandoc required
  by the publishing pipeline.

## Build commands

```bash
# Build the main workflow image
docker build -f .github/gitbook_worker/tools/docker/Dockerfile -t erda-workflow-tools .

# Build the publishing base image
docker build -f .github/gitbook_worker/tools/docker/Dockerfile.python -t erda-workflow-python .
```

Push images to GitHub Container Registry after verifying tests locally.  Keep
this README in sync with the workflow definitions so contributors can reproduce
CI behaviour on their machines.

## Helper script (`run_docker.py`)

Use the convenience wrapper to execute tests or the orchestrator inside the
workflow image.  The script automatically builds the Docker image (with
`--pull`) when needed and mounts the repository into `/workspace`.

```bash
# Run unit tests inside the container
python .github/gitbook_worker/tools/docker/run_docker.py test

# Run the orchestrator with the default profile (includes a Twemoji smoke test)
python .github/gitbook_worker/tools/docker/run_docker.py orchestrator

# Force a clean rebuild without Docker cache before running the orchestrator
python .github/gitbook_worker/tools/docker/run_docker.py orchestrator --rebuild --no-cache
```

### Font integrity smoke test

Before the orchestrator starts, the wrapper executes

```bash
fc-list | grep -qi 'Twemoji'
fc-list | grep -qi 'ERDA CC-BY CJK'
```

If either check fails, the command aborts immediately so developers can rebuild
the image or investigate missing font installations before Pandoc runs.  Run
the commands manually inside the container (`python ... run_docker.py shell`)
to debug font discovery issues.
