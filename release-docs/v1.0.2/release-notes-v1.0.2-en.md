# The ERDA Book – Release v1.0.2

**Date:** 2026-01-01  
**Tag:** `v1.0.2`  
**Author:** Robert Alexander Massinger (with ChatGPT/OpenAI)

---

## 📋 Summary

Version 1.0.2 delivers the complete British English edition and consolidates the bilingual structure (de/en). The release documentation now also includes an English short description.

---

## ✨ Changes

### Content and Structure
- **Complete EN edition & structure:** British English provided as a full edition; repository consistently split into `/de` and `/en`, each with its own publication files.

### Build / Tooling
- The GitBook worker is now an external package and no longer part of the ERDA Book repository.

### Release Documentation
- **New EN description:** An English short summary of the release contents has been added.

---

## 📦 Multilingual Versions in This Release

- de  
- en (British)

---

## 📜 Licensing

No changes to the licensing matrix:

| Category | Licence |
|----------|---------|
| Texts, graphics, diagrams | CC BY-SA 4.0 |
| Code, toolchain, scripts | MIT |
| Self-developed fonts | CC BY 4.0 or MIT |
| Emojis (Twemoji) | CC BY 4.0 |

---

## 🐛 Known Limitations
- CI workflows for 1.0.2 have not yet been re-run.

---

## 🔜 Next Steps
1. Run the orchestrator with the correct `PYTHONPATH` from `.venv` for EN/DE and regenerate the PDF.
2. Execute CI workflows on `release_candidate` for 1.0.2.
3. Set tag `v1.0.2` and publish on Zenodo.

---

**Licence of this release document:** CC BY-SA 4.0  
**Copyright:** © 2026 Robert Alexander Massinger
