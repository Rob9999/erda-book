# Das ERDA Buch – Release v2.5.0

**Datum:** 2026-05-05
**Tag:** `v2.5.0`
**Release name:** Democratic Knowledge
**Autor:** Robert Alexander Massinger (mit ChatGPT/OpenAI und GitHub Copilot/Anthropic)

---

## 📋 Zusammenfassung

Version 2.5.0 vertieft die **normativen Grundlagen** des ERDA-Buches. Im Zentrum steht das Dokument **„Demokratisches Wissen"** – sieben Prinzipien, die als Leitfaden für demokratische Handlungsfähigkeit dienen: zu Macht, zum Umgang mit nicht-demokratiewilligen Staaten, zu Frieden und Sicherheit, zu Wahrheit und Täuschung, zur Demokratie selbst, zu Technologie/KI und zur inneren Verfassung einer demokratischen Gesellschaft.

Darüber hinaus integriert dieses Release konzeptionelle Papers und Umsetzungsbausteine als Buchinhalte: ein **Erziehungsleitbild** (§11.3.7), eine **strategische Reflexion zum Mosaik-Prinzip** (§5.8.4), das **Anti-Game-Over-Prinzip** als **Anhang P.1** und **CIVITAS Public** als **Anhang P.2**. Neu ist außerdem **Anhang M** als messbarer Buchprojektmaßstab für Release-Kriterien, Quellenstandards und offene Projektentscheidungen. Kapitel 6 wurde passend dazu als operative CIVITAS-Architektur vertieft.

---

## ✨ Änderungen

### Neue Inhalte

- **„Demokratisches Wissen" (Sieben Prinzipien):** Eigenständiges Referenzdokument als Desktop-Material (DE + EN) mit klaren, zitierfähigen Leitsätzen zu den Kernthemen demokratischer Resilienz.

- **§11.3.7 – Leitbild: Kindererziehung in Freiheit und Verantwortung (DE + EN):**
  Zwölf Leitsätze für eine demokratische Erziehungskultur – von Verantwortungsübernahme über Angstfreiheit bis zum Umgang mit Macht und Gewissen. Eingefügt in Kapitel 11.3 „Was brauchen Bürger?".

- **§5.8.4 – Strategische Reflexion: Mosaik-Prinzip und demokratische DSN-Resilienz (DE + EN):**
  Verbindung des aus autoritärer Kriegsführung bekannten Mosaik-Prinzips mit der rechtsstaatlich gebundenen DSN-Architektur. Eingefügt in Kapitel 5.8 „Defence Sovereignty Nodes".

- **Anhang M – Maßstab: messbare Buchprojektentscheidungen und Release-Kriterien (DE + EN):**
  Neuer Maßstabsanhang: übersetzt die Buchprojektentscheidungen in prüfbare Kriterien für Baselines, Quellen, Szenarien, Draft-Status, Paper-Compliance und Release-Restrisiken.

- **Anhang P.1 – Paper: Kindheit, Erwachsenwerden und das Anti-Game-Over-Prinzip (DE + EN):**
  Paper-Anhang: entwicklungsphilosophisches Modell, das Kindheit und Erwachsensein als zyklisch wiederkehrende Grundformen offenen Lebens versteht. Formuliert Anti-Game-Over-Prinzipien und das Ideal eines *prosperativen Lebens*. (DOI: 10.5281/zenodo.19244929; APA-Zitation im Paperkopf)

- **Anhang P.2 – Paper: CIVITAS Public: Building a European Digital Agora (DE + EN):**
  Paper-Anhang: veröffentlichtes Working Paper zur europäischen digitalen Agora als erste operative Schicht der größeren CIVITAS-Vision. Enthält DOI, APA-Zitation, deutsche Einordnung und den veröffentlichten englischen Originaltext. (DOI: 10.5281/zenodo.19443256; APA-Zitation im Paperkopf)

