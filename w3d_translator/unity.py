import subprocess
import shutil
from pathlib import Path

from errors import UnityError, CopyError

UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"  # noqa (ignore lint)
EMPTY_SCENE = "../EmptyScene.unity"


# Copy all files from source to destination
def copy_files(source: Path, destination: Path):
    print("COPYING", source, destination)
    try:
        shutil.copytree(str(source), str(destination))
    except Exception as e:
        raise CopyError(
            f"Error: Failed to copy files from {source} "
            + f"to {destination}.\n"
            + f"{e}"
        )


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


# TODO: Load project settings and write scene file (13)
def build_project(unity_dir: Path, yaml):
    pass
