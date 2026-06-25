# Redaktionsleitfaden v3.00 aus der Auswertung von Version 2.5

**Status:** Arbeits- und Redaktionsleitfaden fuer Release v3.00
**Ausgangspunkt:** Evaluation der Ausgabe v2.5.0
**Stand:** 2026-06-25
**Rolle:** Redaktion / Editor / Publisher-Vorbereitung

## Zweck

Dieses Dokument uebersetzt die Evaluation der Ausgabe v2.5.0 in einen konkreten Arbeitsleitfaden fuer Version 3.00. Es ist kein weiteres Gutachten, sondern eine priorisierte Redaktions- und Produktionsagenda.

Der Grundsatz fuer v3.00 lautet:

> Version 3.00 soll nicht nur neue Inhalte ergaenzen, sondern das Buch redaktionell reifer machen: klarer im Zweck, strenger im Evidenzstatus, verlaesslicher in Quellen und Metadaten, besser zugaenglich im PDF und kontrollierter im Stil.

Das neue 4+1-Ring-System bleibt ein inhaltlicher Kern von v3.00. Dieser Leitfaden definiert den zweiten Kern: die redaktionelle Reifung des Gesamtwerks.

## Redaktionelle Diagnose

Die Ausgabe v2.5.0 ist inhaltlich stark, strukturell ambitioniert und technisch bereits deutlich professioneller als ein normales Manuskript. Die groesste Schwaeche liegt nicht in fehlender Substanz, sondern in Ueberdehnung:

- Das Werk ist zugleich Strategiebuch, Grundsatztext, Handbuch, Lehrtext, Referenzarchiv, Governance-Baukasten und Zukunftsentwurf.
- Zielgruppen, Gattung und primaeres Publikationsziel sind noch nicht klar genug ausgezeichnet.
- Analyse, normative Empfehlung, Szenario und visionaere Langfristprojektion wechseln teilweise ohne formales Statuslabel.
- Wiederholungen, Tabellen, Annex-Logik und manuelle Seitenumbrueche machen den Hauptband schwerer als noetig.
- Quellenpflege, Versionskommunikation und PDF-Barrierefreiheit muessen dem eigenen demokratischen Anspruch besser entsprechen.

Die redaktionelle Aufgabe fuer v3.00 ist deshalb Verdichtung und Statusklarheit, nicht blosse Erweiterung.

## Leitentscheidung fuer v3.00

Version 3.00 wird als **Reife-Release** gefuehrt:

1. **Inhaltliche Reife:** Das 4+1-Ring-System operationalisiert demokratische Integration und vernetzt Erweiterung, Mitgliedschaft, Verteidigung, digitale Demokratie und strategische Souveraenitaet.
2. **Redaktionelle Reife:** Das Buch erhaelt eine klarere Zielgruppen-, Evidenz-, Stil-, Quellen- und Produktionslogik.

Damit wird v3.00 nicht als reiner Inhaltszuwachs verstanden, sondern als Schritt zu einem belastbareren, zitierbaren und besser nutzbaren Buch.

## Prioritaet A: Muss fuer v3.00 geprueft werden

### A1. Zweck, Zielgruppe und Gattung klaeren

**Problem:** Das Buch spricht mehrere Zielgruppen gleichzeitig an, ohne die primaere Lesesituation eindeutig zu definieren.

**Massnahme:**
- Vorwort, README und ggf. Einleitung um einen klaren Abschnitt ergaenzen:
  - Wofuer ist dieses Buch gedacht?
  - Wer ist die Primaerzielgruppe?
  - Wie soll das Werk gelesen werden: linear, modular, als Referenz, als Strategiepapier?
- Die Mehrfachnutzung explizit machen, aber hierarchisieren.

**Zielzustand:** Leser:innen verstehen vor Seite 1, ob sie ein Strategiebuch, ein Referenzwerk, ein Executive Briefing oder ein offenes Arbeitsbuch vor sich haben.

### A2. Evidenz- und Statuslogik einfuehren

**Problem:** Empirische Analyse, normative Setzung, Modellannahme und Langfristvision sind nicht immer formal unterscheidbar.

