import subprocess
import shutil
from pathlib import Path

from errors import UnityError, CopyError
from generateDS import classes

UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"  # noqa (ignore lint)
STARTER_PROJECT = "unity/CAVE"


# Copy all files from source to destination
def copy_files(source: Path, destination: Path):
    try:
        shutil.copytree(str(source), str(destination))
    except Exception as e:
        raise CopyError(
            f"Error: Failed to copy files from {source} "
            + f"to {destination}.\n"
            + f"{e}"
        )


# TODO: Load project settings and write scene file (13)
# Creates a new Unity scene file for the given xml file
def build_scene(xml_file: Path, story: classes.Story):
    unity_dir = xml_file.parent
    filename = xml_file.stem

    try:
        sp = subprocess.run(
            [
                f"{UNITY_PATH}",
                "-batchmode",
                "-quit",
                "-projectPath",
                f"{unity_dir}",
                "-executeMethod",
                "CreateScene.NewScene",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        # raise UnityError(
        #     "Error: Failed to launch Unity.\n"
        #     # + f"{sp.stderr}"
        #     + "This script only runs with "
        #     + f"Unity version {UNITY_VERSION}.\n"
        #     + f"The executable should be found at {UNITY_PATH}\n"
        #     + e
        # )
        pass
