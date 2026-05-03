---
content_id: erda.book.anhang.e.erda.buch.baukasten.e.7.template.fur.ein.standardisiertes.erda.quellenverzeichnis
content_lang: de
---
# E.7 🪄 Template für ein standardisiertes ERDA-Quellenverzeichnis

🪄 _**E.7 Template für ein standardisiertes ERDA-Quellenverzeichnis (v1.0)**_

### 🎯 Ziel

Dieses Template richtet sich an Autor:innen, Redakteur:innen, technische Redaktions- und GitBook-Teams sowie Qualitätssicherungs-Reviewer:innen.\
Es unterstützt sie dabei, Quellen- und Verweisverzeichnisse einheitlich, klar und fehlerfrei zu gestalten, fehlerhafte Links zu vermeiden und belegbare sowie verifizierte Quellen sicherzustellen.

Jede Quelle erzählt eine Geschichte – hüte sie mit Sorgfalt.

### 🛠 Aufbau und Struktur

#### 1. Abschnitt: 📎 Verwendete Quellen und Verweise

* **Inhalt:** Nur verifizierte, bestehende externe Quellen und interne GitBook-Verweise.
* **Formatierung:**
  * Nummerierte Liste.
  * Titel (kursiv), Jahr, ggf. kurzer Kontext.
  * Direktlink bei Internetquellen.
  * Relativer Pfad bei GitBook-internen Dokumenten.
  * **Beispiel Internetquelle:** _„Strategic Compass for Security and Defence“_ (Europäische Kommission, 2022): [https://eeas.europa.eu/strategic-compass](https://eeas.europa.eu/strategic-compass)
  * **Beispiel GitBook-Verweis:** _Anhang: Europa 2.0 – Fahrplan für eine lebenswerte, resiliente und führende Union_ (2025): \[../anhang-europa-2.0-fahrplan-fur-eine-lebenswerte-resiliente-und-fuhrende-union.md]
* **Sortierung:**
  * Zuerst Internetquellen (offizielle Dokumente, Studien etc.)
  * Danach GitBook-interne Kapitel.
  * Innerhalb der Kategorien alphabetisch oder thematisch sinnvoll gruppiert.
* **Tutorial-Tipp:**
  * Für Internetlinks: Link aus Browser kopieren.
  * Für GitBook-Verweise: Datei aus `SUMMARY.md` herauskopieren und auf korrekte relative Pfadstruktur achten.

#### 2. Abschnitt: 🛠️ Künftige Erarbeitungen durch ERDA-Institut oder Verfassungsorgane

* **Inhalt:**
  * Geplante, noch zu erarbeitende Konzepte, Plattformen, Frameworks.
* **Formatierung:**
  * Bullet-Point-Liste.
  * Jeweils ein Satz Beschreibung pro Punkt.
* **Beispiele für Mock-Einträge:**
  * **ERDA-Dialogmodell:** Entwicklung eines Frameworks zur skalierbaren Moderation grenzüberschreitender Bürgerforen („EU-Dialogforen für Bürgerbeteiligung“).
  * **Demokratie-Lab-Handbuch:** Erstellung eines Leitfadens für partizipative Workshop-Methoden und Coachingmodule in lokalen Demokratie-Laboren.
* **Motivierender Hinweis:**
  * Diese Module sind Teil der ERDA-Gesamtkonzeption und laden zur Mitgestaltung ein.

### 📐 Formatregeln

| Regelkategorie                | Details                                                                                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Verlinkung**                | Internetlinks in eckigen Klammern, direkt klickbar. GitBook-Verweise relativ mit vollständigem Dateinamen.                                      |
| **Textliche Einheitlichkeit** | Einheitliche Anführungszeichen („“). Bindestriche statt Unterstriche in Dateinamen. Keine Leerzeichen oder Sonderzeichen in GitBook-Dateinamen. |
| **Transparenz**               | Klare Trennung geplanter Konzepte von existierenden Materialien.                                                                                |
| **Fehlervermeidung**          | Keine Platzhalter oder erfundenen Quellen zulassen. Verweise erst nach Verifizierung in `SUMMARY.md` oder offiziellen Dokumenten verwenden.     |

> Tipp für Fortgeschrittene: Für große Kapitel empfiehlt sich der Einsatz eines Link-Check-Tools oder eines Linting-Skripts.

### 🧠 Qualitätssicherung: Standard-Prompts für Prüfung

**Vor jeder finalen Freigabe:**

1. 🔍 **Verifikationsprüfung Internet:**
   * Ist die URL gültig? (Kein 404, korrekter Inhalt)
2. 📂 **Verifikationsprüfung GitBook:**
   * Existiert der Pfad im `SUMMARY.md`?
3. 📑 **Inhaltliche Prüfung:**
   * Passt die Quelle wirklich zur referenzierten Aussage?
   * Handelt es sich um Primärquellen, Sekundärquellen oder Drittquellen?
4. 🚦 **Kategorisierung:**
   * Existierende Quelle vs. künftiges Konzept klar zugewiesen?
5. 📋 **Formale Prüfung:**
   * Einheitliche Darstellung von Titel, Jahr, Link/Pfad.
6. 🛡️ **Finaler Abschluss:**
   * Kontrollsatz prüfen: „Erweckt das Verzeichnis an keiner Stelle den Eindruck, fiktiv oder unausgereift zu sein?“

* **Verantwortung:**
  * Die finale Quellenprüfung liegt beim Kapitelhauptautor oder der zugewiesenen Qualitätssicherungsinstanz.

### 📋 Prüf-Template "Quellenverzeichnis für Kapitel \[Titel]"

* **Kapitel:** \[Kapitelname einsetzen]
* **Datum der Prüfung:** \[Datum einsetzen]
* **Prüfer:in:** \[Name einsetzen]

#### 🔎 Prüfungsschritte:

| Schritt                                                                | Priorität | Status (✔️/❌) | Kommentar |
| ---------------------------------------------------------------------- | --------- | ------------- | --------- |
| Alle Internetlinks aufrufbar und aktuell?                              | Muss      |               |           |
| Alle GitBook-Verweise existieren und stimmen mit `SUMMARY.md` überein? | Muss      |               |           |
| Quellen passen fachlich exakt zum jeweiligen Kapitelinhalt?            | Muss      |               |           |
| Korrekte Unterscheidung existierender und geplanter Quellen?           | Muss      |               |           |
| Einheitliches Layout, keine Tippfehler, vollständige Angaben?          | Muss      |               |           |
| Motivierende Sprache bei zukünftigen Konzepten?                        | Muss      |               |           |
| Kontrollsatz „kein Eindruck von Fiktion“ bestanden?                    | Muss      |               |           |

> **Ergebnis:** \[Freigabe empfohlen / Nacharbeit erforderlich]

***

Dieses Template kann flexibel für jedes ERDA-Kapitel angewendet werden und erhöht die Qualität und Konsistenz des Gesamtwerks deutlich. 🚀

Für eine evolutionäre Qualitätsentwicklung wird empfohlen, die Ergebnisse der Quellenprüfungen kontinuierlich auszuwerten und daraus Optimierungen des Templates abzuleiten.
