# Migration to Multi-Language Structure (v1.0.2)

> **Status (today):** Archived / historical documentation.
> The v1.0.2 migration is complete; this file is kept for traceability. For release records, see `release-docs/`.

**Status:** ✅ Completed  
**Date:** 2025-12-08  
**Responsible:** Robert Alexander Massinger

## Overview

The ERDA Book repository has been restructured to support multiple language versions. Each language now has its own dedicated directory with independent build pipelines and metadata.

## Directory Structure Changes

### Before (v1.0.1)
```
ERDA/
├── content/              # German content (root-level)
├── publish/              # German artifacts
├── book.json             # German config
├── LICENSE*
├── CITATION.cff
└── publish.yml           # German build config
```

### After (v1.0.2)
```
ERDA/
├── de/                   # German version
│   ├── content/
│   ├── publish/
│   ├── book.json
│   ├── citation.cff
│   ├── LICENSE*
│   └── publish.yml
├── en/                   # English version
│   ├── content/
│   ├── publish/
│   ├── book.json
│   ├── citation.cff
│   ├── LICENSE*
│   └── publish.yml
├── assets/               # Shared (fonts, emojis)
├── tools/                # Shared (build toolchain)
└── README.md             # Root entry point
```

## Key Changes

### 1. Language Directories

- **`de/`**: German original ("Das ERDA Buch")
- **`en/`**: English translation ("The ERDA Book")

Each directory is self-contained with:
- `content/` (Markdown sources)
- `publish/` (generated artifacts)
- `book.json` (GitBook config)
- `citation.cff` (language-specific metadata)
- `LICENSE*` files
- `publish.yml` (build configuration)

### 2. Shared Resources

- **`assets/`**: Fonts (ERDA CC-BY CJK, Twemoji) and CSS remain on root level (language-agnostic)
- **`tools/`**: Build toolchain (`workflow_orchestrator`, `publisher`) shared across languages
- **`.github/`**: CI/CD workflows, gitbook_worker tools

### 3. CI/CD Workflow Updates

**`.github/workflows/orchestrator.yml`** now uses a matrix strategy:

```yaml
strategy:
  matrix:
    lang: [de, en]
```

Each language builds independently and commits to its own `publish/` directory.

### 4. Font Path Corrections

Updated relative paths in `publish.yml`:

```yaml
# Old (root-level)
fonts:
- path: .github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf

# New (language subdirectory)
fonts:
- path: ../.github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf
```

### 5. Documentation Updates

- **`README.md`**: Now references both `de/` and `en/` with language flags
- **`Releases.md`**: Documents multi-language structure in v1.0.2 release
- **`de/README.md`**: German-specific documentation
- **`en/README.md`**: English-specific documentation
- **`publish/README.md`**: Deprecation notice pointing to language directories

## Build Commands

### German Version

```powershell
# From root
.\build-pdf.ps1 -Manifest "de\publish.yml" -WorkflowProfile local

# Or from de/ directory
cd de
python -m tools.workflow_orchestrator --root .. --manifest publish.yml --profile local
```

### English Version

```powershell
# From root
.\build-pdf.ps1 -Manifest "en\publish.yml" -WorkflowProfile local

# Or from en/ directory
cd en
python -m tools.workflow_orchestrator --root .. --manifest publish.yml --profile local
```

## Testing

✅ German build tested and successful:
```
Built: C:\RAMProjects\ERDA\de\publish\das-erda-buch.pdf
Status: ✓ OK
```

⏳ English build: WIP (content translation ongoing)

## Attribution Updates

The three-tier attribution system remains intact:

1. **`ATTRIBUTION.md`** (root) — Machine-readable compliance source
2. **`de/content/anhang-l-kolophon.md`** / **`en/content/appendix-l-colophon.md`** — Reader-friendly (PDF)
3. **`de/content/anhang-j-lizenz-and-offenheit.md`** / **`en/content/appendix-j-license-openness.md`** — License philosophy

Path references in `README.md` updated to reflect new structure.

## Breaking Changes

⚠️ **Important:** Any external scripts or workflows referencing the old structure must be updated:

- `content/` → `de/content/` or `en/content/`
- `publish/` → `de/publish/` or `en/publish/`
- `book.json` → `de/book.json` or `en/book.json`

## Rollback Instructions

If issues arise, revert to v1.0.1 structure:

```powershell
# Restore German content to root
Move-Item de\content content
Move-Item de\publish publish
Copy-Item de\book.json .
Copy-Item de\publish.yml .
Remove-Item de -Recurse -Force
```

## Next Steps

1. ✅ Finalize German migration (completed)
2. 🚧 Complete English translation (`en/content/`)
3. 📋 Update GitHub Actions workflows for matrix builds
4. 📚 Document translation workflow (`translation_instruction.md`)
5. 🚀 Test end-to-end build for both languages in CI/CD

## References

- **Release History:** [`release-docs/Releases.md`](release-docs/Releases.md)
- **Contributors Guide:** [`AGENTS.md`](AGENTS.md)
- **Translation Workflow:** [`translation-instruction.md`](translation-instruction.md)

---

**Signed-off-by:** Robert Alexander Massinger <ram@erda-initiative.org>
