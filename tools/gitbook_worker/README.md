# gitbook-worker

To install the helper utilities run:

```bash
pip install .
```

You can then call `gitbook-worker` to process a GitBook repository.
The optional flag `--verbose` prints progress messages to the console. A log
file `gitbook_worker_<timestamp>.log` is always written to the output directory.


## 1. Upgrade notes

Version 2.0.0 of the `gitbook-worker` package consolidates the helper scripts into
an installable module. The command line interface remains compatible, but you
should reinstall the package to get the latest improvements:

```bash
pip install -U gitbook-worker
```

## 2. Dokumentation erzeugen

Um die technische Dokumentation zu erstellen, wechseln Sie in das `docs/`-Verzeichnis und rufen Sie anschließend `make html` auf:

```bash
cd tools/gitbook_worker/docs
make html
```

Die fertige HTML-Dokumentation finden Sie danach unter `tools/gitbook_worker/docs/_build/html`.
