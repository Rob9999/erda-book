import os
import subprocess
import sys


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
        print(f"Building Docker image '{image_name}' ...")
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
            print("Docker build failed:\n", build_result.stderr)
            sys.exit(1)
