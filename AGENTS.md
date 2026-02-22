# AGENT Instructions (rechtssicher)

Diese Anweisungen gelten für den gesamten Inhalt dieses Repositories (GitBook, Toolchain, PDF-Erzeugung).

## Arbeitsprinzipien
- Aufträge nach bestem Wissen und Gewissen erfüllen. Wo eine exakte Umsetzung nicht möglich ist, Gründe transparent nennen und realistische Alternativen vorschlagen.
- Keine Rechts-, Steuer- oder sonstige professionelle Beratung. Inhalte „as is“, ohne Gewähr. Datenschutz-, Sicherheits- und Exportkontrollvorgaben beachten.
- Nachvollziehbare Dokumentation von Abweichungen und Entscheidungen (Commit-Nachricht, Issue-Referenz).

## Übersetzungssynchronisation (DE ↔ EN)
- Änderungen an Inhalten in `de/` sind gemäß `translation-instruction.md` zeitnah nach `en/` nachzuziehen (und vice versa), idealerweise im **gleichen Commit**.
- Wenn eine synchrone Übersetzung nicht möglich ist (z. B. wegen Review-Requirement), muss mindestens der `status:` in EN angepasst und der/die Writer/Redakteur:in aktiv darauf hingewiesen werden.
- **Genehmigungspflicht:** Wenn eine Übersetzung inhaltlich/terminologisch eine **Writer- und/oder Redaktionsfreigabe** benötigt, ist diese Freigabe **aktiv einzuholen**, bevor eine Übersetzung als final/`approved` markiert wird.
   - Liegt keine explizite Freigabe vor, Übersetzungen nur als **Entwurf** (`status: draft` oder `status: in-review`) anlegen/aktualisieren und die Freigabe im Arbeitskontext aktiv anfragen.
   - Bei Änderungen an bereits übersetzten Kapiteln gilt dasselbe: DE↔EN synchronisieren, aber Status/Review-Stand transparent halten.

## Lizenzpolitik (verbindlich)
- **Texte/Grafiken/Diagramme:** **CC BY-SA 4.0** (Share-Alike für Bearbeitungen).
- **Code/Build-Skripte/Toolchain:** **MIT** (separat in `LICENSE-CODE`).
- **Fonts (eigene):** **CC BY 4.0 oder MIT (Dual-Lizenz)** — **keine** OFL-/Apache-/GPL- oder proprietären Fonts im Repo oder Build-Transit.
- **Emojis:** **Twemoji (CC BY 4.0)**; andere Emoji-Sets nur, wenn kompatibel und in `ATTRIBUTION.md` dokumentiert.
- **Drittinhalte:** Nur bei geklärten Rechten. Jede Nutzung mit Quelle, Version und Lizenz in `ATTRIBUTION.md` dokumentieren.

## Beiträge (Contributions)
- **DCO verpflichtend**: Jeder Commit muss einen `Signed-off-by:`-Trailer tragen (Developer Certificate of Origin).
- Beiträge übernehmen automatisch die obige Lizenzierung pro Inhaltsart.
- PRs mit inkompatiblen Lizenzen werden abgelehnt.

## Release-Metadaten (README-Pflicht)

Am Anfang der Root-README (`README.md`) muss die aktuelle Release-Identität **sofort sichtbar** sein:

- **Current version** (z. B. `v1.0.2`)
- **As of (date)** (ISO-Format `YYYY-MM-DD`)
- **Channel** (`main` = stabil, `release_candidate` = Pre-Release)
- **Codename / Release name**
   - auf `release_candidate`: **Codename** (z. B. `v4.0.1 - Milky Way Democrazy` oder klar als `TBD` markieren)
   - auf `main`: **Release name** (z. B. `v3.0.2 - Solar Democracy`)

Wenn sich Version/Datum/Codename ändern, sind README + Release-Dokumentation entsprechend zu aktualisieren.

**Konsistenzregel (Datum):** Das README-Datum (**As of**) muss mit den GitBook-Metadaten übereinstimmen:

- `de/book.json` → `"date"`
- `en/book.json` → `"date"`

**Pflichtregel (Last content change date):** Bei **jeder** inhaltlichen Änderung am Buch (insb. Änderungen unter `de/content/` oder `en/content/`) ist das **Datum der letzten Inhaltsänderung** (ISO `YYYY-MM-DD`) nachzuführen.

