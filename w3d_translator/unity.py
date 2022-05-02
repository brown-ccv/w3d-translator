import subprocess
import shutil
from pathlib import Path

from errors import UnityError


UNITY_VERSION = "2020.3.26f1"
# TODO: Upgrade to Unity 2021
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2020.3.26f1\\Editor\\Unity.exe"  # noqa (ignore lint)
EMPTY_SCENE = "../EmptyScene.unity"


# Create Unity project
def create_project(folder):
    try:
        subprocess.run(
            f'{UNITY_PATH} -batchmode -createProject "{folder}" -quit'
        )
    except Exception:
        raise UnityError(
            "Error: Failed to launch Unity.\n"
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


# Create Scenes folder and add empty scene
def add_empty_scene(unity_dir: Path):
    try:
        destination = Path(unity_dir, "Assets", "Scenes")
        destination.mkdir()
        shutil.copy2(EMPTY_SCENE, Path(destination, "Scene.unity"))
    except Exception:
        raise UnityError(
            "Error: Unable to copy ExampleScene.unity" + f"({EMPTY_SCENE})"
        )
