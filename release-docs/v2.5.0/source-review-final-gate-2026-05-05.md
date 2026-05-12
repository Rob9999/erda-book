# Finales Quellen- und Link-Gate v2.5.0

**Datum:** 2026-05-05
**Rolle:** Redakteur:in
**Scope:** risikobasierter v2.5-Finalscope: Kapitel 13.8, Anhang P.1, Anhang P.2, Kapitel 11.3.7, Kapitel 5.8.4, Anhang M und Kapitel 6 DE.
**Status:** erfüllt mit dokumentierter Begrenzung; keine bekannte 404- oder DOI-Blockade im geprüften Finalscope.

---

## 1. Tool-Dry-run

Ausgeführt wurde der gitbook_worker-Referenzcheck als deterministischer Dry-run ohne Dateiveränderung:

```powershell
.\.venv\Scripts\python.exe -m gitbook_worker.tools.quality.ai_references --root . --language de --as-of-date 2026-05-05 --include-inline-references --include-markdown-links --include-frontmatter-dois --precheck-only --dry-run --json-report tmp/gitbook-worker-ai-v2.5.0/ai-references-v2.5-final-scope-dry-run-20260505-200707.json --files <v2.5-finalscope> --no-progress
```

**Ergebnis:** 35 validiert, 0 failed, 0 rate-limited, 0 repaired, 0 suggested.

Der Dry-run wurde bewusst mit `--precheck-only` ausgeführt. AI-Ergebnisse bleiben im Projekt nur Suchhilfe, nicht Quellenwahrheit; die Freigabe beruht auf technischer Erreichbarkeit und manueller Gegenprüfung.

---

## 2. Link-Audit und Sources-Export

Für denselben Scope wurden zusätzlich ausgeführt:

- `gitbook_worker.tools.quality.link_audit` mit HTTP-Report, Bildcheck, Duplicate-Heading-Check, Citation-Check und TODO-Scan.
- `gitbook_worker.tools.quality.sources` als Quellenexport.

**Reports:**

- `tmp/gitbook-worker-ai-v2.5.0/link-audit-v2.5-final-scope-20260505-200724.csv`
- `tmp/gitbook-worker-ai-v2.5.0/sources-v2.5-final-scope-20260505-200730.csv`

**Link-Audit-Befund:**

| Prüfung | Ergebnis |
|---|---|
| DOI-/HTTP-Links | 0 broken, 2 good |
| Lokale/remote Bilder im Scope | 0 issues |
| Zitationsnummern | 0 files with gaps |
| TODO/FIXME-Marker | 0 entries |
| Duplicate headings | 1 generischer Hinweis `Zusammenfassung` zwischen P.1/P.2 |

Der Duplicate-Heading-Hinweis ist kein Quellen- oder Linkblocker, sondern ein globaler Überschriftenhinweis über zwei Paper-Dateien hinweg. Im jeweiligen Paper-Kontext ist `Zusammenfassung` eine normale Abschnittsüberschrift.

---

## 3. Manuelle Stichprobe

Manuell geprüft wurden die zwei Paper-DOIs sowie vier aktuelle EU-/Eurostat-Quellen aus Kapitel 13.8.

| Referenz | Manuell bestätigter Inhalt | Entscheidung |
|---|---|---|
| `https://doi.org/10.5281/zenodo.19244929` | Zenodo-Record `Childhood, Adulthood, and the Anti-Game-Over Principle`, Version 1.0.0, veröffentlicht 27. März 2026, Lizenz CC BY 4.0, DOI korrekt. | bleibt |
| `https://doi.org/10.5281/zenodo.19443256` | Zenodo-Record `CIVITAS Public: Building a European Digital Agora — A Call to Action`, Version 1.0, veröffentlicht 6. April 2026, Working Paper, Lizenz CC BY 4.0, DOI korrekt. | bleibt |
| EU DG Energy, Solar energy | Seite nennt 272,5 GW (2023), 338 GW (2024), 406 GW (2025) und bestätigt geschätzte 406 GW EU-Solarkapazität 2025. | bleibt |
| European Commission, Social Climate Fund | Seite nennt Start 2026, Zeitraum 2026-2032 und 86,7 Mrd. EUR Finanzierung. | bleibt |
| Eurostat, EU imports of energy products | Datenstand März 2026; bestätigt 2025 USA 56,0 % bei LNG und Norwegen 52,1 % bei gasförmigem Erdgas. | bleibt |
| EU DG Energy, Gas storage | Bestätigt Regulation (EU) 2025/1733, Veröffentlichung 10. September 2025 und 90-%-Ziel in einem Zeitraum 1. Oktober bis 1. Dezember. | bleibt |

---

## 4. Begrenzung und Restrisiko

Dieses Gate schließt nicht die vollständige Aktualitätsprüfung des gesamten Buches. Der Gesamtbestand, insbesondere Anhang B Staatenprofile, bleibt als v2.6-/Backlog-Thema dokumentiert. Für v2.5.0 wurde der Scope bewusst auf neue oder stark geänderte, releaseprägende und risikobehaftete Bereiche begrenzt:

1. neue Paper P.1/P.2 und DOI-/APA-Pflichten,
2. das neue Kapitel 13.8 mit aktuellen Energiezahlen,
3. die CIVITAS-Vertiefung in Kapitel 6,
4. neue normative/qualitative Maßstabslogik in Anhang M,
5. neue Einbettungen in 11.3.7 und 5.8.4.

**Entscheidung:** Für v2.5.0 ist das Quellen-/Link-Gate im Finalscope erfüllt. Eine Gesamtbuch-Link- und Quellenaktualisierung über alle alten Staatenprofile und historischen Baselines hinaus wird nicht als Releaseblocker geführt, sondern als eigener Folgeauftrag.