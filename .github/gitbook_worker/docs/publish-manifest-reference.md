<!-- License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) -->
# `publish.yml` Referenz & Bereitstellungsstrategien

Die `publish.yml` steuert, welche Inhalte der `gitbook-worker` verarbeitet, wie Profile
aufgebaut sind und welche Ausgabeformate erzeugt werden. Dieses Dokument fasst alle
unterstützten Schlüssel zusammen, erläutert Standardwerte und zeigt Beispiel-Manifesten.
Abschließend folgen Vorschläge, wie das Package in eigenständige Veröffentlichungsformen
überführt werden kann.

## Struktur der Datei

Eine gültige Manifest-Datei besteht aus vier Ebenen:

```yaml
version: 0.1.0
profiles: { ... }
meta: { ... }
publish: [ ... ]
```

### `version`

* **Pflichtfeld**. Muss eine SemVer-Angabe ≥ `0.1.0` sein; Major-Versionen ungleich `0`
  werden aktuell abgewiesen. Die Publisher-Skripte brechen ab, wenn das Feld fehlt oder
  außerhalb des unterstützten Bereichs liegt.【F:.github/tools/publishing/publisher.py†L588-L633】

### `profiles`

Profile definieren, welche Orchestrator-Schritte laufen und wie Docker genutzt wird.
Fehlt der Abschnitt, greift ein eingebautes `default`-Profil mit den Schritten
`check_if_to_publish`, `ensure_readme`, `update_citation`, `converter`,
`engineering-document-formatter` und `publisher` sowie deaktiviertem Registry-Zugriff.【F:.github/tools/workflow_orchestrator/orchestrator.py†L30-L263】

Jedes Profil-Objekt unterstützt folgende Schlüssel:

| Schlüssel | Typ | Beschreibung |
| --- | --- | --- |
| `description` | string | Optionale Beschreibung für Menschen. |
| `steps` | Liste[string] | Überschreibt die Schritt-Reihenfolge; leere oder fehlende Liste nutzt die Default-Schritte.【F:.github/tools/workflow_orchestrator/orchestrator.py†L234-L239】 |
| `docker.use_registry` | bool | Nutzt vorgebaute Images anstelle lokaler Builds.【F:.github/tools/workflow_orchestrator/orchestrator.py†L241-L245】 |
| `docker.image` | string | Voll qualifizierter Image-Name; Templates wie `${repo}` werden aufgelöst.【F:.github/tools/workflow_orchestrator/orchestrator.py†L234-L256】 |
| `docker.cache` | bool | Aktiviert Build-Cache-Hints für lokale Container-Läufe.【F:.github/tools/workflow_orchestrator/orchestrator.py†L241-L245】 |
| `env` | Mapping | Zusätzliche Umgebungsvariablen für alle Schritte; andere Typen führen zu einem Fehler.【F:.github/tools/workflow_orchestrator/orchestrator.py†L248-L261】 |

Neben den Standard-Schritten existieren zusätzliche Handler wie `ai-reference-check`, die
falls gewünscht in die `steps`-Liste aufgenommen werden können.【F:.github/tools/workflow_orchestrator/orchestrator.py†L356-L418】【F:.github/tools/workflow_orchestrator/orchestrator.py†L510-L564】

### `meta`

Der Abschnitt bündelt Workflow-Metadaten und ist frei erweiterbar. Empfohlene Schlüssel:

* `publish_on` – Liste der GitHub-Ereignisse (z. B. `push`, `workflow_dispatch`), die den
  Workflow auslösen sollen.
* `artifacts.keep_days` – Anzahl der Tage, die Build-Artefakte aufbewahrt werden sollen.

Aktuell liest der Code diese Werte nicht direkt ein, sie dienen jedoch als
Single-Source-of-Truth für Workflow-Dateien.

### `publish`

Der Herzstück-Bereich beschreibt jede zu bauende Publikation. Nur Einträge mit
`build: true` werden verarbeitet.【F:.github/tools/publishing/publisher.py†L748-L816】

Pflichtfelder je Eintrag:

