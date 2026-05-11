# ERDA Book – Release v2.5.0 Plan

**Status:** finale v2.5.0-Vorbereitung auf `release_candidate`; gitbook_worker 2.9.1 integriert, Tag/Publisher-Freigabe offen
**Letzte Aktualisierung:** 2026-05-11

---

## 🎯 Scope

Release 2.5.0 markiert die **konzeptionelle Vertiefung** des ERDA-Buches. Während v2.0.0 die institutionelle und vertragliche Architektur etabliert hat, fokussiert v2.5.0 auf die **normativen Grundlagen demokratischer Handlungsfähigkeit** – das „Demokratische Wissen" als Orientierungsrahmen für Bürger:innen, Entscheidungsträger:innen und Institutionen.

### Kernthemen

1. **Demokratisches Wissen – Sieben Prinzipien**
   Leitlinien zu Macht, Umgang mit nicht-demokratiewilligen Staaten, Frieden und Sicherheit, Wahrheit und Täuschung, Demokratie, Technologie/KI und der inneren Verfassung. Als eigenständiges Dokument und potentielles Buchkapitel.

2. **Paper-Integration und Konzeptvertiefung**
   - **Kindererziehung** → §11.3.7: Erziehungsleitbild in Freiheit und Verantwortung (12 Leitsätze)
   - **Mosaik-Prinzip** → §5.8.4: Strategische Reflexion zur demokratischen DSN-Resilienz
   - **Anti-Game-Over-Prinzip** → Anhang P.1: Paper zum entwicklungsphilosophischen Modell prosperativen Lebens (DOI: 10.5281/zenodo.19244929; APA-Zitation im Paperkopf)
   - **CIVITAS Public** → Anhang P.2: veröffentlichtes Working Paper zur europäischen digitalen Agora (DOI: 10.5281/zenodo.19443256; APA-Zitation im Paperkopf)
   - **Kapitel 6** → operative CIVITAS-Vertiefung: Governance, Publikationslogik, Review, Technik, Rechtsschutz, Partnerschaften, Bildung und Roadmap
   - **Buchprojektmaßstab** → Anhang M: messbare Buchprojektentscheidungen, Release-Kriterien und Quellenstandards

3. **Redaktionelle Qualitätsoffensive**
   - Überarbeitung der README-Abschnitte „Beiträge und Qualität" (DE + EN) im professionellen redaktionellen Ton (bereits umgesetzt in v2.0.0-Nacharbeiten).
   - Konsistenzprüfung aller Kapitel gegen das Mini-Wording-Set.
   - Worker-Roles-Durchgang „Ethik vor Strategie": ethisch-moralische Stärkung der Kapitel 2, 3, 11, 12 und Anhang H; anschließende strategische Nachschärfung der Kapitel 5, 13, 14 und Anhang D.

4. **Desktop-Materialien**
   - Eigenständige Kurzformen für schnelle Kommunikation (Flyer, Vorträge, Social-Media-Referenz).
   - „Demokratisches Wissen" als DE + EN Dokument in `desktop/misc/`.
   - Konzeptpapiere und Paper-Materialien in `desktop/misc/` und `desktop/papers/`.

### Weitere mögliche Inhalte nach v2.5.0

- Vertiefung der Bürgerresilienz-Modelle (Kap. 11)
- Glossar-Erweiterung
- Konsistenz-Review aller Kapitelverweise nach v2.0.0-Erweiterung

---

## 🗺️ Meilensteine

| # | Meilenstein | Status |
|---|---|---|
| 1 | Release-Planung und Versionsumstellung (v2.5.0) | ✅ |
| 2 | „Demokratisches Wissen" – Texterstellung DE + EN | ✅ |
| 3 | Desktop-Ablage (DE + EN) | ✅ |
| 4 | Paper-Integration (Kindererziehung, Mosaik-Prinzip, Anti-Game-Over, CIVITAS Public) | ✅ |
| 5 | Redaktionelle Qualitätsprüfung (README, Mini-Wording-Set) | ✅ |
| 6 | Content-Freeze & Artefakte (PDF/MD) | ⏳ |
| 7 | Final Review & Tag `v2.5.0` | ⏳ |

---

## 📦 Deliverables

- „Demokratisches Wissen" als Desktop-Dokument (`desktop/misc/`) in DE + EN
- Konzeptpapiere integriert: §11.3.7 + §5.8.4 + Anhang P.1 + Anhang P.2 (DE + EN)
- Anhang M als messbarer Buchprojektmaßstab ergänzt (DE + EN)
- Kapitel 6 als operative CIVITAS-Architektur vertieft (DE + EN)
- Querverweise in Kapiteln 11.2, 3.5, 4.3.5 (DE + EN)
- Aktualisierte Versionsnummern und Metadaten (README, book.json, CITATION.cff)
- Rollenbasierte Ethik-vor-Strategie-Integration (DE + EN) inklusive Glossar- und Anhang-K-Dokumentation
- Kapitel 8 ARKTIS redaktionell konsolidiert und vertieft (DE + EN)
- Root-Attribution und normalisiertes DE/EN-Frontmatter
- Release-Dokumentation in `release-docs/v2.5.0/`
- Aktualisierte Publish-Artefakte (PDF/MD) nach Content-Freeze; aktueller RC-Artefaktstand mit gitbook_worker 2.9.1 nach Kapitel-8-Konsolidierung: DE 866 Seiten, EN 826 Seiten

---

## 🔧 Arbeitsströme & Aufgaben

- [x] Versionsumstellung auf v2.5.0 (README, book.json, CITATION.cff)
- [x] Release-Docs-Ordner `v2.5.0/` anlegen
- [x] „Demokratisches Wissen" – Texterstellung (7 Prinzipien)
- [x] Desktop-Ablage DE + EN
- [x] Paper-Integration: Kindererziehung → §11.3.7 (DE + EN)
- [x] Paper-Integration: Mosaik-Prinzip → §5.8.4 (DE + EN)
- [x] Paper-Integration: Anti-Game-Over → Anhang P.1 (DE + EN)
- [x] Paper-Integration: CIVITAS Public → Anhang P.2 (DE + EN)
- [x] Kapitel-6-Vertiefung: CIVITAS Public, Governance, Technik, Rechtsschutz, Roadmap (DE + EN)
- [x] Maßstab-Integration: Buchprojektentscheidungen → Anhang M (DE + EN)
- [x] Querverweise in Kap. 11.2, 3.5, 4.3.5 (DE + EN)
- [x] SUMMARY.md aktualisiert (DE + EN)
- [x] book.json-Datum auf 2026-05-11 (DE + EN)
- [x] Root-`ATTRIBUTION.md` ergänzt
- [x] Frontmatter DE/EN normalisiert (`content_id`, `content_lang`, EN `source`, `status`; keine Content-Keys `lang`, `language`, `lang-version` wegen PDF-Fontfallback)
- [x] Konsistenzprüfung gegen Mini-Wording-Set
- [x] Worker-Roles-Durchgang „Ethik vor Strategie“ integriert (DE + EN)
- [ ] Content-Review und ggf. Integration als Buchkapitel
- [x] Publish-Artefakte (PDF/MD) mit v2.5.0-Metadaten erneuert (DE + EN, gitbook_worker 2.9.1; Quality-Gate `passed_with_warnings`, 0 blocked, 0 fail)
- [x] Zertifizierungsprotokoll erstellt; finale Freigabeentscheidung bleibt offen
- [ ] Tag und Release
