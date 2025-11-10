#!/usr/bin/env python3
"""
Plattformunabhängiges Convenience-Modul zum Ausführen von Tests und Orchestrator im Docker Container.

Verwendung:
    python run_docker.py test                    # Alle Tests
    python run_docker.py test-slow               # Nur Integrationstests
    python run_docker.py orchestrator            # Orchestrator mit Default-Profil
    python run_docker.py orchestrator --profile ci  # Mit spezifischem Profil
    python run_docker.py orchestrator --rebuild     # Image neu bauen und Orchestrator starten
    python run_docker.py shell                   # Interaktive Shell im Container
    python run_docker.py build                   # Nur Image bauen

Optionen:
    --no-build    Image nicht bauen, wenn es fehlt
    --rebuild     Image vor Ausführung neu bauen (erzwingt --pull)
    --no-cache    Docker-Build ohne Layer-Cache
    --profile     Profil für Orchestrator (default: local)
    --verbose     Mehr Logging-Output
"""

import argparse
import sys
from pathlib import Path

# Füge den tools-Pfad zum Python-Pfad hinzu
REPO_ROOT = Path(__file__).resolve().parent
TOOLS_PATH = REPO_ROOT / ".github" / "gitbook_worker" / "tools"
sys.path.insert(0, str(TOOLS_PATH))

from utils.docker_runner import main as docker_runner_main


def build_docker_args(
    command: str,
    profile: str = "local",
    no_build: bool = False,
    verbose: bool = False,
    rebuild: bool = False,
    no_cache: bool = False,
) -> list[str]:
    """Erstelle die Argumentliste für docker_runner."""

    dockerfile = str(
        REPO_ROOT / ".github" / "gitbook_worker" / "tools" / "docker" / "Dockerfile"
    )
    tag = "erda-workflow-tools"
    context = str(REPO_ROOT)
    workdir = str(REPO_ROOT)

    args = [
        "--dockerfile",
        dockerfile,
        "--tag",
        tag,
        "--context",
        context,
        "--workdir",
        workdir,
        "--env",
        "PYTHONPATH=/workspace",
    ]

    if no_build:
        args.append("--no-build")

    if verbose:
        args.append("--verbose")

    if rebuild:
        args.append("--rebuild")

    if no_cache:
        args.append("--no-cache")

    # Füge den Container-Befehl hinzu
    args.append("--it")

    if command == "test":
        args.extend(
            [
                "bash",
                "-c",
                "cd /workspace && python3 -m pytest .github/gitbook_worker/tests -v --tb=short",
            ]
        )
    elif command == "test-slow":
        args.extend(
            [
                "bash",
                "-c",
                "cd /workspace && python3 -m pytest .github/gitbook_worker/tests -v -m slow --tb=short",
            ]
        )
    elif command == "orchestrator":
        font_guard = (
            "fc-list | grep -qi 'Twemoji' || "
            "{ echo 'ERROR: Twemoji font missing'; exit 45; }; "
            "fc-list | grep -qi 'ERDA CC-BY CJK' || "
            "{ echo 'ERROR: ERDA CC-BY CJK font missing'; exit 46; }; "
        )
        orchestrator_cmd = (
            "python3 -m tools.workflow_orchestrator --root /workspace "
            "--manifest publish.yml --profile "
            f"{profile}"
        )
        args.extend(
            [
                "bash",
                "-c",
                f"cd /workspace && {font_guard}{orchestrator_cmd}",
            ]
        )
    elif command == "shell":
        args.extend(["bash"])
    elif command == "build":
        # Nur bauen, nichts ausführen
        args = [
            "--dockerfile",
            dockerfile,
            "--tag",
            tag,
            "--context",
            context,
            "--workdir",
            workdir,
            "--print-only",  # Nur anzeigen, nicht ausführen
            "--it",
            "true",  # Dummy-Befehl
        ]
    else:
        raise ValueError(f"Unbekannter Befehl: {command}")

    return args


def main():
    parser = argparse.ArgumentParser(
        description="Docker-basierte Tests und Workflows ausführen",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  %(prog)s test                      # Alle Unit-Tests ausführen
  %(prog)s test-slow                 # Integrationstests ausführen
  %(prog)s orchestrator              # Orchestrator mit local-Profil
  %(prog)s orchestrator --profile ci # Orchestrator mit ci-Profil
  %(prog)s shell                     # Interaktive Shell im Container
  %(prog)s build                     # Nur Docker-Image bauen
        """,
    )

    parser.add_argument(
        "command",
        choices=["test", "test-slow", "orchestrator", "shell", "build"],
        help="Auszuführender Befehl",
    )

    parser.add_argument(
        "--profile",
        default="local",
        help="Profil für den Orchestrator (default: local)",
    )

    parser.add_argument(
        "--no-build", action="store_true", help="Image nicht bauen, wenn es fehlt"
    )

    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Image vor dem Start neu bauen (inkl. --pull)",
    )

    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Docker-Build ohne Layer-Cache ausführen",
    )

    parser.add_argument("--verbose", action="store_true", help="Mehr Logging-Output")

    args = parser.parse_args()

    # Spezialfall: Nur bauen
    if args.command == "build":
        print("Building Docker image...")
        docker_args = [
            "--dockerfile",
            str(
                REPO_ROOT
                / ".github"
                / "gitbook_worker"
                / "tools"
                / "docker"
                / "Dockerfile"
            ),
            "--tag",
            "erda-workflow-tools",
            "--context",
            str(REPO_ROOT),
            "--workdir",
            str(REPO_ROOT),
        ]
        if args.verbose:
            docker_args.append("--verbose")
        if args.no_cache:
            docker_args.append("--no-cache")
        docker_args.append("--rebuild")
        docker_args.extend(["--it", "true"])  # Dummy-Befehl, wird nicht ausgeführt

        # Baue das Image
        try:
            return docker_runner_main(docker_args)
        except SystemExit as e:
            if e.code == 0:
                print("SUCCESS: Docker image built successfully!")
            return e.code

    # Normale Befehle
    docker_args = build_docker_args(
        command=args.command,
        profile=args.profile,
        no_build=args.no_build,
        verbose=args.verbose,
        rebuild=args.rebuild,
        no_cache=args.no_cache,
    )

    if args.verbose:
        print(f"Docker command: {args.command}")
        print(f"Profile: {args.profile}")
        print(f"No-Build: {args.no_build}")

    try:
        exit_code = docker_runner_main(docker_args)
        if exit_code == 0:
            print(f"\nSUCCESS: Command '{args.command}' completed successfully!")
        else:
            print(f"\nERROR: Command '{args.command}' failed (exit code: {exit_code})")
        return exit_code
    except KeyboardInterrupt:
        print("\nWARNING: Interrupted by user")
        return 130
    except Exception as e:
        print(f"\nERROR: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
