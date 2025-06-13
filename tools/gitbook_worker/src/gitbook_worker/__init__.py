import ast
import io
import random
import time
from typing import List
from enum import Enum
import stat
import subprocess
import sys
import os
import re
import argparse
import csv
from typing import Any, Dict
import requests
import logging
from datetime import datetime
import requests
import json
import shutil

__version__ = "2.0.0"
import tqdm

# Optional dependencies; ensure these are installed or wrapped in try/except
try:
    import yaml
except ImportError:
    yaml = None

try:
    import textstat
    import shutil
    from difflib import SequenceMatcher
except ImportError:
    textstat = None

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def run(cmd, cwd=None, capture_output=False):
    """Execute a shell command. Exit on failure or return output."""
    logging.info("Running command: %s", cmd)
    result = subprocess.run(
        cmd,
        cwd=cwd,
        shell=True,
        stdout=subprocess.PIPE if capture_output else None,
        stderr=subprocess.PIPE if capture_output else None,
        text=True,
    )
    if capture_output:
        return result.stdout, result.stderr, result.returncode
    if result.returncode != 0:
        logging.error("Command failed (%s): %s", result.returncode, cmd)
        sys.exit(result.returncode)


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


def get_extract_multiline_list_items_pattern() -> re.Pattern:
    """
    Returns a regex pattern to extract multiline list items from text.

    It supports numbered lists (e.g., "1.", "2-", "b)", "c-"), as well as bullet lists
    using "*", "-", or "+". Continuation lines that do not start with a list marker
    are considered part of the previous list item.

    Example which this pattern matches:
    1. This is the first item
    continued on the next line
    2- Second item here
    * Bullet item here
    continuing bullet
    another line
    b) Alphabetically numbered item
    c) Another one
    with multiple lines
    - Simple dash bullet
    """
    return re.compile(
        r"^(?:\s*)(?:\d+[\.\)-]|[a-zA-Z][\.\)-]|[*\-+])\s+.*(?:\n(?!\s*(?:\d+[\.\)-]|[a-zA-Z][\.\)-]|[*\-+])\s).*)*",
        re.MULTILINE,
    )


def extract_multiline_list_items(text):
    """
    Extracts multiline list items from a given text.

    This function identifies and extracts list items that may span multiple lines.
    It supports numbered lists (e.g., "1.", "2-", "b)", "c-"), as well as bullet lists
    using "*", "-", or "+". Continuation lines that do not start with a list marker
    are considered part of the previous list item.

    Args:
        text (str): The input text containing potential multiline list items.

    Returns:
        list: A list of strings, each representing a multiline list item.

        >>> extract_multiline_list_items(
        ...     "1. First item\ncontinued line\n2- Second item\n* Bullet\nmore bullet"
        ... )
        ['1. First item\ncontinued line', '2- Second item', '* Bullet\nmore bullet']

    Example:
    1. This is the first item
    continued on the next line
    2- Second item here
    * Bullet item here
    continuing bullet
    another line
    b) Alphabetically numbered item
    c) Another one
    with multiple lines
    - Simple dash bullet
    """
    pattern = get_extract_multiline_list_items_pattern()
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")
    return pattern.findall(text)


