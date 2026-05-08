# gitbook_worker-Lieferantenbeschreibung 2026-05-08

Repository: Rob9999/erda-book
Branch: release_candidate
Projektversion: ERDA Book v2.5.0
Gepruefter Worker: gitbook_worker 2.7.0
Gepruefte Manifeste: `de/publish.yml`, `en/publish.yml`

## Kurzfassung

Das Upgrade auf `gitbook_worker 2.7.0` ist im Repository operativ vollzogen:

- `requirements.txt` zeigt auf `packages/gitbook-worker/gitbook_worker-2.7.0-py3-none-any.whl`.
- `.github/workflows/orchestrator.yml` entpackt `packages/gitbook-worker/gitbook_worker-2.7.0.tar.gz`.
- DE und EN wurden mit der Repo-venv neu gebaut.
- Die neuen PDFs enthalten TwemojiMozilla und ERDACCbyCJK-Regular.
- Die frueheren Code-Fence- und H4-/Run-in-Heading-Befunde sind unter 2.7.0 nicht mehr reproduzierbar.
- Die frueheren breiten Tabellenueberlaeufe sind im Vollscan nicht mehr enthalten; 2.7.0 schaltet fuer breite Inhalte auf groessere bzw. querformatige Seiten.

Offen bleiben ein Windows-spezifischer Font-Sandbox-Hinweis und kleine echte URL-/Quellenzeilenueberlaeufe. Diese Restbefunde sind keine Tabellenpapierueberlaeufe.

## Build- und Pruefprotokoll