- **Kapitel 6 – Das CIVITAS Konzept (DE + EN):**
  Deutlich vertieft als Buchkapitel: CIVITAS Public, Rollen- und Publikationsarchitektur, Review-Level, Governance-Gremien, technische Schichten, DSGVO-/DSA-Schutz, Young CIVITAS, Partnerschaften und Roadmap.

- **Querverweise** in den Kapiteln 11.2, 11.3, 3.5 und 4.3.5 auf Anhang P.1 sowie in Kapitel 6 auf Anhang P.2.

### Redaktionelle Verbesserungen

- **README „Beiträge und Qualität":** DE- und EN-Abschnitte in professionellem redaktionellem Ton umgeschrieben – das ERDA-Buch als lebendiges Dokument demokratischer Resilienz, mit strukturierten Leitlinien (Qualitätsanspruch, verbindliche Regeln, Peer-Review-Prinzip).

- **Rollen- und Freigabemodell:** Writer, Editor, Lektor, Redakteur und Publisher wurden mit Rechten, Pflichten, Freigabegrenzen und demokratischer Rollenpflicht in `worker-roles.md` definiert und in den verbindlichen Guides verankert.

- **Ethik vor Strategie:** Ein Worker-Roles-Durchgang stärkt Kapitel 2, 3, 11, 12 und Anhang H ethisch-moralisch und schärft danach Kapitel 5, 13, 14 sowie Anhang D strategisch nach. Neue Glossarbegriffe sind u. a. Demokratie der Mündigen, Wir sind der Staat, demokratische Bündnisverlässlichkeit, Ukraine-First-Prinzip und Anti-Veto.

- **Glossar und Mini-Wording:** Zentrale v2.5-Begriffe wurden redaktionell ergänzt: Demokratisches Wissen, Mosaik-Prinzip, Anti-Game-Over-Prinzip und prosperatives Leben.

### Technisch

- Versionsumstellung auf v2.5.0
- Release-Dokumentation in `release-docs/v2.5.0/`
- Desktop-Materialien in `desktop/misc/`
- `book.json`-Datum aktualisiert auf 2026-05-05 (DE + EN)
- SUMMARY.md aktualisiert (DE + EN) mit Anhang-M- und Anhang-P-Einträgen
- Root-`ATTRIBUTION.md` als Primärquelle für Drittinhalte ergänzt
- YAML-Frontmatter mit `content_id`, `content_lang`, `source` und `status` für DE/EN-Inhaltsdateien normalisiert; Pandoc/Babel-nahe Keys wie `lang`, `language` und `lang-version` werden im Content-Frontmatter vermieden, um Twemoji/ERDA-CJK-Fontfallbacks im PDF stabil zu halten
- Release-Metadaten-Gate umgesetzt: README-Datum, `book.json`, CFF-Dateien und `.zenodo.json` synchronisiert
- Englische Appendix-J/L-Dateipfade auf `appendix-j-license-and-openness.md` und `appendix-l-colophon.md` normalisiert
- DE/EN-Querverweise auf Appendix/Anhang P.1 in Kapitel 3.5, 4.3.5, 11.2 und 11.3 aktualisiert
- DE/EN-Querverweise auf Appendix/Anhang P.2 in Kapitel 6 ergänzt
- Vendorte gitbook_worker-Version auf 2.4.0 aktualisiert; EN-Titelseite, Projektversion und ERDA-CJK-Fallback wurden damit wieder konsistent erzeugt
- Quellen-/Link-Gate für den v2.5-Finalscope per gitbook_worker-Dry-run, Link-Audit, Sources-Export und manueller Webprüfung dokumentiert

---

## 📦 Mehrsprachige Versionen in diesem Release

- de (Source of Truth)
- en (synchron, Draft/Review; keine native finale Vollfreigabe in diesem Release)

---

## 🔗 Weiterführende Dokumente

- [Release-Plan](release-plan-v2.5.0.md)
- [Release-Status](RELEASE-2.5.0-STATUS.md)
