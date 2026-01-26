# ERDA Book – Release v2.0.0 Plan

**Status:** draft
**Letzte Aktualisierung:** 2026-01-26

---

## 🎯 Scope (geplant)
- Normative Schärfung des ERDA-Leitbilds:
ERDA als evolutive, verfassungsgemäß gebundene Weiterentwicklung der EU – explizit, konsistent und kapitelübergreifend verankert.
- Neues Kapitel **10. Das KI Konzept** (Konzept, Governance, Ethik, Architektur, Use-Cases).
- Beginn / Ausbau **11. Das Bürger Konzept** (evolutiv stabile Resilienzmodelle für Alltag, Bildung, Pflichten/Rechte, Anreize, Dienste, Mitwirkung).
- Überarbeitung **EDA Konzept** (Kap. 5) inhaltlich und strukturell.
- Lektorale, inhaltsschärfende Überarbeitungen (DE/EN), Konsistenz in Terminologie & Narrative.

## 🧭 Aktueller Stand (2026-01-26)

- **Kapitel 10 (KI Konzept):** begonnen und **nahezu fertiggestellt** (DE als Source of Truth, EN synchron als Draft).
- Ergänzt wurden u. a. **Executive Summary** (nicht nummeriert, zitierfähig) am Kapitelanfang sowie **Anhang 10.A (KEI)** als Reife-/Frühwarninstrument.
- Navigation (`SUMMARY.md`) und Publish-Artefakte (MD/PDF) wurden für DE/EN bereits aktualisiert.
- **Kapitel 11 (Bürger Konzept):** begonnen (Einleitung/Grundrahmen vorhanden; Ausbau der Unterkapitel als nächster Arbeitsblock).

## 📦 Deliverables
- Vollständige Inhalte in `/de` und `/en` (Kapitel, SUMMARY, Book JSON).
- Aktualisierte Publikationsdateien (`de/en/publish.yml`, PDFs/MDs in `publish/`).
- Release-Dokumentation in `release-docs/v2.0.0` (Status, Notes, Certification).
- Tag `v2.0.0` und optional Zenodo-Record.

## 🗺️ Meilensteine
1) Struktur & Outline festziehen (Kap. 10, EDA-Redlines) — **in Arbeit**
2) Inhaltliche Ausarbeitung DE — **Kap. 10: weitgehend abgeschlossen**; **Kap. 5: offen**
3) Übersetzung/Adaption EN — **Kap. 10: synchron (draft)**; Kap. 11 **begonnen (draft)**; weitere Kapitel **TBD**
4) Technische Reviews (Build/Orchestrator, Links, Fonts) — **laufend**
5) Content-Freeze & PDFs — **nach Kap. 5 / Konsistenzreview**
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
- [ ] Kap. 11 (Bürger Konzept) im geplanten Umfang fertiggestellt.
- [ ] Lektorat/Terminologie geprüft; Links/Querverweise funktionieren.
- [ ] Orchestrator (de/en) erfolgreich durchgelaufen, PDFs/MDs committed.
- [ ] Release-Dokus (`release-docs/v2.0.0`) aktualisiert (Notes, Status, Certification).
- [ ] Tag `v2.0.0` gesetzt und gepusht; ggf. Zenodo-Publish.

## 📋 Nächste Schritte (kurzfristig)
- Restarbeiten und Konsistenz-Review Kapitel 10 abschließen (Querverweise, Terminologie, Redlines).
- Struktur-/Prioritätenliste für Kapitel 11 definieren (welche Unterkapitel in v2.0.0 zwingend, welche optional).
- EDA-Redline-Plan finalisieren und Kap. 5 priorisiert überarbeiten.
- Redline-Plan für EDA-Konzept festlegen (Abschnitte priorisieren).
- Lektorats-Guidelines/Terminologie-Liste aktualisieren.

## ⚠️ Risiken & Beobachtung
- Missverständnisrisiko „ERDA = Bruch mit der EU“ → durch explizite Leitformeln und Wiederholungen minimieren.
- Umfang Kap. 10 könnte Zeitplan strecken.
- Übersetzungsdrift DE/EN bei späten Änderungen.
- Build/Fonts/Orchestrator: sicherstellen, dass Docker-Image und CI grün bleiben.

---

**Lizenz:** CC BY-SA 4.0 (Release-Dokumentation)
