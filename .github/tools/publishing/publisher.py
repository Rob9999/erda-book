#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Selective Publisher
- Liest publish.yml|yaml aus dem Repo-Root
- Ermittelt alle Einträge mit build: true -> get_publish_list()
- Bereitet Umgebung vor (PyYAML, optional Pandoc/LaTeX & Emoji-Fonts) -> prepareYAML(), prepare_publishing()
- Baut PDFs für 'file' und 'folder' -> build_pdf()
- Setzt nach erfolgreichem Build das Flag per reset-publish-flag.py zurück -> main()

Aufrufbeispiele:
  python .github/tools/publishing/publisher.py
  python .github/tools/publishing/publisher.py --manifest publish.yml --use-summary
  python .github/tools/publishing/publisher.py --no-apt --only-prepare

Optionen siehe argparse unten.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from collections.abc import Mapping
from functools import lru_cache

from tools.logging_config import get_logger

from tools.publishing.markdown_combiner import (
    add_geometry_package,
    combine_markdown,
    normalize_md,
)
from tools.publishing.preprocess_md import process
from tools.publishing.gitbook_style import (
    DEFAULT_MANUAL_MARKER,
    SummaryContext,
    ensure_clean_summary,
    get_summary_layout,
)
from tools.publishing.emoji_report import emoji_report

# ------------------------------- Utils ------------------------------------- #

logger = get_logger(__name__)


_TRUE_VALUES = {"1", "true", "yes", "on", "y"}

_SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+][0-9A-Za-z.-]+)?$"
)
_MANIFEST_VERSION_MIN = (0, 1, 0)
_MANIFEST_VERSION_CURRENT = (0, 1, 0)


_DEFAULT_LUA_FILTERS: List[str] = [
    ".github/tools/publishing/lua/image-path-resolver.lua",
]
_DEFAULT_HEADER_PATH = ".github/tools/publishing/texmf/tex/latex/local/deeptex.sty"
_DEFAULT_METADATA: Dict[str, List[str]] = {
    "color": ["true"],
}
_DEFAULT_VARIABLES: Dict[str, str] = {
    "mainfont": "DejaVu Serif",
    "sansfont": "DejaVu Sans",
    "monofont": "DejaVu Sans Mono",
    "geometry": "margin=1in",
    "longtable": "true",
    "max-list-depth": "9",
}
_DEFAULT_EXTRA_ARGS: Tuple[str, ...] = ()

EMOJI_RANGES = (
    "1F300-1F5FF, 1F600-1F64F, 1F680-1F6FF, 1F700-1F77F, 1F780-1F7FF, "
    "1F800-1F8FF, 1F900-1F9FF, 1FA00-1FA6F, 1FA70-1FAFF, "
    "2600-26FF, 2700-27BF, 2300-23FF, 2B50, 2B06, 2934-2935, 25A0-25FF"
)


@dataclass(frozen=True)
class EmojiOptions:
    """Runtime configuration for emoji handling in Pandoc runs."""

    color: bool = True
    report: bool = False
    report_dir: Optional[Path] = None


