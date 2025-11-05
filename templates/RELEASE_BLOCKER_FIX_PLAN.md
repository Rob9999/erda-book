# Release-Blocker & Fix-Plan für v1.0.1

**Status:** 🚨 **RELEASE BLOCKIERT**  
**Datum:** 2025-11-05  
**Kritikalität:** HOCH

---

## 🚨 Kritischer Blocker #1: OpenMoji-Lizenz-Verstoß

### Problem
**AGENTS.md** schreibt **explizit Twemoji (CC BY 4.0)** vor und verbietet andere Emoji-Sets.  
Aktuell werden aber **OpenMoji-Fonts** in mehreren Dateien referenziert:

1. **`publish.yml` (Zeile 59)**
   ```yaml
   mainfont_fallback: OpenMoji Color:mode=harf; [.github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf]:mode=harf
   ```

2. **`.github/gitbook_worker/tools/publishing/publisher.py`**
   - Zeilen 545-546: `candidates.append("OpenMoji Color")` + `"OpenMoji Black"`
   - Zeilen 593-596: OpenMoji-Fallback-Logic
   - Zeilen 1268-1287: OpenMoji-Font-Download-URLs

3. **`.github/gitbook_worker/tools/README.md` (Zeile 100, 156)**
   - Dokumentiert OpenMoji als Feature

### Rechtliche Risiken
- **Lizenz-Inkonsistenz:** AGENTS.md vs. tatsächliche Implementierung
- **Zenodo-Archivierung:** Falsche Attribution (OpenMoji statt Twemoji)
- **Compliance-Verstoß:** CI sollte Build abbrechen (tut es aber nicht)

---

## 🔧 Fix-Plan: Twemoji-Migration

### Schritt 1: `publish.yml` korrigieren

**Datei:** `publish.yml` (Zeile 59)

**Alt:**
```yaml
mainfont_fallback: OpenMoji Color:mode=harf; [.github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf]:mode=harf
```

**Neu:**
```yaml
mainfont_fallback: Twemoji Mozilla:mode=harf; [.github/fonts/erda-ccby-cjk/true-type/erda-ccby-cjk.ttf]:mode=harf
```

**Begründung:** Twemoji ist vorinstalliert in den meisten Linux-Systemen als `Twemoji Mozilla`. Falls nicht vorhanden, muss es über `fonts-twemoji` installiert werden (siehe Dockerfile).

---

### Schritt 2: `publisher.py` auf Twemoji umstellen

**Datei:** `.github/gitbook_worker/tools/publishing/publisher.py`

#### 2.1 Emoji-Kandidaten anpassen (Zeilen 545-546)

**Alt:**
```python
candidates.append("OpenMoji Color")
candidates.extend(["OpenMoji Black", "Segoe UI Emoji"])
```

**Neu:**
```python
candidates.append("Twemoji Mozilla")
candidates.extend(["Twemoji", "Segoe UI Emoji"])
```

#### 2.2 Fallback-Logic entfernen (Zeilen 593-596)

**Alt:**
```python
if _normalize_font_name("OpenMoji Color") in seen:
    if _normalize_font_name("OpenMoji Black") not in seen:
        entries.append("OpenMoji Black:mode=harf")
        seen.add(_normalize_font_name("OpenMoji Black"))
```

**Neu:**
```python
# Twemoji hat keinen separaten "Black"-Modus → entfernen
```

#### 2.3 Font-Download-URLs ersetzen (Zeilen 1268-1287)

**Alt:**
```python
font_black = os.path.join(font_dir, "OpenMoji-black-glyf.ttf")
# ...
url = "https://github.com/hfg-gmuend/openmoji/raw/master/font/OpenMoji-black-glyf/OpenMoji-black-glyf.ttf"

font_color = os.path.join(font_dir, "OpenMoji-color-glyf_colr_0.ttf")
# ...
url = "https://github.com/hfg-gmuend/openmoji/raw/master/font/OpenMoji-color-glyf_colr_0/OpenMoji-color-glyf_colr_0.ttf"
```

**Neu:**
```python
# Twemoji über System-Package-Manager installieren (apt-get install fonts-twemoji)
# Keine manuellen Downloads mehr erforderlich
# Falls doch: https://github.com/mozilla/twemoji-colr/releases/latest/download/Twemoji.ttf
```

**Alternative (wenn Download notwendig):**
```python
font_twemoji = os.path.join(font_dir, "Twemoji.ttf")
if not os.path.exists(font_twemoji):
    try:
        url = "https://github.com/mozilla/twemoji-colr/releases/latest/download/Twemoji.ttf"
        _download_file(url, font_twemoji)
        logger.info("Twemoji-Font installiert.")
    except Exception as e:
        logger.warning("Konnte Twemoji nicht installieren: %s", e)
```

---

### Schritt 3: Dockerfile aktualisieren

**Datei:** `.github/gitbook_worker/tools/docker/Dockerfile`

**Sicherstellen, dass Twemoji installiert ist:**

