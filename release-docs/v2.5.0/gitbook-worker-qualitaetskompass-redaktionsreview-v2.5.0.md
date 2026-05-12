---
version: 1.0.0
date: 2026-05-09
status: proposed
target_release: "gitbook_worker v2.9.0 Qualitaetskompass"
review_role: Redakteur:in
source_status: Lieferanten-Pflichtenheft proposed 2026-05-09
history:
  - "1.0.0: 2026-05-09 - Redaktionelle Pruefung und ERDA-Ergaenzungen zum Qualitaetskompass-Pflichtenheft dokumentiert."
---

# Redaktionelles Review: Qualitaetskompass-Pflichtenheft

**Gegenstand:** Pflichtenheft des gitbook_worker-Lieferanten fuer redaktionelle Qualitaetsmetriken und Abnahmewerkzeuge  
**Zielrelease des Lieferanten:** `v2.9.0 Qualitaetskompass`  
**ERDA-Kontext:** v2.5.0-Finalisierung nach gitbook_worker 2.8.0-Default-Build  
**Redaktionelle Rolle:** Redakteur:in

## Kurzentscheidung

Das Pflichtenheft ist redaktionell **grundsaetzlich abnahmefaehig als Entwicklungsauftrag**, wenn die unten genannten ERDA-Ergaenzungen in den Lieferantenscope aufgenommen oder als verbindliche Abnahmekriterien nachgezogen werden.

Die Stoßrichtung ist richtig: Die Schlussredaktion braucht ein einziges Dossier, das vorhandene Einzeltools, Build-Metriken, PDF-Befunde, Quellenlage, Frontmatter-Status und Restbefunde nachvollziehbar zusammenfuehrt. Genau diese Zerstreuung war im v2.5.0-Prozess ein reales Risiko.

## Was am Pflichtenheft bereits passt

| Bereich | Redaktionelle Bewertung |
|---|---|
| Trennung Metrik vs. Entscheidung | Richtig. Das Werkzeug darf keine menschliche Freigabe ersetzen. |
| Offline-Default | Richtig und wichtig fuer Datenschutz, Kundenprojekte und reproduzierbare CI-Laeufe. |
| JSON plus Markdown | Richtig. JSON fuer Maschinen, Markdown fuer Redakteur:innen und Publisher-Freigabe. |
| Severity-Modell | Richtig, muss aber um redaktionelle Ausnahme-/Restrisiko-Logik ergaenzt werden. |
| Integration bestehender Tools | Richtig. Link-Audit, AI-Referenzcheck, PDF-TOC, Font-/PDF-Checks und Tabellenstrategie duerfen nicht weitere Inselloesungen bleiben. |
| Exit-Codes | Richtig. CI braucht eindeutige Gruende fuer `failed` und `blocked`. |

## ERDA-Ergaenzungen als Muss-Anforderungen

### E1 Report-Drift und Artefakt-Frische

Das Abnahmewerkzeug MUSS erkennen, ob Release-Dokumentation, Metrikreports und Artefakte zueinander passen.

Mindestsignale:

| Pruefung | Erwartung |
|---|---|
| Worker-Version | Report nennt installierte Worker-Version und Build-Worker-Version pro Artefakt. |
| PDF-Frische | PDF `CreationDate`/Dateigroesse/Seitenzahl werden im Dossier ausgewiesen. |
| Report-Frische | Alte Metrikreports duerfen nicht stillschweigend als aktuelle Freigabegrundlage erscheinen. |
| Dokumentationsdrift | Wenn Release-Doku noch alte Seitenzahlen, alte Worker-Versionen oder alte Layoutbefunde nennt, muss mindestens `warn`, bei finalem Releaseprofil `fail` entstehen. |

Begruendung aus v2.5.0: Nach dem Wechsel von gitbook_worker 2.7.0 auf 2.8.0 waren PDF-Artefakte deutlich besser, aber mehrere Release-Dokumente nannten weiterhin 2.7.0, 1016/978 Seiten oder alte Layoutbefunde.

### E2 Wenigzeiler- und Leerseiten-Metrik

