# Release-Zertifizierungsprotokoll v1.0.1

**Projekt:** ERDA – Das Buch  
**Version:** 1.0.1  
**Datum:** [WIRD AUTOMATISCH GESETZT]  
**Prüfer:** GitHub Copilot (automatisiert)  
**Status:** 🔄 IN BEARBEITUNG

---

## Übersicht

Dieses Protokoll dokumentiert die **systematische Qualitätsprüfung** vor der Release-Freigabe v1.0.1. Alle Punkte müssen mit ✅ (BESTANDEN) markiert sein, bevor das Release freigegeben werden kann.

---

## 1️⃣ Lizenz-Compliance (KRITISCH)

### 1.1 Emoji-Lizenz: Twemoji (CC BY 4.0)

**Anforderung:** Gemäß `AGENTS.md` sind **ausschließlich Twemoji (CC BY 4.0)** erlaubt. OpenMoji und andere Emoji-Sets sind **explizit verboten**.

| Checkpoint | Status | Details |
|------------|--------|---------|
| `AGENTS.md` spezifiziert Twemoji (CC BY 4.0) | ⏳ | Prüfung erforderlich |
| `ATTRIBUTION.md` listet nur Twemoji | ⏳ | Prüfung erforderlich |
| `publish.yml` verwendet Twemoji (nicht OpenMoji) | ❌ | **PROBLEM: OpenMoji Color in mainfont_fallback** |
| `build/emoji-report.json` enthält nur Twemoji-Assets | ⏳ | Prüfung erforderlich |
| Python-Code (`publisher.py`) verwendet Twemoji | ❌ | **PROBLEM: OpenMoji-Downloads/Fallbacks im Code** |
| Keine OpenMoji-Fonts in `.github/gitbook_worker/tools/publishing/fonts/` | ⏳ | Prüfung erforderlich |
| Dockerfile verwendet nur Twemoji | ⏳ | Prüfung erforderlich |

**Kritische Findings:**
- ⚠️ `publish.yml` Zeile 59: `mainfont_fallback: OpenMoji Color:mode=harf`
- ⚠️ `publisher.py` Zeilen 545-546, 1268-1287: OpenMoji-Download-URLs
- ⚠️ Mehrere README/Docs erwähnen OpenMoji als Feature

**Erforderliche Maßnahmen:**
1. `publish.yml` → Twemoji statt OpenMoji in `mainfont_fallback`
2. `publisher.py` → Twemoji-Download-URLs statt OpenMoji
3. Alle Referenzen zu OpenMoji aus Docs entfernen
4. Build testen mit reinem Twemoji-Stack

**Status:** ❌ **NICHT BESTANDEN** (muss behoben werden)

---

### 1.2 Font-Lizenz: Dual CC BY 4.0 / MIT

**Anforderung:** Eigenentwickelte Fonts (`erda-ccby-cjk`) müssen dual-lizenziert sein. **Keine** OFL-, GPL-, Apache- oder proprietären Fonts.

| Checkpoint | Status | Details |
|------------|--------|---------|
| `LICENSE-FONTS` existiert und ist korrekt | ⏳ | Prüfung erforderlich |
| `ATTRIBUTION.md` dokumentiert Font-Lizenzen | ⏳ | Prüfung erforderlich |
| Alle Fonts in `.github/fonts/` sind CC BY 4.0 oder MIT | ⏳ | Prüfung erforderlich |
| Keine verbotenen Font-Lizenzen (OFL, GPL, UFL, proprietär) | ⏳ | Prüfung erforderlich |
| Font-Metadaten in `publish.yml` korrekt | ⏳ | Prüfung erforderlich |

**Status:** ⏳ **AUSSTEHEND**

---

### 1.3 Allgemeine Lizenz-Dokumentation