Installierte Version:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -c "import importlib.metadata as m; print(m.version('gitbook-worker'))"
```

Ergebnis: `2.7.0`.

Erfolgreiche Build-Kommandos:

```powershell
$env:LOCALAPPDATA = "C:\RAMProjects\ERDA\tmp\gbw-localappdata"
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest de/publish.yml --profile local --content-config content.yaml --lang de
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest en/publish.yml --profile local --content-config content.yaml --lang en
```

Orchestrator-Ergebnisse:

| Sprache | Converter | Publisher |
| ---- | ---- | ---- |
| DE | ok | ok |
| EN | ok | ok |

Artefakte:

| Artefakt | Ergebnis |
| ---- | ---- |
| `de/publish/das-erda-buch.pdf` | 1019 Seiten, 4.380.285 Bytes, Producer LuaTeX-1.22.0, CreationDate 2026-05-08 10:14 MESZ |
| `en/publish/the-erda-book.pdf` | 981 Seiten, 4.375.866 Bytes, Producer LuaTeX-1.22.0, CreationDate 2026-05-08 10:20 MESZ |

Vendorte Worker-Artefakte:

| Artefakt | SHA256 |
| ---- | ---- |
| `packages/gitbook-worker/gitbook_worker-2.7.0-py3-none-any.whl` | `B1CC73C97CBB5D56027E07E7168DAA3928D326B0C847760ED6376AAFB56FD8A5` |
| `packages/gitbook-worker/gitbook_worker-2.7.0.tar.gz` | `B21DDBD57F5F2700233CF4C3136789548C21022A461010E96F7AF95077489F42` |

`pdffonts` bestaetigt fuer beide PDFs:

- `TwemojiMozilla`, eingebettet/subsetted/Unicode: yes/yes/yes
- `ERDACCbyCJK-Regular`, eingebettet/subsetted/Unicode: yes/yes/yes
- DejaVu Serif/Sans/Mono-Familien, eingebettet/subsetted/Unicode: yes/yes/yes

Seitengroessen nach 2.7.0:

| PDF | Format | Seiten |
| ---- | ---- | ----: |
| DE | Letter 612.0 x 792.0 pt | 21 |
| DE | A4 hoch 595.3 x 841.9 pt | 826 |
| DE | A4 quer 841.9 x 595.3 pt | 123 |
| DE | A3 quer 1190.6 x 841.9 pt | 31 |
| DE | A2 quer 1683.8 x 1190.6 pt | 15 |
| DE | A1 quer 2383.9 x 1683.8 pt | 3 |
| EN | Letter 612.0 x 792.0 pt | 22 |
| EN | A4 hoch 595.3 x 841.9 pt | 811 |
| EN | A4 quer 841.9 x 595.3 pt | 99 |
| EN | A3 quer 1190.6 x 841.9 pt | 30 |
| EN | A2 quer 1683.8 x 1190.6 pt | 15 |
| EN | A1 quer 2383.9 x 1683.8 pt | 4 |

## Layout-Scan 2.7.0

Vollscan:

```powershell
.\.venv\Scripts\python.exe scripts\quality\markdown_pdf_layout_scan.py --root . --max-pdf-findings 500 --pdf-right-margin 0 --pdf de/publish/das-erda-buch.pdf --pdf en/publish/the-erda-book.pdf tmp/gbw-localappdata
```

Ergebnis:

| Befundklasse | Anzahl |
| ---- | ----: |
| Gesamtbefunde | 19 |
| `pdf-line-right-overflow` | 10 |
| `pdf-block-right-overflow` | 9 |

Schlimmste Restbefunde:

| PDF | Seite | Art | Ausmass | Ursache |
| ---- | ----: | ---- | ----: | ---- |
| DE | 890 | line/block | 4.7 pt | lange World-Bank-URL in Quellen-/Bulletzeile |
| DE | 1018 | line/block | 1.6 pt | lange DOI-Zeile |
| EN | 980 | line/block | 5.5 pt | lange DOI-Zeile |
| EN | 427 | line/block | 4.9 pt | lange Wikipedia-/Quellenzeile |

Die zuvor unter 2.6.0 dokumentierten Tabellenueberlaeufe in Anhang A und den Staatenprofil-Tabellen sind im 2.7.0-Vollscan nicht mehr vorhanden. Die Restbefunde betreffen lange URLs bzw. Quellenzeilen und sollten als eigener Quellen-/URL-Umbruch-Follow-up behandelt werden.

Gezielte Regressionen:

- H4-/Run-in-Heading-Beispiel 9.6.1.1: Ueberschrift und Folgezeile stehen unter 2.7.0 auf getrennten Zeilen.
- Code-Fence-Scan an den bekannten Problemstellen: `Findings: 0`.

## Priorisierte Findings

### P0 - Windows-Build kann durch stale ERDA-Indic/Ethiopic-Font-Stubs fatal abbrechen

Status: offen / Worker-Hardening bzw. reproduzierbarer Fontkontext erforderlich
Auswirkung: lokaler Windows-Publisher-Build kann vor PDF-Erzeugung abbrechen

Der erfolgreiche 2.7.0-Lauf wurde bewusst mit repo-lokalem `LOCALAPPDATA` ausgefuehrt:

```powershell
$env:LOCALAPPDATA = "C:\RAMProjects\ERDA\tmp\gbw-localappdata"
```

Grund ist der bekannte lokale Windows-Befund: Im echten User-Font-Verzeichnis liegen alte 5-Byte-Stubs fuer `ERDA CC-BY Indic` und `ERDA CC-BY Ethiopic`. Wenn `luaotfload` diese Dateien bei `\IfFontExistsTF` aufloest, kann der Build fatal abbrechen. Der 2.7.0-Test hat diesen Pfad nicht erneut ohne Sandbox validiert.

Empfehlung an den Worker:

- Optionale Script-Fonts nur nach positiver Validierung der Fontdatei in LaTeX-Pruefungen aufnehmen.
- Gefundene Fontdateien minimal validieren (Dateigroesse, lesbarer SFNT/TTF-Header, interne Family-Namen).
- Einen offiziellen Font-Sandbox-/Env-Schalter fuer reproduzierbare lokale Builds dokumentieren.

### P1 - Breite Tabellen schalten auf groesseres Papier

Status: positiv verifiziert / als geloest behandeln, Publisher-Sichtpruefung bleibt sinnvoll
Auswirkung: fruehere Tabellenueberlaeufe sind nicht mehr reproduzierbar

gitbook_worker 2.7.0 erzeugt gemischte Seitengroessen und nutzt fuer breite Inhalte A4 quer, A3 quer, A2 quer oder A1 quer. Der Vollscan meldet keine der zuvor dokumentierten breiten Tabellenueberlaeufe mehr.

Empfehlung:

- Die automatische Seitengroessenwahl als Worker-Regressionstest aufnehmen.
- Publisher-Sichtpruefung auf die Lesbarkeit der sehr grossen A1/A2-Tabellenseiten legen.

### P1 - Code-Fence-Wrapping und H4-Blockueberschriften

Status: positiv verifiziert / als geloest behandeln
Auswirkung: fruehere Code-Fence- und Run-in-Heading-Befunde sind nicht mehr reproduzierbar

Die gezielten Scans an den bekannten Code-Fence-Stellen melden `Findings: 0`. Das H4-Beispiel 9.6.1.1 wird nicht mehr als Run-in-Heading mit dem Folgeabsatz in derselben Zeile gesetzt.

Empfehlung:

- Regressionstest fuer Code-Fence-Wrapping und H4-Blockueberschriften beibehalten.

### P2 - Kleine echte Seitenueberlaeufe bleiben bei langen URLs und Quellenzeilen

Status: offen / allgemeines PDF-Layout-Hardening
Auswirkung: 19 messbare Restbefunde im 2.7.0-Vollscan

Die Restbefunde sind keine Tabellenpapierueberlaeufe. Sie betreffen vor allem lange URLs, DOI-Zeilen und Quellenzeilen. Der groesste Einzelbefund liegt bei 5.5 pt.

Empfehlung an den Worker bzw. die Redaktion:

- URL-/DOI-Umbruchregeln weiter haerten (`xurl`/`url`-Breaks oder Pandoc/LaTeX-Header-Regeln).
- Alternativ die betroffenen Quellenzeilen redaktionell umbrechen oder als Fussnoten-/Quellenformat gesondert behandeln.

### P3 - Lokale Poppler-Pruefung meldet Display-Font-Warnungen

Status: Umgebungsrauschen / nicht build-blockierend
Auswirkung: `pdffonts` erzeugt Warnungen, listet die eingebetteten Fonts aber korrekt

`pdffonts` meldete lokal mehrfach fehlende Display-Fonts wie `ArialNarrow`, `HelveticaNarrow`, `BookAntiqua` und `ArialUnicode`. Die eigentliche Fonttabelle ist trotzdem vollstaendig, und die relevanten PDF-Fonts sind eingebettet.

## Reproduktionshinweise

Standardlauf mit repo-lokalem Fontkontext:

```powershell
New-Item -ItemType Directory -Force C:\RAMProjects\ERDA\tmp\gbw-localappdata\Microsoft\Windows\Fonts
$env:LOCALAPPDATA = "C:\RAMProjects\ERDA\tmp\gbw-localappdata"
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest de/publish.yml --profile local --content-config content.yaml --lang de
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest en/publish.yml --profile local --content-config content.yaml --lang en
```

Fontpruefung:

```powershell
pdffonts de/publish/das-erda-buch.pdf
pdffonts en/publish/the-erda-book.pdf
```

Layout-Scan:

```powershell
.\.venv\Scripts\python.exe scripts\quality\markdown_pdf_layout_scan.py --root . --max-pdf-findings 500 --pdf-right-margin 0 --pdf de/publish/das-erda-buch.pdf --pdf en/publish/the-erda-book.pdf tmp/gbw-localappdata
```

## Abnahmestatus fuer diesen Repo-Stand

- Upgrade-Pins: erledigt.
- DE/EN-PDF-Neubau: erledigt mit repo-lokalem Fontkontext.
- PDF-Commit-Bedingung: erfuellt, weil beide PDFs TwemojiMozilla und ERDACCbyCJK-Regular enthalten.
- Breite Tabellen: 2.7.0 loest die bisher dokumentierten Tabellenueberlaeufe durch groessere bzw. querformatige Seiten.
- Attribution: keine neue Attribution erforderlich; die bestehenden Font-/Emoji-Angaben bleiben passend.
- Offene Follow-ups: Windows-Font-Sandbox/Fontvalidierung, URL-/DOI-Umbrueche, Publisher-Sichtpruefung fuer sehr grosse Tabellenpapierformate.