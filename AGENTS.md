# AGENT Instructions (rechtssicher)

Diese Anweisungen gelten für den gesamten Inhalt dieses Repositories (GitBook, Toolchain, PDF-Erzeugung).

## Arbeitsprinzipien
- Aufträge nach bestem Wissen und Gewissen erfüllen. Wo eine exakte Umsetzung nicht möglich ist, Gründe transparent nennen und realistische Alternativen vorschlagen.
- Keine Rechts-, Steuer- oder sonstige professionelle Beratung. Inhalte „as is“, ohne Gewähr. Datenschutz-, Sicherheits- und Exportkontrollvorgaben beachten.
- Nachvollziehbare Dokumentation von Abweichungen und Entscheidungen (Commit-Nachricht, Issue-Referenz).

## Übersetzungssynchronisation (DE ↔ EN)
- Änderungen an Inhalten in `de/` sind gemäß `translation-instruction.md` zeitnah nach `en/` nachzuziehen (und vice versa), idealerweise im **gleichen Commit**.
- Wenn eine synchrone Übersetzung nicht möglich ist (z. B. wegen Review-Requirement), muss mindestens der `status:` in EN angepasst und der/die Writer/Redakteur:in aktiv darauf hingewiesen werden.

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

## Pflichtdateien
- `LICENSE` (CC BY-SA 4.0 für Texte/Grafiken/Diagramme)
- `LICENSE-CODE` (MIT)
- `LICENSE-FONTS` (CC BY 4.0 oder MIT; Marken-/Namenshinweis für Font-Familien)
- `ATTRIBUTION.md` (konkrete Quellen/Lizenzen inkl. Emojis/Fonts)
- `content/anhang-j-lizenz-and-offenheit.md` (Buchanhang mit Lizenzkonzept)
- `content/anhang-l-kolophon.md` (PDF-Kolophon mit Font-Attribution und Produktionsdetails)

## Attribution-Hierarchie (verbindlich)
**Drei-Ebenen-System für Transparenz und Rechtssicherheit:**

1. **`ATTRIBUTION.md` (Repository-Ebene)** — **Primärquelle**
   - Maschinenlesbare Tabelle aller Drittinhalte (Fonts, Emojis, Assets)
   - Pflichtfelder: Asset, Urheber, Lizenz, Version, Quelle, Verwendung
   - Wird von CI/CD-Tools geprüft (Compliance-Check)
   - **Zielgruppe:** Entwickler, Maintainer, Rechtsprüfung, Compliance-Tools

2. **`content/anhang-l-kolophon.md` (PDF-Ebene)** — **Leserfreundliche Darstellung**
   - Narrative Aufbereitung der Font-Attribution für PDF-Leser
   - Produktionsdetails (TeX Live, Pandoc, Build-Umgebung)
   - Verweist auf `ATTRIBUTION.md` für vollständige Details
   - **Zielgruppe:** Buchleser, die kein Repo-Zugriff haben

3. **`content/anhang-j-lizenz-and-offenheit.md` (Konzept-Ebene)** — **Lizenzphilosophie**
   - Erklärt Lizenzkonzept und Share-Alike-Prinzip
   - Verweist auf `ATTRIBUTION.md` für konkrete Drittinhalte
   - Rechtliche Rahmenbedingungen und mehrsprachige Klauseln
   - **Zielgruppe:** Rechtsinteressierte, KI-Trainer, Remix-Projekte

**Pflegehinweis (KRITISCH):**
Bei **jeder Änderung** an Fonts, Emojis oder Drittinhalten müssen **alle drei Ebenen** aktualisiert werden:
- ✅ `ATTRIBUTION.md` erweitern (neue Zeile in Tabelle)
- ✅ `content/anhang-l-kolophon.md` aktualisieren (L.2 Typografie)
- ✅ `content/anhang-j-lizenz-and-offenheit.md` prüfen (ggf. Lizenzmatrix erweitern)
- ✅ Commit mit `Signed-off-by:` und Referenz auf geänderte Assets

## Compliance-Check (Empfehlung)
- CI bricht Builds ab, wenn Fonts/Assets mit OFL, GPL, UFL, proprietären Lizenzen o. ä. erkannt werden.
- Automatisierter Abgleich der in `ATTRIBUTION.md` aufgeführten Assets mit dem tatsächlichen Bestand.