| Checkpoint | Status | Details |
|------------|--------|---------|
| `LICENSE` (CC BY-SA 4.0 für Texte) vorhanden | ⏳ | Prüfung erforderlich |
| `LICENSE-CODE` (MIT) vorhanden | ⏳ | Prüfung erforderlich |
| `LICENSE-FONTS` (Dual CC BY 4.0 / MIT) vorhanden | ⏳ | Prüfung erforderlich |
| `ATTRIBUTION.md` vollständig und aktuell | ⏳ | Prüfung erforderlich |
| `content/anhang-j-lizenz-and-offenheit.md` aktuell | ⏳ | Prüfung erforderlich |
| `.zenodo.json` enthält korrekte Lizenzmatrix | ⏳ | Prüfung erforderlich |
| `CITATION.cff` Lizenz = CC-BY-SA-4.0 | ⏳ | Prüfung erforderlich |

**Status:** ⏳ **AUSSTEHEND**

---

## 2️⃣ GitHub Actions Workflows (KRITISCH)

**Anforderung:** Alle Workflows müssen erfolgreich durchlaufen (keine Syntax-Fehler, alle Tests grün).

| Workflow | Status | Details |
|----------|--------|---------|
| `.github/workflows/publisher.yml` | ⏳ | Syntax-Check ausstehend |
| `.github/workflows/pdf-integration.yml` | ⏳ | Syntax-Check ausstehend |
| `.github/workflows/orchestrator.yml` | ⏳ | Syntax-Check ausstehend |
| `.github/workflows/emoji-pdf-harness.yml` | ⏳ | Syntax-Check ausstehend |
| `.github/workflows/qa.yml` | ⏳ | Syntax-Check ausstehend |
| `.github/workflows/python-package.yml` | ⏳ | Syntax-Check ausstehend |
| Weitere Workflows (10+) | ⏳ | Syntax-Check ausstehend |

**Prüfschritte:**
1. YAML-Syntax-Validierung (alle Workflows)
2. Workflow-Trigger korrekt konfiguriert
3. Secrets/Environment-Variables dokumentiert
4. Keine Hard-Coded Credentials
5. Workflow-Permissions korrekt gesetzt

**Status:** ⏳ **AUSSTEHEND**

---

## 3️⃣ Docker Container (KRITISCH)

**Anforderung:** Docker-Image muss lokal und in GitHub Actions erfolgreich bauen und laufen.

| Checkpoint | Status | Details |
|------------|--------|---------|
| `Dockerfile` existiert | ⏳ | Prüfung erforderlich |
| Docker-Build lokal erfolgreich | ⏳ | Build-Test ausstehend |
| Docker-Run lokal erfolgreich | ⏳ | Laufzeit-Test ausstehend |
| GitHub Actions Docker-Build erfolgreich | ⏳ | CI-Test ausstehend |
| Alle Python-Dependencies installierbar | ⏳ | Dependency-Check ausstehend |
| Twemoji-Assets korrekt im Container | ⏳ | Asset-Check ausstehend |
| Keine OpenMoji-Downloads im Container-Build | ⏳ | Lizenz-Check ausstehend |

**Build-Befehle (lokal):**
```powershell
cd .github\gitbook_worker\tools\docker
docker build -t erda-book-builder:local .
docker run --rm erda-book-builder:local python --version
```

**Status:** ⏳ **AUSSTEHEND**

---

## 4️⃣ Metadaten & Reproduzierbarkeit

| Checkpoint | Status | Details |
|------------|--------|---------|
| `CITATION.cff` Version = 1.0.1 | ⏳ | Prüfung erforderlich |
| `CITATION.cff` Datum = 2025-11-05 | ⏳ | Prüfung erforderlich |
| `.zenodo.json` Version = 1.0.1 | ✅ | OK (bereits geprüft) |
| `publish/das-erda-buch.pdf` existiert | ✅ | OK (bereits geprüft) |
| `publish/das-erda-buch.md` aktuell | ⏳ | Prüfung erforderlich |
| `publish.yml` Manifest vollständig | ⏳ | Prüfung erforderlich |
| `README.md` verweist auf v1.0.1 | ⏳ | Prüfung erforderlich |

**Status:** ⏳ **AUSSTEHEND**

---

## 5️⃣ PDF-Qualität

