# ERDA Book

## Schriftarten-Design

### PDF-Generierung
Bei der PDF-Generierung werden **keine** Noto-Schriftarten verwendet, um das Design konsistent mit der Markenidentität zu halten. Die Schriftarten können in der `publish.yml` über die `pdf_options` konfiguriert werden:

```yaml
pdf_options:
  emoji_color: true
  main_font: "DejaVu Serif"  # Hauptschriftart für Fließtext
  sans_font: "DejaVu Sans"   # Serifenlose Schriftart für Überschriften
  mono_font: "DejaVu Mono"   # Monospace-Schriftart für Code
```

Diese Konfiguration stellt sicher, dass das Dokumentendesign den Vorgaben entspricht.