```dockerfile
# Twemoji-Font installieren
RUN apt-get update && \
    apt-get install -y fonts-twemoji && \
    fc-cache -fv && \
    rm -rf /var/lib/apt/lists/*
```

**Prüfung nach Installation:**
```dockerfile
RUN fc-list | grep -i twemoji
```

---

### Schritt 4: Dokumentation aktualisieren

**Datei:** `.github/gitbook_worker/tools/README.md`

**Zeile 100 & 156 ändern:**

**Alt:**
```markdown
and colour OpenMoji fonts, `--emoji-report`/`--emoji-report-dir` to emit
assets, preferring Twemoji (CC BY 4.0) and falling back to OpenMoji Black.
```

**Neu:**
```markdown
and Twemoji fonts (CC BY 4.0), `--emoji-report`/`--emoji-report-dir` to emit
assets using Twemoji (CC BY 4.0) exclusively as per AGENTS.md policy.
```

---

### Schritt 5: `ATTRIBUTION.md` validieren

**Prüfen:**
- ✅ Nur Twemoji (CC BY 4.0) gelistet
- ❌ Keine OpenMoji-Referenzen

**Falls OpenMoji vorhanden → entfernen!**

---

### Schritt 6: Build testen

**Lokal (PowerShell):**
```powershell
# 1. Docker-Image bauen
cd .github\gitbook_worker\tools\docker
docker build -t erda-book-builder:twemoji-fix .

# 2. PDF-Build im Container testen
docker run --rm -v ${PWD}:/workspace erda-book-builder:twemoji-fix `
  python -m tools.workflow_orchestrator --root /workspace --manifest publish.yml --profile local

# 3. Emoji-Report prüfen
Get-Content build\emoji-report.json | Select-String -Pattern "openmoji|OpenMoji"
# → MUSS leer sein!
```

**Erwartetes Ergebnis:**
- ✅ PDF wird erfolgreich gebaut
- ✅ Keine OpenMoji-Referenzen in `emoji-report.json`
- ✅ Twemoji-Glyphen korrekt im PDF

---

### Schritt 7: GitHub Actions testen

**Workflow:** `.github/workflows/pdf-integration.yml`

1. Fix-Commit pushen → `release_candidate` Branch
2. Workflow automatisch triggern
3. Build-Logs prüfen:
   - ✅ Keine OpenMoji-Downloads
   - ✅ Twemoji korrekt erkannt
   - ✅ PDF-Artefakt erfolgreich

---

## 📋 Checkliste: Twemoji-Migration

- [ ] `publish.yml` → Twemoji statt OpenMoji
- [ ] `publisher.py` → Emoji-Kandidaten angepasst
- [ ] `publisher.py` → OpenMoji-Fallback-Logic entfernt
- [ ] `publisher.py` → OpenMoji-Download-URLs entfernt/ersetzt
- [ ] `Dockerfile` → Twemoji-Installation sichergestellt
- [ ] `README.md` (Tools) → OpenMoji-Referenzen entfernt
- [ ] `ATTRIBUTION.md` → Nur Twemoji gelistet
- [ ] Lokaler Docker-Build erfolgreich
- [ ] PDF-Build lokal erfolgreich
- [ ] `emoji-report.json` enthält keine OpenMoji-Referenzen
- [ ] GitHub Actions Build erfolgreich
- [ ] PDF-Qualität geprüft (Emoji-Darstellung)

---

## 🚨 Kritischer Blocker #2: GitHub Actions Ungetestet

### Problem
Alle Workflows (12+) wurden noch **nie** nach den letzten Änderungen getestet.

### Fix-Plan

1. **YAML-Syntax-Validierung:**
   ```powershell
   # GitHub CLI
   gh workflow list
   gh workflow view publisher.yml
   ```

2. **Manueller Trigger (Test-Run):**
   ```powershell
   gh workflow run publisher.yml --ref release_candidate
   ```

3. **Status überwachen:**
   ```powershell
   gh run list --workflow=publisher.yml
   gh run view <run-id> --log
   ```

---

## 🚨 Kritischer Blocker #3: Docker Container Ungetestet

### Problem
Docker-Build wurde lokal noch **nie** getestet.

### Fix-Plan

**Siehe Schritt 6 oben** (Twemoji-Migration → Build testen)

---

## 🎯 Release-Freigabe Kriterien

Release v1.0.1 ist **FREIGEGEBEN**, wenn:

- [x] **Emoji-Lizenz:** 100% Twemoji (CC BY 4.0), keine OpenMoji
- [ ] **GitHub Actions:** Alle relevanten Workflows grün
- [ ] **Docker Container:** Build + Run lokal erfolgreich
- [ ] **PDF-Qualität:** Manueller Check bestanden
- [ ] **Git-Status:** Clean (keine uncommitted changes außer Protokoll)

---

**Geschätzte Fixing-Zeit:** 2-4 Stunden  
**Priorität:** 🔥 **HÖCHSTE** (Lizenz-Compliance)

**Nächster Schritt:** Implementierung der Twemoji-Migration starten!