| Checkpoint | Status | Details |
|------------|--------|---------|
| PDF-Bookmarks korrekt (Kapitelhierarchie) | ⏳ | Manueller Check ausstehend |
| Fonts korrekt eingebettet | ⏳ | Font-Audit ausstehend |
| Keine Emoji-Darstellungsfehler | ⏳ | Visueller Check ausstehend |
| CJK-Zeichen korrekt dargestellt | ⏳ | Visueller Check ausstehend |
| Inhaltsverzeichnis vollständig | ⏳ | Manueller Check ausstehend |
| Seitennummerierung korrekt | ⏳ | Manueller Check ausstehend |
| Keine abgeschnittenen Tabellen/Grafiken | ⏳ | Visueller Check ausstehend |

**Status:** ⏳ **AUSSTEHEND**

---

## 6️⃣ Git & Versioning

| Checkpoint | Status | Details |
|------------|--------|---------|
| Branch `release_candidate` sauber | ⏳ | Git-Status-Check ausstehend |
| Keine uncommitted Changes (außer Protokoll) | ⏳ | Git-Status-Check ausstehend |
| Alle Release-Dateien committed | ⏳ | Git-Status-Check ausstehend |
| `main` Branch bereit für Merge | ⏳ | Branch-Vergleich ausstehend |
| Tag `v1.0.1` noch nicht vorhanden | ⏳ | Tag-Check ausstehend |

**Status:** ⏳ **AUSSTEHEND**

---

## 7️⃣ Dokumentation

| Checkpoint | Status | Details |
|------------|--------|---------|
| `RELEASE_NOTES_v1.0.1.md` vollständig | ✅ | OK (bereits erstellt) |
| `RELEASE_GUIDE_v1.0.1.md` vollständig | ✅ | OK (bereits erstellt) |
| `README.md` aktualisiert | ⏳ | Version-Badge-Check ausstehend |
| `CHANGELOG.md` aktualisiert (falls vorhanden) | ⏳ | Prüfung erforderlich |

**Status:** ⏳ **AUSSTEHEND**

---

## 🎯 Zusammenfassung

### Kritische Blocker (müssen behoben werden)

1. ❌ **Emoji-Lizenz-Verstoß:** OpenMoji-Referenzen in `publish.yml` und `publisher.py`
2. ⏳ **GitHub Actions:** Workflows nicht getestet
3. ⏳ **Docker Container:** Build/Run nicht getestet

### Empfohlene Maßnahmen (vor Release)

1. ⏳ **PDF-Qualitätskontrolle:** Manueller Check des finalen PDFs
2. ⏳ **Font-Lizenz-Audit:** Alle Fonts auf Lizenz-Compliance prüfen
3. ⏳ **Git-Status:** Clean-State sicherstellen

---

## ✍️ Release-Freigabe

**Release v1.0.1 ist FREIGEGEBEN:** ❌ **NEIN**

**Gründe:**
- ❌ Emoji-Lizenz-Compliance nicht erfüllt (OpenMoji statt Twemoji)
- ⏳ GitHub Actions nicht getestet
- ⏳ Docker Container nicht getestet

**Freigabe durch:** _[NAME]_  
**Datum:** _[DATUM]_  
**Signatur:** _[DIGITAL ODER MANUELL]_

---

## 📋 Nächste Schritte

1. **Emoji-Fix implementieren** (höchste Priorität)
   - [ ] `publish.yml` → Twemoji statt OpenMoji
   - [ ] `publisher.py` → Twemoji-Download-URLs
   - [ ] Alle OpenMoji-Referenzen entfernen
   
2. **GitHub Actions testen**
   - [ ] YAML-Syntax-Validierung
   - [ ] Workflow-Dry-Run (falls möglich)
   
3. **Docker Container testen**
   - [ ] Lokal bauen
   - [ ] Lokal ausführen
   - [ ] GitHub Actions Docker-Build prüfen

4. **Finale Checkliste**
   - [ ] Alle ✅ gesetzt
   - [ ] PDF-Qualität bestätigt
   - [ ] Git-Status clean
   - [ ] Release-Freigabe erteilt

---

**Protokoll erstellt:** _[TIMESTAMP]_  
**Protokoll-Version:** 1.0  
**Lizenz:** CC BY-SA 4.0 (dieses Protokoll)