* `path` – Quelldatei oder -ordner relativ zur Manifest-Datei.【F:.github/tools/publishing/publisher.py†L763-L773】
* `out` – Name der Ziel-Datei inklusive Erweiterung (derzeit ausschließlich PDF).【F:.github/tools/publishing/publisher.py†L763-L774】【F:.github/tools/publishing/publisher.py†L1567-L1573】

Optionale Felder (mit Standardwerten):

| Schlüssel | Standard | Wirkung |
| --- | --- | --- |
| `build` | `false` | Muss aktiv auf `true` gesetzt werden, damit der Eintrag gebaut wird.【F:.github/tools/publishing/publisher.py†L759-L761】 |
| `out_dir` | `publish/` relativ zum Manifest | Überschreibt den Ausgabepfad; absolute Pfade sind möglich.【F:.github/tools/publishing/publisher.py†L769-L778】【F:.github/tools/publishing/publisher.py†L1575-L1581】 |
| `out_format` | `pdf` | Andere Formate werden aktuell abgelehnt.【F:.github/tools/publishing/publisher.py†L774-L775】【F:.github/tools/publishing/publisher.py†L1568-L1573】 |
| `source_type` | auto | Erzwingt `file` oder `folder`. Ohne Angabe wird anhand des Pfads entschieden.【F:.github/tools/publishing/publisher.py†L774-L783】【F:.github/tools/publishing/publisher.py†L1404-L1444】 |
| `source_format` | `markdown` | Reserviert für alternative Quelltypen (noch experimentell).【F:.github/tools/publishing/publisher.py†L774-L783】 |
| `use_summary` | `false` | Bei Ordnern: GitBook `SUMMARY.md` berücksichtigen, um Reihenfolgen zu übernehmen.【F:.github/tools/publishing/publisher.py†L774-L785】【F:.github/tools/publishing/publisher.py†L1617-L1633】 |
| `use_book_json` | `false` | Liest Titel/Metadaten aus `book.json` ein.【F:.github/tools/publishing/publisher.py†L774-L785】【F:.github/tools/publishing/publisher.py†L1322-L1379】 |
| `keep_combined` | `false` | Behält die zusammengeführte Markdown-Datei für Debugging.【F:.github/tools/publishing/publisher.py†L774-L785】【F:.github/tools/publishing/publisher.py†L1364-L1399】 |
| `summary_mode` | `null` | Steuert `gitbook_style.summary` (z. B. `gitbook` oder `legacy`).【F:.github/tools/publishing/publisher.py†L774-L787】【F:.github/tools/publishing/publisher.py†L1575-L1620】 |
| `summary_order_manifest` | `null` | Pfad zu einer alternativen Reihenfolge-Definition.【F:.github/tools/publishing/publisher.py†L774-L787】【F:.github/tools/publishing/publisher.py†L1585-L1592】 |
| `summary_manual_marker` | `DEFAULT_MANUAL_MARKER` | Marker für manuell gepflegte Bereiche.【F:.github/tools/publishing/publisher.py†L774-L787】【F:.github/tools/publishing/publisher.py†L1593-L1597】 |
| `summary_appendices_last` | `false` | Verschiebt Anhänge ans Ende der Navigation.【F:.github/tools/publishing/publisher.py†L774-L788】【F:.github/tools/publishing/publisher.py†L1627-L1629】 |
| `assets` | `[]` | Zusätzliche Ressourcen (z. B. Bilderverzeichnisse). Pfade werden relativ zum Manifest bzw. Eintrag aufgelöst.【F:.github/tools/publishing/publisher.py†L791-L815】【F:.github/tools/publishing/publisher.py†L706-L742】 |
| `pdf_options` | `{}` | Überschreibt Pandoc-Schriften und Emoji-Rendering; erlaubt `emoji_color`, `main_font`, `sans_font`, `mono_font`, `mainfont_fallback`.【F:.github/tools/publishing/publisher.py†L665-L703】【F:.github/tools/publishing/publisher.py†L1604-L1615】 |
| `reset_build_flag` | `false` | Setzt nach erfolgreichem Build `build: false`, entweder via Hilfsskript oder Manifest-Schreibzugriff.【F:.github/tools/publishing/publisher.py†L774-L789】【F:.github/tools/publishing/publisher.py†L1634-L1660】 |

