# 🇩🇪 Release 1.0.2 – 1. Januar 2026

**Verantwortlich:**
Robert Alexander Massinger (Lead)
mit Unterstützung von ChatGPT / OpenAI für Übersetzungen

## Zielsetzung

**Technisch**

* Aufbau eines klaren **Übersetzungs-Workspaces** als Grundlage für kommende Release-Zyklen
* Angleichung und Dokumentation von **Metadaten- und Übersetzungsregeln**
* Auslagerung des `gitbook_worker` in ein **pip-installierbares Paket**
* **Neuorganisation des Repositories**:

  * `/de` – Deutsche Fassung
  * `/en` – Englische Fassung

**Inhaltlich**

* Veröffentlichung der **britisch-englischen Ausgabe**: *“The ERDA Book”*
* Jede Sprachversion erhält eine **vollständig eigenständige Struktur**, inklusive:

  * Lizenzierung
  * Zitierempfehlung
  * `publish.yml`
  * Attribution
  * Zertifizierung
  * Release-Beschreibung

## Highlights

* 🔖 Versionsupdate auf **1.0.2**
* 🌍 **Mehrsprachige Repository-Struktur** (`/de`, `/en`)
* 🧩 **Dedizierte Build-Pipelines pro Sprache**
  (Inhalte, Lizenzen, Zitation, Publisher-Konfiguration)
* 📘 Formeller Übersetzungs-Workflow (`translation_instruction.md`)
* 🕒 Repository-weite, konsolidierte **Release-Historie**
* ⚙️ **Matrix-basierte CI/CD-Workflows** für parallele Sprach-Builds

> Dieses Release schafft die strukturelle Grundlage für eine langfristig skalierbare, nachvollziehbare und zitierfähige Mehrsprachen-Publikation des ERDA-Buchs.