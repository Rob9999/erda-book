"""High-level orchestrator that mirrors the GitHub workflow chain.

The module glues together the existing helper scripts so the full publishing
pipeline can run either locally or inside GitHub Actions.  Profiles configured
in ``publish.yml`` decide which steps are executed and whether a pre-built
Docker image from GHCR should be used.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import shlex
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import Iterable, Mapping, MutableMapping, Sequence

import yaml

from tools.logging_config import get_logger

LOGGER = get_logger(__name__)

_DEFAULT_STEPS = (
    "check_if_to_publish",
    "ensure_readme",
    "update_citation",
    "converter",
    "engineering-document-formatter",
    "publisher",
)

_SKIP_DIRS = {
    ".git",
    ".github",
    ".venv",
    "__pycache__",
    "node_modules",
    "simulations",
}

README_FILENAMES = ("README.md", "readme.md", "Readme.md")


@dataclass(frozen=True)
class DockerSettings:
    """Docker related configuration for a profile."""

    use_registry: bool
    image: str | None
    cache: bool


@dataclass(frozen=True)
class OrchestratorProfile:
    """Resolved profile information loaded from ``publish.yml``."""

    name: str
    steps: tuple[str, ...]
    docker: DockerSettings
    description: str | None = None
    env: Mapping[str, str] | None = None


@dataclass(frozen=True)
class OrchestratorConfig:
    """Immutable runtime options for the orchestrator."""

    root: Path
    manifest: Path
    profile: OrchestratorProfile
    repo_visibility: str
    repository: str | None
    commit: str | None
    base: str | None
    reset_others: bool
    publisher_args: tuple[str, ...]
    dry_run: bool
    steps_override: tuple[str, ...] | None = None


class RuntimeContext:
    """Mutable helper carrying derived runtime values."""

    def __init__(self, config: OrchestratorConfig) -> None:
        self.config = config
        self.root = config.root
        self.python = sys.executable or "python"
        self.tools_dir = self.root / ".github" / "tools"
        self.python_path = str(self.tools_dir)

    def env(self, extra: Mapping[str, str] | None = None) -> MutableMapping[str, str]:
        env: MutableMapping[str, str] = os.environ.copy()
        env.setdefault("PYTHONPATH", self.python_path)
        if self.config.repository:
            env.setdefault("GITHUB_REPOSITORY", self.config.repository)
        env.setdefault("ORCHESTRATOR_PROFILE", self.config.profile.name)
        env.setdefault("ORCHESTRATOR_REPO_VISIBILITY", self.config.repo_visibility)
        if self.config.profile.env:
            env.update(self.config.profile.env)
        if extra:
            env.update(extra)
        return env

    def run_command(
        self,
        cmd: Sequence[str],
        *,
        cwd: Path | None = None,
        env: Mapping[str, str] | None = None,
        check: bool = True,
    ) -> subprocess.CompletedProcess:
        display = " ".join(shlex.quote(part) for part in cmd)
        LOGGER.info("→ %s", display)
        if self.config.dry_run:
            LOGGER.info("Dry-run aktiv – Befehl wird übersprungen.")
            return subprocess.CompletedProcess(cmd, 0)
        result = subprocess.run(
            list(cmd),
            cwd=str(cwd or self.root),
            env=self.env(env),
            check=check,
            text=True,
        )
        return result

    def git_last_commit_date(self, path: Path) -> str:
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--format=%cs", str(path.relative_to(self.root))],
                cwd=str(self.root),
                capture_output=True,
                text=True,
                check=False,
            )
            value = (result.stdout or "").strip()
            return value or "1970-01-01"
        except Exception:
            return "1970-01-01"


def _as_bool(value: object, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        text = value.strip().lower()
        return text in {"1", "true", "yes", "on", "y"}
    return default


def _expand_template(value: object, variables: Mapping[str, str]) -> object:
    if isinstance(value, str):
        return Template(value).safe_substitute(variables)
    if isinstance(value, list):
        return type(value)(_expand_template(v, variables) for v in value)
    if isinstance(value, dict):
        return {k: _expand_template(v, variables) for k, v in value.items()}
    return value


def _load_manifest(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return data


def _resolve_profile(
    manifest: dict,
    profile_name: str,
    variables: Mapping[str, str],
) -> OrchestratorProfile:
    profiles = manifest.get("profiles") or {}
    if not profiles:
        docker = DockerSettings(use_registry=False, image=None, cache=False)
        return OrchestratorProfile(
            name="default",
            steps=_DEFAULT_STEPS,
            docker=docker,
            description=None,
            env=None,
        )

    raw = profiles.get(profile_name)
    if raw is None:
        if profile_name != "default" and "default" not in profiles:
            available = ", ".join(sorted(profiles)) or "<none>"
            raise KeyError(
                f"Profil '{profile_name}' nicht gefunden. Verfügbare Profile: {available}"
            )
        LOGGER.warning(
            "Profil '%s' nicht gefunden – fallback auf 'default'", profile_name
        )
        raw = profiles.get("default")
        profile_name = "default"

    raw = _expand_template(raw or {}, variables)
    steps_raw = raw.get("steps")
    if not steps_raw:
        steps = _DEFAULT_STEPS
    else:
        steps = tuple(str(step).strip() for step in steps_raw if str(step).strip())

    docker_raw = raw.get("docker") or {}
    docker = DockerSettings(
        use_registry=_as_bool(docker_raw.get("use_registry")),
        image=str(docker_raw.get("image")) if docker_raw.get("image") else None,
        cache=_as_bool(docker_raw.get("cache")),
    )

    env = raw.get("env")
    if env and not isinstance(env, Mapping):
        raise TypeError("Profile 'env' erwartet ein Mapping")

    description = raw.get("description")
    if description is not None:
        description = str(description)

    return OrchestratorProfile(
        name=profile_name,
        steps=steps,
        docker=docker,
        description=description,
        env=env,
    )


def _detect_repo_visibility(explicit: str) -> str:
    if explicit != "auto":
        return explicit

    override = os.getenv("ORCHESTRATOR_REPO_VISIBILITY")
    if override:
        return override

    event_path = os.getenv("GITHUB_EVENT_PATH")
    if event_path and Path(event_path).is_file():
        try:
            payload = json.loads(Path(event_path).read_text(encoding="utf-8"))
            repo_info = payload.get("repository") or {}
            if repo_info.get("private"):
                return "private"
            return "public"
        except Exception:
            LOGGER.debug("Konnte GITHUB_EVENT_PATH nicht auswerten", exc_info=True)

    return "public"


def _resolve_paths(root: Path, manifest: Path | None) -> tuple[Path, Path]:
    repo_root = root.resolve()
    if manifest is None:
        for candidate in (repo_root / "publish.yml", repo_root / "publish.yaml"):
            if candidate.exists():
                return repo_root, candidate.resolve()
        raise FileNotFoundError("publish.yml oder publish.yaml nicht gefunden")
    manifest_path = manifest if manifest.is_absolute() else (repo_root / manifest)
    return repo_root, manifest_path.resolve()


def _split_publisher_args(values: Iterable[str] | None) -> tuple[str, ...]:
    if not values:
        return ()
    result: list[str] = []
    for value in values:
        if not value:
            continue
        for part in shlex.split(value):
            result.append(part)
    return tuple(result)


def build_config(args: argparse.Namespace) -> OrchestratorConfig:
    root, manifest = _resolve_paths(args.root, args.manifest)
    repository = args.repository or os.getenv("GITHUB_REPOSITORY")
    variables = {
        "repo": repository or "",
        "profile": args.profile,
        "visibility": args.repo_visibility,
    }
    manifest_data = _load_manifest(manifest)
    profile = _resolve_profile(manifest_data, args.profile, variables)
    repo_visibility = _detect_repo_visibility(args.repo_visibility)
    publisher_args = _split_publisher_args(args.publisher_arg)
    steps_override = tuple(args.step) if args.step else None
    return OrchestratorConfig(
        root=root,
        manifest=manifest,
        profile=profile,
        repo_visibility=repo_visibility,
        repository=repository,
        commit=args.commit,
        base=args.base,
        reset_others=args.reset_others,
        publisher_args=publisher_args,
        dry_run=args.dry_run,
        steps_override=steps_override,
    )


def run(config: OrchestratorConfig) -> None:
    ctx = RuntimeContext(config)
    steps = config.steps_override or config.profile.steps
    LOGGER.info(
        "Starte Orchestrator-Profil '%s' mit Schritten: %s",
        config.profile.name,
        ", ".join(steps) or "<none>",
    )
    for step in steps:
        handler = STEP_HANDLERS.get(step)
        if handler is None:
            raise KeyError(f"Unbekannter Schritt: {step}")
        LOGGER.info("Schritt '%s' starten", step)
        handler(ctx)
    LOGGER.info("Orchestrator abgeschlossen")


def _step_check_if_to_publish(ctx: RuntimeContext) -> None:
    script = ctx.tools_dir / "publishing" / "set_publish_flag.py"
    if not script.exists():
        LOGGER.warning("set_publish_flag.py nicht gefunden – Schritt wird übersprungen")
        return
    cmd = [
        ctx.python,
        str(script),
        "--publish-file",
        str(ctx.config.manifest),
    ]
    if ctx.config.commit:
        cmd.extend(["--commit", ctx.config.commit])
    if ctx.config.base:
        cmd.extend(["--base", ctx.config.base])
    if ctx.config.reset_others:
        cmd.append("--reset-others")
    ctx.run_command(cmd)


def _step_ensure_readme(ctx: RuntimeContext) -> None:
    created: list[Path] = []
    for directory in ctx.root.rglob("*"):
        if not directory.is_dir():
            continue
        rel = directory.relative_to(ctx.root)
        if any(part.startswith(".") and part != "." for part in rel.parts):
            continue
        if any(part in _SKIP_DIRS for part in rel.parts if part):
            continue
        if rel == Path("."):
            continue
        if any((directory / name).exists() for name in README_FILENAMES):
            continue
        target = directory / "readme.md"
        created.append(target)
        if ctx.config.dry_run:
            continue
        target.write_text(f"# {directory.name}\n", encoding="utf-8")
    if created:
        LOGGER.info("%d neue readme.md-Dateien erstellt", len(created))
    else:
        LOGGER.info("Alle Verzeichnisse besitzen bereits eine readme.md")


def _step_update_citation(ctx: RuntimeContext) -> None:
    citation = ctx.root / "docs" / "public" / "publish" / "citation.cff"
    if not citation.exists():
        LOGGER.info("Keine citation.cff gefunden – Schritt wird übersprungen")
        return
    today = _dt.datetime.now(tz=_dt.UTC).date().isoformat()
    version_line = f"version: The_zenodo_release_on_{today}"
    date_line = f"date-released: '{today}'"
    text = citation.read_text(encoding="utf-8").splitlines()
    changed = False
    for idx, line in enumerate(text):
        if line.startswith("version:") and line != version_line:
            text[idx] = version_line
            changed = True
        elif line.startswith("date-released:") and line != date_line:
            text[idx] = date_line
            changed = True
    if not changed:
        LOGGER.info("citation.cff ist bereits aktuell")
        return
    LOGGER.info("Aktualisiere citation.cff auf %s", today)
    if ctx.config.dry_run:
        return
    citation.write_text("\n".join(text) + "\n", encoding="utf-8")


def _step_converter(ctx: RuntimeContext) -> None:
    dump_script = ctx.tools_dir / "publishing" / "dump_publish.py"
    convert_script = ctx.tools_dir / "converter" / "convert_assets.py"
    if not dump_script.exists() or not convert_script.exists():
        LOGGER.warning("Konverter-Skripte nicht gefunden – Schritt wird übersprungen")
        return
    ctx.run_command(
        [
            ctx.python,
            str(dump_script),
            "--manifest",
            str(ctx.config.manifest),
        ]
    )
    # Run the converter as a module (so relative imports inside it work).
    # Pass the manifest path so the converter computes PUBLIC from the manifest
    # parent directory rather than a hardwired docs/public path.
    ctx.run_command(
        [
            ctx.python,
            "-m",
            "tools.converter.convert_assets",
            "--manifest",
            str(ctx.config.manifest),
        ]
    )


_TEMPLATE_ORDER = (
    ("id", '""'),
    ("title", '""'),
    ("version", "v0.0.0"),
    ("state", "DRAFT"),
    ("evolution", '""'),
    ("discipline", '""'),
    ("system", "[]"),
    ("system_id", "[]"),
    ("seq", "[]"),
    ("owner", '""'),
    ("reviewers", "[]"),
    ("source_of_truth", "false"),
    ("supersedes", "null"),
    ("superseded_by", "null"),
    ("rfc_links", "[]"),
    ("adr_links", "[]"),
    ("cr_links", "[]"),
    ("date", "1970-01-01"),
    ("lang", "EN"),
)
_TEMPLATE_MAP = dict(_TEMPLATE_ORDER)


def _ensure_yaml_header(path: Path, ctx: RuntimeContext) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = False
    if not lines:
        lines = []
    if not lines or lines[0].strip() != "---":
        date = ctx.git_last_commit_date(path)
        header = (
            ["---"]
            + [
                f"{key}: {date if key == 'date' else default}"
                for key, default in _TEMPLATE_ORDER
            ]
            + ["---", ""]
        )
        lines = header + lines
        changed = True
    else:
        end_idx = None
        for idx, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                end_idx = idx
                break
        if end_idx is None:
            lines.append("---")
            lines.append("")
            end_idx = len(lines) - 2
            changed = True
        header_lines = lines[1:end_idx]
        existing = {
            entry.split(":", 1)[0].strip() for entry in header_lines if ":" in entry
        }
        missing = [key for key, _ in _TEMPLATE_ORDER if key not in existing]
        if missing:
            date = ctx.git_last_commit_date(path)
            insert = [
                f"{key}: {date if key == 'date' else _TEMPLATE_MAP[key]}"
                for key in missing
            ]
            lines = (
                [lines[0]]
                + header_lines
                + insert
                + [lines[end_idx]]
                + lines[end_idx + 1 :]
            )
            changed = True
    if changed and not ctx.config.dry_run:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def _step_engineering_docs(ctx: RuntimeContext) -> None:
    changed_files: list[Path] = []
    for path in ctx.root.rglob("*.md"):
        rel = path.relative_to(ctx.root)
        if any(part in _SKIP_DIRS for part in rel.parts):
            continue
        if path.name.lower() == "readme.md":
            continue
        if _ensure_yaml_header(path, ctx):
            changed_files.append(path)
    if changed_files:
        LOGGER.info("YAML-Header für %d Dateien aktualisiert", len(changed_files))
    else:
        LOGGER.info("Alle Engineering-Dokumente besitzen gültige Header")


def _step_publisher(ctx: RuntimeContext) -> None:
    pipeline = ctx.tools_dir / "publishing" / "pipeline.py"
    if not pipeline.exists():
        LOGGER.warning("pipeline.py nicht gefunden – Schritt wird übersprungen")
        return
    cmd: list[str] = [
        ctx.python,
        str(pipeline),
        "--root",
        str(ctx.root),
        "--manifest",
        str(ctx.config.manifest),
    ]
    if ctx.config.commit:
        cmd.extend(["--commit", ctx.config.commit])
    if ctx.config.base:
        cmd.extend(["--base", ctx.config.base])
    if ctx.config.reset_others:
        cmd.append("--reset-others")
    for arg in ctx.config.publisher_args:
        cmd.extend(["--publisher-args", arg])
    ctx.run_command(cmd)


STEP_HANDLERS = {
    "check_if_to_publish": _step_check_if_to_publish,
    "ensure_readme": _step_ensure_readme,
    "update_citation": _step_update_citation,
    "converter": _step_converter,
    "engineering-document-formatter": _step_engineering_docs,
    "publisher": _step_publisher,
}


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the ERDA workflow orchestrator",
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Pfad zu publish.yml (Standard: --root/publish.yml)",
    )
    parser.add_argument(
        "--profile",
        default="default",
        help="Profilname aus publish.yml",
    )
    parser.add_argument(
        "--repo-visibility",
        choices=("auto", "public", "private"),
        default="auto",
        help="Sichtbarkeit des Repositories",
    )
    parser.add_argument(
        "--repository",
        help="Repository-Slug (owner/name) für Template-Substitution",
    )
    parser.add_argument("--commit", help="Commit-SHA für Änderungsdetektion")
    parser.add_argument("--base", help="Basis-SHA für Änderungsdetektion")
    parser.add_argument(
        "--reset-others",
        action="store_true",
        help="Beim Setzen der Publish-Flags andere Einträge zurücksetzen",
    )
    parser.add_argument(
        "--publisher-arg",
        action="append",
        dest="publisher_arg",
        help="Zusätzliche Argumente für pipeline.py (mehrfach möglich)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Nur anzeigen, welche Schritte ausgeführt würden",
    )
    parser.add_argument(
        "--step",
        action="append",
        help="Überschreibt die im Profil definierten Schritte",
    )
    return parser.parse_args(list(argv) if argv is not None else None)


def main(argv: Iterable[str] | None = None) -> None:
    args = parse_args(argv)
    config = build_config(args)
    run(config)


__all__ = [
    "DockerSettings",
    "OrchestratorProfile",
    "OrchestratorConfig",
    "build_config",
    "parse_args",
    "run",
    "main",
]
