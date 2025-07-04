import os
import re
import subprocess
import sys
import logging
from typing import List, Tuple
import requests

# Emoji ranges supported by the LaTeX header
EMOJI_RANGES = (
    "1F300-1F5FF, 1F600-1F64F, 1F680-1F6FF, 1F700-1F77F, 1F780-1F7FF, "
    "1F800-1F8FF, 1F900-1F9FF, 1FA00-1FA6F, 1FA70-1FAFF, "
    "2600-26FF, 2700-27BF, 2300-23FF, 2B50, 2B06, 2934-2935, 25A0-25FF"
)

try:
    import textstat
except ImportError:  # pragma: no cover - optional dep
    textstat = None

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def run(cmd, cwd=None, capture_output=False, input_text=None):
    """Execute a command without invoking a shell."""
    logging.info("Running command: %s", cmd)
    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=False,
        stdout=subprocess.PIPE if capture_output else None,
        stderr=subprocess.PIPE if capture_output else None,
        input=input_text,
        text=True,
        encoding="utf-8",
    )
    if capture_output:
        return result.stdout, result.stderr, result.returncode
    if result.returncode != 0:
        logging.error("Command failed (%s): %s", result.returncode, cmd)
        sys.exit(result.returncode)


def get_pandoc_version() -> Tuple[int, ...]:
    """Return the installed pandoc version as a tuple."""
    out, _, code = run(["pandoc", "--version"], capture_output=True)
    if code != 0 or not out:
        logging.warning("pandoc --version failed")
        return (0,)
    first = out.splitlines()[0]
    m = re.search(r"pandoc\s+([0-9]+(?:\.[0-9]+)*)", first)
    if not m:
        logging.warning("Unable to parse pandoc version from: %s", first)
        return (0,)
    return tuple(int(p) for p in m.group(1).split("."))


def font_available(name: str) -> bool:
    """Check if a font with the given name is available on the system."""
    if sys.platform.startswith("win"):
        fonts_dir = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts")
        try:
            for f in os.listdir(fonts_dir):
                if name.lower() in f.lower():
                    return True
        except Exception:  # pragma: no cover - environment specific
            pass
        return False
    out, _, code = run(["fc-list"], capture_output=True)
    if code != 0:
        return False
    return name.lower() in out.lower()


def parse_summary(summary_path):
    """Parse SUMMARY.md to get an ordered list of markdown file paths."""
    files = []
    base = os.path.dirname(summary_path)
    try:
        with open(summary_path, encoding="utf-8") as f:
            for line in f:
                match = re.match(r"\s*\*+\s*\[.*\]\(([^)]+\.md)\)", line)
                if match:
                    files.append(os.path.join(base, match.group(1)))
    except Exception as e:
        logging.error("Failed to read SUMMARY.md: %s", e)
        sys.exit(1)
    return files


def readability_report(md_files):
    """Compute readability scores for each markdown file."""
    report = []
    if not textstat:
        logging.warning("textstat not installed; skipping readability checks.")
        return report
    for md in md_files:
        try:
            with open(md, encoding="utf-8") as f:
                text = f.read()
            fre = textstat.flesch_reading_ease(text)
            fk = textstat.flesch_kincaid_grade(text)
            report.append((md, fre, fk))
        except Exception as e:
            logging.warning("Readability check failed for %s: %s", md, e)
    return report


