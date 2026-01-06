# ERDA Book – Release v2.0.0 Plan

**Status:** draft
**Letzte Aktualisierung:** 2026-01-06

---

## 🎯 Scope (geplant)
- Neues Kapitel **10. Das KI Konzept** (Konzept, Governance, Ethik, Architektur, Use-Cases).
- Überarbeitung **EDA Konzept** (Kap. 5) inhaltlich und strukturell.
- Lektorale, inhaltsschärfende Überarbeitungen (DE/EN), Konsistenz in Terminologie & Narrative.

## 📦 Deliverables
- Vollständige Inhalte in `/de` und `/en` (Kapitel, SUMMARY, Book JSON).
- Aktualisierte Publikationsdateien (`de/en/publish.yml`, PDFs/MDs in `publish/`).
- Release-Dokumentation in `release-docs/v2.0.0` (Status, Notes, Certification).
- Tag `v2.0.0` und optional Zenodo-Record.

## 🗺️ Meilensteine
1) Struktur & Outline festziehen (Kap. 10, EDA-Redlines) — **TBD**
2) Inhaltliche Ausarbeitung DE — **TBD**
3) Übersetzung/Adaption EN — **TBD**
4) Technische Reviews (Build/Orchestrator, Links, Fonts) — **TBD**
5) Content-Freeze & PDFs — **TBD**
6) Final Review & Tag `v2.0.0` — **TBD**

## 🔧 Arbeitsströme & Aufgaben
- **Kapitel 10 (KI Konzept):** Outline, Kernthesen, Leitplanken (Ethik, Safety, Governance), Architekturskizze, Use-Cases, Quellen.
- **EDA-Überarbeitung:** Aktualisierte Leitidee, Membership/Structure, Doktrin, Integration, DSN, Nukleare Abschreckung, Kommunikation; Querverweise ins Gesamtkonzept.
- **Lektorat/Schärfung:** Terminologie-Glosar-Check, konsistente Überschriften/IDs, kurze Abstracts pro Abschnitt, Figuren/Boxen prüfen.
- **Internationalisierung:** DE → EN Synchronisation, SUMMARY in beiden Sprachen konsistent, Links/Assets prüfen.
- **Tooling/Build:** Orchestrator-Run (Docker), Fonts sync, Status-Checks grün, PDF/MD-Artefakte aktualisieren.

## ✅ Ready-for-Release Checkliste
- [ ] Inhalte komplett (DE/EN) inkl. SUMMARY, Book-JSON aktualisiert.
- [ ] Kap. 10 fertig; EDA (Kap. 5) überarbeitet.
- [ ] Lektorat/Terminologie geprüft; Links/Querverweise funktionieren.
- [ ] Orchestrator (de/en) erfolgreich durchgelaufen, PDFs/MDs committed.
- [ ] Release-Dokus (`release-docs/v2.0.0`) aktualisiert (Notes, Status, Certification).
- [ ] Tag `v2.0.0` gesetzt und gepusht; ggf. Zenodo-Publish.

## 📋 Nächste Schritte (kurzfristig)
- Outline für Kapitel 10 abstimmen und ins Repo legen.
- Redline-Plan für EDA-Konzept festlegen (Abschnitte priorisieren).
- Lektorats-Guidelines/Terminologie-Liste aktualisieren.

## ⚠️ Risiken & Beobachtung
- Umfang Kap. 10 könnte Zeitplan strecken.
- Übersetzungsdrift DE/EN bei späten Änderungen.
- Build/Fonts/Orchestrator: sicherstellen, dass Docker-Image und CI grün bleiben.

---

**Lizenz:** CC BY-SA 4.0 (Release-Dokumentation)
