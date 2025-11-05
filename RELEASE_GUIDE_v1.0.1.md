# GitHub Release v1.0.1 – Schritt-für-Schritt Anleitung

## Voraussetzungen
- [x] `.zenodo.json` im Repo-Root liegt vor und enthält korrekte Metadaten
- [x] `publish/das-erda-buch.pdf` existiert und ist aktuell
- [x] `CITATION.cff` harmonisiert (Version 1.0.1, Datum 2025-11-05)
- [x] `RELEASE_NOTES_v1.0.1.md` erstellt
- [x] Zenodo-Account mit GitHub verbunden (https://zenodo.org/account/settings/github/)
- [x] Repository `Rob9999/erda-book` ist **public** und bei Zenodo aktiviert

---

## Option A: Git-CLI (Kommandozeile)

### 1. Branch wechseln und aktualisieren
```powershell
git switch main
git pull origin main
```

### 2. Änderungen committen (falls noch nicht geschehen)
```powershell
# Status prüfen
git status

# Falls .zenodo.json oder andere Änderungen noch nicht committed sind:
git add .zenodo.json RELEASE_NOTES_v1.0.1.md
git commit -m "chore: prepare Zenodo release 1.0.1 (metadata + release notes)" -m "Signed-off-by: Robert Alexander Massinger <your-email@example.com>"

# Änderungen pushen
git push origin main
```

### 3. Tag erstellen und pushen
```powershell
# Annotated Tag mit Release-Nachricht erstellen
git tag -a v1.0.1 -m "Das ERDA Buch 1.0.1 – technisch überarbeitetes PDF`n`nTechnische Verbesserungen:`n- Konsistente Schriften (erda-ccby-cjk)`n- Optimierte Typografie und Layout`n- Saubere Inhaltsverzeichnisse`n- Reproduzierbare Build-Pipeline`n`nLizenzierung:`n- Texte: CC BY-SA 4.0`n- Code: MIT`n- Fonts: CC BY 4.0 / MIT (Dual)`n`nSiehe RELEASE_NOTES_v1.0.1.md für Details."

# Tag auf GitHub pushen
git push origin v1.0.1
```

### 4. GitHub Release erstellen (via CLI mit `gh`)
```powershell
# GitHub CLI installieren: https://cli.github.com/
gh release create v1.0.1 `
  --title "Das ERDA Buch v1.0.1" `
  --notes-file RELEASE_NOTES_v1.0.1.md `
  --latest

# Optional: PDF als Release-Asset anhängen (zusätzlich zum Repo-Inhalt)
# gh release upload v1.0.1 publish/das-erda-buch.pdf
```

---

## Option B: GitHub Web-UI

### 1. Änderungen ins Repository pushen
```powershell
git switch main
git pull origin main

# Falls noch Änderungen ausstehen:
git add .zenodo.json RELEASE_NOTES_v1.0.1.md
git commit -m "chore: prepare Zenodo release 1.0.1"
git push origin main
```

### 2. Release auf GitHub erstellen

1. Gehe zu: https://github.com/Rob9999/erda-book/releases
2. Klicke auf **"Draft a new release"**
3. Fülle das Formular aus:
   - **Tag version:** `v1.0.1`
   - **Target:** `main` (oder aktueller Branch)
   - **Release title:** `Das ERDA Buch v1.0.1`
   - **Description:** Inhalt aus `RELEASE_NOTES_v1.0.1.md` kopieren
4. Optional: Weitere Assets anhängen (PDF ist bereits im Repo)
5. Klicke auf **"Publish release"**

---

## Option C: Nur Tag pushen (minimale Variante)

Wenn du nur den Tag setzen möchtest (Release-Notes später):

```powershell
git switch main
git pull origin main
git tag -a v1.0.1 -m "Release v1.0.1 – technisch überarbeitetes PDF"
git push origin v1.0.1
```

GitHub erkennt den Tag automatisch und du kannst später unter "Releases" die Release-Notes ergänzen.

---

## Nach dem Release: Zenodo-Überprüfung

### 1. Warten (ca. 5-10 Minuten)
Zenodo braucht etwas Zeit, um den GitHub-Webhook zu verarbeiten und den Release zu archivieren.

### 2. Zenodo-Datensatz prüfen
1. Gehe zu: https://zenodo.org/deposit
2. Suche nach deinem neuen Datensatz (Version 1.0.1)
3. Prüfe:
   - [x] Titel korrekt
   - [x] Autoren-Reihenfolge (Massinger + ChatGPT)
   - [x] Lizenz = CC-BY-SA-4.0
   - [x] Keywords vollständig
   - [x] Related Identifiers (GitHub-Repo, Anhang J, ATTRIBUTION.md)
   - [x] PDF vorhanden (`publish/das-erda-buch.pdf`)

### 3. Metadaten feinjustieren (falls nötig)
Falls Zenodo etwas falsch interpretiert hat:
- Klicke auf **"Edit"** im Zenodo-Datensatz
- Korrigiere die Metadaten
- **Wichtig:** Änderungen gelten nur für diesen Record, nicht für `.zenodo.json` im Repo

### 4. DOI kopieren und dokumentieren
```powershell
# DOI in README.md einbauen (Badge)
# Beispiel:
# [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

---

## Checkliste: Release vollständig?

- [ ] `.zenodo.json` im Repo-Root (Version 1.0.1)
- [ ] `publish/das-erda-buch.pdf` im Repo vorhanden
- [ ] Tag `v1.0.1` erstellt und auf GitHub
- [ ] GitHub Release mit Release-Notes veröffentlicht
- [ ] Zenodo-Record automatisch erstellt (nach 5-10 Min)
- [ ] Zenodo-Metadaten geprüft und ggf. korrigiert
- [ ] DOI kopiert und in README.md / CITATION.cff ergänzt

---

## Tipps & Troubleshooting

### ❓ Zenodo erstellt keinen Record
- **Prüfe:** Ist das Repo **public**?
- **Prüfe:** Ist `Rob9999/erda-book` bei Zenodo aktiviert? (Account → GitHub → Toggle)
- **Prüfe:** Gibt es einen neuen **Release** (nicht nur Tag)?

### ❓ PDF fehlt im Zenodo-Archiv
- Zenodo archiviert den **Repo-Snapshot** zum Release-Tag.
- Das PDF muss **im Repo** liegen (`publish/das-erda-buch.pdf`), nicht als Release-Asset.
- Lösung: PDF ins Repo committen, neuen Tag erstellen.

### ❓ Falsche Metadaten in Zenodo
- `.zenodo.json` wird nur beim **ersten Upload** oder bei **neuem Major-Release** vollständig ausgewertet.
- Für bestehende Records: Manuell in Zenodo korrigieren oder neuen Tag mit aktualisierter `.zenodo.json` erstellen.

### ❓ Community "erda" existiert nicht
- Zenodo-Communities müssen vorher beantragt/erstellt werden.
- Fallback: `"identifier": "zenodo"` (Standard-Community) verwenden.
- Später über Zenodo-UI die richtige Community zuweisen.

---

## Nächste Schritte nach Release

1. **DOI in Dokumentation einpflegen**
   - README.md Badge ergänzen
   - CITATION.cff aktualisieren (DOI-Feld hinzufügen)

2. **Release kommunizieren**
   - Social Media (falls vorhanden)
   - Mailingliste / Newsletter
   - Relevante Communities informieren

3. **Feedback sammeln**
   - GitHub Issues aktivieren
   - Community-Diskussionen beobachten
   - Verbesserungsvorschläge für v1.0.2 sammeln

4. **Monitoring**
   - Zenodo-Downloads überwachen
   - GitHub-Stars / Forks beobachten
   - Zitationen tracken (Google Scholar, Semantic Scholar)

---

**Viel Erfolg mit dem Release! 🎉**

**Bei Fragen:** GitHub Issues im Repository öffnen oder Zenodo-Support kontaktieren.