def extract_sources_of_a_md_file_to_dict(
    md_file,
) -> Dict[
    str, List[Dict[str, Dict[str, Any]]]
]:  # returns a dict {str(md_file): [{name: {numbering, link, comment, line, kind}}]}
    """Extract 'Sources' sections from markdown files into a dict.<br>
    Typically references, sources or bibliography sections.<br>
    TODO: get_language_dependent_header_pattern_for_sources()<br>
    1. Current Header Pattern: ^.* Quellen<br>
    2. Current List Pattern: see get_extract_multiline_list_items_pattern()<br>
    <br>
    Dict Format:<br>
    <code>{
        "md_file_name": {
            "name": <-- the source name; e.g. the name part (plus possibly quotes) of: "name":[https://example.com](https://example.com) or [name](https://example.com) or 1. name: https://example.com
            {
                "numbering": "numbering_text",  <-- optional: any numbering, bullets, alphabetical numbering; e.g. 1., a., i., *, a), etc. or empty
                "link" : "valid_link",  <-- optional: any valid link; e.g. the url part of [link_description](https://example.com) or [../anhang/123] or empty
                "comment": "comment_text", <-- optional: any comment text; e.g. the comment part of [example](https://example.com), comment or [example](https://example.com) - comment or empty
                "lineno": line_number, <-- optional: line number of the source entry in the markdown file
                "line": full_line, <-- optional: full line of the source entry in the markdown file
                "kind": "source_type", <-- optional: type of source; e.g. document, book, article, website, internal GitBook reference, external (url), etc.
            }
        }
    }</code><br>
    Example:
    <code>{
        "file1.md": {
            "EU Codex 123":
            {
                "numbering": "1.",
                "link": "https://eu.eu?123",
                "comment": "The codex 123 of the EU is an interesting source for the topic 456.",
                "kind": "external"
            }
        },
        "file2.md": {
            European Parliament Codex 123":
            {
                "numbering": "*",
                "link": "",
                "comment": "",
                "kind": "document"
            }
        }
    }</code><br>
    <br>
    This function will look for the header pattern in each markdown file and then look for the list pattern within that section.
    It will return a dictionary where the keys are the markdown file names and the values are lists of dictionaries representing the sources found in each file.
    Returns a dictionary of sources found in the markdown files.
    """
    sources = {}
    header_pattern = re.compile(r"^(#{1,6})\s*.*Quellen", re.IGNORECASE)
    list_pattern = get_extract_multiline_list_items_pattern()
    if md_file:
        try:
            with open(md_file, encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            logging.warning("Cannot open %s: %s", md_file, e)
            return {}
        in_section = False
        level = None
        sources[str(md_file)] = []
        for lineno, line in enumerate(lines, 1):
            header = header_pattern.match(line)
            if header:
                in_section = True
                level = len(header.group(1))
                continue
            if in_section and line.startswith("#"):
                current = len(line) - len(line.lstrip("#"))
                if current <= level:
                    break
            if in_section and list_pattern.match(line):
                entry = {
                    "numbering": None,
                    "link": None,
                    "comment": None,
                    "lineno": lineno,
                    "line": line.strip(),
                    "kind": "external",
                }
                match = list_pattern.match(line)
                if match:
                    entry["numbering"] = match.group(0).strip()
                name_match = re.search(r"^\s*([0-9a-z\*]+[\.) ]|[-*+])\s+(.*)", line)
                if name_match:
                    name = name_match.group(2).strip()
                    # Remove numbering and quotes from the name if present
                    name = re.sub(
                        r"^[0-9a-z\*]+[\.) ]\s*", "", name
                    )  # Remove numbering
                    name = re.sub(r'^"(.*)"$', r"\1", name)  # Remove surrounding quotes
                    # Remove link if present
                    name = re.sub(r"\[.*?\]\(.*?\)", "", name).strip()
                link_match = re.search(r"\[.*?\]\((.*?)\)", line)
                if link_match:
                    entry["link"] = link_match.group(1)
                if link_match and not name:
                    name = link_match.group(0).split("]")[0].strip()
                comment_match = re.search(r"\((.*?)\)", line)
                if comment_match:
                    entry["comment"] = comment_match.group(1)
                if not name:
                    name = "Referenz zu Zeile " + str(lineno)
                sources[str(md_file)].append({name: entry})
    return sources


def extract_sources_to_dict(md_files) -> Dict[str, List[Dict[str, Dict[str, Any]]]]:
    """Extract 'Sources' sections from markdown files into a dict.<br>
    Typically references, sources or bibliography sections.<br>
    TODO: get_language_dependent_header_pattern_for_sources()<br>
    1. Current Header Pattern: ^.* Quellen<br>
    2. Current List Pattern: ^\s*([0-9a-z\*]+[\.) ]|[-*+])\s+<br>
    Shall find all lines starting with<br>
        a number followed by a dash or bracket or whitespace and then text<br>
        a bullet followed by a whitespace and then text<br>
        an alphabetically numbering then followed by a dash or bracket or whitespace and then text<br>
    <br>
    Dict Format:<br>
    <code>{
        "md_file_name": {
            "name": <-- the source name; e.g. the name part (plus possibly quotes) of: "name":[https://example.com](https://example.com) or [name](https://example.com) or 1. name: https://example.com
            {
                "numbering": "numbering_text",  <-- optional: any numbering, bullets, alphabetical numbering; e.g. 1., a., i., *, a), etc. or empty
                "link" : "valid_link",  <-- optional: any valid link; e.g. the url part of [link_description](https://example.com) or [../anhang/123] or empty
                "comment": "comment_text", <-- optional: any comment text; e.g. the comment part of [example](https://example.com), comment or [example](https://example.com) - comment or empty
                "lineno": line_number, <-- optional: line number of the source entry in the markdown file
                "line": full_line, <-- optional: full line of the source entry in the markdown file
                "kind": "source_type", <-- optional: type of source; e.g. document, book, article, website, internal GitBook reference, external (url), etc.
            }
        }
    }</code><br>
    Example:
    <code>{
        "file1.md": {
            "EU Codex 123":
            {
                "numbering": "1.",
                "link": "https://eu.eu?123",
                "comment": "The codex 123 of the EU is an interesting source for the topic 456.",
                "kind": "external",
            }
        },
        "file2.md": {
            "European Parliament Codex 123":
            {
                "numbering": "*",
                "link": "",
                "comment": "",
                "kind": "document",
            }
        }
    }</code><br>
    <br>
    This function will look for the header pattern in each markdown file and then look for the list pattern within that section.
    It will return a dictionary where the keys are the markdown file names and the values are lists of dictionaries representing the sources found in each file.
    Returns a dictionary of sources found in the markdown files.
    """
    sources = {}
    for md in md_files:
        if not os.path.isfile(md):
            logging.warning("Skipping missing file: %s", md)
            continue
        sources_of_file = extract_sources_of_a_md_file_to_dict(
            md
        )  # returns a dict {str(md_file): {name: {numbering, link, comment, line, kind}}}
        tag = str(md)
        if tag in sources:
            if isinstance(sources[tag], list):
                sources[tag].append(sources_of_file[tag])
            else:
                sources[tag] = sources_of_file[tag]
        else:
            sources[tag] = sources_of_file[tag]
    return sources


def extract_sources(md_files, output_csv):
    """Extract 'Sources' sections from markdown files into a CSV."""
    sources = extract_sources_to_dict(md_files)
    if not sources:
        logging.warning("No sources found in markdown files.")
        return
    # Write sources to CSV
    try:
        with open(output_csv, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                [
                    "File",
                    "Name",
                    "Link",
                    "Numbering",
                    "Comment",
                    "Kind",
                    "LineNo",
                    "Line",
                ]
            )
            for md_file, entries in sources.items():
                for entry in entries:
                    for name, reference in entry.items():
                        if not reference:
                            continue
                        # Remove numbering and quotes from the name if present
                        name = re.sub(r"^[0-9a-z\*]+[\.) ]\s*", "", name)
                    writer.writerow(
                        [
                            md_file,
                            name,
                            reference.get("link", ""),
                            reference.get("numbering", ""),
                            reference.get("comment", ""),
                            reference.get("kind", ""),
                            reference.get("lineno", ""),
                            reference.get("line", ""),
                        ]
                    )
        logging.info("Sources extracted to %s", output_csv)
    except Exception as e:
        logging.error("Failed to write sources CSV: %s", e)
        sys.exit(1)


def check_links(md_files, report_csv: str):
    """Check HTTP links in markdown files and return list of broken ones."""
    try:
        with open(report_csv, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["GO", "File", "Link", "Line#", "Line", "Status Code", "Error"]
            )
            broken = []
            good = []
            link_pattern = re.compile(r"\[.*?\]\((https?://[^)]+)\)")
            print("Starting external link check...")
            logging.info("Starting external link check...")
            for md in tqdm.tqdm(md_files, desc=" Files", unit=" File"):
                try:
                    with open(md, encoding="utf-8") as f:
                        for lineno, line in enumerate(f, 1):
                            for url in link_pattern.findall(line):
                                finding = None
                                try:
                                    response = requests.head(url, timeout=5)
                                    if response.status_code >= 400:
                                        finding = (
                                            "❌",
                                            md,
                                            url,
                                            lineno,
                                            line,
                                            response.status_code,
                                            response.reason,
                                        )
                                    else:
                                        g_finding = (
                                            "✅",
                                            md,
                                            url,
                                            lineno,
                                            line,
                                            response.status_code,
                                            "OK",
                                        )
                                        good.append(g_finding)
                                        writer.writerow(g_finding)
                                        logging.info(
                                            f"✅ Good link found in {md}: {url} (Line {lineno}) (Finding: '{g_finding}')"
                                        )

                                except Exception as e:
                                    finding = (
                                        "💥❌",
                                        md,
                                        url,
                                        lineno,
                                        line,
                                        "unknown",
                                        str(e),
                                    )
                                if finding:
                                    broken.append(finding)
                                    writer.writerow(finding)
                                    logging.info(
                                        f"❌ Broken link found in {md}: {url} (Line {lineno}) (Finding: '{finding}')"
                                    )
                except Exception as e:
                    logging.warning("Failed to open %s for link check: %s", md, e)
                    print(f"❌ Failed to open {md} for link check: {e}")
            print(
                f"\n\n--- Final Report: {len(broken)} broken links, {len(good)} good links ---"
            )
            logging.info(
                f"\n\n--- Final Report: {len(broken)} broken links, {len(good)} good links ---"
            )
            if broken:
                print(
                    f"❌ Found {len(broken)} broken links. Check report '{report_csv}' for details."
                )
                logging.info(
                    f"❌ Found {len(broken)} broken links. Check report '{report_csv}' for details."
                )
            else:
                print(f"✅ All check done. All fine.")
                logging.info(f"✅ All check done. All fine.")
    except Exception as e:
        logging.error("Failed to check links and write report to  CSV: %s", e)
        sys.exit(1)


def split_reference_to_decription_and_urluri(name):
    # Extract URL or URI clearly enclosed by parentheses or brackets
    url_pattern = re.compile(
        r"\(?\[?(https?://[^\s\)\]\[]+|[^\s\)\]\[]+\.[^\s\)\]\[]+)\]?\)?"
    )
    url_match = url_pattern.search(name)

    if url_match:
        value_part = url_match.group(1).strip()
        # Remove URL from the name to cleanly isolate the descriptive text
        key_part = url_pattern.sub("", name).strip(', ":()[]').strip()
    else:
        key_part = name.strip(', ":()[]').strip()
        value_part = ""

    return key_part, value_part


def proof_and_repair_internal_references(md_files, summary_md):
    """
    1) Repariert gebrochene interne GitBook-Links anhand von SUMMARY.md.
    2) Wrappt Plain-Text-Kapitelreferenzen im Fließtext als Fußnoten.
    3) Fügt neue Einträge in eine vorhandene 'Quellen & Verweise' ein (merge),
       oder legt eine neue Sektion an, falls keine existierte.
    4) Header-Zeilen (#...) werden unverändert gelassen.
    """

    # 1. SUMMARY.md → title→link map
    summary_map = {}
    link_re = re.compile(r"\*+\s*\[(?P<title>[^\]]+)\]\((?P<link>[^)]+\.md)\)")
    with open(summary_md, encoding="utf-8") as sf:
        for line in sf:
            m = link_re.search(line)
            if m:
                summary_map[m.group("title").strip()] = m.group("link").strip()

    report = []
    internal_link_re = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<target>[^)]+\.md)\)")
    title_patterns = [
        (re.compile(rf"\b{re.escape(t)}\b"), t, link) for t, link in summary_map.items()
    ]

    for file in md_files:
        # --- Fußnotenverwaltung pro Datei ---
        local_footnotes = {}
        footnote_counter = 1

        def get_footnote_idx(
            title: str, link: str, comment: str = None, kind: str = "external"
        ) -> Dict[str, Any]:
            nonlocal footnote_counter
            key = (title, link)
            if key not in local_footnotes:
                local_footnotes[key] = {
                    "index": footnote_counter,
                    "title": title,
                    "link": link,
                    "comment": comment,
                    "kind": kind,
                }
                report.append(
                    {
                        "action": "footnote_added",
                        "file": file,
                        "title": title,
                        "link": link,
                        "index": footnote_counter,
                        "comment": comment,
                        "kind": kind,
                    }
                )
                footnote_counter += 1
            return local_footnotes[key]

        def repl_link(m):
            tgt = m.group("target")
            if tgt in summary_map.values():
                report.append(
                    {
                        "action": "link_ok",
                        "file": file,
                        "target": tgt,
                    }
                )
                return m.group(0)
            base = os.path.basename(tgt)
            for alt in summary_map.values():
                if os.path.basename(alt) == base:
                    report.append(
                        {
                            "action": "link_repaired",
                            "file": file,
                            "orig": tgt,
                            "new": alt,
                        }
                    )
                    return f"[{m.group('label')}]({alt})"
            report.append(
                {
                    "action": "link_broken",
                    "file": file,
                    "target": tgt,
                }
            )
            return m.group(0)

        # target: gather all local footnotes from the file (existing one, repaired internal ones, possible internal new ones)

        # --- 1. read file ---
        lines = open(file, encoding="utf-8").read().splitlines(keepends=True)
        block_start = None
        block_end = None

        # --- 2. fetch all existing footnotes in the file ---
        existing_sources = extract_sources_of_a_md_file_to_dict(file)

        # --- 3. if there are existing sources then
        if existing_sources:
            # --- gather all existing footnotes, repair possibly broken internal ones ---
            for _, entries in existing_sources.items():
                if entries:
                    for entry in entries:
                        for name, reference in entry.items():
                            if not reference:
                                continue
                            # --- 3a. check the entry for being an internal link and repair it if broken (using the summary map) ---
                            block_start = (
                                min(block_start, reference.get("lineno"))
                                if block_start
                                else reference.get("lineno")
                            )
                            block_end = (
                                max(block_end, reference.get("lineno"))
                                if block_end
                                else reference.get("lineno")
                            )
                            block_level = reference.get("level")

                            # Split into Key-part and Value-part e.g. "🧩 Interaktive Elemente (Checkliste & Quiz)", 2025 uri or url
                            name_key_part, name_value_part = (
                                split_reference_to_decription_and_urluri(name)
                            )

                            # check if the name is in the summary map
                            for key, value in summary_map.items():
                                # print(f"name: {name}, key: {key}, value: {value}")
                                if name in key:
                                    if reference.get("link") == value:
                                        # report.append(
                                        #    {
                                        #        "action": "link_ok",
                                        #        "file": file,
                                        #        "name": name,
                                        #        "target": reference["link"],
                                        #        "kind": reference.get("kind"),
                                        #    }
                                        # )
                                        pass
                                    else:
                                        report.append(
                                            {
                                                "action": "link_repaired",
                                                "file": file,
                                                "name": name,
                                                "orig": reference.get("link"),
                                                "new": value,
                                                "kind": reference.get("kind"),
                                            }
                                        )
                                        reference["link"] = value
                                    break
                                # Perform a similarity check between the name_key_part and the key
                                # If the similarity exceeds a threshold, consider it a match
                                similarity = SequenceMatcher(
                                    None, name_key_part, key
                                ).ratio()
                                threshold = 0.7  # Adjust this threshold as needed
                                if (
                                    "Interaktive Elemente" in name
                                    and "Interaktive Elemente" in key
                                ):
                                    pass
                                if similarity >= threshold:
                                    report.append(
                                        {
                                            "action": "link_repaired_by_similarity_matched",
                                            "file": file,
                                            "name": name,
                                            "orig": reference.get("link"),
                                            "new": value,
                                            "similarity": similarity,
                                            "kind": reference.get("kind"),
                                        }
                                    )
                                    reference["link"] = value
                                    name = key
                                    break

                            footnote = get_footnote_idx(
                                name,
                                reference.get("link"),
                                reference.get("comment"),
                                reference.get("kind"),
                            )
                            # --- 3b. check for footnote references in the plain text and replace them with new genarated ones ---
                            if reference.get("numbering"):
                                # find numbering f"[{numbering}]" in the text and replace it with the actual footnote reference
                                def get_numbering(reference: dict[str, str]) -> str:
                                    return reference.get("numbering", "").strip()

                                pattern = re.compile(
                                    rf"\b{re.escape(f'[{get_numbering(reference=reference)}]')}\b"
                                )
                                pattern.sub(
                                    lambda m: f"[{m.group(0)}]",
                                    "".join(lines),
                                )
                                reference["indexed"] = True

        # remove existing block
        if block_start is not None:
            before = (
                lines[: block_start - 1] if block_start > 0 else lines[:block_start]
            )
            after = (
                lines[block_end + 1 :] if block_end < len(lines) else lines[block_end:]
            )
        else:
            # No existing block found, so we can just append to the end of the file but put append an empty line before
            lines.append("\n")
            lines.append(f"## Quellen & Verweise\n\n")
            before = lines
            after = []

        # gather all possible local references from the file
        local_references = {
            (link, title)
            for local_line in lines
            for title, link in summary_map.items()
            if title in local_line or link in local_line
        }

        # 4. gather possible new internal links from the file
        for ln in lines:
            ln = internal_link_re.sub(repl_link, ln)

            # Identify and add footnotes for plain text references found in the markdown content but exclude local references
            def find_new_footnote(title, link):
                # exclude local reference
                if (link, title) in local_references:
                    return None
                # add a new footnote and never a local reference
                return get_footnote_idx(title, link, None, "internal")["index"]

            for patt, title, link in title_patterns:
                ln = patt.sub(
                    lambda m: f"[{m.group(0)}][{find_new_footnote(title, link)}]",
                    ln,
                )

        # check if we have to process anything in the file
        if not local_footnotes:
            # No local footnotes, so we leave the file as is and continue to the next one
            continue

        # --- rebuild file ---
        processed = []
        for ln in before:
            processed.append(ln)

        # --- rebuild footnotes part ---
        new_entries = [
            f'{content["index"]}. {title}: [{title}]({link}) {content["comment"]}\n'
            for (title, link), content in sorted(
                local_footnotes.items(), key=lambda x: x[1]["index"]
            )
        ]
        for entry in new_entries:
            processed.append(entry)
        processed.append("\n")

        for ln in after:
            processed.append(ln)

        # --- save rebuild file ---
        with open(file, "w", encoding="utf-8") as wf:
            wf.write("".join(processed))

    return report


