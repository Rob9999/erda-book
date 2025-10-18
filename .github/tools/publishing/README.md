# Publishing Tools

Scripts assisting selective publishing workflows.

`set_publish_flag.py` updates build flags in `publish.yml` based on repository changes.

`reset_publish_flag.py` clears build flags after successful publishing runs.

`pipeline.py` orchestrates the end-to-end publishing flow. It shells out to the
helper scripts below so a single GitHub Actions job can refresh GitBook assets
and invoke the PDF builder without duplicating logic in workflow YAML files.

`publisher.py` builds PDFs for entries marked for publishing. Manifest entries
under `publish.yml` can provide the keys `out_dir`, `out_format`,
`source_type`, `source_format`, `use_summary`, `use_book_json` and
`keep_combined`. Relative directories are resolved against the manifest
location and default to the repository level `publish/` folder. At the moment
only `out_format: pdf` is supported; other values are skipped with a warning.

`dump_publish.py` prints the entries of `publish.yml` as JSON for use in other scripts.

`preprocess_md.py` scans Markdown files for wide tables and large images and wraps
them with LaTeX snippets to enlarge the paper size and, when requested via
`--landscape`, rotate the page. This helps prevent content from overflowing
when rendering PDFs.

`markdown_combiner.py` preprocesses and concatenates multiple Markdown files,
inserting LaTeX packages and helper macros for optional landscape sections and
long tables before separating them with page breaks. Pass `--landscape` to enable
landscape orientation. It is used by `publisher.py` and can also be run
standalone. `publisher.py` invokes Pandoc with `--variable=longtable=true` so
wide tables span multiple pages without changing the font size.

`gitbook_style.py` contains utilities used by the GitHub Actions workflow to
normalise filenames to the GitBook convention and regenerate `SUMMARY.md`
content defined by `book.json`.
