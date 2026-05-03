# Redaktionelle Bewertung der ERDA-Grafik-Startwelle

Stand: 2026-05-03
Rolle: Redakteur

## Entscheidung

Die vorhandenen acht SVG-Dateien sind als Konzeptentwuerfe brauchbar, aber nicht als Serie releasefaehig. Sie werden daher nicht im Bulk in das Buch uebernommen.

Gruende:

- zu hohe Textdichte fuer PDF-Skalierung,
- mehrere sichtbare Text- und Box-Ueberlaeufe in der Gesamtpreview,
- uneinheitliche Lesbarkeit bei Kapitel- und Druckgroesse,
- keine geprueften DE/EN-Varianten fuer alle Motive.

## Freigegebener Pilot

Als Pilot wurde Grafik 02 zum Reformpfad 2025-2035 neu gesetzt und bewusst vereinfacht:

- DE-Asset: `de/content/.gitbook/assets/erda-reformpfad-2025-2035.svg`
- EN-Asset: `en/content/.gitbook/assets/erda-reform-path-2025-2035.svg`
- Verankerung: Kapitel 4.2 in DE und EN

Die Pilotgrafik verwendet kurze Meilensteine statt kleinteiliger Timeline-Details. Der Build erzeugt aus dem SVG automatisch ein PDF-Artefakt fuer LaTeX/PDF.

## Toolchain-Entscheidung

GitBook-konforme Quellen liegen unter `content/.gitbook/assets`. Die Publish-Manifeste muessen diesen Pfad als Asset-Quelle verwenden, damit die vorhandene SVG-zu-PDF-Konvertierung im `gitbook-worker` greift.

Workflow je Grafik:

1. SVG als editierbare Quelle im jeweiligen Sprach-Asset-Ordner ablegen.
2. Bild im Kapitel als Markdown-Image verankern.
3. Lokalen DE- und EN-Build ausfuehren.
4. PDF-Seite als PNG rendern und visuell pruefen.
5. Erst danach die naechste Grafik bearbeiten.

## 90-Grad-PNG-Regel

Sehr breite Grafiken koennen als 90-Grad-PNG fuer eine eigene Querformat-/Drehseite sinnvoll sein. Das ist aber ein Spezialmodus, kein Standard.

Freigabekriterien fuer 90-Grad-PNG:

- nur fuer echte Panorama- oder Systemkarten,
- SVG bleibt die redaktionelle Quelle,
- PNG wird aus der finalen SVG mit hoher Aufloesung erzeugt,
- im PDF wird die Drehung visuell geprueft,
- Bildunterschrift erklaert klar, dass die Grafik gedreht gelesen wird.

## Naechster Schritt

Die restlichen sieben Motive werden einzeln neu bewertet und, falls geeignet, nach dem Pilotmuster neu gesetzt. Ueberfuellte Motive werden geteilt oder textlich reduziert, nicht kleiner skaliert.