## Beispiel-Manifest-Varianten

### Minimaler Einzel-Build

```yaml
version: 0.1.0
publish:
  - build: true
    path: docs/book
    out: erda-book.pdf
    use_summary: true
    keep_combined: true
```

### Profilgesteuerter Workflow mit QA-Schritt

```yaml
version: 0.1.0
profiles:
  default:
    description: Vollständiger CI-Lauf inkl. Referenzprüfung
    steps:
      - check_if_to_publish
      - ensure_readme
      - update_citation
      - ai-reference-check
      - converter
      - engineering-document-formatter
      - publisher
    docker:
      use_registry: true
      image: ghcr.io/${repo}/publisher
      cache: true
publish:
  - build: true
    path: ./
    out: artefact.pdf
    source_type: folder
    use_summary: true
    summary_appendices_last: true
    pdf_options:
      emoji_color: true
      main_font: "IBM Plex Serif"
      mainfont_fallback: "Segoe UI Emoji:mode=harf"
```

### Lokales Testprofil und separates Artefakt-Verzeichnis

```yaml
version: 0.1.0
profiles:
  default:
    steps:
      - converter
      - publisher
  local-test:
    description: Publisher ohne Registry-Image für lokale Iterationen
    steps:
      - converter
      - publisher
    docker:
      use_registry: false
publish:
  - build: true
    path: content/whitepaper.md
    out: whitepaper.pdf
    source_type: file
    out_dir: build/pdf
    keep_combined: true
    assets:
      - path: assets/diagrams
        copy_to_output: true
```

## Strategien für die zukünftige Veröffentlichung des `gitbook-worker`

Da das Toolkit mittelfristig als eigenständiges Produkt erscheinen soll, bieten sich
mehrere Paketierungs- und Distributionsansätze an:

1. **Side-Package im `.github`-Ordner** – Den aktuellen Code unter
   `.github/gitbook_worker` als versionierten Download veröffentlichen (z. B. per
   GitHub Release). Vorteil: Konsumenten können das Bundle direkt in ihre Projekte
   kopieren, ohne den kompletten `erda-book`-Inhalt zu übernehmen.
2. **Dedizierte GitHub-Action** – Aus den bestehenden Orchestrator- und Publisher-Skripten
   eine Composite-Action bauen, die `publish.yml` akzeptiert. Damit ließen sich Workflows
   via `uses: erda-foundation/gitbook-worker@vX` integrieren, während die Python-Tools im
   Repository verbleiben.【F:.github/tools/workflow_orchestrator/orchestrator.py†L310-L353】【F:.github/tools/publishing/pipeline.py†L101-L198】
3. **Python-Package (PyPI & GitHub Releases)** – Die Module aus `.github/tools` in ein
   reguläres Paket extrahieren, inklusive CLI-Einstiegspunkten (`workflow-orchestrator`,
   `gitbook-publisher`). Tests können gemeinsam mit dem Paket verteilt werden, indem sie
   in einen `tests/`-Ordner unter `.github/gitbook_worker` umziehen und in `pyproject.toml`
   referenziert werden.
4. **Hybrid-Ansatz** – Kombination aus PyPI-Paket und leichtgewichtiger GitHub-Action,
   welche das Paket installiert und den Orchestrator ausführt. Dadurch bleiben die Tests
   lokal reproduzierbar, während CI-Konsumenten nur eine Action einbinden müssen.

### Abgrenzung & Code-Bündelung

> **Empfehlung zur Code-Bündelung:** Für alle Varianten empfiehlt es sich, die vorhandenen
> Tools und zugehörigen Tests in den Ordner `.github/gitbook_worker` zu verschieben oder per
> Packaging-Skripten zu bündeln. So entsteht eine klar abgrenzbare Codebasis, die unabhängig
> vom Buch-Content versioniert und dokumentiert werden kann.【F:.github/tools/publishing/README.md†L12-L37】【F:.github/tools/workflow_orchestrator/README.md†L8-L31】