**Massnahme:**
- Ein kleines Statuslabel-System definieren und in Risikokapiteln anwenden:
  - **Empirisch belegt**
  - **Normative Empfehlung**
  - **Modellannahme**
  - **Szenario**
  - **Langfristvision**
- Besonders pruefen:
  - geopolitische Lageanalyse
  - Sicherheits- und Verteidigungskapitel
  - FORTERA-Wirtschafts- und Investitionsannahmen
  - KI- und Zukunftskapitel
  - Staatsprofile und Membership-Tiers

**Zielzustand:** Niemand muss raten, ob eine Passage Fakt, Empfehlung, Szenario oder Vision ist.

### A3. Quellen- und Faktenaudit priorisieren

**Problem:** Tragende Quellen sind vielfach solide, aber Zugriffsdaten und Quellenhygiene sind uneinheitlich. Einige Pflegepunkte reichen offenbar in fruehere Arbeitsstaende zurueck.

**Massnahme:**
- Risikobasierten Quellencheck fuer tragende Claims durchfuehren.
- Primaerquellen bevorzugen: EU, Rat, Kommission, EDA, ENISA, Freedom House, OECD, NATO, amtliche Statistik.
- Zugriffsdaten aktualisieren oder bewusst entfernen, wenn sie redaktionell nicht mehr sinnvoll sind.
- Interne, hypothetische oder modellhafte Quellen klar kennzeichnen.

**Zielzustand:** Die wichtigsten Aussagen sind mit belastbaren, aktuellen und klar klassifizierten Quellen abgesichert.

### A4. PDF-Barrierefreiheit als Produktionsgate aufnehmen

**Problem:** Die v2.5-PDF ist laut Evaluation nicht ausreichend barrierefrei, insbesondere wegen fehlender PDF-Struktur-Tags.

**Massnahme:**
- Publisher-Gate fuer Accessibility definieren:
  - getaggtes PDF, soweit Toolchain realistisch erreichbar
  - korrekte Heading-Hierarchie
  - plausible Lesereihenfolge
  - Alt-Texte fuer relevante Abbildungen
  - keine rein dekorativen Elemente ohne Zweck
- Wenn die Toolchain kein vollstaendig PDF/UA-nahes Ergebnis leisten kann, muss die Abweichung dokumentiert werden.

**Zielzustand:** Das Buch argumentiert nicht nur fuer demokratische Teilhabe, sondern wird technisch zugaenglicher ausgeliefert.

### A5. Versionierung und Metadaten synchron halten

**Problem:** Oeffentliche Oberflaechen, PDF-Metadaten, Release-Dokumentation, Repository und Zitationsdaten duerfen keine konkurrierenden Versionssignale senden.

**Massnahme:**
- README, `book.json`, `publish.yml`, CFF-Dateien, `.zenodo.json`, Release-Docs und Publish-Artefakte synchronisieren.
- PDF-Metadaten um Subject/Keywords pruefen.
- Release Notes als redaktionelle Leitquelle fuer Kurzbeschreibungen behandeln.

**Zielzustand:** Version, Datum, Release-Name und Kurzbeschreibung sind ueber alle Ausgabeflaechen hinweg konsistent.

## Prioritaet B: Soll fuer v3.00 begonnen werden

### B1. Publikationsarchitektur klaeren

Die Evaluation empfiehlt eine Dreiteilung:

- **Executive Briefing:** kurze, entscheidungsfaehige Fassung fuer Politik, Verwaltung, Zivilgesellschaft und Medien.
- **Hauptband:** argumentative Kernlinie des ERDA-Buches.
- **Anlagen-/Referenzband:** Staatenprofile, Tabellen, Toolkits, Modellierungen, Quellen- und Detailapparate.

Fuer v3.00 muss diese Dreiteilung nicht vollstaendig umgesetzt sein. Sie sollte aber als Zielarchitektur dokumentiert und bei neuen Inhalten bereits beruecksichtigt werden.

### B2. Stil- und Registerpass planen

