# gitbook_worker-Lieferantenbeschreibung 2026-05-07

Repository: Rob9999/erda-book
Branch: release_candidate
Projektversion: ERDA Book v2.5.0
Gepruefter Worker: gitbook_worker 2.4.2
Gepruefte Manifeste: `de/publish.yml`, `en/publish.yml`

## Kurzfassung

Das Upgrade auf `gitbook_worker 2.4.2` ist im Repository operativ vollzogen:

- `requirements.txt` zeigt auf `packages/gitbook-worker/gitbook_worker-2.4.2-py3-none-any.whl`.
- `.github/workflows/orchestrator.yml` entpackt `packages/gitbook-worker/gitbook_worker-2.4.2.tar.gz`.
- DE und EN wurden mit der Repo-venv neu gebaut.
- Die neuen PDFs enthalten TwemojiMozilla und ERDACCbyCJK-Regular.

Der CJK-Fontbefund ist fuer die neuen PDFs positiv. Zwei Worker-Follow-ups bleiben aber priorisiert offen: ein Windows-spezifischer Build-Blocker bei stale/defekten ERDA-Font-Stubs und das H4-/Run-in-Heading-Verhalten.

## Build- und Pruefprotokoll

Installierte Version:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -c "import importlib.metadata as m; print(m.version('gitbook-worker'))"
```

Ergebnis: `2.4.2`.

Erfolgreiche Build-Kommandos:

```powershell
$env:LOCALAPPDATA = "C:\RAMProjects\ERDA\tmp\gbw-localappdata"
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest de/publish.yml --profile local --content-config content.yaml --lang de
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest en/publish.yml --profile local --content-config content.yaml --lang en
```

Artefakte:

| Artefakt | Ergebnis |
| ---- | ---- |
| `de/publish/das-erda-buch.pdf` | 826 Seiten, 4.331.272 Bytes, Producer LuaTeX-1.22.0 |
| `en/publish/the-erda-book.pdf` | 800 Seiten, 4.332.854 Bytes, Producer LuaTeX-1.22.0 |

Vendorte Worker-Artefakte:

| Artefakt | SHA256 |
| ---- | ---- |
| `packages/gitbook-worker/gitbook_worker-2.4.2-py3-none-any.whl` | `6559D48B0716819DABCCC5F92F245D9DC2D6ADA2A599915F3DD0FEBC78D19FDA` |
| `packages/gitbook-worker/gitbook_worker-2.4.2.tar.gz` | `BCBF7F7AFD2F9F58926459830E904E4C376B942BE7F22B80F7D941BA9B25C9DE` |

`pdffonts` bestaetigt fuer beide PDFs:

- `TwemojiMozilla`, eingebettet/subsetted/Unicode: yes/yes/yes
- `ERDACCbyCJK-Regular`, eingebettet/subsetted/Unicode: yes/yes/yes
- DejaVu Serif/Sans/Mono-Familien, eingebettet/subsetted/Unicode: yes/yes/yes

CJK-Text-Extraktion:

| PDF | Japanisch | Koreanisch | Traditionelles Chinesisch |
| ---- | ---- | ---- | ---- |
| DE | `日本語` extrahierbar | `한국어` extrahierbar | `繁體中文` extrahierbar |
| EN | `日本語` extrahierbar | `한국어` extrahierbar | `繁體中文` extrahierbar |

CJK-Bounding-Box-Pruefung auf den relevanten Lizenzseiten:

- DE: 15 CJK-Zeilen geprueft; breiteste CJK-Zeile Seite 782, `xMax=540.0`, Seitenbreite `595.3` pt.
- EN: 15 CJK-Zeilen geprueft; breiteste CJK-Zeile Seite 755, `xMax=540.0`, Seitenbreite `595.3` pt.

Damit liegt die CJK-Zeilenbreite in beiden PDFs innerhalb der Seitenbox; die fruehere CJK-Randueberlappung ist in diesem Pruefpunkt nicht mehr reproduzierbar.

## Priorisierte Findings

### P0 - Windows-Build kann durch stale ERDA-Indic/Ethiopic-Font-Stubs fatal abbrechen

Status: offen / Worker-Hardening erforderlich
Auswirkung: lokaler Windows-Publisher-Build bricht vor PDF-Erzeugung ab

Der erste DE-Build mit `gitbook_worker 2.4.2` schlug fehl:

```text
\IfFontExistsTF{ERDA CC-BY Indic}
luaotfload/fontloader-2023-12-28.lua:19600: bad argument #1 to 'for iterator' (table expected, got nil)
Fatal error occurred, no output PDF file produced
```

Diagnose im lokalen Windows-User-Font-Verzeichnis:

```text
C:\Users\User\AppData\Local\Microsoft\Windows\Fonts\erda-ccby-indic.ttf     5 bytes
C:\Users\User\AppData\Local\Microsoft\Windows\Fonts\erda-ccby-ethiopic.ttf  5 bytes
```

`luaotfload-tool --find="ERDA CC-BY Indic"` und `--find="ERDA CC-BY Ethiopic"` loesten auf diese 5-Byte-Dateien auf. Die 2.4.2-LaTeX-Header-Erzeugung erstellt fuer `INDIC` und `ETHIOPIC` trotzdem `\IfFontExistsTF`-Pruefungen aus den Default-Fontnamen. In dieser Umgebung ist schon die Font-Existenzpruefung fatal, bevor der eigentliche Inhalt gerendert wird.

Workaround fuer den erfolgreichen lokalen Build war ein repo-lokaler, leerer Fontkontext:

```powershell
$env:LOCALAPPDATA = "C:\RAMProjects\ERDA\tmp\gbw-localappdata"
```

Empfehlung an den Worker:

- `\IfFontExistsTF` fuer optionale Script-Fonts nur erzeugen, wenn der Worker eine gueltige, verwaltete Fontdatei gefunden hat.
- Gefundene Fontdateien vor Registrierung/Verwendung minimal validieren (Dateigroesse, lesbarer SFNT/TTF-Header, interne Family-Namen).
- Defekte ERDA-Stubs in User-Font-Verzeichnissen entweder ignorieren oder mit klarer Diagnose abbrechen, bevor LaTeX startet.
- User-Font-Verzeichnisse nicht hoeher priorisieren als repo-/manifestverwaltete Fonts, wenn reproduzierbare Buildartefakte gefordert sind.
- Optional: ein offizieller `--font-sandbox`-/Env-Schalter fuer reproduzierbare lokale Builds ohne historische Windows-User-Fonts.

### P1 - H4-/Run-in-Heading-Verhalten bleibt in 2.4.2 bestehen

Status: offen / Layout-Fix erforderlich
Auswirkung: `####`-Ueberschriften werden als Run-in-Headings gesetzt; der folgende Absatz beginnt in derselben Zeile

