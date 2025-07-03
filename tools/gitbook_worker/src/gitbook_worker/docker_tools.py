import os
import subprocess
import sys
import logging

logger = logging.getLogger(__name__)


def ensure_docker_image(image_name, dockerfile_path) -> None:
    # Prüfe, ob das Image schon existiert
    result = subprocess.run(
        ["docker", "images", "-q", image_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if not result.stdout.strip():
        # Baue das Image, falls es nicht existiert
        logger.info("Building Docker image '%s' ...", image_name)
        build_result = subprocess.run(
            [
                "docker",
                "build",
                "-t",
                image_name,
                "-f",
                dockerfile_path,
                os.path.dirname(dockerfile_path),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if build_result.returncode != 0:
            logger.error("Docker build failed:\n%s", build_result.stderr)
            sys.exit(1)
