Utility scripts for converting CSV data into Markdown tables and charts.

`csv2md_and_chart.py` converts a CSV file to a Markdown table and optionally a
PNG chart.  The script now supports:

- `--title-level` to control the heading depth of the generated table title.
- `--wide A3|A2|A1` to wrap the table in the LaTeX macros
  `\WideStartAthree`/`\WideStartAtwo`/`\WideStartAone` followed by
  `\WideEnd`, enabling landscape pages in larger paper sizes without altering
  the font.