Das PDF-Metriktool MUSS textarme Seiten strukturiert ausweisen.

Mindestmetriken:

| Metrik | Beschreibung |
|---|---|
| `pages_total` | Gesamtseitenzahl je PDF. |
| `low_text_pages_le_15` | Seiten mit hoechstens 15 nichtleeren Inhaltszeilen, reine Seitenzahl-Footer ignoriert. |
| `very_low_text_pages_le_5` | Seiten mit hoechstens 5 Inhaltszeilen. |
| `empty_text_pages` | Seiten ohne extrahierbare Inhaltszeile. |
| `low_text_reason_hint` | Heuristik: Tabelle, Bild/Caption, Kapitelstart, Quellen-/URL-Seite, unbekannt. |

Die Schwellen muessen konfigurierbar sein. Fuer ERDA haben sich `15` und `5` als sinnvolle redaktionelle Startwerte erwiesen.

### E3 Seitenzahl- und Zielkorridor-Pruefung

Das Abnahmewerkzeug SOLL pro Profil optionale Zielkorridore fuer Seitenzahlen und Delta-Grenzen unterstuetzen.

Beispiel:

```yaml
acceptance_profile:
  pdf_targets:
    de/publish/das-erda-buch.pdf:
      target_pages_min: 820
      target_pages_max: 850
      warn_pages_max: 875
    en/publish/the-erda-book.pdf:
      target_pages_min: 820
      target_pages_max: 850
```

Ein Zielkorridor ist kein allgemeiner Worker-Default, sondern ein projektspezifisches Releaseprofil.

### E4 ERDA-Frontmatter- und Uebersetzungsregeln

Das Frontmatter-Modul MUSS projektspezifische Pflichtfelder und verbotene Felder abbilden koennen.

ERDA-Profil:

| Bereich | Regel |
|---|---|
| DE Content | `content_id` und `content_lang: de` erforderlich, ausgenommen Sonderdateien wie `SUMMARY.md`. |
| EN Content | `content_id`, `content_lang: en`, `source`, `status` erforderlich. |
| EN Status | `status` nur `draft`, `in-review`, `approved`. |
| Approved-Schutz | `approved` muss als bewusst freigegeben markierbar und im Report separat zaehlbar sein. |
| Verbotene Keys | `lang`, `language`, `lang-version` im Buchcontent als `fail` oder mindestens `warn`, weil Pandoc/Babel-Fontfallbacks stoeren koennen. |
| Translation Drift | EN `source` muss repo-relativ existieren; `content_id` muss DE/EN-identisch sein. |

### E5 Publikationsprofil und Scope-Klarheit

Das Werkzeug MUSS zwischen publizierten, nicht publizierten und verwaisten Dateien unterscheiden.

Mindestanforderung:

- `use_summary: true` und GitBook-SUMMARY-Reihenfolge beruecksichtigen.
- Dateien unter `desktop/`, `tmp/`, `logs/`, `release-docs/` und `publish/` nicht automatisch als Buchcontent bewerten, ausser explizit im Profil aktiviert.
- Fuer Release-Dokumentation separate Profile ermoeglichen.

### E6 PDF-TOC, SUMMARY und Heading-Abgleich

Der Abgleich Markdown zu PDF MUSS fuer ERDA mehr leisten als eine reine Anzahlpruefung.

Mindestbefunde:

- fehlende SUMMARY-Eintraege,
- PDF-Outline-Eintrag ohne korrespondierenden Markdown-Heading,
- Markdown-Heading im publizierten Scope ohne PDF-Outline, sofern durch `toc_depth` erwartet,
- auffaellige Heading-Spruenge,
- doppelte Titel im gleichen Dokument oder in direkter PDF-Naehe,
- Kapitel-/Anhang-Reihenfolge gegen `summary_appendices_last`.

### E7 Tabellenstrategie als eigener Befundblock

Die Tabellenlayout-JSONL darf nicht nur Artefakt sein, sondern MUSS aggregiert werden.

Mindestmetriken:

