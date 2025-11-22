# ERDA Book (Published Branch)

Dieser Branch spiegelt den **veröffentlichten Stand** des ERDA Buches wider.

- **Version:** 1.0.1
- **Archivierung:** Zenodo (inkl. DOI)
- **Veröffentlichte PDF-Datei:** liegt im Ordner `publish` als `das-erda-buch.pdf`.

Offenes Buchprojekt zur strategischen, ethischen und technologischen Erneuerung Europas. Version 1.0.1 enthält ein technisch überarbeitetes PDF (konsistente Schriften, optimierte Typografie, saubere Inhaltsverzeichnisse) und reproduzierbare Quellen. Texte: CC BY-SA 4.0; Code: MIT; Fonts: CC BY 4.0 oder MIT (Dual-Lizenz). Details in `ATTRIBUTION.md` und Anhang J.

> Hinweis: Für inhaltliche Weiterentwicklung (Version 2.0.0 ff.) ist der Branch `release_candidate` maßgeblich; `published` bleibt der eingefrorene, veröffentlichte Stand.

## 📥 Zugriff auf die veröffentlichte PDF-Version

- **Lokal im Repo:**
   - `publish/das-erda-buch.pdf` -> [das-erda-buch.pdf](publish/das-erda-buch.pdf)
- **Zenodo:**
   - DOI: https://doi.org/10.5281/zenodo.17618845

Der obige DOI verweist auf die bei Zenodo archivierte Version 1.0.1 des ERDA Buches.

## 📜 Attribution und Lizenzierung

Dieses Projekt verwendet ein **Drei-Ebenen-System** für Transparenz und Rechtssicherheit:

### Attribution-Hierarchie

1. **`ATTRIBUTION.md`** (Repository) — **Primärquelle** für Compliance
   - Maschinenlesbare Tabelle aller Drittinhalte (Fonts, Emojis, Assets)
   - Wird von CI/CD-Tools geprüft
   - **Zielgruppe:** Entwickler, Maintainer, Rechtsprüfung

2. **`content/anhang-l-kolophon.md`** (PDF-Buch) — **Leserfreundlich**
   - Narrative Font-Attribution für PDF-Leser
   - Produktionsdetails (TeX Live, Pandoc, Build-Umgebung)
   - **Zielgruppe:** Buchleser ohne Repo-Zugriff

3. **`content/anhang-j-lizenz-and-offenheit.md`** (Konzept) — **Lizenzphilosophie**
   - Rechtliche Rahmenbedingungen und Share-Alike-Prinzip
   - **Zielgruppe:** Rechtsinteressierte, KI-Trainer, Remix-Projekte

### ⚠️ Wichtig: Bei Änderungen an Fonts/Emojis/Assets

**Alle drei Ebenen aktualisieren:**
1. ✅ `ATTRIBUTION.md` → Neue Zeile in Tabelle
2. ✅ `content/anhang-l-kolophon.md` → Abschnitt L.2 Typografie
3. ✅ `content/anhang-j-lizenz-and-offenheit.md` → Lizenzmatrix prüfen
4. ✅ Commit mit `Signed-off-by:` (DCO)

Details siehe [`AGENTS.md`](AGENTS.md) → "Attribution-Hierarchie".

---

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

Die folgende Sektion richtet sich primär an **Entwickler:innen und Maintainer:innen** und beschreibt die technische Toolchain zur PDF-Erstellung. Für Leser:innen, die nur das Buch bzw. den DOI nutzen möchten, ist dieser Abschnitt nicht relevant.

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

---

## Zitierempfehlung

Wenn Sie das ERDA Buch zitieren möchten, verwenden Sie bitte vorzugsweise den Zenodo-Eintrag mit DOI:

> ERDA-Initiative (2025): *Das ERDA Buch – Europäische Resilienz, Demokratie und Allmende*. Version 1.0.1. Zenodo. https://doi.org/10.5281/zenodo.17618845

Für maschinelle Auswertungen (z. B. LaTeX/BibTeX) steht im Repository zusätzlich `CITATION.cff` zur Verfügung.