def wrap_wide_tables(md_file: str, threshold: int = 6) -> None:
    """Wrap wide markdown tables in a fenced ``Div`` with class ``landscape``.

    Consecutive lines starting with a pipe character are considered part of a
    table. If the table contains more columns than ``threshold`` it is wrapped
    inside ``::: {.landscape cols=N}`` and ``:::` markers where ``N`` is the
    number of columns. A Pandoc Lua filter can later convert this ``Div`` into
    the appropriate LaTeX ``landscape`` environment and adjust the font size
    based on the ``cols`` attribute. The file is modified in place.
    """

    try:
        with open(md_file, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to read %s: %s", md_file, e)
        raise

    new_lines: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith("|"):
            table = []
            max_cols = line.count("|") - 1
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table.append(lines[i])
                max_cols = max(max_cols, lines[i].count("|") - 1)
                i += 1
            if max_cols > threshold:
                new_lines.append(f"::: {{.landscape cols={max_cols}}}\n")
                new_lines.extend(table)
                new_lines.append(":::\n")
            else:
                new_lines.extend(table)
        elif stripped.startswith("<table"):
            table = []
            while i < len(lines):
                table.append(lines[i])
                if "</table>" in lines[i]:
                    i += 1
                    break
                i += 1
            html_table = "".join(table)
            md_table = table
            try:
                out, err, code = run(
                    [
                        "pandoc",
                        "-f",
                        "html",
                        "-t",
                        "gfm",
                        "--wrap=none",
                        "-",
                    ],
                    capture_output=True,
                    input_text=html_table,
                )
                if code == 0:
                    md_table = [l + "\n" for l in out.splitlines()]
            except Exception as e:  # pragma: no cover - pandoc issues
                logging.warning("HTML table conversion failed: %s", e)
            max_cols = 0
            for l in md_table:
                if l.lstrip().startswith("|"):
                    max_cols = max(max_cols, l.count("|") - 1)
            if max_cols > threshold:
                new_lines.append(f"::: {{.landscape cols={max_cols}}}\n")
                new_lines.extend(md_table)
                new_lines.append(":::\n")
            else:
                new_lines.extend(md_table)
        else:
            new_lines.append(line)
            i += 1

    try:
        with open(md_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to write %s: %s", md_file, e)
        raise


def validate_table_columns(md_file: str) -> List[str]:
    """Return a list of errors for tables with inconsistent column counts."""

    try:
        with open(md_file, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to read %s: %s", md_file, e)
        raise

    errors: List[str] = []
    ref_cols = 0
    in_table = False
    for idx, line in enumerate(lines, start=1):
        if line.lstrip().startswith("|"):
            cols = line.count("|") - 1
            if not in_table:
                in_table = True
                ref_cols = cols
            if cols != ref_cols:
                errors.append(f"Line {idx}: has {cols} columns (expected {ref_cols})")
        else:
            in_table = False
            ref_cols = 0

    return errors


def download_remote_images(md_file: str, out_dir: str) -> int:
    """Download remote images referenced in ``md_file``.

    Remote images (``http`` or ``https`` URLs) are downloaded into
    ``out_dir`` and the markdown file is updated to reference the local
    copy. Returns the number of images successfully downloaded."""

    pattern = re.compile(r"(!\[[^\]]*\]\()\s*(https?://[^\s)]+)(\))")

    try:
        text = open(md_file, encoding="utf-8").read()
    except Exception as e:  # pragma: no cover - unlikely
        logging.error("Failed to read %s: %s", md_file, e)
        raise

    count = 0

    def repl(match: re.Match) -> str:
        nonlocal count
        url = match.group(2)
        try:
            os.makedirs(out_dir, exist_ok=True)
            name = os.path.basename(url.split("?")[0]) or f"img_{count}"
            base, ext = os.path.splitext(name)
            dest = os.path.join(out_dir, name)
            suffix = 1
            while os.path.exists(dest):
                dest = os.path.join(out_dir, f"{base}_{suffix}{ext}")
                suffix += 1
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(dest, "wb") as wf:
                wf.write(response.content)
            logging.info("Downloaded image %s -> %s", url, dest)
            count += 1
            return f"{match.group(1)}{dest}{match.group(3)}"
        except Exception as e:  # pragma: no cover - network issues
            logging.error("Failed to download image %s: %s", url, e)
            return match.group(0)

    new_text = pattern.sub(repl, text)

    if count:
        try:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(new_text)
        except Exception as e:  # pragma: no cover - unlikely
            logging.error("Failed to write %s: %s", md_file, e)
            raise
    return count


def _write_pandoc_header(
    temp_dir: str,
    emoji_font: str,
    sans_font: str,
    mono_font: str,
    main_font: str,
    wrap_tables: bool,
    threshold: int,
    md_file: str,
) -> str:
    """Create a temporary pandoc header file and optionally wrap wide tables.

    Returns the path to the created header file."""

    header_file = os.path.join(temp_dir, "pandoc_header.tex")
    try:
        with open(header_file, "w", encoding="utf-8") as hf:
            hf.write("\\usepackage{fontspec}\n")
            hf.write(f"\\setsansfont{{{sans_font}}}\n")
            hf.write(f"\\setmonofont{{{mono_font}}}\n")
            hf.write(f"\\setmainfont{{{main_font}}}\n")
            if emoji_font:
                if emoji_font.startswith("OpenMoji"):
                    hf.write(
                        f"\\newfontfamily\\EmojiOne{{{emoji_font}}}[Range={{{EMOJI_RANGES}}}]\n"
                    )
                elif emoji_font == "Segoe UI Emoji":
                    hf.write("\\IfFontExistsTF{Segoe UI Emoji}{\n")
                    hf.write(
                        f"  \\newfontfamily\\EmojiOne{{Segoe UI Emoji}}[Renderer=Harfbuzz,Range={{{EMOJI_RANGES}}}]\n"
                    )
                    hf.write(
                        '  \\directlua{luaotfload.add_fallback("mainfont", "Segoe UI Emoji:mode=harf")}\n'
                    )
                    hf.write("}{}\n")
                else:
                    hf.write(
                        f"\\newfontfamily\\EmojiOne{{{emoji_font}}}[Range={{{EMOJI_RANGES}}}]\n"
                    )
            if wrap_tables:
                logging.info("Wrapping wide tables in landscape environment...")
                wrap_wide_tables(md_file, threshold=threshold)
                hf.write("\\usepackage{pdflscape}\n")
                logging.info("Wide tables wrapped successfully.")
    except Exception as e:
        logging.error("Failed to write pandoc header tex file: %s", e)
        raise
    logging.info("Pandoc header tex file created: %s", header_file)
    return header_file