| Metrik | Beschreibung |
|---|---|
| Tabellen gesamt | Anzahl erkannter Markdown-Pipe-Tabellen. |
| Papierentscheidungen | Zaehlen nach A4 portrait, A4 landscape, A3/A2/A1 usw. |
| Methoden | `editorial-best-fit`, `lowest-score-fallback`, `override`, `disabled`, `oversize-preserve-column-heuristic`. |
| Problemfaelle | Tabellen mit Fallback, Override oder nicht akzeptierten Kandidaten. |
| Quellbezug | Datei und Tabellenindex oder naheliegender Heading-Kontext. |

ERDA-Erfahrung: Eine strengere `preferred_max_avg_row_lines`-Schwelle kann kontraproduktiv sein, weil Landscape-Seiten vertikal weniger Inhalt tragen. Das Dossier soll solche Trade-offs sichtbar machen.

### E8 PDF-Layout: BBox plus visuelle Review-Hinweise

PDF-Overflow-Befunde muessen quantifiziert und redaktionell einsortiert werden.

Mindestfelder:

- PDF-Seite,
- Art (`line`, `block`, `image`, `link_annotation`, `table_region`, soweit ermittelbar),
- Ueberstand in Punkten und Millimetern,
- Textauszug gekuerzt,
- vermutete Ursache,
- Healing-Step.

Kleine Ueberstaende bei DOI-/URL-Zeilen sollten im Releaseprofil als `warn` statt automatisch `fail` konfigurierbar sein, muessen aber im Dossier sichtbar bleiben.

### E9 Font- und Textextraktions-Gates

Das PDF-Metriktool MUSS Projektfonts und Extraktionssignale pruefen.

ERDA-Profil:

| Fontsignal | Erwartung |
|---|---|
| DejaVu Serif/Sans/Sans Mono | eingebettet oder begruendet ersetzt. |
| TwemojiMozilla | eingebettet, wenn `emoji_color: true`. |
| ERDACCbyCJK-Regular | eingebettet, wenn CJK/Hangul/Kana im publizierten Scope vorkommt. |
| Ersatzglyphen | auffaellige `□`, `�`, `.notdef`-Signale als Befund. |
| CJK/Hangul/Kana-Text | Stichproben muessen extrahierbar sein, wenn im Content vorhanden. |

### E10 Quellen-, Rechts- und AI-Referenzsignale

Das Akzeptanzdossier soll Quellenpruefung nicht behaupten, wenn nur technische Signale vorliegen.

Pflichtformulierung im Report:

- Linkstatus ist technische Erreichbarkeit, keine inhaltliche Quellenwahrheit.
- AI-Referenzchecks sind Such-/Plausibilitaetshilfen, keine autoritative Validierung.
- Rechts-/Konformitaetsbefunde sind redaktionelle Review-Signale, keine Rechtsberatung.

### E11 Konfigurierbare Abnahmeprofile

`editorial_acceptance` MUSS Profile unterstuetzen, mindestens:

| Profil | Zweck |
|---|---|
| `local-preview` | schnelle lokale Orientierung, keine Netzwerkchecks, Warnungen blockieren nicht. |
| `release-candidate` | harte Artefakt-, Frontmatter-, Build- und Report-Frische-Gates. |
| `publish-final` | keine blockierenden Befunde, Publisher-Sichtpruefung dokumentiert oder explizit als manuelle Freigabe referenziert. |
| `docs-only` | Release-Dokumentation ohne Buch-PDFs pruefen. |

### E12 Manuelle Freigabe und Restrisiko-Protokoll

Das Dossier MUSS einen Abschnitt fuer menschliche Entscheidung enthalten:

```yaml
human_decision:
  role: Redakteur:in | Publisher
  decision: approved | approved_with_risk | rejected | deferred
  decided_at: YYYY-MM-DD
  accepted_risks:
    - finding_id: ...
      reason: ...
```

Das Tool darf diese Felder nicht automatisch setzen. Es darf aber eine Vorlage erzeugen.

### E13 Stabile IDs und Baseline-Vergleich

