# ERDA Book

## Schriftarten-Design

### PDF-Generierung
Bei der PDF-Generierung werden **keine** zusätzlichen System-Emoji-Schriftarten aus externen Paketen eingebunden, um das Design konsistent mit der Markenidentität zu halten. Die Schriftarten können in der `publish.yml` über die `pdf_options` konfiguriert werden:

```yaml
pdf_options:
  emoji_color: true
  main_font: "DejaVu Serif"  # Hauptschriftart für Fließtext
  sans_font: "DejaVu Sans"   # Serifenlose Schriftart für Überschriften
  mono_font: "DejaVu Mono"   # Monospace-Schriftart für Code
```

Diese Konfiguration stellt sicher, dass das Dokumentendesign den Vorgaben entspricht.

## Docker-Namenskonfiguration

Die Docker-Image- und Container-Namen für die GitBook Worker Toolchain sind jetzt vollständig konfigurierbar und verwenden ein mehrschichtiges Merge-System.

### Quick Start

```bash
# Get Docker names for test context
./docker-names.ps1 get-name --type image --context test --publish-name space-tests

# Get all names as JSON
./docker-names.ps1 get-all-names --context docker-test --publish-name space-tests
```

### Konfigurationsebenen

1. **`.github/gitbook_worker/defaults/docker_config.yml`** - Standard-Konfiguration
2. **`docker_config.yml`** (Repo-Root) - Repository-weite Überschreibungen
3. **`publish.yml`** - `docker_config` Sektion - Allgemeine Einstellungen
4. **`publish.yml`** - Spezifischer Publish-Eintrag - Eintragsspezifische Überschreibungen

### Verfügbare Kontexte

- `github-action` - GitHub Actions CI/CD
- `prod` - Produktionsumgebung
- `test` - Lokale Tests (pytest)
- `docker-test` - Docker-basierte Integrationstests

### Template-Variablen

- `{context}` - Ausführungskontext
- `{repo_name}` - Repository-Name
- `{branch}` - Git-Branch
- `{publish_name}` - Publish-Eintragsname aus publish.yml

### Dokumentation

- **[README.md](.github/gitbook_worker/docs/docker-names-README.md)** - Vollständige API- und CLI-Dokumentation
- **[INTEGRATION.md](.github/gitbook_worker/docs/docker-names-INTEGRATION.md)** - Integrationsbeispiele für Tests, Workflows und Skripte
- **[MIGRATION.md](.github/gitbook_worker/docs/docker-names-MIGRATION.md)** - Migrationsleitfaden von hardkodierten zu konfigurierbaren Namen

### Python API

```python
from gitbook_worker.tools.docker import smart_merge

names = smart_merge.get_all_docker_names(
    repo_root=Path("/path/to/repo"),
    publish_name="space-tests",
    context="docker-test",
    extra_vars={"branch": "main"}
)

print(f"Image: {names['image']}")
print(f"Container: {names['container']}")
```