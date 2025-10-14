# Tests of the .github/tools

Unit and integration tests for publishing and conversion tools.  
The integration suite ensures Markdown documents in `docs/public/documents` can be rendered to PDF with Pandoc.

The suite also includes a Docker integration test that builds the image from `.github/tools/docker` and executes all tests inside that container.

---

## Tests without docker container

### A single test
```bash
python -m pytest .github/tests/test_documents_publishing.py -v
```

### All tests

```bash
python -m pytest .github/tests/ -v
```

---

## Tests with docker container

### Test local (non-GitHub workflow)

#### Build docker container for tests

```bash
docker build -f .github/tools/docker/Dockerfile -t sphere-space-workflow-tools-tests .
```

#### Run the tests inside docker container

##### A single test

```bash
docker run --rm -v "${PWD}:/workspace" -e PYTHONPATH=/workspace sphere-space-workflow-tools-tests python3 -m pytest .github/tests/test_documents_publishing.py -v
```

##### All tests

```bash
docker run --rm -v "${PWD}:/workspace" -e PYTHONPATH=/workspace sphere-space-workflow-tools-tests python3 -m pytest .github/tests/ -v
```

**or**

```bash
docker exec -it -e INSIDE_DOCKER=1 -e PYTHONPATH=/workspace -e PYTHONIOENCODING=utf-8 -e LC_ALL=C.UTF-8 -e LANG=C.UTF-8 sphere-space-workflow-tools-tests-container bash -c "PYTHONPATH=/workspace/.github/tools/publishing pytest -v --tb=long --showlocals --no-header --capture=no /workspace/.github/tests/"
```

---

### Test inside GitHub workflow engine

#### Run the tests inside docker container

##### A single test

```bash
docker run -v "${PWD}:/workspace" -w /workspace ghcr.io/actions/python:3.10.12 pytest .github/tests/test_documents_publishing.py -v
```

##### All tests

```bash
docker run -v "${PWD}:/workspace" -w /workspace ghcr.io/actions/python:3.10.12 pytest .github/tests/ -v
```