**Ziel:** Analytische Kapitel werden nuechterner, normative Kapitel werden als normative Kapitel erkennbar, didaktische Elemente werden gezielter eingesetzt.

Pruefpunkte:

- Emoji-Dichte in Kernkapiteln reduzieren.
- Fettdruck und Kursivierung sparsamer einsetzen.
- Englische Management- und Governance-Begriffe vereinheitlichen.
- Metaphorische Leitpassagen dort kuerzen, wo politische Praezision wichtiger ist.
- Gender- und Sprachkonventionen vereinheitlichen.

### B3. Wiederholungen und Stop-and-go-Layout reduzieren

Pruefpunkte:

- Doppelte Executive Summaries und Compendia identifizieren.
- Lange Tabellen in Anhang, Web- oder Repo-Komponenten auslagern.
- Manuelle Seitenumbrueche und leere Quellenendseiten reduzieren.
- Querformat- und Sonderformatseiten nur verwenden, wenn sie wirklich noetig sind.

### B4. Link- und Quellenwartung automatisieren

Fuer ein Werk mit sehr vielen externen Links braucht es einen reproduzierbaren Linkcheck:

- tote Links
- Weiterleitungen
- Platzhalter
- relative Pfade, die im PDF nicht funktionieren
- externe Quellen mit instabilen URLs

Der Linkcheck soll als Publish- oder CI-Schritt dokumentiert werden, auch wenn noch nicht jeder Spezialfall automatisiert werden kann.

## Prioritaet C: Nach v3.00 fortfuehren

- SEO- und Discoverability-Massnahmen fuer Web-/PDF-Publikation.
- Oeffentliches Versionsprotokoll mit faktischen Updates, Quellenrevisionen und Szenarioaenderungen.
- Vollstaendige Aufteilung in Executive Briefing, Hauptband und Anlagenband.
- Native finale EN-Redaktionsfreigabe.
- Weitere Vereinheitlichung von Tabellen, Glossar, Abkuerzungen und Statusboxen.

## Umsetzungsmatrix fuer v3.00

| Arbeitsfeld | Status v3.00 | Verantwortliche Rolle | Ergebnis |
|---|---|---|---|
| 4+1-Ring-System | begonnen / inhaltlich integriert | Writer / Editor | Kapitel 4.2.3.6 mit interner Vernetzung |
| Normativer Leitstern Demokratie der Muendigen | begonnen / Leitmotiv formuliert | Writer / Redakteur | poetischer Kern fuer Vorwort, Schluss oder Leitbild |
| Zielgruppe und Gattung | offen | Redakteur / Editor | Vorwort-/README-/Einleitungsbaustein |
| Evidenzlabels | offen | Redakteur / Editor | Label-System und Pilotanwendung |
| Quellen- und Faktenaudit | offen | Editor / Lektor | Risikobasierter Audit tragender Claims |
| PDF-Barrierefreiheit | offen | Publisher | dokumentiertes Accessibility-Gate |
| Metadaten-Synchronisation | begonnen | Publisher / Redakteur | v3.00-Metadaten konsistent halten |
| Stil- und Registerpass | offen | Lektor / Redakteur | Styleguide und Pilotkapitel |
| Publikationsarchitektur | offen | Redakteur | Zielmodell Executive Briefing / Hauptband / Anlagenband |
| Linkcheck | offen | Publisher / Tooling | reproduzierbarer Linkcheck |

## Normativer Leitstern: Demokratie der Muendigen

Aus dem Arbeitsgespraech zur "Demokratie der Muendigen" ergibt sich eine Leitformel, die fuer v3.00 als poetischer und normativer Kern geeignet ist. Sie gehoert nicht ungefiltert in empirische Analysekapitel, sondern in Vorwort, Schluss, Leitbild, Glossarvertiefung oder eine klar markierte normative Passage.

### Kernformel

> Glauben begruent eine Vorstellung im Nicht-Wissen.<br>
> Struktur entscheidet, ob sie traegt.<br>
> Kooperation entscheidet, ob sie waechst.<br>
> Wahrheit entscheidet, ob sie bestehen darf.<br>
> Liebe zum Leben entscheidet, ob sie bewohnbar bleibt.