def _resolve_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _as_bool(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in _TRUE_VALUES
    return default


def _run(
    cmd: List[str],
    check: bool = True,
    capture: bool = False,
    env: Optional[Dict[str, str]] = None,
) -> subprocess.CompletedProcess:
    kwargs: Dict[str, Any] = {"text": True}
    if capture:
        kwargs["stdout"] = subprocess.PIPE
        kwargs["stderr"] = subprocess.PIPE
    if env:
        kwargs["env"] = {**os.environ, **env}
    logger.info("→ %s", " ".join(cmd))
    cp = subprocess.run(cmd, **kwargs)
    if check and cp.returncode != 0:
        if capture:
            logger.info(cp.stdout or "")
            logger.error(cp.stderr or "")
        raise subprocess.CalledProcessError(cp.returncode, cmd)
    return cp


def _which(name: str) -> Optional[str]:
    return shutil.which(name)


def _is_debian_like() -> bool:
    return pathlib.Path("/etc/debian_version").exists()


def _ensure_dir(path: str) -> None:
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def _coerce_sequence(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        raise TypeError("Mappings können nicht als Sequenz interpretiert werden.")
    try:
        return [str(item) for item in value]
    except TypeError:
        return [str(value)]


def _merge_sequence(base: Sequence[str], override: Any) -> Tuple[str, ...]:
    values = list(base)
    if override is None:
        return tuple(values)
    if isinstance(override, Mapping):
        if "replace" in override:
            return tuple(_coerce_sequence(override.get("replace")))
        if "prepend" in override:
            values = _coerce_sequence(override.get("prepend")) + values
        if "append" in override:
            values.extend(_coerce_sequence(override.get("append")))
        if "remove" in override:
            removals = set(_coerce_sequence(override.get("remove")))
            values = [item for item in values if item not in removals]
        return tuple(values)
    return tuple(_coerce_sequence(override))


def _merge_metadata(
    base: Dict[str, Sequence[str]], override: Any
) -> Dict[str, Tuple[str, ...]]:
    result: Dict[str, Tuple[str, ...]] = {
        key: tuple(values) for key, values in base.items()
    }
    if not override:
        return result
    if not isinstance(override, Mapping):
        logger.warning("Pandoc-Metadaten-Override muss ein Mapping sein.")
        return result
    replace_block = override.get("replace")
    if isinstance(replace_block, Mapping):
        result = {
            str(key): tuple(_coerce_sequence(value))
            for key, value in replace_block.items()
        }
    for key, value in override.items():
        if key == "replace":
            continue
        if value is None:
            result.pop(str(key), None)
            continue
        if isinstance(value, Mapping):
            try:
                result[str(key)] = _merge_sequence(result.get(str(key), tuple()), value)
            except TypeError as exc:
                logger.warning(
                    "Pandoc-Metadaten-Override für %s konnte nicht angewendet werden: %s",
                    key,
                    exc,
                )
            continue
        try:
            result[str(key)] = tuple(_coerce_sequence(value))
        except TypeError as exc:
            logger.warning(
                "Pandoc-Metadaten-Override für %s konnte nicht geparst werden: %s",
                key,
                exc,
            )
    return result


def _merge_variables(base: Dict[str, str], override: Any) -> Dict[str, str]:
    result = dict(base)
    if not override:
        return result
    if not isinstance(override, Mapping):
        logger.warning("Pandoc-Variablen-Override muss ein Mapping sein.")
        return result
    replace_block = override.get("replace")
    if isinstance(replace_block, Mapping):
        result = {str(key): str(value) for key, value in replace_block.items()}
    for key, value in override.items():
        if key == "replace":
            continue
        if value is None:
            result.pop(str(key), None)
        else:
            if isinstance(value, Mapping):
                logger.warning(
                    "Verschachtelte Variablen-Overrides für %s werden nicht unterstützt.",
                    key,
                )
                continue
            result[str(key)] = str(value)
    return result


def _normalize_font_name(value: str) -> str:
    """Return a normalised version of ``value`` for fuzzy font matching."""

    return re.sub(r"[^a-z0-9]", "", value.lower())


def _font_available(name: str) -> bool:
    """Return ``True`` if fontconfig or local assets can resolve ``name``."""

    normalized = _normalize_font_name(name)

    fc_list = _which("fc-list")
    if fc_list:
        try:
            result = subprocess.run(
                [fc_list, name],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
        except OSError:
            result = None
        else:
            if result and result.stdout:
                for line in result.stdout.splitlines():
                    if normalized in _normalize_font_name(line):
                        return True

    fonts_dir = _resolve_repo_root() / ".github" / "tools" / "publishing" / "fonts"
    try:
        for font_file in fonts_dir.rglob("*.ttf"):
            stem = _normalize_font_name(font_file.stem)
            if stem and (normalized in stem or stem in normalized):
                return True
    except OSError:
        pass
    return False


@lru_cache(maxsize=1)
def _get_pandoc_version() -> Tuple[int, ...]:
    """Return the installed Pandoc version as a tuple or ``()`` if unknown."""

    pandoc = _which("pandoc")
    if not pandoc:
        return ()
    try:
        result = subprocess.run(
            [pandoc, "--version"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError:
        return ()
    if result.returncode != 0 or not result.stdout:
        return ()
    first_line = result.stdout.splitlines()[0]
    match = re.search(r"pandoc\s+([0-9]+(?:\.[0-9]+)*)", first_line)
    if not match:
        return ()
    return tuple(int(part) for part in match.group(1).split("."))


def _needs_harfbuzz(font_name: str) -> bool:
    """Return ``True`` if ``font_name`` requires HarfBuzz rendering."""

    lowered = font_name.lower()
    return "color" in lowered or "segoe ui emoji" in lowered


def _select_emoji_font(prefer_color: bool) -> Tuple[Optional[str], bool]:
    """Select the best available emoji font.

    Returns a tuple ``(font_name, needs_harfbuzz)`` describing the selected
    font and whether HarfBuzz rendering should be enabled for it.
    """

    candidates: List[str] = []
    if prefer_color:
        candidates.append("OpenMoji Color")
    candidates.extend(["OpenMoji Black", "Segoe UI Emoji"])

    for candidate in candidates:
        if _font_available(candidate):
            logger.info("ℹ Verwende Emoji-Font %s", candidate)
            return candidate, _needs_harfbuzz(candidate)

    logger.warning("⚠ Keine spezielle Emoji-Schrift gefunden – fallback auf Hauptfont")
    return None, False


def _build_font_header(
    *,
    main_font: str,
    sans_font: str,
    mono_font: str,
    emoji_font: Optional[str],
    include_mainfont: bool,
    needs_harfbuzz: bool,
    manual_fallback_spec: Optional[str],
) -> str:
    """Render a Pandoc header snippet configuring fonts and fallbacks."""

    lines = ["\\usepackage{fontspec}"]
    lines.append(f"\\setsansfont{{{sans_font}}}")
    lines.append(f"\\setmonofont{{{mono_font}}}")
    if include_mainfont:
        lines.append(f"\\setmainfont{{{main_font}}}")
    if emoji_font:
        options: List[str] = [f"Range={{{EMOJI_RANGES}}}"]
        if needs_harfbuzz:
            options.insert(0, "Renderer=Harfbuzz")
        option_block = "[" + ",".join(options) + "]"
        lines.append(f"\\IfFontExistsTF{{{emoji_font}}}{{")
        lines.append(f"  \\newfontfamily\\EmojiOne{{{emoji_font}}}{option_block}")
        if manual_fallback_spec:
            lines.append(
                f'  \\directlua{{luaotfload.add_fallback("mainfont", "{manual_fallback_spec}")}}'
            )
        lines.append("}{}")
    lines.extend(
        [
            "\\newcommand*{\\panEmoji}[1]{%",
            "  \\ifdefined\\EmojiOne",
            "    {\\EmojiOne #1}%",
            "  \\else",
            "    {#1}%",
            "  \\fi",
            "}",
        ]
    )
    if _DEFAULT_HEADER_PATH:
        header_path = Path(_DEFAULT_HEADER_PATH).as_posix()
        lines.append(f"\\input{{{header_path}}}")
    return "\n".join(lines) + "\n"


def _combine_header_paths(
    default_header: Optional[Any],
    override_header: Optional[Any],
    extra_headers: Sequence[str],
) -> List[str]:
    headers: List[str] = []

    for candidate in (default_header, override_header):
        if not candidate:
            continue
        if isinstance(candidate, (list, tuple, set)):
            headers.extend(str(item) for item in candidate)
        else:
            headers.append(str(candidate))

    headers.extend(extra_headers)
    return headers


def _emit_emoji_report(md_file: str, pdf_out: Path, options: EmojiOptions) -> None:
    if not options.report:
        return

    try:
        counts, table_md = emoji_report(md_file)
    except Exception as exc:  # pragma: no cover - keep build running
        logger.error("Emoji-Analyse fehlgeschlagen: %s", exc)
        return

    timestamp = datetime.now(timezone.utc)
    target_dir = Path(options.report_dir) if options.report_dir else pdf_out.parent
    target_dir.mkdir(parents=True, exist_ok=True)
    report_path = (
        target_dir / f"{pdf_out.stem}_emoji_report_{timestamp:%Y%m%d%H%M%S}.md"
    )

    lines = [
        "# Emoji usage report",
        "",
        f"* Source: {pdf_out.name}",
        f"* Generated: {timestamp.isoformat()}",
        "",
        table_md,
    ]
    if counts:
        lines.append("")
        lines.append("## Counts")
        for name, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"* {name}: {count}")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    logger.info("ℹ Emoji-Report geschrieben nach %s", report_path)


def _load_pandoc_overrides() -> Dict[str, Any]:
    inline = os.environ.get("ERDA_PANDOC_DEFAULTS_JSON")
    if inline:
        try:
            data = json.loads(inline)
            if isinstance(data, dict):
                return data
            logger.warning(
                "ERDA_PANDOC_DEFAULTS_JSON muss ein JSON-Objekt liefern, nicht %s.",
                type(data).__name__,
            )
        except json.JSONDecodeError as exc:
            logger.warning("Konnte ERDA_PANDOC_DEFAULTS_JSON nicht parsen: %s", exc)
    path = os.environ.get("ERDA_PANDOC_DEFAULTS_FILE")
    if path:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
            if isinstance(data, dict):
                return data
            logger.warning(
                "%s muss ein JSON-Objekt enthalten, nicht %s.",
                path,
                type(data).__name__,
            )
        except OSError as exc:
            logger.warning("Konnte %s nicht lesen: %s", path, exc)
        except json.JSONDecodeError as exc:
            logger.warning("Konnte %s nicht parsen: %s", path, exc)
    return {}


@lru_cache(maxsize=1)
def _get_pandoc_defaults() -> Dict[str, Any]:
    overrides = _load_pandoc_overrides()
    defaults: Dict[str, Any] = {
        "lua_filters": tuple(_DEFAULT_LUA_FILTERS),
        "metadata": {key: tuple(values) for key, values in _DEFAULT_METADATA.items()},
        "variables": dict(_DEFAULT_VARIABLES),
        "header_path": _DEFAULT_HEADER_PATH,
        "pdf_engine": "lualatex",
        "extra_args": _DEFAULT_EXTRA_ARGS,
    }
    if not overrides:
        return defaults
    if "lua_filters" in overrides:
        try:
            defaults["lua_filters"] = _merge_sequence(
                defaults["lua_filters"], overrides["lua_filters"]
            )
        except TypeError as exc:
            logger.warning("Pandoc-Filter-Override ungültig: %s", exc)
    if "metadata" in overrides:
        defaults["metadata"] = _merge_metadata(
            defaults["metadata"], overrides["metadata"]
        )
    if "variables" in overrides:
        defaults["variables"] = _merge_variables(
            defaults["variables"], overrides["variables"]
        )
    if "header_path" in overrides:
        header_override = overrides.get("header_path")
        if header_override is None:
            defaults["header_path"] = None
        else:
            defaults["header_path"] = str(header_override)
    if "pdf_engine" in overrides:
        engine_override = overrides.get("pdf_engine")
        defaults["pdf_engine"] = str(engine_override) if engine_override else ""
    if "extra_args" in overrides:
        try:
            defaults["extra_args"] = _merge_sequence(
                defaults["extra_args"], overrides["extra_args"]
            )
        except TypeError as exc:
            logger.warning("Pandoc-Argument-Override ungültig: %s", exc)
    return defaults


def _reset_pandoc_defaults_cache() -> None:
    _get_pandoc_defaults.cache_clear()


def _parse_semver(value: str) -> Tuple[int, int, int]:
    if not isinstance(value, str):
        raise ValueError("Manifest-Version muss ein String sein.")
    candidate = value.strip()
    match = _SEMVER_RE.match(candidate)
    if not match:
        raise ValueError(
            "Manifest-Version muss dem SemVer-Format MAJOR.MINOR.PATCH entsprechen."
        )
    major_s, minor_s, patch_s = match.groups()
    return int(major_s), int(minor_s), int(patch_s)


def _format_semver(parts: Tuple[int, int, int]) -> str:
    return ".".join(str(p) for p in parts)


def _resolve_publish_directory(base_dir: Path, value: Optional[str]) -> Path:
    target = Path(value) if value else Path("publish")
    if not target.is_absolute():
        target = (base_dir / target).resolve()
    return target


def _download(url: str, dest: str) -> None:
    import urllib.request

    logger.info("↓ Download %s -> %s", url, dest)
    pathlib.Path(os.path.dirname(dest)).mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as r, open(dest, "wb") as f:
        f.write(r.read())


# ----------------------------- YAML Helpers -------------------------------- #


def prepareYAML() -> None:
    """Installiert PyYAML, falls nicht vorhanden."""
    try:
        import yaml  # noqa: F401

        return
    except Exception:
        pass
    py = sys.executable or "python"
    _run([py, "-m", "pip", "install", "--upgrade", "pip"], check=False)
    _run([py, "-m", "pip", "install", "pyyaml"])


def find_publish_manifest(explicit: Optional[str] = None) -> str:
    if explicit and os.path.exists(explicit):
        return explicit
    for name in ("publish.yml", "publish.yaml"):
        if os.path.exists(name):
            return name
    logger.error("publish.yml|yaml nicht im Repo-Root gefunden.")
    sys.exit(2)


def _load_yaml(path: str) -> Dict[str, Any]:
    import yaml

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    version_value = data.get("version")
    if version_value is None:
        logger.error("Manifest-Version fehlt (Schlüssel 'version').")
        sys.exit(3)

    try:
        manifest_version = _parse_semver(str(version_value))
    except ValueError as exc:
        logger.error("Ungültige Manifest-Version '%s': %s", version_value, exc)
        sys.exit(3)

    if manifest_version[0] != _MANIFEST_VERSION_CURRENT[0]:
        logger.error(
            "Manifest-Major-Version %s wird nicht unterstützt (erwartet %d.x.x).",
            version_value,
            _MANIFEST_VERSION_CURRENT[0],
        )
        sys.exit(3)

    if manifest_version < _MANIFEST_VERSION_MIN:
        logger.error(
            "Manifest-Version %s ist zu alt. Minimal unterstützt: %s.",
            version_value,
            _format_semver(_MANIFEST_VERSION_MIN),
        )
        sys.exit(3)

    if manifest_version > _MANIFEST_VERSION_CURRENT:
        logger.warning(
            "Manifest-Version %s ist neuer als die getestete %s – versuche fortzufahren.",
            version_value,
            _format_semver(_MANIFEST_VERSION_CURRENT),
        )

    data["_manifest_version"] = manifest_version

    if "publish" not in data or not isinstance(data["publish"], list):
        logger.error("Ungültiges Manifest – Top-Level 'publish' (Liste) fehlt.")
        sys.exit(3)
    return data


def _save_yaml(path: str, data: Dict[str, Any]) -> None:
    import yaml

    serialisable = {k: v for k, v in data.items() if not str(k).startswith("_")}
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(serialisable, f, sort_keys=False, allow_unicode=True)


def _dedupe_preserve_order(values: Iterable[str]) -> List[str]:
    seen: set[str] = set()
    result: List[str] = []
    for raw in values:
        if not raw:
            continue
        candidate = os.path.normpath(str(raw))
        if candidate in seen:
            continue
        seen.add(candidate)
        result.append(candidate)
    return result


def _build_resource_paths(additional: Optional[Iterable[str]] = None) -> List[str]:
    defaults = [".", "assets", ".gitbook/assets"]
    if additional:
        defaults.extend(additional)
    return _dedupe_preserve_order(defaults)


def _parse_pdf_options(raw: Any) -> Dict[str, Any]:
    if not isinstance(raw, Mapping):
        return {}

    parsed: Dict[str, Any] = {}

    if "emoji_color" in raw:
        parsed["emoji_color"] = _as_bool(raw.get("emoji_color"))

    for key in ("main_font", "sans_font", "mono_font"):
        value = raw.get(key)
        if value is None:
            continue
        value_str = str(value).strip()
        if value_str:
            parsed[key] = value_str

    fallback_value = raw.get("mainfont_fallback") or raw.get("main_font_fallback")
    if fallback_value is not None:
        fallback_str = str(fallback_value).strip()
        if fallback_str:
            parsed["mainfont_fallback"] = fallback_str

    return parsed


def _build_variable_overrides(pdf_options: Mapping[str, Any]) -> Dict[str, str]:
    variables: Dict[str, str] = {}
    mapping = {
        "main_font": "mainfont",
        "sans_font": "sansfont",
        "mono_font": "monofont",
        "mainfont_fallback": "mainfontfallback",
    }
    for option_key, variable_key in mapping.items():
        value = pdf_options.get(option_key)
        if isinstance(value, str) and value.strip():
            variables[variable_key] = value.strip()
    return variables


def _resolve_asset_paths(
    assets: Iterable[Any], manifest_dir: Path, entry_path: Path
) -> List[str]:
    resolved: List[str] = []
    entry_base = entry_path if entry_path.is_dir() else entry_path.parent

    for asset in assets:
        if isinstance(asset, dict):
            path_value = asset.get("path")
        else:
            path_value = asset

        if not path_value:
            continue

        candidate = Path(str(path_value))

        if candidate.is_absolute():
            resolved.append(str(candidate))
            continue

        # Prefer manifest-relative resolution, fall back to the entry folder.
        manifest_candidate = (manifest_dir / candidate).resolve()
        if manifest_candidate.exists():
            resolved.append(str(manifest_candidate))
            continue

        entry_candidate = (entry_base / candidate).resolve()
        if entry_candidate.exists():
            resolved.append(str(entry_candidate))
            continue

        # As a last resort keep the manifest-relative absolute path even if it
        # does not exist yet (e.g. generated later in the pipeline).
        resolved.append(str(manifest_candidate))

    return _dedupe_preserve_order(resolved)


# --------------------------- Public API (A) -------------------------------- #


def get_publish_list(manifest_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """Return all manifest entries that should be built."""

    prepareYAML()
    mpath = find_publish_manifest(manifest_path)
    data = _load_yaml(mpath)
    manifest_version = data.get("_manifest_version")
    if isinstance(manifest_version, tuple):
        logger.info("Manifest-Version: %s", _format_semver(manifest_version))
    res: List[Dict[str, Any]] = []

    for entry in data.get("publish", []):
        if not _as_bool(entry.get("build"), default=False):
            continue

        path = entry.get("path")
        out = entry.get("out")
        if not path or not out:
            logger.warning("Überspringe Manifest-Eintrag ohne path/out: %s", entry)
            continue

        out_dir = entry.get("out_dir")
        result: Dict[str, Any] = {
            "path": str(path),
            "out": str(out),
            "out_dir": str(out_dir) if out_dir not in (None, "") else None,
            "out_format": str(entry.get("out_format", "pdf") or "pdf").lower(),
            "source_type": str(entry.get("source_type") or entry.get("type") or "")
            .lower()
            .strip(),
            "source_format": str(entry.get("source_format", "markdown") or "markdown")
            .lower()
            .strip(),
            "use_summary": _as_bool(entry.get("use_summary")),
            "use_book_json": _as_bool(entry.get("use_book_json")),
            "keep_combined": _as_bool(entry.get("keep_combined")),
            "summary_mode": entry.get("summary_mode"),
            "summary_order_manifest": entry.get("summary_order_manifest"),
            "summary_manual_marker": entry.get("summary_manual_marker"),
            "summary_appendices_last": entry.get("summary_appendices_last"),
            "reset_build_flag": _as_bool(entry.get("reset_build_flag")),
        }

        assets_value = entry.get("assets")
        assets: List[Dict[str, Any]] = []
        if isinstance(assets_value, list):
            for raw_asset in assets_value:
                if isinstance(raw_asset, dict):
                    path_value = raw_asset.get("path")
                    if not path_value:
                        continue
                    assets.append(
                        {
                            "path": str(path_value),
                            "type": str(raw_asset.get("type") or "").strip() or None,
                            "copy_to_output": _as_bool(raw_asset.get("copy_to_output")),
                        }
                    )
                elif raw_asset:
                    assets.append(
                        {
                            "path": str(raw_asset),
                            "type": None,
                            "copy_to_output": False,
                        }
                    )
        result["assets"] = assets
        result["pdf_options"] = _parse_pdf_options(entry.get("pdf_options"))
        res.append(result)

    return res


# ---------------------- Environment Prep (B / B.1) ------------------------- #


def prepare_publishing(no_apt: bool = False) -> None:
    """
    Installiert die System- und Python-Abhängigkeiten für den PDF-Build.
    - PyYAML (via prepareYAML)
    - Pandoc + LaTeX (apt-get auf Debian/Ubuntu)
    - OpenMoji Fonts (schwarz + farbig) + fc-cache
    - latex-emoji.lua (Pandoc Lua-Filter) für Legacy-Pipelines
    """
    prepareYAML()  # B.1

    # Pandoc vorhanden?
    have_pandoc = _which("pandoc") is not None
    have_lualatex = _which("lualatex") is not None

    if not (have_pandoc and have_lualatex):
        if no_apt:
            logger.warning(
                "pandoc/lualatex fehlen, --no-apt gesetzt. Bitte vorinstallieren."
            )
        elif _is_debian_like():
            sudo = _which("sudo")
            prefix = [sudo] if sudo else []
            _run(prefix + ["apt-get", "update"])
            _run(
                prefix
                + [
                    "apt-get",
                    "install",
                    "-y",
                    "pandoc",
                    "texlive-luatex",
                    "texlive-fonts-recommended",
                    "texlive-latex-extra",
                    "texlive-lang-cjk",
                    "fonts-dejavu-core",
                    "wget",
                ]
            )
        else:
            logger.warning(
                "Nicht-Debian System erkannt – installiere pandoc/LaTeX manuell."
            )

    # OpenMoji-Font & fc-cache
    font_dir = ".github/tools/publishing/fonts/truetype/openmoji"
    font_cache_refreshed = False

    def _maybe_refresh_font_cache() -> None:
        nonlocal font_cache_refreshed
        if font_cache_refreshed:
            return
        if _which("fc-cache"):
            _run(["fc-cache", "-f", "-v"], check=False)
            font_cache_refreshed = True

    def _register_font(font_path: str) -> None:
        if not font_path:
            return
        try:
            path_obj = Path(font_path)
            if not path_obj.exists():
                return
            user_font_dir = Path.home() / ".local" / "share" / "fonts"
            user_font_dir.mkdir(parents=True, exist_ok=True)
            target = user_font_dir / path_obj.name
            if not target.exists():
                shutil.copy2(path_obj, target)
            _maybe_refresh_font_cache()
        except Exception as exc:  # pragma: no cover - best effort only
            logger.warning("Konnte Font %s nicht registrieren: %s", font_path, exc)

    font_black = os.path.join(font_dir, "OpenMoji-black-glyf.ttf")
    if not os.path.exists(font_black):
        try:
            _ensure_dir(font_dir)
            url = "https://github.com/hfg-gmuend/openmoji/raw/master/font/OpenMoji-black-glyf/OpenMoji-black-glyf.ttf"
            _download(url, font_black)
            _maybe_refresh_font_cache()
        except Exception as e:
            logger.warning("Konnte OpenMoji black nicht installieren: %s", e)
    _register_font(font_black)

    font_color = os.path.join(font_dir, "OpenMoji-color-glyf_colr_0.ttf")
    if not os.path.exists(font_color):
        try:
            _ensure_dir(font_dir)
            url = "https://github.com/hfg-gmuend/openmoji/raw/master/font/OpenMoji-color-glyf_colr_0/OpenMoji-color-glyf_colr_0.ttf"
            _download(url, font_color)
            _maybe_refresh_font_cache()
        except Exception as e:
            logger.warning("Konnte OpenMoji color nicht installieren: %s", e)
    _register_font(font_color)

    # latex-emoji.lua Filter
    lua_dir = ".github/tools/publishing/lua"
    lua_path = os.path.join(lua_dir, "latex-emoji.lua")
    if not os.path.exists(lua_path):
        try:
            _ensure_dir(lua_dir)
            url = "https://gist.githubusercontent.com/zr-tex8r/a5410ad20ab291c390884b960c900537/raw/latex-emoji.lua"
            _download(url, lua_path)
        except Exception as e:
            logger.warning("Konnte latex-emoji.lua nicht laden: %s", e)


# --------------------------- PDF Build (C) --------------------------------- #


def _get_book_title(folder: str) -> Optional[str]:
    try:
        # Pfad zum book.json eine Ebene über dem Ordner
        book_json_path = pathlib.Path(folder).parent / "book.json"
        if not book_json_path.exists():
            return None
        with book_json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("title")
    except Exception:
        return None


def _run_pandoc(
    md_path: str,
    pdf_out: str,
    add_toc: bool = False,
    title: Optional[str] = None,
    resource_paths: Optional[List[str]] = None,
    *,
    lua_filters: Optional[Sequence[str]] = None,
    metadata: Optional[Dict[str, Sequence[str] | str]] = None,
    variables: Optional[Dict[str, str]] = None,
    header_path: Optional[str] = None,
    pdf_engine: Optional[str] = None,
    from_format: Optional[str] = None,
    to_format: Optional[str] = None,
    extra_args: Optional[Sequence[str]] = None,
    toc_depth: Optional[int] = None,
    emoji_options: Optional[EmojiOptions] = None,
) -> None:
    _ensure_dir(os.path.dirname(pdf_out))

    defaults = _get_pandoc_defaults()

    resource_path_values = _build_resource_paths(resource_paths)
    resource_path_arg = (
        os.pathsep.join(resource_path_values) if resource_path_values else None
    )

    filters = (
        list(lua_filters) if lua_filters is not None else list(defaults["lua_filters"])
    )

    metadata_map: Dict[str, List[str]] = {
        key: list(values) for key, values in defaults["metadata"].items()
    }
    if metadata:
        for key, value in metadata.items():
            if isinstance(value, Mapping):
                try:
                    metadata_map[key] = list(
                        _merge_sequence(tuple(metadata_map.get(key, [])), value)
                    )
                except TypeError as exc:
                    logger.warning(
                        "Metadaten-Override für %s konnte nicht angewendet werden: %s",
                        key,
                        exc,
                    )
            elif isinstance(value, (list, tuple, set)):
                metadata_map[key] = [str(v) for v in value]
            else:
                metadata_map[key] = [str(value)]

    variable_map: Dict[str, str] = dict(defaults["variables"])
    if variables:
        for key, value in variables.items():
            if value is None:
                variable_map.pop(key, None)
            else:
                variable_map[key] = str(value)

    fallback_override = variable_map.pop("mainfontfallback", None)
    if fallback_override is not None:
        fallback_override = str(fallback_override).strip() or None

    options = emoji_options or EmojiOptions()

    if options.color:
        metadata_map["color"] = ["true"]
    else:
        metadata_map["color"] = ["false"]

    pandoc_version = _get_pandoc_version()
    if pandoc_version:
        logger.info("ℹ Erkannte Pandoc-Version: %s", ".".join(map(str, pandoc_version)))
    else:
        logger.warning("⚠ Pandoc-Version konnte nicht bestimmt werden")

    emoji_font, needs_harfbuzz = _select_emoji_font(options.color)
    if emoji_font:
        metadata_map["emojifont"] = [emoji_font]

    main_font = variable_map.get("mainfont", _DEFAULT_VARIABLES["mainfont"])
    sans_font = variable_map.get(
        "sansfont", variable_map.get("mainfont", _DEFAULT_VARIABLES["sansfont"])
    )
    mono_font = variable_map.get(
        "monofont",
        variable_map.get("sansfont", _DEFAULT_VARIABLES["monofont"]),
    )

    supports_mainfont_fallback = bool(pandoc_version and pandoc_version >= (3, 1, 12))
    cli_fallback_spec: Optional[str] = None
    manual_fallback_spec: Optional[str] = None
    if fallback_override:
        if supports_mainfont_fallback:
            cli_fallback_spec = fallback_override
        else:
            manual_fallback_spec = fallback_override
        if not emoji_font:
            fallback_font_name = fallback_override.split(":", 1)[0].strip()
            if fallback_font_name:
                emoji_font = fallback_font_name
                metadata_map["emojifont"] = [fallback_font_name]
                if _needs_harfbuzz(fallback_override):
                    needs_harfbuzz = True
    elif emoji_font:
        fallback_spec = f"{emoji_font}{':mode=harf' if needs_harfbuzz else ''}"
        if supports_mainfont_fallback:
            cli_fallback_spec = fallback_spec
        else:
            manual_fallback_spec = fallback_spec

    header_defaults = defaults["header_path"]
    engine = pdf_engine if pdf_engine is not None else defaults["pdf_engine"]

    additional_args: List[str] = list(defaults["extra_args"])
    if extra_args:
        additional_args.extend(str(arg) for arg in extra_args)
    if cli_fallback_spec:
        additional_args.extend(["-V", f"mainfontfallback={cli_fallback_spec}"])

    header_override = header_path

    with tempfile.TemporaryDirectory() as temp_dir:
        header_file = Path(temp_dir) / "pandoc-fonts.tex"
        header_file.write_text(
            _build_font_header(
                main_font=main_font,
                sans_font=sans_font,
                mono_font=mono_font,
                emoji_font=emoji_font,
                include_mainfont=not supports_mainfont_fallback,
                needs_harfbuzz=needs_harfbuzz,
                manual_fallback_spec=manual_fallback_spec,
            ),
            encoding="utf-8",
        )

        header_args = _combine_header_paths(
            header_defaults, header_override, [str(header_file)]
        )

        cmd: List[str] = ["pandoc", md_path, "-o", pdf_out]
        if from_format:
            cmd.extend(["-f", from_format])
        if to_format:
            cmd.extend(["-t", to_format])
        if engine:
            cmd.extend(["--pdf-engine", engine])
        if resource_path_arg:
            cmd.extend(["--resource-path", resource_path_arg])
            logger.info("ℹ Pandoc resource paths: %s", resource_path_arg)
        for header in header_args:
            cmd.extend(["-H", header])
        for filter_path in filters:
            cmd.extend(["--lua-filter", filter_path])
        for key, values in metadata_map.items():
            for value in values:
                cmd.extend(["-M", f"{key}={value}"])
        for key, value in variable_map.items():
            cmd.extend(["--variable", f"{key}={value}"])
        if add_toc:
            cmd.append("--toc")
            if toc_depth is not None:
                cmd.extend(["--toc-depth", str(toc_depth)])
        if title:
            cmd.extend(["-V", f"title={title}"])
        cmd.extend(additional_args)

        _run(cmd)


def _extract_md_paths_from_summary(summary_path: Path, root_dir: Path) -> List[str]:
    if not summary_path.exists():
        return []

    resolved: "OrderedDict[str, None]" = OrderedDict()
    pattern = re.compile(r"\(([^)]+\.(?:md|markdown))\)", re.IGNORECASE)

    try:
        with summary_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                for match in pattern.findall(line):
                    target = match.split("#", 1)[0].strip()
                    if not target or target.startswith(("http://", "https://")):
                        continue
                    candidate = (root_dir / target).resolve()
                    if candidate.suffix.lower() not in {".md", ".markdown"}:
                        continue
                    resolved[str(candidate)] = None
    except Exception as exc:
        logger.warning("Konnte SUMMARY in %s nicht lesen: %s", summary_path, exc)
        return []

    return list(resolved.keys())


def _iter_summary_candidates(folder: Path, summary_path: Optional[Path]) -> List[Path]:
    candidates: List[Path] = []
    seen: set[Path] = set()

    if summary_path is not None:
        resolved = summary_path.resolve()
        candidates.append(resolved)
        seen.add(resolved)

    for name in ("SUMMARY.md", "summary.md"):
        candidate = (folder / name).resolve()
        if candidate not in seen:
            candidates.append(candidate)
            seen.add(candidate)

    return candidates


def _collect_folder_md(
    folder: str,
    use_summary: bool,
    *,
    summary_layout: Optional[SummaryContext] = None,
) -> List[str]:
    folder_path = Path(folder).resolve()
    root_dir = summary_layout.root_dir if summary_layout else folder_path
    summary_candidates = _iter_summary_candidates(
        folder_path, summary_layout.summary_path if summary_layout else None
    )

    if use_summary:
        for candidate in summary_candidates:
            md_files = _extract_md_paths_from_summary(candidate, root_dir)
            logger.info(
                "ℹ %d Markdown-Dateien aus %s gelesen.",
                len(md_files),
                candidate,
            )
            if md_files:
                return md_files
    # Fallback: alle .md rekursiv, README bevorzugt
    md_files: List[str] = []
    for root, _, files in os.walk(folder_path):
        for fname in sorted(files):
            if fname.lower().endswith((".md", ".markdown")):
                full = os.path.join(root, fname)
                if fname.lower() == "readme.md":
                    md_files.insert(0, full)
                else:
                    md_files.append(full)
    logger.info("ℹ %d Markdown-Dateien in %s gefunden.", len(md_files), folder_path)
    return md_files


def convert_a_file(
    md_file: str,
    pdf_out: str,
    keep_converted_markdown: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
    resource_paths: Optional[List[str]] = None,
    emoji_options: Optional[EmojiOptions] = None,
    variables: Optional[Dict[str, str]] = None,
) -> None:
    logger.info(
        "========================================================================"
    )
    logger.info("Convert a new single file")
    logger.info(
        "------------------------------------------------------------------------"
    )
    logger.info("File                    : %s", md_file)
    logger.info("PDF OUT                 : %s", pdf_out)
    logger.info("Keep Converted Markdown : %s", keep_converted_markdown)
    logger.info("Publish Dir             : %s", publish_dir)
    logger.info("Paper Format            : %s", paper_format)
    if resource_paths:
        logger.info("Pandoc resource paths   : %s", resource_paths)

    # preprocess for wide content (tables, images), will change page geometry
    processed = process(md_file, paper_format=paper_format)
    logger.info("%s: Nach Preprocessing %d Zeichen.", md_file, len(processed))
    # normalize for pandoc
    normalized = normalize_md(processed)
    logger.info("%s: Nach Normalisierung %d Zeichen.", md_file, len(normalized))
    # add geometry package
    content = add_geometry_package(
        normalized,
        paper_format=paper_format,
    )
    with tempfile.NamedTemporaryFile(
        "w", suffix=".md", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(content)
        tmp_md = tmp.name
    try:
        options = emoji_options or EmojiOptions()
        _emit_emoji_report(tmp_md, Path(pdf_out), options)
        _run_pandoc(
            tmp_md,
            pdf_out,
            resource_paths=resource_paths,
            emoji_options=options,
            variables=variables,
        )
    finally:
        try:
            if not keep_converted_markdown:
                os.unlink(tmp_md)
            else:
                converted_md_path = pdf_out.replace(".pdf", ".md")
                logger.info(
                    "Keeping converted markdown in %s",
                    converted_md_path,
                )
                print(
                    "Keeping converted markdown in " + converted_md_path,
                )
                shutil.move(str(tmp_md), str(converted_md_path))
        except OSError as e:
            logger.error("Failed to operate on converted markdown caused by %s", e)
            pass
        logger.info(
            "------------------------------------------------------------------------"
        )
        logger.info("%s", content)
        logger.info(
            "========================================================================"
        )


def convert_a_folder(
    folder: str,
    pdf_out: str,
    use_summary: bool = True,
    keep_converted_markdown: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
    summary_layout: Optional[SummaryContext] = None,
    resource_paths: Optional[List[str]] = None,
    emoji_options: Optional[EmojiOptions] = None,
    variables: Optional[Dict[str, str]] = None,
) -> None:

    logger.info(
        "========================================================================"
    )
    logger.info("Convert a folder")
    logger.info(
        "------------------------------------------------------------------------"
    )
    logger.info("Folder                  : %s", folder)
    logger.info("PDF OUT                 : %s", pdf_out)
    logger.info("Keep Converted Markdown : %s", keep_converted_markdown)
    logger.info("Publish Dir             : %s", publish_dir)
    logger.info("Paper Format            : %s", paper_format)
    if resource_paths:
        logger.info("Pandoc resource paths   : %s", resource_paths)

    md_files = _collect_folder_md(
        folder, use_summary=use_summary, summary_layout=summary_layout
    )
    if not md_files:
        logger.info("ℹ Keine Markdown-Dateien in %s – übersprungen.", folder)
        raise Exception(f"No markdown files found in {folder}")
    combined = add_geometry_package(
        combine_markdown(md_files, paper_format=paper_format), paper_format=paper_format
    )
    with tempfile.NamedTemporaryFile(
        "w", suffix=".md", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(combined)
        tmp_md = tmp.name
    try:
        title = _get_book_title(folder)
        if title:
            logger.info("ℹ Buch-Titel aus book.json: %s", title)
        else:
            logger.info("ℹ Kein Buch-Titel")
        options = emoji_options or EmojiOptions()
        _emit_emoji_report(tmp_md, Path(pdf_out), options)
        _run_pandoc(
            tmp_md,
            pdf_out,
            add_toc=True,
            title=title,
            resource_paths=resource_paths,
            emoji_options=options,
            variables=variables,
        )
    finally:
        try:
            if not keep_converted_markdown:
                os.unlink(tmp_md)
            else:
                converted_markdown = pdf_out.replace(".pdf", ".md")
                logger.info("ℹ Behalte kombiniertes Markdown in %s", converted_markdown)
                _ensure_dir(publish_dir)
                shutil.move(str(tmp_md), str(converted_markdown))
        except OSError as e:
            logger.error("Failed to operate on converted markdown caused by %s", e)
            pass
        logger.info(
            "------------------------------------------------------------------------"
        )
        logger.info("%s", combined)
        logger.info(
            "========================================================================"
        )


def build_pdf(
    path: str | Path,
    out: str,
    typ: str,
    use_summary: bool = False,
    use_book_json: bool = False,
    keep_combined: bool = False,
    publish_dir: str = "publish",
    paper_format: str = "a4",
    summary_mode: Optional[str] = None,
    summary_order_manifest: Optional[Path] = None,
    summary_manual_marker: Optional[str] = DEFAULT_MANUAL_MARKER,
    summary_appendices_last: bool = False,
    resource_paths: Optional[List[str]] = None,
    emoji_options: Optional[EmojiOptions] = None,
    variables: Optional[Dict[str, str]] = None,
) -> Tuple[bool, Optional[str]]:
    """
    Baut ein PDF gemäß Typ ('file'/'folder').
    Gibt True bei Erfolg zurück und False bei Fehlern plus eine detaillierte Fehlernachricht.
    """
    publish_path = Path(publish_dir).resolve()
    _ensure_dir(str(publish_path))
    pdf_out = publish_path / out
    path_obj = Path(path).resolve()

    logger.info("✔ Building %s from %s (type=%s)", pdf_out, path_obj, typ)

    # Typ autodetektion, falls leer/ungewohnt
    _typ = (typ or "").lower().strip()
    if not _typ or _typ not in {"file", "folder"}:
        if path_obj.is_dir():
            _typ = "folder"
        else:
            _typ = "file"

    try:
        if _typ == "file":
            # _convert_single_file(
            #    path,
            #    pdf_out,
            #    paper_format=paper_format,
            # )
            convert_a_file(
                str(path_obj),
                str(pdf_out),
                keep_converted_markdown=True,
                publish_dir=str(publish_path),
                paper_format=paper_format,
                resource_paths=resource_paths,
                emoji_options=emoji_options,
                variables=variables,
            )
        elif _typ == "folder":
            summary_layout: Optional[SummaryContext] = None
            needs_summary_refresh = (
                use_book_json
                or summary_mode is not None
                or summary_order_manifest is not None
                or (
                    summary_manual_marker is not None
                    and summary_manual_marker != DEFAULT_MANUAL_MARKER
                )
            )
            if needs_summary_refresh:
                try:
                    summary_layout = get_summary_layout(path_obj)
                    ensure_clean_summary(
                        summary_layout.base_dir,
                        run_git=False,
                        summary_mode=summary_mode,
                        summary_order_manifest=summary_order_manifest,
                        manual_marker=summary_manual_marker,
                        summary_appendices_last=summary_appendices_last,
                    )
                except Exception as exc:  # pragma: no cover - best effort logging
                    logger.warning(
                        "Konnte SUMMARY via book.json nicht aktualisieren: %s", exc
                    )
            convert_a_folder(
                str(path_obj),
                str(pdf_out),
                use_summary=use_summary or use_book_json or summary_layout is not None,
                keep_converted_markdown=keep_combined,
                publish_dir=str(publish_path),
                paper_format=paper_format,
                summary_layout=summary_layout,
                resource_paths=resource_paths,
                emoji_options=emoji_options,
                variables=variables,
            )
        else:
            logger.warning("⚠ Unbekannter type='%s' – übersprungen.", typ)
            return False, f"Unknown type='{typ}' - skipped"
        return True, None
    except subprocess.CalledProcessError as e:
        logger.error("Pandoc/LaTeX Build fehlgeschlagen (rc=%s).", e.returncode)
        return False, str(e) + "\n" + (e.stdout or "") + "\n" + (e.stderr or "")
    except Exception as e:
        logger.error("Build-Fehler: %s", e)
        stdout = getattr(e, "stdout", "")
        stderr = getattr(e, "stderr", "")
        return False, f"{e}\n{stdout}\n{stderr}"


# -------------------------------- Main (D) --------------------------------- #


def _write_github_outputs(built: List[str], failed: List[str], manifest: str) -> None:
    gh_out = os.getenv("GITHUB_OUTPUT")
    if gh_out:
        try:
            with open(gh_out, "a", encoding="utf-8") as f:
                f.write(f"built_count={len(built)}\n")
                f.write(f"built_files={json.dumps(built, ensure_ascii=False)}\n")
                f.write(f"failed_files={json.dumps(failed, ensure_ascii=False)}\n")
                f.write(f"manifest={manifest}\n")
        except Exception as e:
            logger.warning("Konnte GITHUB_OUTPUT nicht schreiben: %s", e)


def main() -> None:
    logger.info("Selective Publisher gestartet: argv=%s", sys.argv)
    ap = argparse.ArgumentParser(description="Selective publisher für publish.yml")
    ap.add_argument("--manifest", help="Pfad zu publish.yml|yaml (Default: Root)")
    ap.add_argument(
        "--no-apt", action="store_true", help="Keine apt-Installation versuchen"
    )
    ap.add_argument(
        "--only-prepare",
        action="store_true",
        help="Nur Umgebung vorbereiten und beenden",
    )
    ap.add_argument(
        "--reset-script",
        default=".github/tools/publishing/reset-publish-flag.py",
        help="Pfad zum Reset-Tool",
    )
    ap.add_argument(
        "--paper-format",
        help="Enable landscape orientation for wide content",
        default="a4",
    )
    ap.add_argument(
        "--publish-dir",
        help="The directory to publish to.",
        default="publish",
    )
    ap.add_argument(
        "--emoji-color",
        dest="emoji_color",
        action="store_true",
        default=True,
        help="Render emojis with the colour OpenMoji font when available.",
    )
    ap.add_argument(
        "--no-emoji-color",
        dest="emoji_color",
        action="store_false",
        help="Disable colour emoji rendering.",
    )
    ap.add_argument(
        "--emoji-report",
        action="store_true",
        help="Write a usage report for emojis encountered during the build.",
    )
    ap.add_argument(
        "--emoji-report-dir",
        help="Optional output directory for emoji reports (defaults to publish dir).",
    )
    args = ap.parse_args()

    if args.only_prepare:
        # B.1 + B
        prepare_publishing(no_apt=args.no_apt)
        logger.info("✔ Umgebung vorbereitet. (only-prepare)")
        return

    # prepareYAML()  # B.1
    prepareYAML()
    # get manifest publish list (A)
    manifest = find_publish_manifest(args.manifest)
    targets = get_publish_list(manifest)

    if not targets:
        logger.info("ℹ Keine zu publizierenden Einträge (build: true).")
        _write_github_outputs([], [], manifest)
        return

    logger.info("ℹ %d zu publizierende Einträge gefunden.", len(targets))
    # prepare huge environment (B)
    prepare_publishing(no_apt=args.no_apt)
    built: List[str] = []
    failed: List[str] = []

    manifest_path = Path(manifest).resolve()
    manifest_dir = manifest_path.parent
    default_publish_dir = _resolve_publish_directory(manifest_dir, args.publish_dir)

    emoji_report_dir = (
        Path(args.emoji_report_dir).resolve() if args.emoji_report_dir else None
    )
    emoji_options = EmojiOptions(
        color=args.emoji_color,
        report=args.emoji_report,
        report_dir=emoji_report_dir,
    )

    # C + Reset je nach Erfolg
    for entry in targets:
        original_path = entry["path"]
        path = Path(original_path)
        if not path.is_absolute():
            path = (manifest_dir / path).resolve()
        out = entry["out"]
        out_format = entry.get("out_format", "pdf")
        if out_format.lower() != "pdf":
            msg = f"Unsupported out_format='{out_format}'"
            logger.warning("⚠ %s – Eintrag wird übersprungen.", msg)
            failed.append(f"{out}: {msg}")
            continue

        typ = entry.get("source_type") or entry.get("type", "")
        publish_base = entry.get("out_dir")
        publish_dir_path = (
            _resolve_publish_directory(manifest_dir, publish_base)
            if publish_base
            else default_publish_dir
        )
        summary_mode = entry.get("summary_mode")
        if summary_mode is not None:
            summary_mode = str(summary_mode).strip() or None
        manifest_value = entry.get("summary_order_manifest")
        summary_manifest_path: Optional[Path]
        if manifest_value:
            summary_manifest_path = Path(str(manifest_value))
            if not summary_manifest_path.is_absolute():
                summary_manifest_path = (manifest_dir / summary_manifest_path).resolve()
        else:
            summary_manifest_path = None
        summary_manual_marker_value = entry.get("summary_manual_marker")
        if summary_manual_marker_value is None:
            summary_manual_marker = DEFAULT_MANUAL_MARKER
        else:
            summary_manual_marker = str(summary_manual_marker_value)

        assets_for_entry = entry.get("assets") or []
        resolved_resource_paths = _resolve_asset_paths(
            assets_for_entry, manifest_dir, path
        )

        pdf_options = entry.get("pdf_options") or {}
        variable_overrides = (
            _build_variable_overrides(pdf_options) if pdf_options else {}
        )
        if "emoji_color" in pdf_options:
            entry_emoji_options = EmojiOptions(
                color=bool(pdf_options["emoji_color"]),
                report=emoji_options.report,
                report_dir=emoji_options.report_dir,
            )
        else:
            entry_emoji_options = emoji_options

        ok, msg = build_pdf(
            path=path,
            out=out,
            typ=typ,
            use_summary=entry["use_summary"],
            use_book_json=entry.get("use_book_json", False),
            keep_combined=entry["keep_combined"],
            paper_format=args.paper_format,
            publish_dir=str(publish_dir_path),
            summary_mode=summary_mode,
            summary_order_manifest=summary_manifest_path,
            summary_manual_marker=summary_manual_marker,
            summary_appendices_last=_as_bool(entry.get("summary_appendices_last")),
            resource_paths=resolved_resource_paths,
            emoji_options=entry_emoji_options,
            variables=variable_overrides or None,
        )
        if ok:
            built.append(str((publish_dir_path / out).resolve()))
            # Reset publish-Flag (D) – nur bei Erfolg und wenn reset_build_flag true ist
            if entry.get("reset_build_flag", False):
                reset_tool = args.reset_script
                if os.path.exists(reset_tool):
                    try:
                        _run(
                            [
                                sys.executable or "python",
                                reset_tool,
                                "--path",
                                str(path),
                                "--multi",
                            ],
                            check=True,
                        )
                    except Exception as e:
                        logger.warning(
                            "Konnte reset-publish-flag nicht aufrufen: %s", e
                        )
                else:
                    # Fallback: direkt im Manifest auf false setzen
                    try:
                        data = _load_yaml(manifest)
                        for e in data.get("publish", []):
                            if str(e.get("path")) == original_path:
                                e["build"] = False
                        _save_yaml(manifest, data)
                    except Exception as e:
                        logger.warning(
                            "Konnte Manifest-Fallback-Reset nicht schreiben: %s", e
                        )
        else:
            failed.append(
                str((publish_dir_path / out).resolve()) + (f": {msg}" if msg else "")
            )

    # Outputs
    logger.info("::group::publisher.outputs")
    logger.info(
        json.dumps(
            {
                "built_count": len(built),
                "built_files": built,
                "failed_files": failed,
                "manifest": manifest,
            },
            ensure_ascii=False,
        )
    )
    logger.info("::endgroup::")

    _write_github_outputs(built, failed, manifest)

    # Exit-Code, wenn Builds fehlgeschlagen sind (aber nicht hart abbrechen, wenn ein Teil ok ist)
    if built and not failed:
        sys.exit(0)
    elif failed and not built:
        sys.exit(1)
    else:
        # Teilweise erfolgreich
        sys.exit(0)


if __name__ == "__main__":
    main()
