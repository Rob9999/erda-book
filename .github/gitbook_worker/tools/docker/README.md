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