Quelle, Beispiel DE:

```md
### 9.6.1.1 Zieldefinition und Zeitplanung fuer die Rauminfrastrukturen

_**Zieldefinition und Zeitplanung fuer die Rauminfrastrukturen**_

* Legen Sie Rauminfrastrukturen ...
```

Kombiniertes Markdown nach gewollter Combiner-Anpassung:

```md
#### 9.6.1.1 Zieldefinition und Zeitplanung fuer die Rauminfrastrukturen

_**Zieldefinition und Zeitplanung fuer die Rauminfrastrukturen**_

* Legen Sie Rauminfrastrukturen ...
```

Textauszug aus dem neuen DE-PDF 2.4.2:

```text
9.6.1.1 Zieldefinition und Zeitplanung fuer die Rauminfrastrukturen Zieldefinition
und Zeitplanung fuer die Rauminfrastrukturen
```

Textauszug aus dem neuen EN-PDF 2.4.2:

```text
9.6.1.1 Goal definition and timeline for the space infrastructures Goal definition and
timeline for the space infrastructures
```

Die Wiederholungszeile ist ein bewusstes Stilmittel in den Quellen und soll nicht entfernt werden. Auch die Header-Level-Anpassung des Combiners ist beabsichtigt. Die Ursache liegt sehr wahrscheinlich darin, dass Pandoc/LaTeX `####` auf `\paragraph{...}` abbildet und Standard-LaTeX `\paragraph` als Run-in-Heading setzt.

Empfehlung an den Worker:

- In der PDF-/LaTeX-Header-Schicht `\paragraph` und ggf. `\subparagraph` als Blockueberschriften definieren.
- Nummerierung und Inhaltsverzeichnis unveraendert lassen.
- Das Verhalten fuer DE und EN gleich halten.
- Regressionstest mit Kapitel 9.6.1.1 aufnehmen.

### P1 - CJK-Randueberlappung im 2.4.2-Artefakt nicht mehr reproduzierbar

Status: positiv verifiziert / als behoben behandeln, aber Regressionstest aufnehmen
Auswirkung: frueherer CJK-Fallback-Befund ist im aktuellen Artefakt nicht sichtbar