- Bevorzugt: in `de/book.json` und `en/book.json` das Feld `"date"` setzen.
- Alternativ: das Datum in `de/publish.yml` und `en/publish.yml` unter einem eindeutigen Meta-Feld dokumentieren (z. B. `meta: content_last_changed: YYYY-MM-DD`).

## Tooling-Hinweis (gitbook_worker)

Die Build-Toolchain (`gitbook_worker`) ist **outgesourced** und wird aus dem externen Repository geliefert:

- https://github.com/Rob9999/gitbook-worker

In diesem Repository wird eine **gepinnt/vendorte** Paket-Artefakt-Version verwendet (siehe `requirements.txt`). Änderungen am Tooling erfolgen grundsätzlich upstream; hier werden primär Konfiguration, Inhalte und Release-Artefakte gepflegt.

## Pflichtdateien
- `LICENSE` (CC BY-SA 4.0 für Texte/Grafiken/Diagramme)
- `LICENSE-CODE` (MIT)
- `LICENSE-FONTS` (CC BY 4.0 oder MIT; Marken-/Namenshinweis für Font-Familien)
- `ATTRIBUTION.md` (konkrete Quellen/Lizenzen inkl. Emojis/Fonts)
- `de/content/anhang-j-lizenz---offenheit.md` (Buchanhang mit Lizenzkonzept, DE)
- `en/content/appendix-j-license-and-openness.md` (Book appendix, EN)
- `de/content/anhang-l-kolophon.md` (PDF-Kolophon mit Font-Attribution und Produktionsdetails, DE)
- `en/content/appendix-l-colophon.md` (PDF colophon, EN)

## Attribution-Hierarchie (verbindlich)
**Drei-Ebenen-System für Transparenz und Rechtssicherheit:**

1. **`ATTRIBUTION.md` (Repository-Ebene)** — **Primärquelle**
   - Maschinenlesbare Tabelle aller Drittinhalte (Fonts, Emojis, Assets)
   - Pflichtfelder: Asset, Urheber, Lizenz, Version, Quelle, Verwendung
   - Wird von CI/CD-Tools geprüft (Compliance-Check)
   - **Zielgruppe:** Entwickler, Maintainer, Rechtsprüfung, Compliance-Tools

2. **`de/content/anhang-l-kolophon.md` / `en/content/appendix-l-colophon.md` (PDF-Ebene)** — **Leserfreundliche Darstellung**
   - Narrative Aufbereitung der Font-Attribution für PDF-Leser
   - Produktionsdetails (TeX Live, Pandoc, Build-Umgebung)
   - Verweist auf `ATTRIBUTION.md` für vollständige Details
   - **Zielgruppe:** Buchleser, die kein Repo-Zugriff haben

3. **`de/content/anhang-j-lizenz---offenheit.md` / `en/content/appendix-j-license-and-openness.md` (Konzept-Ebene)** — **Lizenzphilosophie**
   - Erklärt Lizenzkonzept und Share-Alike-Prinzip
   - Verweist auf `ATTRIBUTION.md` für konkrete Drittinhalte
   - Rechtliche Rahmenbedingungen und mehrsprachige Klauseln
   - **Zielgruppe:** Rechtsinteressierte, KI-Trainer, Remix-Projekte

**Pflegehinweis (KRITISCH):**
Bei **jeder Änderung** an Fonts, Emojis oder Drittinhalten müssen **alle drei Ebenen** aktualisiert werden:
- ✅ `ATTRIBUTION.md` erweitern (neue Zeile in Tabelle)
- ✅ `de/content/anhang-l-kolophon.md` / `en/content/appendix-l-colophon.md` aktualisieren (L.2 Typografie)
- ✅ `de/content/anhang-j-lizenz---offenheit.md` / `en/content/appendix-j-license-and-openness.md` prüfen (ggf. Lizenzmatrix erweitern)
- ✅ Commit mit `Signed-off-by:` und Referenz auf geänderte Assets

## Compliance-Check (Empfehlung)
- CI bricht Builds ab, wenn Fonts/Assets mit OFL, GPL, UFL, proprietären Lizenzen o. ä. erkannt werden.
- Automatisierter Abgleich der in `ATTRIBUTION.md` aufgeführten Assets mit dem tatsächlichen Bestand.
