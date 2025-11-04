# AGENT Instructions (rechtssicher)

Diese Anweisungen gelten für den gesamten Inhalt dieses Repositories (GitBook, Toolchain, PDF-Erzeugung).

## Arbeitsprinzipien
- Aufträge nach bestem Wissen und Gewissen erfüllen. Wo eine exakte Umsetzung nicht möglich ist, Gründe transparent nennen und realistische Alternativen vorschlagen.
- Keine Rechts-, Steuer- oder sonstige professionelle Beratung. Inhalte „as is“, ohne Gewähr. Datenschutz-, Sicherheits- und Exportkontrollvorgaben beachten.
- Nachvollziehbare Dokumentation von Abweichungen und Entscheidungen (Commit-Nachricht, Issue-Referenz).

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

## Compliance-Check (Empfehlung)
- CI bricht Builds ab, wenn Fonts/Assets mit OFL, GPL, UFL, proprietären Lizenzen o. ä. erkannt werden.
- Automatisierter Abgleich der in `ATTRIBUTION.md` aufgeführten Assets mit dem tatsächlichen Bestand.
