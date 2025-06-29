# Misc
This folder contains miscellaneous tools.

## 1. check_staatenprofil_links.py

`check_staatenprofil_links.py` scans all Markdown files with `staatenprofil` in the filename and checks each external link using HTTP `HEAD` requests. It writes the results to a CSV report and prints a short summary.

Example usage:

```bash
python3 tools/check_staatenprofil_links.py --root anhang-b-erda-staatenprofile --output links.csv
```

The generated CSV lists the file path, line number, URL, HTTP status, and any error messages. Broken links can then be corrected manually.
