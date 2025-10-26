from importlib import util
from pathlib import Path

spec = util.spec_from_file_location("g", r".github/tools/publishing/gitbook_style.py")
mod = util.module_from_spec(spec)
spec.loader.exec_module(mod)
ctx = mod.get_summary_layout(Path("."))
opts = mod._build_summary_options(
    ctx,
    mode=None,
    manifest=None,
    manual_marker=mod.DEFAULT_MANUAL_MARKER,
    appendices_last=True,
)
print("appendices_last:", opts.appendices_last)
print("summary_path:", ctx.summary_path)
# Print top files ordering for root
files = mod._md_files_in_dir(ctx.root_dir, ctx.summary_path, ctx, opts)
print("Top files count:", len(files))
print("Top files (names):")
for p in files:
    print("-", p.name)

# Print sorted top others using _sort_file_paths
other_files = [p for p in files if p.name.lower() != "readme.md"]
print("\nTop others after sorting:")
for p in mod._sort_file_paths(other_files, ctx, opts):
    print("-", p.name)
