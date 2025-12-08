# Das ERDA Buch (Deutsche Fassung)

**Ganzheitliches Konzept zur demokratischen Resilienz Europas**

## 📖 Über dieses Verzeichnis

Dieses Verzeichnis enthält die **deutsche Originalfassung** des ERDA Buchs, einschließlich aller Quellmaterialien, Metadaten und Build-Konfigurationen.

### Verzeichnisstruktur

```
de/
├── book.json              # GitBook-Konfiguration (Deutsch)
├── citation.cff           # Zitationsmetadaten
├── LICENSE*               # Lizenzdateien (CC BY-SA 4.0, MIT, etc.)
├── publish.yml            # Build & Publish-Konfiguration
├── content/               # Markdown-Quellen
│   ├── SUMMARY.md
│   ├── README.md
│   └── [Kapitel & Anhänge]
└── publish/               # Generierte Artefakte (PDF, MD, etc.)
    ├── das-erda-buch.pdf
    ├── das-erda-buch.md
    ├── CITATION.cff
    └── ATTRIBUTION.md
```

## 🚀 Lokales Build

```powershell
# PDF generieren (lokales Profil)
cd de
python -m tools.workflow_orchestrator --root .. --manifest publish.yml --profile local

# Oder via Root-Wrapper (empfohlen)
cd ..
.\build-pdf.ps1 -Manifest "de\publish.yml" -WorkflowProfile local
```

## 📜 Lizenz & Attribution

- **Texte/Grafiken:** CC BY-SA 4.0 (siehe [`LICENSE`](LICENSE))
- **Code/Toolchain:** MIT (siehe [`LICENSE-CODE`](LICENSE-CODE))
- **Fonts:** Dual-Lizenz CC BY 4.0 / MIT (siehe [`LICENSE-FONTS`](LICENSE-FONTS))

Siehe [`publish/ATTRIBUTION.md`](publish/ATTRIBUTION.md) für Drittinhalte.

## 🔗 Weitere Informationen

- **English Version:** [`../en/`](../en/)
- **Release History:** [`../Releases.md`](../Releases.md)
- **Contributors Guide:** [`../AGENTS.md`](../AGENTS.md)
