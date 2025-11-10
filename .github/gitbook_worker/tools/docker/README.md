# Docker Tools für ERDA GitBook Worker

Docker-basierte Tools für Tests, Publishing und Workflow-Orchestrierung des ERDA-Buchs.

## Images

### ERDA Smart Worker ⭐ (Best Practice, empfohlen)
* **`Dockerfile.dynamic`** – Intelligentes, dynamisch konfiguriertes Multi-Stage-Build
  - **Docker Tag:** `erda-smart-worker`
  - Liest Konfiguration aus `fonts.yml` (Single Source of Truth)
  - Automatische License-Compliance-Prüfung (AGENTS.md)
  - Integrierte Validierung (Fonts, Tools, Packages)
  - Out-of-the-box ready mit dokumentierten Build-Artefakten
  - **Siehe:** `DOCKER_DYNAMIC_CONFIG_BEST_PRACTICE.md`

### Legacy (deprecated)
* `Dockerfile` – Multi-Stage-Build mit hardcodierten Fonts (Tag: `erda-workflow-tools`)
* `Dockerfile.python` – Base Image mit LaTeX, Fonts und Pandoc

## Schnellstart

### Mit ERDA Smart Worker (empfohlen) ⭐

```bash
# Build mit intelligenter dynamischer Konfiguration
python .github/gitbook_worker/tools/docker/run_docker.py build --use-dynamic

# Build-Informationen anzeigen
python .github/gitbook_worker/tools/docker/run_docker.py info --use-dynamic

# Tests ausführen
python .github/gitbook_worker/tools/docker/run_docker.py test --use-dynamic
```

### Direkter Docker-Build

```bash
# ERDA Smart Worker (empfohlen)
docker build -f .github/gitbook_worker/tools/docker/Dockerfile.dynamic \
             -t erda-smart-worker:latest .

# Legacy (deprecated)
docker build -f .github/gitbook_worker/tools/docker/Dockerfile \
             -t erda-workflow-tools:latest .
```

## Helper Script: `run_docker.py`

Convenience-Wrapper für Docker-Befehle. Automatisches Image-Build (mit `--pull`), 
Repository wird nach `/workspace` gemountet.

### Verfügbare Befehle

```bash
# Tests
python .github/gitbook_worker/tools/docker/run_docker.py test --use-dynamic
python .github/gitbook_worker/tools/docker/run_docker.py test-slow --use-dynamic

# Orchestrator
python .github/gitbook_worker/tools/docker/run_docker.py orchestrator --use-dynamic
python .github/gitbook_worker/tools/docker/run_docker.py orchestrator --profile ci --use-dynamic

# Build & Info
python .github/gitbook_worker/tools/docker/run_docker.py build --use-dynamic
python .github/gitbook_worker/tools/docker/run_docker.py info --use-dynamic

# Shell
python .github/gitbook_worker/tools/docker/run_docker.py shell --use-dynamic

# Rebuild ohne Cache
python .github/gitbook_worker/tools/docker/run_docker.py orchestrator --rebuild --no-cache --use-dynamic
```

### Optionen

| Option | Beschreibung |
|--------|--------------|
| `--use-dynamic` | Verwende `Dockerfile.dynamic` (Best Practice, empfohlen) |
| `--profile PROFIL` | Orchestrator-Profil (`local`, `ci`, etc.) |
| `--rebuild` | Image vor Ausführung neu bauen |
| `--no-cache` | Docker-Build ohne Layer-Cache |
| `--verbose` | Mehr Logging-Output |

### Font Integrity Check

Bei `--use-dynamic`: Automatische Validierung während des Builds:
- ✅ Font-Dateien vorhanden und Checksums korrekt
- ✅ Font-Cache aktualisiert (`fc-cache`)
- ✅ Fonts in System-Cache registriert (`fc-list`)
- ✅ License Compliance (AGENTS.md)

Bei Legacy-Dockerfile: Smoke-Test vor Orchestrator-Start:
```bash
fc-list | grep -qi 'Twemoji'
fc-list | grep -qi 'ERDA CC-BY CJK'
```

Debug mit: `python .github/gitbook_worker/tools/docker/run_docker.py shell --use-dynamic`

## ERDA Smart Worker - Intelligente Konfiguration

### Warum ERDA Smart Worker (`--use-dynamic`)?

✅ **"Smart" bedeutet:**
- Intelligente automatische Konfiguration aus `fonts.yml`
- Selbst-validierendes Setup (License, Integrität, Tools)
- Keine hardcodierten Werte im Dockerfile
- Automatische Anpassung an Konfigurationsänderungen

✅ **Vorteile:**
- Keine hardcodierten Fonts im Dockerfile
- Automatische License-Compliance (AGENTS.md: CC BY 4.0, MIT, SIL OFL 1.1)
- Integrierte Integritätstests
- Konfiguration aus `fonts.yml` (Single Source of Truth)
- Build-Artefakte dokumentiert
- **Docker Tag:** `erda-smart-worker`

### Build-Artefakte

Nach dem Build verfügbar in `/opt/gitbook_worker/reports/`:
- `docker_font_installation.json` - Installation Manifest (Fonts + Checksums)
- `docker_validation_report.json` - Validation Report (PASS/FAIL + Errors)

Anzeigen mit: `python run_docker.py info --use-dynamic`

### Vollständige Dokumentation

Siehe: **`DOCKER_DYNAMIC_CONFIG_BEST_PRACTICE.md`** für:
- Architektur und Dateifluss
- Setup & Validation Module
- License Compliance Details
- Troubleshooting Guide
- CI/CD Integration
- Migration vom Legacy-Dockerfile
