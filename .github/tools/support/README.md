# Support Utilities

This package collects helper scripts that make it easier to verify the GitBook
configuration outside of the main publishing pipeline.

## Appendix layout inspector

`appendix_layout_inspector.py` mirrors the behaviour of the historical
`_test_appendix_check.py` script, but exposes it as a reusable module and CLI.
It inspects the resolved `SUMMARY.md` configuration, reports the active summary
mode and lists the top-level entries, making it straightforward to verify that
appendices are sorted to the end of the navigation tree.

Run the inspector with:

```bash
python -m tools.support.appendix_layout_inspector --base-dir . --appendices-last
```

The command prints the resolved summary path, mode/submode combination and the
ordered list of Markdown entries.  The module is primarily intended for tests
but can also be used when debugging publishing issues locally.
