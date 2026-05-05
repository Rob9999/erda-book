#!/usr/bin/env python3
"""Run gitbook_worker AI reference checks with throttling.

The upstream gitbook_worker package is intentionally left untouched in this
repository. This wrapper reuses its discovery, source extraction and model-call
functions, but sleeps between individual reference tasks, cools down after rate
limits and writes sanitized local reports.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from dataclasses import asdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import quote

from gitbook_worker.tools.quality.ai_references import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_PROMPT,
    DEFAULT_TIMEOUT,
    ModelConfig,
    ReferenceTask,
    apply_fixes,
    call_model,
    discover_markdown_files,
    load_reference_tasks,
)

RATE_LIMIT_MARKERS = (
    "429",
    "rate limit",
    "too many requests",
    "resource_exhausted",
    "quota",
)

INLINE_REFERENCE_RE = re.compile(r"\bhttps?://\S+|\bdoi:\s*\S+|\bdoi\.org/\S+", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BARE_REFERENCE_RE = re.compile(r"^<?(?:https?://\S+|doi:\s*\S+|doi\.org/\S+)>?$", re.IGNORECASE)


def read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def env_value(env_file: Mapping[str, str], *names: str) -> str | None:
    for name in names:
        value = env_file.get(name) or os.getenv(name)
        if value:
            return value
    return None


def read_files_list(path: Path) -> list[Path]:
    return [
        Path(line.strip())
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def compact_title(line: str) -> str:
    without_markdown_links = MARKDOWN_LINK_RE.sub(r"\1", line)
    without_urls = re.sub(r"https?://\S+", "", without_markdown_links)
    return re.sub(r"\s+", " ", without_urls).strip()[:240] or line[:240]


def numbering_from_line(line: str) -> str | None:
    bracket_match = re.match(r"^\[(\d+)\]", line)
    if bracket_match:
        return bracket_match.group(1)
    ordered_match = re.match(r"^(\d+)[.)]\s+", line)
    if ordered_match:
        return ordered_match.group(1)
    return None


def previous_nonempty_line(lines: Sequence[str], before_index: int) -> str | None:
    for candidate in reversed(lines[:before_index]):
        stripped = candidate.strip()
        if stripped:
            return stripped
    return None


def inline_task_line(lines: Sequence[str], index: int, stripped: str) -> str:
    if not BARE_REFERENCE_RE.match(stripped):
        return stripped
    previous = previous_nonempty_line(lines, index)
    if not previous or previous.startswith("#"):
        return stripped
    return f"{previous} {stripped}"


def load_inline_reference_tasks(files: Sequence[Path]) -> list[ReferenceTask]:
    tasks: list[ReferenceTask] = []
    for file in files:
        try:
            lines = file.read_text(encoding="utf-8-sig").splitlines()
        except OSError:
            continue
        for line_number, line in enumerate(lines, start=1):
            stripped = line.strip()
            if not stripped or not INLINE_REFERENCE_RE.search(stripped):
                continue
            task_line = inline_task_line(lines, line_number - 1, stripped)
            tasks.append(
                ReferenceTask(
                    file=file.resolve(),
                    title=compact_title(task_line),
                    line=task_line,
                    lineno=line_number,
                    numbering=numbering_from_line(task_line),
                )
            )
    return tasks


def merge_tasks(source_tasks: Sequence[ReferenceTask], inline_tasks: Sequence[ReferenceTask]) -> list[ReferenceTask]:
    merged: list[ReferenceTask] = []
    seen: set[tuple[str, int, str]] = set()
    for task in list(source_tasks) + list(inline_tasks):
        key = (str(task.file), task.lineno, task.line)
        if key in seen:
            continue
        seen.add(key)
        merged.append(task)
    return merged


def build_review_prompt(base_prompt: str, as_of_date: str) -> str:
    return (
        f"{base_prompt}\n\n"
        "Review context and rules:\n"
        f"- Current review date: {as_of_date}.\n"
        f"- The JSON field validation_date must be exactly \"{as_of_date}\" for this review.\n"
        "- Do not invent access dates, publication dates, publishers, titles or authors.\n"
        "- Preserve an existing access date from the source line unless it is explicitly impossible.\n"
        "- If details cannot be verified from the provided reference line itself, set success=false and explain what needs manual review.\n"
        "- Keep the original URL or DOI in any proposed replacement.\n"
        "- Return JSON only."
    )


def sanitize(value: Any, secrets: Sequence[str]) -> Any:
    if isinstance(value, str):
        redacted = value
        for secret in secrets:
            if not secret:
                continue
            redacted = redacted.replace(secret, "<redacted>")
            redacted = redacted.replace(quote(secret, safe=""), "<redacted>")
        return redacted
    if isinstance(value, list):
        return [sanitize(item, secrets) for item in value]
    if isinstance(value, tuple):
        return [sanitize(item, secrets) for item in value]
    if isinstance(value, dict):
        return {str(key): sanitize(item, secrets) for key, item in value.items()}
    return value


def contains_rate_limit(value: Any) -> bool:
    text = json.dumps(value, ensure_ascii=False).lower()
    return any(marker in text for marker in RATE_LIMIT_MARKERS)


class SafeLog:
    def __init__(self, path: Path | None, secrets: Sequence[str]) -> None:
        self.path = path
        self.secrets = secrets
        if self.path:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text("", encoding="utf-8")

    def write(self, message: str) -> None:
        clean = sanitize(message, self.secrets)
        print(clean, flush=True)
        if self.path:
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(clean + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Throttled wrapper for gitbook_worker ai_references"
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument(
        "--env-file", type=Path, default=Path(".env"), help="Local env file"
    )
    parser.add_argument("--manifest", type=Path, help="Optional publish.yml filter")
    parser.add_argument(
        "--summary", type=Path, help="SUMMARY.md to discover Markdown files"
    )
    parser.add_argument("--files", type=Path, nargs="*", help="Explicit Markdown files")
    parser.add_argument(
        "--files-list", type=Path, help="Text file containing Markdown paths"
    )
    parser.add_argument("--language", default="de", help="Source section language")
    parser.add_argument(
        "--max-level", type=int, default=6, help="Maximum source heading level"
    )
    parser.add_argument(
        "--prompt", default=DEFAULT_PROMPT, help="Base prompt for the AI service"
    )
    parser.add_argument(
        "--as-of-date",
        default=date.today().isoformat(),
        help="Current review date to pass into the AI prompt as YYYY-MM-DD",
    )
    parser.add_argument("--ai-url", help="AI endpoint URL")
    parser.add_argument("--ai-provider", help="AI provider identifier")
    parser.add_argument("--model", help="Model name")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES)
    parser.add_argument(
        "--delay-seconds",
        type=float,
        default=8.0,
        help="Delay after every reference task",
    )
    parser.add_argument(
        "--jitter-seconds", type=float, default=3.0, help="Random extra delay"
    )
    parser.add_argument(
        "--cooldown-on-429-seconds",
        type=float,
        default=90.0,
        help="Cooldown after rate-limit results",
    )
    parser.add_argument(
        "--max-consecutive-429",
        type=int,
        default=5,
        help="Abort after this many consecutive rate limits",
    )
    parser.add_argument("--max-files", type=int, help="Limit number of files")
    parser.add_argument("--max-tasks", type=int, help="Limit number of reference tasks")
    parser.add_argument(
        "--include-inline-links",
        action="store_true",
        help="Also create tasks from inline URL/DOI lines when no source block is present",
    )
    parser.add_argument(
        "--json-report", type=Path, required=True, help="Sanitized JSON report path"
    )
    parser.add_argument("--log-file", type=Path, help="Sanitized log path")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Apply successful fixes. Default is dry-run",
    )
    return parser


def resolve_files(args: argparse.Namespace, root: Path) -> list[Path]:
    explicit: list[Path] = []
    if args.files:
        explicit.extend(args.files)
    if args.files_list:
        explicit.extend(read_files_list(args.files_list))
    files = discover_markdown_files(
        root=root,
        manifest=args.manifest.resolve() if args.manifest else None,
        summary=args.summary.resolve() if args.summary else None,
        explicit_files=explicit or None,
    )
    if args.max_files is not None:
        files = files[: max(args.max_files, 0)]
    return files


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    env_file = read_env_file(
        (root / args.env_file).resolve()
        if not args.env_file.is_absolute()
        else args.env_file
    )

    api_key = env_value(env_file, "AI_REFERENCE_API_KEY", "AI_API_KEY")
    provider = (
        args.ai_provider
        or env_value(env_file, "AI_REFERENCE_PROVIDER", "AI_PROVIDER")
        or "openai"
    )
    base_url = (
        args.ai_url
        or env_value(env_file, "AI_REFERENCE_URL", "AI_URL")
        or "https://api.openai.com/v1/chat/completions"
    )
    model = (
        args.model or env_value(env_file, "AI_REFERENCE_MODEL", "AI_MODEL") or "gpt-4"
    )
    secrets = [secret for secret in (api_key,) if secret]

    log = SafeLog(args.log_file, secrets)
    files = resolve_files(args, root)
    if not files:
        log.write("No Markdown files selected.")
        return 0

    source_tasks = load_reference_tasks(
        files, language=args.language, max_level=args.max_level
    )
    inline_tasks = load_inline_reference_tasks(files) if args.include_inline_links else []
    tasks = merge_tasks(source_tasks, inline_tasks)
    tasks = sorted(tasks, key=lambda task: (str(task.file), task.lineno, task.title))
    if args.max_tasks is not None:
        tasks = tasks[: max(args.max_tasks, 0)]
    if not tasks:
        log.write(
            "No reference tasks found in selected files. "
            "If these files use inline URLs/DOIs instead of Quellen/References sections, "
            "rerun with --include-inline-links."
        )
        return 0

    config = ModelConfig(
        base_url=base_url,
        api_key=api_key,
        provider=provider,
        model=model,
        temperature=args.temperature,
        timeout=args.timeout,
        max_retries=args.max_retries,
    )
    review_prompt = build_review_prompt(args.prompt, args.as_of_date)

    log.write(f"THROTTLED_AI_REFERENCES_START={datetime.now(timezone.utc).isoformat()}")
    log.write(f"FILES={len(files)} TASKS={len(tasks)} DRY_RUN={not args.write}")
    log.write(f"AS_OF_DATE={args.as_of_date}")
    log.write(
        f"TASK_SOURCES=source_sections={len(source_tasks)} "
        f"inline_links={len(inline_tasks)} include_inline_links={args.include_inline_links}"
    )
    log.write(f"PROVIDER={provider} MODEL={model} URL={base_url}")
    log.write(
        "THROTTLE="
        f"delay={args.delay_seconds}s jitter={args.jitter_seconds}s "
        f"cooldown429={args.cooldown_on_429_seconds}s maxConsecutive429={args.max_consecutive_429}"
    )

    results = []
    consecutive_429 = 0
    aborted = False
    for index, task in enumerate(tasks, start=1):
        log.write(f"TASK {index}/{len(tasks)} {task.file}:{task.lineno}")
        result = call_model(task, review_prompt, config)
        results.append(result)
        entry = result.to_report_entry()
        limited = contains_rate_limit(entry)
        if limited:
            consecutive_429 += 1
            log.write(f"RATE_LIMIT task={index} consecutive={consecutive_429}")
            if consecutive_429 >= args.max_consecutive_429:
                log.write("ABORTING=max consecutive rate limits reached")
                aborted = True
                break
            sleep_for = args.cooldown_on_429_seconds
        else:
            consecutive_429 = 0
            sleep_for = args.delay_seconds + random.uniform(
                0, max(args.jitter_seconds, 0.0)
            )
        if index < len(tasks):
            log.write(f"SLEEP_SECONDS={sleep_for:.1f}")
            time.sleep(max(sleep_for, 0.0))

    if args.write:
        report = apply_fixes(results, write_changes=True)
    else:
        report = [result.to_report_entry() for result in results]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "aborted": aborted,
        "dry_run": not args.write,
        "as_of_date": args.as_of_date,
        "prompt": review_prompt,
        "model_config": sanitize(asdict(config), secrets),
        "files": [str(path) for path in files],
        "tasks_total": len(tasks),
        "tasks_completed": len(results),
        "task_sources": {
            "source_sections": len(source_tasks),
            "inline_links": len(inline_tasks),
            "include_inline_links": args.include_inline_links,
        },
        "results": sanitize(report, secrets),
    }
    args.json_report.parent.mkdir(parents=True, exist_ok=True)
    args.json_report.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    repaired = sum(1 for entry in report if entry.get("success") and entry.get("new"))
    validated = sum(
        1 for entry in report if entry.get("success") and not entry.get("new")
    )
    failed = sum(1 for entry in report if not entry.get("success"))
    rate_limited = sum(1 for entry in report if contains_rate_limit(entry))
    log.write(
        f"THROTTLED_AI_REFERENCES_DONE repaired={repaired} "
        f"validated={validated} failed={failed} rate_limited={rate_limited} "
        f"report={args.json_report}"
    )
    return 2 if aborted else 0


if __name__ == "__main__":
    raise SystemExit(main())
