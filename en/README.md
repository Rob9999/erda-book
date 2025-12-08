# The ERDA Book (English Version)

**Holistic framework for Europe's democratic resilience**

## 📖 About This Directory

This directory contains the **British English translation** of the ERDA Book, including all source materials, metadata, and build configurations.

### Directory Structure

```
en/
├── book.json              # GitBook configuration (English)
├── citation.cff           # Citation metadata
├── LICENSE*               # License files (CC BY-SA 4.0, MIT, etc.)
├── publish.yml            # Build & publish configuration
├── translation-plan.md    # Translation roadmap & status
├── content/               # Markdown sources
│   ├── SUMMARY.md
│   ├── README.md
│   └── [Chapters & Appendices]
└── publish/               # Generated artifacts (PDF, MD, etc.)
    ├── the-erda-book.pdf
    ├── the-erda-book.md
    ├── CITATION.cff
    └── ATTRIBUTION.md
```

## 🚀 Local Build

```bash
# Generate PDF (local profile)
cd en
python -m tools.workflow_orchestrator --root .. --manifest publish.yml --profile local

# Or via root wrapper (recommended)
cd ..
.\build-pdf.ps1 -Manifest "en\publish.yml" -WorkflowProfile local
```

## 📜 License & Attribution

- **Text/Graphics:** CC BY-SA 4.0 (see [`LICENSE`](LICENSE))
- **Code/Toolchain:** MIT (see [`LICENSE-CODE`](LICENSE-CODE))
- **Fonts:** Dual-licensed CC BY 4.0 / MIT (see [`LICENSE-FONTS`](LICENSE-FONTS))

See [`publish/ATTRIBUTION.md`](publish/ATTRIBUTION.md) for third-party content.

## 🔗 More Information

- **Deutsche Fassung:** [`../de/`](../de/)
- **Release History:** [`../Releases.md`](../Releases.md)
- **Contributors Guide:** [`../AGENTS.md`](../AGENTS.md)

---

**Translation Status:** 🚧 Work in Progress  
See [`translation-plan.md`](translation-plan.md) for details.