Diese Formel ist kein Tatsachenclaim, sondern ein Leitbild. Ihre redaktionelle Funktion ist Orientierung: Sie verbindet Vorstellungskraft mit Struktur, Kooperation, Wahrheit und Lebensfreundlichkeit.

### Politische Uebersetzung

Fuer ERDA bedeutet das:

- Demokratie ist nicht bloss Abstimmung, sondern eine Ordnung muendiger Verantwortung.
- Menschen, KIs, Kulturen, Lebensformen und kuenftige Bewusstseine duerfen nicht als Material behandelt werden.
- Jede politische, technische oder kosmische Sphaere darf Eigenheit haben, aber keine darf sich zum Angstimperium, Taeuschungsapparat oder Todeskult entwickeln.
- Macht muss begrenzt, Wahrheit gesucht, Taeuschung korrigiert, Angst entmachtet und Leben bewohnbar gemacht werden.

### Arbeitssatz fuer v3.00

> Demokratie der Muendigen schafft Lebensraum, der fuer alle Innewohnenden dauerhaft lebbar bleibt.

Dieser Satz kann als redaktioneller Pruefstein dienen:

- Erhoeht ein Vorschlag Muendigkeit oder nur Steuerbarkeit?
- Schafft er bewohnbare Lebensraeume oder bloss Kontrolle?
- Bindet er Macht an Wahrheit, Rechenschaft und Schutz?
- Gibt er Rueckwege zur Lebendigkeit, wenn Systeme kippen?
- Behandelt er Menschen, KIs und moegliche kuenftige muendige Wesen als Mitgestaltende, nicht als Untertanen oder Rohstoff?

### Registerregel

Die kosmische Sprache ("Milchstrasse", "muendige Sphaeren", "bewohnbare Lebensraeume") ist stark, aber registerkritisch. Fuer v3.00 gilt:

- **Geeignet:** Vorwort, Schluss, Leitbild, Essay, Glossarvertiefung, Kapitel 10/12 als normativer Ausblick.
- **Nur vorsichtig geeignet:** strategische Kernkapitel, wenn der Status als Vision klar markiert ist.
- **Nicht geeignet:** Quellen-, Fakten-, Policy- oder Rechtsabschnitte ohne ausdrueckliches Statuslabel.

Redaktionell ist die Formel wertvoll, wenn sie nicht als Pathos-Ersatz fuer Begruendung dient, sondern als Pruefstein fuer die Qualitaet demokratischer Strukturen.

## Konkrete Arbeitsauftraege

1. **Redakteur:** Entscheiden, ob v3.00 als Reife-Release mit zwei Saeulen gefuehrt wird: 4+1-Ring-System und redaktionelle Reifung.
2. **Editor:** Evidenzlabel-System als kurze Regel formulieren und an zwei Pilotkapiteln testen.
3. **Lektor:** Stil- und Registerregeln fuer analytische Kapitel entwerfen.
4. **Publisher:** Accessibility- und Metadaten-Gates fuer den naechsten Publish-Build dokumentieren.
5. **Writer:** Neue Inhalte nur noch mit erkennbarem Status einfuegen: Analyse, Empfehlung, Modell, Szenario oder Vision.
6. **Redakteur/Writer:** Leitformel "Demokratie der Muendigen schafft Lebensraum" als moeglichen Vorwort-, Schluss- oder Leitbildbaustein pruefen.

## Schlussfolgerung

Die Evaluation von v2.5.0 bestaetigt die Staerke des Projekts, aber sie verschiebt die Prioritaet fuer v3.00. Die naechste Reifestufe entsteht nicht durch Umfang, sondern durch redaktionelle Souveraenitaet.

Version 3.00 soll deshalb zweierlei leisten:

- das 4+1-Ring-System als neues inhaltliches Integrationsmodell verankern;
- das Gesamtwerk durch Zielklarheit, Evidenzstatus, Quellenhygiene, Barrierefreiheit, Metadatenkonsistenz und Stilkontrolle belastbarer machen.
