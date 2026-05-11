# Release v2.5.0 – Status

**Codename:** Democratic Knowledge
**Stand:** 2026-05-11
**Phase:** Finale v2.5.0-Vorbereitung auf `release_candidate`; gitbook_worker 2.9.1 integriert, Tag/Publisher-Freigabe offen

---

## Checkliste

| # | Aufgabe | Status | Anmerkung |
|---|---|---|---|
| 1 | Versionsumstellung (README, book.json, CITATION.cff) | ✅ | v2.5.0 |
| 2 | Release-Docs-Ordner angelegt | ✅ | |
| 3 | „Demokratisches Wissen" – DE + EN erstellt | ✅ | `desktop/misc/` |
| 4 | Release History aktualisiert | ✅ | `Releases.md` |
| 5 | Redaktionelle Überarbeitung README | ✅ | DE + EN, Commit dcf68c2 |
| 6 | Paper-Integration: Kindererziehung → §11.3.7 | ✅ | DE + EN, Commit e7e5005 |
| 7 | Paper-Integration: Mosaik-Prinzip → §5.8.4 | ✅ | DE + EN, Commit e7e5005 |
| 8 | Paper-Integration: Anti-Game-Over → Anhang P.1 | ✅ | DE + EN, ursprünglich Commit e7e5005, nachträglich nach P verschoben |
| 9 | Querverweise (11.2, 3.5, 4.3.5 → Anhang P.1) | ✅ | DE + EN, nach M/P-Entscheidung aktualisiert |
| 10 | SUMMARY.md + book.json aktualisiert | ✅ | DE + EN, Commit e7e5005 |
| 11 | Konsistenzprüfung Mini-Wording-Set | ✅ | DE + EN ergänzt, v2.5-Begriffe aufgenommen |
| 12 | Content-Freeze | ⏳ | nach finaler Redakteur-/Publisher-Freigabe |
| 13 | Publish-Artefakte (PDF/MD) | ✅ | v2.5.0-Lauf DE/EN mit gitbook_worker 2.9.1 erfolgreich; nach Kapitel-8-Anhangserweiterung (Anhänge 8.A–8.D) und §10.2.1 DE 880 Seiten, EN 837 Seiten |
| 14 | Zertifizierungsprotokoll | ⏳ | Final-Gates und 2.9.1-Quality-Gate dokumentiert; Tag-/Publisher-Entscheidung offen |
| 15 | Final Review & Tag | ⏳ | |
| 16 | Root-Attribution + Metadaten-Gate | ✅ | `ATTRIBUTION.md`, README/book/CFF/Zenodo synchronisiert |
| 17 | Frontmatter-Normalisierung | ✅ | DE/EN `content_id`, `content_lang`, EN `source`, `status`; keine Content-Keys `lang`, `language`, `lang-version` wegen PDF-Fontfallback |
| 18 | EN-Querverweise Appendix P.1 | ✅ | Kapitel 3.5, 4.3.5, 11.2 und 11.3 aktualisiert |
| 20 | Anhang M als messbarer Buchprojektmaßstab | ✅ | DE + EN, aus `buchprojektentscheidungen-v2.5.0.md` abgeleitet |
| 19 | Worker-Roles-Durchgang „Ethik vor Strategie“ | ✅ | Kapitel 2/3/11/12/H/I ethisch gestärkt, Kapitel 5/13/14/D/I strategisch nachgeschärft |
| 21 | CIVITAS Public als Anhang P.2 | ✅ | DE + EN, DOI 10.5281/zenodo.19443256, APA-Zitation im Paperkopf |
| 22 | Kapitel 6 CIVITAS vertieft | ✅ | DE + EN, Governance, Publikationslogik, Technik, Rechtsschutz, Partnerschaften, Bildung, Roadmap |
| 23 | Kapitel 8 ARKTIS konsolidiert | ✅ | DE + EN, Wenigzeiler zusammengelegt, strategische Säulen vertieft, HTML-Tabellen in Markdown-Tabellen zurückgeführt |
| 24 | Kapitel 10 §10.2.1 Demokratie der Mündigen | ✅ | DE + EN, neuer Verantwortungsrahmen nach Reife, Rolle und Fähigkeit |

---

## Offene Punkte

- Finaler Review der Kapitelverweise nach Frontmatter- und Pfadnormalisierung
- Content-Freeze nach Redakteur-Freigabe
- 2.9.1-Publish-Artefakte in finaler Sichtprüfung bestätigen
- Zertifizierungsprotokoll final entscheiden
- Final Review & Tag

## Erledigte Punkte

- [x] Release-Planung erstellt
- [x] Versionsumstellung auf v2.5.0
- [x] „Demokratisches Wissen" DE + EN verfasst
- [x] Desktop-Ablage
- [x] README „Beiträge und Qualität" überarbeitet (DE + EN)
- [x] Kindererziehung-Essay als §11.3.7 integriert (DE + EN)
- [x] Mosaik-Prinzip als §5.8.4 integriert (DE + EN)
- [x] Anti-Game-Over-Prinzip als Anhang P.1 / Paper erstellt (DE + EN)
- [x] CIVITAS Public als Anhang P.2 / Paper erstellt (DE + EN)
- [x] Kapitel 6 als CIVITAS-Architektur vertieft (DE + EN)
- [x] Kapitel 10 §10.2.1 als Demokratie der Mündigen / Democracy of the Mature synchronisiert (DE + EN)
- [x] Anhang M als messbarer Buchprojektmaßstab erstellt (DE + EN)
- [x] Querverweise in Kap. 11.2, 3.5, 4.3.5 (DE)
- [x] SUMMARY.md + book.json aktualisiert (DE + EN)
- [x] Root-`ATTRIBUTION.md` ergänzt
- [x] Release-Metadaten synchronisiert (README, book.json, CFF, Zenodo) auf 2026-05-11 / v2.5.0
- [x] YAML-Frontmatter DE/EN normalisiert
- [x] DE/EN-Querverweise auf Anhang/Appendix P.1 aktualisiert
- [x] Glossar + Mini-Wording-Set um v2.5-Begriffe erweitert
- [x] Worker-Roles-Durchgang „Ethik vor Strategie“ zweisprachig integriert
- [x] gitbook_worker 2.9.1 Abnahmefix integriert; `editorial-quality` fuer DE/EN/Project mit `passed_with_warnings`, 0 blocked, 0 fail reproduziert
