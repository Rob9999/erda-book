# Release-Zertifizierungsprotokoll v1.0.1

**Projekt:** ERDA – Das Buch  
**Version:** 1.0.1  
**Timestamp:** 2025-11-05_19-41-33  
**Prüfer:** GitHub Copilot (AI-gestützt)  
**Status:** ⏳ TEILWEISE ABGESCHLOSSEN (Emoji-Fix implementiert)

---

## 🎯 Executive Summary

**Kritischer Befund:** OpenMoji-Lizenz-Verstoß wurde **vollständig behoben**.  
**Nächste Schritte:** Docker/GitHub Actions Tests ausstehend.

---

## 1️⃣ Lizenz-Compliance ✅ BESTANDEN

### 1.1 Emoji-Lizenz: Twemoji (CC BY 4.0) ✅

**Status:** ✅ **BEHOBEN** (alle OpenMoji-Referenzen entfernt)

| Datei | Änderung | Status |
|-------|----------|--------|
| `publish.yml` | `OpenMoji Color` → `Twemoji Mozilla` | ✅ |
| `publisher.py` (Zeile 545) | `OpenMoji Color` → `Twemoji Mozilla` | ✅ |
| `publisher.py` (Zeile 546) | `OpenMoji Black` → `Twemoji` | ✅ |
| `publisher.py` (Zeilen 593-596) | OpenMoji-Fallback-Logic entfernt | ✅ |
| `publisher.py` (Zeilen 1268-1287) | OpenMoji-Downloads entfernt, Kommentar ergänzt | ✅ |
| `Dockerfile` (Zeilen 61-64) | OpenMoji-wget entfernt, `fonts-twemoji` installiert | ✅ |
| `README.md` (Tools, Zeile 100) | OpenMoji-Referenz → Twemoji | ✅ |
| `README.md` (Tools, Zeile 156) | OpenMoji-Fallback → Twemoji-Exklusiv | ✅ |

**Commit-Nachricht (empfohlen):**
```
fix: replace OpenMoji with Twemoji (CC BY 4.0) for license compliance

- publish.yml: mainfont_fallback now uses Twemoji Mozilla
- publisher.py: emoji font candidates changed to Twemoji
- Dockerfile: install fonts-twemoji package instead of OpenMoji wget
- Remove all OpenMoji download URLs and fallback logic
- Update documentation to reflect Twemoji-only policy

Complies with AGENTS.md license requirements (Twemoji CC BY 4.0 only).

Signed-off-by: GitHub Copilot <copilot@github.com>
```

---

### 1.2 Font-Lizenz: Dual CC BY 4.0 / MIT ⏳

**Status:** ⏳ **AUSSTEHEND** (manueller Check erforderlich)

| Checkpoint | Status |
|------------|--------|
| `LICENSE-FONTS` existiert | ⏳ |
| Fonts in `.github/fonts/` sind CC BY 4.0/MIT | ⏳ |
| Keine verbotenen Lizenzen (OFL, GPL, UFL) | ⏳ |

**Empfehlung:** Manueller Font-Audit vor Release.

---

### 1.3 Allgemeine Lizenz-Dokumentation ⏳

| Checkpoint | Status |
|------------|--------|
| `LICENSE` (CC BY-SA 4.0) | ⏳ |
| `LICENSE-CODE` (MIT) | ⏳ |
| `ATTRIBUTION.md` vollständig | ⏳ |
| `.zenodo.json` korrekt | ✅ |
| `CITATION.cff` | ⏳ |

---

## 2️⃣ GitHub Actions Workflows ⏳

**Status:** ⏳ **NICHT GETESTET**

**Empfehlung:** YAML-Syntax-Validierung + Workflow-Dry-Run vor Release.

---

## 3️⃣ Docker Container ⏳

**Status:** ⏳ **NICHT GETESTET**

**Nächster Schritt:**
```powershell
cd .github\gitbook_worker\tools\docker
docker build -t erda-book-builder:v1.0.1-test .
docker run --rm erda-book-builder:v1.0.1-test fc-list | Select-String -Pattern "Twemoji"
```

**Erwartetes Ergebnis:**
- ✅ Build erfolgreich
- ✅ `Twemoji Mozilla` in Font-Liste
- ❌ Keine `OpenMoji`-Fonts

---

## 4️⃣ Metadaten & Reproduzierbarkeit ✅

| Checkpoint | Status |
|------------|--------|
| `.zenodo.json` Version = 1.0.1 | ✅ |
| `publish/das-erda-buch.pdf` vorhanden | ✅ |
| `RELEASE_NOTES_v1.0.1.md` | ✅ |
| `RELEASE_GUIDE_v1.0.1.md` | ✅ |

---

## 🔧 Durchgeführte Fixes

### Fix #1: publish.yml
```diff
- mainfont_fallback: OpenMoji Color:mode=harf; [...]
+ mainfont_fallback: Twemoji Mozilla:mode=harf; [...]
```

### Fix #2: publisher.py (Emoji-Kandidaten)
```diff
- candidates.append("OpenMoji Color")
- candidates.extend(["OpenMoji Black", "Segoe UI Emoji"])
+ candidates.append("Twemoji Mozilla")
+ candidates.extend(["Twemoji", "Segoe UI Emoji"])
```

### Fix #3: publisher.py (Fallback-Logic)
```diff
- if _normalize_font_name("OpenMoji Color") in seen:
-     if _normalize_font_name("OpenMoji Black") not in seen:
-         entries.append("OpenMoji Black:mode=harf")
+ # Twemoji has no separate "Black" variant - removed OpenMoji-specific logic
+ # as per AGENTS.md requirement (Twemoji CC BY 4.0 only)
```

### Fix #4: publisher.py (Downloads)
```diff
- font_black = os.path.join(font_dir, "OpenMoji-black-glyf.ttf")
- url = "https://github.com/hfg-gmuend/openmoji/raw/master/..."
+ # Twemoji is installed via system package (fonts-twemoji) in Dockerfile
+ # No manual download required - as per AGENTS.md requirement
```

### Fix #5: Dockerfile
```diff
- # Install OpenMoji font
- RUN mkdir -p $GITHUB_TOOLS/publishing/fonts/truetype/openmoji && \
-     wget -O ... OpenMoji-black-glyf.ttf && \
-     ln -s ...
+ # Install Twemoji font (CC BY 4.0 - as required by AGENTS.md)
+ RUN apt-get update && apt-get install -y \
+     fonts-twemoji \
+     && apt-get clean \
+     && rm -rf /var/lib/apt/lists/*
```

### Fix #6: README.md (Tools)
```diff
- and colour OpenMoji fonts, `--emoji-report`
+ and Twemoji (CC BY 4.0) color fonts, `--emoji-report`

- preferring Twemoji (CC BY 4.0) and falling back to OpenMoji Black.
+ using Twemoji (CC BY 4.0) exclusively as per AGENTS.md license policy.
```

---

## ✍️ Release-Freigabe

**Release v1.0.1 ist FREIGEGEBEN:** ❌ **NEIN** (Tests ausstehend)

**Grund:** Docker/GitHub Actions noch nicht getestet.

**Nächste Schritte:**
1. Docker-Build lokal testen
2. GitHub Actions YAML validieren
3. Font-Lizenz-Audit (manuell)
4. PDF-Qualität prüfen (visuell)

---

**Protokoll erstellt:** 2025-11-05 19:41:33  
**Protokoll-Version:** 1.1 (nach Emoji-Fix)  
**Nächste Revision:** Nach Docker/GitHub Actions Tests  
**Lizenz:** CC BY-SA 4.0 (dieses Protokoll)
