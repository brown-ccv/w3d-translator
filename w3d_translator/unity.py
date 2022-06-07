import subprocess
import shutil
from pathlib import Path

from errors import UnityError

UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"  # noqa (ignore lint)
EMPTY_SCENE = "../EmptyScene.unity"


# Create Unity project and copy original files
def create_project(project_dir: Path, unity_dir: Path):
    try:
        sp = subprocess.run(
            [
                f"{UNITY_PATH}",
                "-batchmode",
                "-createProject",
                f"{unity_dir}",
                "-quit",
            ],
            check=True,
            capture_output=True,
        )
        copy_files(project_dir, unity_dir)
        Path(unity_dir, "Assets", "Scenes").mkdir()
    except Exception:
        raise UnityError(
            "Error: Failed to launch Unity.\n"
            + f"{sp.stderr}"
            + "This script only runs with "
            + f"Unity version {UNITY_VERSION}.\n"
            + f"The executable should be found at {UNITY_PATH}"
        )


# Copy project into [unity_dir]/Assets/originals
def copy_files(project_dir: Path, unity_dir: Path):
    destination = Path(unity_dir, "Assets", "originals")
    try:
        shutil.copytree(str(project_dir), str(destination))
    except Exception as e:
        raise UnityError(
            f"Error: Failed to copy files from {project_dir} "
            + f"to {destination}.\n"
            + f"{e}"
        )


# TODO: Load project settings and write scene file (13)
def build_project(unity_dir: Path, yaml):
    pass