Findings brauchen stabile IDs, die nicht bei jeder Seitenverschiebung unbrauchbar werden.

Empfohlen:

- Hash aus Regel-ID, relativer Datei, nahem Heading, normalisiertem Evidenztext und optional Seite.
- Baseline-Vergleich: `new`, `existing`, `resolved`, `changed`.
- Unterstuetzung fuer bewusst akzeptierte Befunde mit Ablaufdatum oder Releasebezug.

### E14 Pfad- und Datenschutzvorgaben

Zusaetzlich zu den Lieferantenanforderungen:

- Markdown-Reports sollen workspace-relative Pfade verwenden.
- JSON darf absolute Pfade nur optional und deaktivierbar enthalten.
- Evidenzauszuege sollen kurz bleiben und keine ganzen Kundentexte kopieren.
- Netzwerkchecks muessen sichtbar im Report als aktiviert/deaktiviert markiert sein.

## Ergaenzte Mindestabnahme fuer gitbook_worker v2.9.0

Aus ERDA-Sicht ist das Lieferantenrelease erst abnahmefaehig, wenn zusaetzlich zu den gelieferten Mindestpunkten folgende Szenarien getestet sind:

| Szenario | Erwartung |
|---|---|
| Sauberes Sample | `passed` mit Markdown- und PDF-Metrikreport plus Markdown-Dossier. |
| Warnungs-Sample | `passed_with_warnings`, z. B. lange URL mit kleinem PDF-Ueberstand. |
| Fehler-Sample | `failed`, z. B. verbotener Frontmatter-Key, fehlender PDF-Font oder nicht lesbares Pflichtartefakt. |
| Blocked-Sample | `blocked`, wenn erwartete PDF/Markdown-Artefakte fehlen. |
| Drift-Sample | `failed` oder `warn`, wenn Release-Doku eine alte Worker-Version oder alte Seitenzahlen behauptet. |
| Translation-Sample | EN-Datei ohne `source`/`status` oder mit falscher `content_id` erzeugt Befund. |
| Table-Sample | Tabellenstrategie-Report wird aggregiert und mindestens ein Landscape-/Fallback-Fall erscheint im Dossier. |
| Wenigzeiler-Sample | Textarme und leere Seiten werden reproduzierbar gezaehlt. |

## Vorgeschlagene ERDA-Abnahmeprofile

```yaml
profiles:
  erda-release-candidate:
    network: false
    markdown:
      forbidden_frontmatter_keys:
        - lang
        - language
        - lang-version
      required_de_frontmatter:
        - content_id
        - content_lang
      required_en_frontmatter:
        - content_id
        - content_lang
        - source
        - status
      allowed_en_status:
        - draft
        - in-review
        - approved
    pdf:
      low_text_page_threshold: 15
      very_low_text_page_threshold: 5
      overflow_warn_pt: 0.1
      overflow_fail_pt: 12.0
      required_fonts:
        - DejaVuSerif
        - DejaVuSans
        - DejaVuSansMono
        - TwemojiMozilla
        - ERDACCbyCJK-Regular
    documentation:
      fail_on_stale_worker_version: true
      fail_on_stale_page_count: true
```

## Redaktionelle Schlussbewertung

Das Pflichtenheft sollte angenommen werden, aber nicht als vollstaendig gelten. Die wichtigsten Nachtraege sind **Report-Drift**, **Wenigzeiler-Metrik**, **ERDA-Frontmatter-/Uebersetzungsregeln**, **Tabellenstrategie-Aggregation**, **konfigurierbare Akzeptanzprofile** und **manuelle Restrisiko-Entscheidung**.

Wenn diese Punkte integriert werden, wuerde `Qualitaetskompass` genau die Luecke schliessen, die im v2.5.0-Releaseprozess sichtbar wurde: Der Redakteur muesste nicht mehr Einzelreports, Terminalausgaben, PDF-Metadaten, Fontlisten, Layoutscans und alte Release-Dokumente manuell zusammenfuehren, sondern bekaeme ein belastbares, auditierbares Entscheidungsdossier.