def extract_json_from_ai_output(generated_text: str):
    original_input = generated_text  # für Logging im Fehlerfall

    # Schritt 1: Entferne Markdown-Codeblockmarker
    text = generated_text.strip()
    if text.startswith("```json"):
        text = text[7:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()

    # Schritt 2: Entferne äußere Anführungszeichen
    text = text.strip().strip("'").strip('"')

    # Schritt 3: Versuch direkter JSON-Parse
    try:
        return True, json.loads(text)
    except json.JSONDecodeError:
        pass  # weiter zu Escape-Entschlüsselung

    # Schritt 4: Versuch Escape-Sequenzen zu entschlüsseln
    unescaped = None
    # Fallback: ent-escape mit ast.literal_eval
    try:
        # Direkt, wenn möglich
        unescaped = ast.literal_eval(text)
    except SyntaxError:
        # Falls geschachtelte Quotes o. ä. Probleme machen, manuell sichern
        safe = text.replace("\\", "\\\\").replace('"', '\\"')
        unescaped = ast.literal_eval(f'"{safe}"')
    try:
        unescaped = ast.literal_eval(unescaped)
        return True, json.loads(unescaped)
    except Exception as e:
        logging.debug(f"Escape-Decode failed: {e}")

    # Schritt 5: Erkenne Schema-Definitionen (statt Instanz)
    if "$schema" in text or "properties" in text:
        logging.warning("KI hat ein JSON-Schema geliefert, kein Instanzobjekt.")
        return False, text

    # Schritt 6: Alles gescheitert – Logging & Fallback
    logging.warning(
        "JSON parsing failed for AI response. Returning raw text.\n" + original_input
    )
    return False, original_input


def ask_ai(
    prompt: str,
    ai_url: str,
    ai_api_key: str,
    ai_provider: str,
    retry_count: int = 0,
    max_retries: int = 3,  # Maximale Anzahl der Wiederholungen
) -> tuple[bool, str]:

    # Allgemeine Header
    headers = {
        "Authorization": f"Bearer {ai_api_key}",
        "Content-Type": "application/json",
    }

    # Anfrage-Daten und Parsing je nach Anbieter
    if ai_provider.lower() == "openai":
        payload = {
            "model": "gpt-4",  # ggf. anpassbar
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
        try:
            response = requests.post(ai_url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return True, result["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return False, f"[OpenAI] Fehler: {e}"

    elif ai_provider.lower() == "genai":
        # genai
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
        }
        headers = {
            "Content-Type": "application/json",
        }

        # API-URL mit API-Schlüssel als Query-Parameter
        url_with_key = f"{ai_url}?key={ai_api_key}"

        try:
            # Sende die Anfrage
            response = requests.post(url_with_key, headers=headers, json=payload)
            response.raise_for_status()  # Löst eine Exception aus, wenn der Statuscode nicht 2xx ist
            result = response.json()
            # Extrahiere den generierten Text
            generated_text = result["candidates"][0]["content"]["parts"][0][
                "text"
            ].strip()
            return extract_json_from_ai_output(generated_text)
        except requests.exceptions.RequestException as e:
            if e.response.status_code == 429:
                if retry_count < max_retries:
                    # 429 Client Error: Too Many Requests for url
                    wait_time = random.randint(1, 8)
                    # wait some seconds and retry
                    logging.warning(
                        f"[GenAI] Zu viele Anfragen. Warte {wait_time} Sekunden und versuche es erneut ({retry_count + 1}/{max_retries})"
                    )
                    time.sleep(wait_time)
                    return ask_ai(
                        prompt,
                        ai_url,
                        ai_api_key,
                        ai_provider,
                        retry_count + 1,
                    )
                else:
                    return False, f"[GenAI] Fehler: {e} (max retries reached)"
            return False, f"[GenAI] Fehler: {e}"
        except Exception as e:
            return False, f"[GenAI] Fehler: {e}"
    else:
        return (
            False,
            f"Unbekannter AI-Provider: '{ai_provider}'. Nur 'openai' oder 'genai' werden unterstützt.",
        )


def proof_and_repair_external_reference(
    reference_as_line: str,
    footnote_index: int,
    prompt: str,
    ai_url: str,
    ai_api_key: str,
    ai_provider: str,
) -> tuple[bool, str]:
    """
    Sendet einen Prompt an die gewählte AI-API (OpenAI oder Google GenAI),
    inklusive Quellenangabe und Fußnotennummer, und gibt die AI-Antwort zurück.

    Args:
        reference_as_line (str): Die Zitationszeile für die Referenz.
        footnote_index (int): Die Fußnotennummer.
        prompt (str): Der zu bearbeitende Prompt.
        ai_url (str): Der URL-Endpunkt der AI-API.
        ai_api_key (str): Der API-Schlüssel zur Authentifizierung.
        ai_provider (str): Anbieterkennung, z. B. "openai" oder "genai".

    Returns:
        str: Antwort der AI oder Fehlermeldung.
    """

    # JSON Formatierung
    structured_schema = """
    {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zitationsprüfungsergebnis",
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean",
      "description": "Ob die Zitation erfolgreich validiert und ggf. korrigiert wurde"
    },
    "org": {
      "type": "string",
      "description": "Die original eingegebene (ungeprüfte) Quellenangabe"
    },
    "new": {
      "type": "string",
      "description": "Die neue, wissenschaftlich korrekte Zitationszeile im gewünschten Format (optional)",
      "nullable": true
    },
    "error": {
      "type": "string",
      "description": "Fehlermeldung, falls die Zitation nicht erstellt werden konnte (optional)",
      "nullable": true
    },
    "hint": {
      "type": "string",
      "description": "Hilfestellung zur Verbesserung oder Vervollständigung der Quelle (optional)",
      "nullable": true
    },
    "validation_date": {
      "type": "string",
      "format": "date",
      "description": "Das Datum der Prüfung und ggf. der URL-Validierung (today)"
    },
    "type": {
      "type": "string",
      "description": "Kategorisierung der Quelle: 'internal reference', 'external url', 'external reference' oder '?'",
      "enum": ["internal reference", "external url", "external reference", "?"]
    }
  },
  "required": ["success", "org", "validation_date", "type"]
}
    """

    json_hint = """
    {
        "success": true|false,
        "org": "<Originalquelle>",
        "new": "<neue Zitationszeile oder null>",
        "error": "<Fehlermeldung oder null>",
        "hint": "<Hinweis oder null>",
        "validation_date": "YYYY-MM-DD",
        "type": "internal reference" | "external url" | "external reference" | "?"
    }
"""

    # Prompt um Quellenhinweis ergänzen
    full_prompt = f"{prompt}\n\nQuelle [{footnote_index}]: {reference_as_line}\n\n\n\nGenerate a structured JSON according:\n{json_hint}"

    return ask_ai(full_prompt, ai_url, ai_api_key, ai_provider)


def proof_and_repair_external_references(
    md_files, prompt, ai_url, ai_api_key, ai_provider
) -> List[Dict[str, Any]]:
    """Proof and repair external references in markdown files."""
    report = []
    block_start = None
    block_end = None
    block_level = None
    for file in tqdm.tqdm(md_files, desc=" Files", unit=" File"):
        # --- 1. fetch all existing footnotes in the file ---
        existing_sources = extract_sources_of_a_md_file_to_dict(file)
        repaired_references = []
        # --- 2. if there are existing sources then
        if existing_sources:
            for _, entries in existing_sources.items():
                if entries:
                    for entry in entries:
                        for name, reference in entry.items():
                            if not reference:
                                continue
                            # --- 3a. check the entry for being an internal link and repair it if broken (using the summary map) ---
                            block_start = (
                                min(block_start, reference.get("lineno"))
                                if block_start
                                else reference.get("lineno")
                            )
                            block_end = (
                                max(block_end, reference.get("lineno"))
                                if block_end
                                else reference.get("lineno")
                            )
                            block_level = reference.get("level")
                            try:
                                # Extract integer from numbering or set to -1 if not possible
                                numbering = reference.get("numbering", "").strip()
                                if numbering.isdigit():
                                    footnote_index = int(numbering)
                                else:
                                    match = re.match(r"(\d+)", numbering)
                                    footnote_index = (
                                        int(match.group(1)) if match else -1
                                    )
                            except Exception:
                                footnote_index = -1

                            success, result = proof_and_repair_external_reference(
                                reference_as_line=reference.get("line"),
                                footnote_index=footnote_index,
                                prompt=prompt,
                                ai_url=ai_url,
                                ai_api_key=ai_api_key,
                                ai_provider=ai_provider,
                            )
                            has_json = True if isinstance(result, dict) else False
                            repaired_references.append(
                                {
                                    "line": reference.get("line"),
                                    "lineno": reference.get("lineno"),
                                    "success": success
                                    and has_json
                                    and result.get("success"),
                                    "new": result.get("new") if has_json else None,
                                    "error": (
                                        result.get("error")
                                        if has_json
                                        else f"ai response data error: {result}"
                                    ),
                                    "hint": (
                                        result.get("hint")
                                        if has_json
                                        else "repair prompt, details in error"
                                    ),
                                    "validation_date": (
                                        result.get("validation_date")
                                        if has_json
                                        else None
                                    ),
                                    "type": result.get("type") if has_json else None,
                                }
                            )

            # read the file and replace the line with the repaired one
            with open(file, encoding="utf-8") as rf:
                lines = rf.readlines()
            for repaired_reference in repaired_references:
                if repaired_reference["success"] and repaired_reference["new"]:
                    # at the reference line
                    lineno = repaired_reference["lineno"]
                    # replace the line with the repaired one
                    lines[lineno - 1] = (
                        lines[lineno - 1].replace(
                            repaired_reference["line"],
                            repaired_reference["new"],
                        )
                        + "\n"
                    )
                    report.append(
                        {
                            "action": "link_repaired",
                            "file": file,
                            "lineno": repaired_reference["lineno"],
                            "orig": repaired_reference["line"],
                            "new": repaired_reference["new"],
                            "validation_date": repaired_reference["validation_date"],
                            "type": repaired_reference["type"],
                            "hint": repaired_reference["hint"],
                        }
                    )
                    logging.info(
                        "Repaired reference: %s -> %s, file: %s",
                        repaired_reference["line"],
                        repaired_reference["new"],
                        file,
                    )
                elif repaired_reference["success"]:
                    # just write report
                    report.append(
                        {
                            "action": "link_check_succeeded",
                            "file": file,
                            "lineno": repaired_reference["lineno"],
                            "orig": repaired_reference["line"],
                            "validation_date": repaired_reference["validation_date"],
                            "type": repaired_reference["type"],
                            "hint": repaired_reference["hint"],
                        }
                    )
                    logging.info(
                        "Reference already ok: %s, file: %s",
                        repaired_reference["line"],
                        file,
                    )
                else:
                    # just write report
                    report.append(
                        {
                            "action": "link_repair_failed",
                            "file": file,
                            "lineno": repaired_reference["lineno"],
                            "orig": repaired_reference["line"],
                            "error": repaired_reference["error"],
                            "validation_date": repaired_reference["validation_date"],
                            "type": repaired_reference["type"],
                            "hint": repaired_reference["hint"],
                        }
                    )
                    logging.warning(
                        "Failed to repair reference: %s, file: %s, error: %s",
                        repaired_reference["line"],
                        file,
                        repaired_reference["error"],
                    )
            # write back the result to the file
            with open(file, "a", encoding="utf-8") as wf:
                wf.writelines(lines)
    return report


def lint_markdown(repo_dir):
    """Run markdownlint on the repository and return its output."""
    return run("markdownlint **/*.md", cwd=repo_dir, capture_output=True)


def check_images(md_files):
    """Check if images (local or remote) referenced in markdown exist."""
    missing = []
    img_pattern = re.compile(r"!\[.*?\]\((.*?)\)")
    for md in md_files:
        try:
            with open(md, encoding="utf-8") as f:
                for lineno, line in enumerate(f, 1):
                    for path in img_pattern.findall(line):
                        if path.startswith("http"):
                            try:
                                response = requests.head(path, timeout=5)
                                if response.status_code >= 400:
                                    missing.append(
                                        (md, lineno, path, response.status_code)
                                    )
                            except Exception as e:
                                missing.append((md, lineno, path, str(e)))
                        else:
                            full_path = os.path.join(os.path.dirname(md), path)
                            if not os.path.exists(full_path):
                                missing.append((md, lineno, full_path, "Not found"))
        except Exception as e:
            logging.warning("Failed to open %s for image check: %s", md, e)
    return missing


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


def validate_metadata(md_files):
    """Validate YAML frontmatter metadata in markdown files."""
    issues = []
    if not yaml:
        logging.warning("PyYAML not installed; skipping metadata validation.")
        return issues
    for md in md_files:
        try:
            with open(md, encoding="utf-8") as f:
                content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 2:
                    meta = yaml.safe_load(parts[1])
                    for field in ("title", "author", "date"):
                        if field not in meta:
                            issues.append((md, f"Missing metadata field: {field}"))
        except Exception as e:
            issues.append((md, f"Metadata parse error: {e}"))
    return issues


def check_duplicate_headings(md_files):
    """Detect duplicate headings across markdown files."""
    seen = {}
    duplicates = []
    header_pattern = re.compile(r"^(#{1,6})\s*(.+)")
    for md in md_files:
        try:
            with open(md, encoding="utf-8") as f:
                for lineno, line in enumerate(f, 1):
                    match = header_pattern.match(line)
                    if match:
                        title = match.group(2).strip().lower()
                        ref = f"{md}:{lineno}"
                        if title in seen:
                            duplicates.append((md, lineno, title, seen[title]))
                        else:
                            seen[title] = ref
        except Exception as e:
            logging.warning("Failed to open %s for heading check: %s", md, e)
    return duplicates


def check_citation_numbering(md_files):
    """Ensure numbered citations run consecutively without gaps."""
    gaps = []
    num_pattern = re.compile(r"^\s*([0-9]+)\.\s")
    for md in md_files:
        nums = []
        try:
            with open(md, encoding="utf-8") as f:
                for line in f:
                    match = num_pattern.match(line)
                    if match:
                        nums.append(int(match.group(1)))
            if nums:
                expected = set(range(1, max(nums) + 1))
                missing = expected - set(nums)
                if missing:
                    gaps.append((md, sorted(missing)))
        except Exception as e:
            logging.warning("Failed to open %s for citation check: %s", md, e)
    return gaps


def list_todos(md_files):
    """List all TODO and FIXME comments in markdown files."""
    todos = []
    markers = re.compile(r"\b(TODO|FIXME)\b")
    for md in md_files:
        try:
            with open(md, encoding="utf-8") as f:
                for lineno, line in enumerate(f, 1):
                    if markers.search(line):
                        todos.append((md, lineno, line.strip()))
        except Exception as e:
            logging.warning("Failed to open %s for TODO check: %s", md, e)
    return todos


def spellcheck(repo_dir):
    """Run codespell to check for common spelling mistakes."""
    return run("codespell -q 3", cwd=repo_dir, capture_output=True)


def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def remove_tree(path):
    try:
        shutil.rmtree(path, onerror=remove_readonly)
    except Exception as e:
        logging.error("Failed to remove directory %s: %s", path, e)
        sys.exit(1)


def checkout_branch(repo_dir, branch_name):
    """Check out a specific branch in the given Git repository."""
    try:
        # Prüfen, ob der Branch existiert
        run(f"git -C {repo_dir} fetch --all")
        run(f"git -C {repo_dir} checkout {branch_name}")
        logging.info("Checked out branch: %s", branch_name)
    except SystemExit as e:
        logging.error(
            "Failed to check out branch '%s': Exit code %s", branch_name, e.code
        )
        sys.exit(e.code)


def clone_or_update_repo(repo_url, clone_dir, branch_name=None):
    if os.path.isdir(clone_dir):
        resp = (
            input(f"Directory '{clone_dir}' exists. Clean and reclone? (y/N) ")
            .strip()
            .lower()
        )
        if resp == "y":
            # check if a .git directory exists
            if os.path.isdir(os.path.join(clone_dir, ".git")) and branch_name:
                try:
                    run(f"git -C {clone_dir} status", capture_output=True)
                    logging.info("Valid Git repository found: %s", clone_dir)
                    # Überschreibe den Arbeitsbaum mit Git
                    run(f"git -C {clone_dir} fetch --all")
                    run(f"git -C {clone_dir} reset --hard origin/{branch_name}")
                    run(f"git -C {clone_dir} clean -fdx")
                except SystemExit as e:
                    logging.warning(
                        "Git command failed with exit code %s. Re-cloning repository.",
                        e.code,
                    )
                    # Remove the directory and re-clone
                    logging.info("Cleaning directory: %s", clone_dir)
                    remove_tree(clone_dir)
                    run(f"git clone {repo_url} {clone_dir}")
            else:
                logging.info("Cleaning non-repo directory: %s", clone_dir)
                remove_tree(clone_dir)
                if branch_name:
                    run(f"git clone --branch {branch_name} {repo_url} {clone_dir}")
                else:
                    run(f"git clone {repo_url} {clone_dir}")
        else:
            # fetch all, switch to branch and pull
            run(f"git -C {clone_dir} fetch --all")
            run(f"git -C {clone_dir} checkout {branch_name}")
            run(f"git -C {clone_dir} pull origin {branch_name}")
    else:
        run(f"git clone --branch {branch_name} {repo_url} {clone_dir}")