Die neuen DE/EN-PDFs enthalten `ERDACCbyCJK-Regular`; Japanisch, Koreanisch und traditionelles Chinesisch sind per `pdftotext -enc UTF-8` extrahierbar. Die breiteste CJK-Zeile in den geprueften Lizenzseiten endet bei `xMax=540.0` pt auf einer `595.3`-pt-Seite und bleibt damit innerhalb der Seitenbox.

Empfehlung an den Worker:

- CJK-Lizenzseiten als feste Regression in die Release-Pruefung aufnehmen.
- `pdffonts`-Check auf `ERDACCbyCJK-Regular` plus Bounding-Box-Pruefung fuer CJK-Zeilen automatisieren.

### P2 - Kleine echte Seitenueberlaeufe bleiben bei langen URLs, Tabellen und Template-Zeilen

Status: offen / allgemeines PDF-Layout-Hardening
Auswirkung: keine CJK-spezifische Regression, aber weiterhin messbare Ueberlaeufe

Ein kompletter `pdftotext -bbox-layout`-Scan mit rechter Seitenkante als Grenze meldet:

| PDF | Line-overflows | Block-overflows | Schlimmster Befund |
| ---- | ----: | ----: | ---- |
| DE | 57 | 31 | Seite 715, URL-/World-Bank-Zeile, ca. 4.7 pt ueber Seitenbreite |
| EN | 50 | 30 | Seite 90, lange Europa-Parlament-URL, ca. 6.0 pt ueber Seitenbreite |

Die Befunde betreffen vor allem lange URLs, Tabellen und Template-/Codezeilen. Sie sind nicht Teil des CJK-Fixes, sollten aber als generelles PDF-Layout-Hardening in den Worker-Backlog.

Empfehlung an den Worker:

- URL-/Code-/Tabellen-Umbruchregeln robuster setzen.
- Fuer lange URLs `xurl`/`url`-Breaks oder Pandoc/LaTeX-Header-Regeln pruefen.
- Fuer sehr breite Markdown-Tabellen alternative longtable-/font-size-/landscape-Strategien anbieten.

### P3 - Lokale Poppler-Pruefung meldet Display-Font-Warnungen

Status: Umgebungsrauschen / nicht build-blockierend
Auswirkung: `pdffonts` erzeugt Warnungen, listet die eingebetteten Fonts aber korrekt

`pdffonts` meldete lokal mehrfach:

```text
Syntax Error: No display font for 'ArialNarrow'
Syntax Error: No display font for 'HelveticaNarrow'
Syntax Error: No display font for 'BookAntiqua'
Syntax Error: No display font for 'ArialUnicode'
```

Die eigentliche Fonttabelle ist trotzdem vollstaendig, und die relevanten PDF-Fonts sind eingebettet. Dieser Punkt ist eher eine lokale Poppler/fontconfig-Sichtpruefungsnotiz als ein Worker-Blocker.

## Reproduktionshinweise

Standardlauf, der in der betroffenen Windows-Umgebung wegen 5-Byte-Indic/Ethiopic-Stubs fehlschlagen kann:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.workflow_orchestrator run --root C:\RAMProjects\ERDA --manifest de/publish.yml --profile local --content-config content.yaml --lang de
```

Nicht-destruktiver lokaler Workaround:

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

H4-Run-in-Pruefung:

```powershell
pdftotext -enc UTF-8 de/publish/das-erda-buch.pdf -
pdftotext -enc UTF-8 en/publish/the-erda-book.pdf -
```

Suchmuster:

- `9.6.1.1 Zieldefinition und Zeitplanung`
- `9.6.1.1 Goal definition and timeline`

Layout-Scan:

```powershell
.\.venv\Scripts\python.exe scripts\quality\markdown_pdf_layout_scan.py --root . --max-pdf-findings 40 --pdf-right-margin 0 --pdf de/publish/das-erda-buch.pdf --pdf en/publish/the-erda-book.pdf tmp/gbw-localappdata
```

## Abnahmestatus fuer diesen Repo-Stand

- Upgrade-Pins: erledigt.
- DE/EN-PDF-Neubau: erledigt mit repo-lokalem Fontkontext.
- PDF-Commit-Bedingung: erfuellt, weil beide PDFs TwemojiMozilla und ERDACCbyCJK-Regular enthalten.
- Attribution: keine neue Attribution erforderlich; die bestehenden Font-/Emoji-Angaben bleiben passend.
- Offene Worker-Follow-ups: P0 Windows-Font-Stub-Hardening, P1 H4-Blockueberschriften, P2 allgemeines Layout-Hardening.
