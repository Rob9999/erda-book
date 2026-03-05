# Release-Versionierungscheckliste / Release Versioning Checklist

> **Zweck:** Diese Datei listet **alle** Dateien, die bei einem Versionswechsel aktualisiert werden müssen.
> Wird als verbindliche Prüfliste bei jedem Release verwendet.
>
> **Purpose:** This file lists **all** files that must be updated on a version change.
> Used as a binding checklist for every release.

**Letzte Aktualisierung / Last updated:** 2026-03-05 (v2.5.0-rc1)

---

## 1. Versions- und Datumsfelder / Version and date fields

| # | Datei / File | Feld(er) / Field(s) | Beispiel / Example |
|---|---|---|---|
| 1 | `README.md` | Badge-URL, **Current version**, **As of (date)**, **Codename**, ToC-Einträge (DE+EN), Release-Überschriften (DE+EN) | `v2.5.0-rc1`, `2026-03-05` |
| 2 | `CITATION.cff` (Root) | `version`, `date-released` | `"2.5.0-rc1"`, `'2026-03-05'` |
| 3 | `de/CITATION.cff` | `version`, `date-released` | wie Root |
| 4 | `en/CITATION.cff` | `version`, `date-released` | wie Root |
| 5 | `de/publish/CITATION.cff` | `version`, `date-released` | wie Root |
| 6 | `en/publish/CITATION.cff` | `version`, `date-released` | wie Root |
| 7 | `de/book.json` | `"date"` | `"2026-03-05"` |
| 8 | `en/book.json` | `"date"` | `"2026-03-05"` |
| 9 | `de/publish.yml` | `project.version` | `2.5.0-rc1` |
| 10 | `en/publish.yml` | `project.version` | `2.5.0-rc1` |
| 11 | `.zenodo.json` | `"version"` | `"2.5.0-rc1"` |

---

## 2. Release-Dokumentation / Release documentation

| # | Datei / File | Aktion / Action |
|---|---|---|
| 12 | `release-docs/Releases.md` | Neuen Eintrag oben einfügen / Add new entry at top |
| 13 | `release-docs/v{X.Y.Z}/README.md` | Ordner + Index anlegen / Create folder + index |
| 14 | `release-docs/v{X.Y.Z}/release-plan-v{X.Y.Z}.md` | Release-Plan erstellen / Create release plan |
| 15 | `release-docs/v{X.Y.Z}/release-notes-v{X.Y.Z}.md` | Release Notes DE / Create DE release notes |
| 16 | `release-docs/v{X.Y.Z}/release-notes-v{X.Y.Z}-en.md` | Release Notes EN / Create EN release notes |
| 17 | `release-docs/v{X.Y.Z}/RELEASE-{X.Y.Z}-STATUS.md` | Status-Checkliste / Status checklist |

---

## 3. Bedingte Aktualisierungen / Conditional updates

Diese Dateien müssen nur aktualisiert werden, wenn sich der jeweilige Inhalt ändert:

| # | Datei / File | Bedingung / Condition |
|---|---|---|
| 18 | `.zenodo.json` → `"description"` | Bei neuem Zenodo-Upload: HTML-Beschreibung aktualisieren |
| 19 | `de/content/anhang-j-lizenz---offenheit.md` | Bei Lizenz-/Font-/Emoji-Änderungen |
| 20 | `en/content/appendix-j-license-and-openness.md` | Bei Lizenz-/Font-/Emoji-Änderungen |
| 21 | `de/content/anhang-l-kolophon.md` | Bei Font-/Tooling-/Build-Änderungen |
| 22 | `en/content/appendix-l-colophon.md` | Bei Font-/Tooling-/Build-Änderungen |
| 23 | `ATTRIBUTION.md` | Bei neuen Drittinhalten (Fonts, Emojis, Assets) |

---

## 4. Artefakte (nach Content-Freeze) / Artifacts (post content-freeze)

| # | Datei / File | Aktion / Action |
|---|---|---|
| 24 | `de/publish/das-erda-buch.md` | Neu generieren / Regenerate |
| 25 | `de/publish/das-erda-buch.pdf` | Neu generieren / Regenerate |
| 26 | `en/publish/the-erda-book.md` | Neu generieren / Regenerate |
| 27 | `en/publish/the-erda-book.pdf` | Neu generieren / Regenerate |

---

## 5. Konsistenzregel / Consistency rule

Gemäß `AGENTS.md` und `how-to-release.md`:

- Das **As of**-Datum in `README.md` **muss** mit `de/book.json` → `"date"` und `en/book.json` → `"date"` übereinstimmen.
- Alle 5 `CITATION.cff`-Dateien **müssen** denselben `version`- und `date-released`-Wert haben.
- Die `project.version` in `de/publish.yml` und `en/publish.yml` **muss** mit der README-Version übereinstimmen.

---

## 6. Schnellbefehl zur Prüfung / Quick verification command

```powershell
# Alle Dateien mit alter Version finden / Find all files with old version
git grep -n "OLD_VERSION" -- "*.md" "*.json" "*.yml" "*.yaml" "*.cff"
```

Ersetze `OLD_VERSION` mit der vorherigen Versionsnummer (z. B. `2.0.0`).
