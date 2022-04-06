import subprocess
import shutil
import os
import sys

# Path to Unity executable
UNITY_VERSION = "2020.3.26f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2020.3.26f1\\Editor\\Unity.exe"  # noqa (ignore lint)

EMPTY_SCENE = "../EmptyScene.unity"
# TODO: Install MiddleVR package
# TODO: Working with VR and MiddleVR?


# TODO Create a Unity project at the given folder
# Create Unity project
def create_project(folder):
    try:
        subprocess.run(
            f'{UNITY_PATH} -batchmode -createProject "{folder}" -quit'
        )
    except Exception:
        sys.exit(
            "Error: Failed to launch Unity.\n"
            + "This script only runs with "
            + f"Unity version {UNITY_VERSION}.\n"
            + f"The executable should be found at {UNITY_PATH}"
        )


# Copy project into [unity_dir]/Assets/originals
# TODO: Don't exit program. Bubble error up and only close that thread
def copy_files(project_dir, unity_dir):
    destination = os.path.join(unity_dir, "Assets", "originals")
    try:
        shutil.copytree(project_dir, destination)
    except Exception as e:
        sys.exit(
            f"Error: Failed to copy files from {project_dir} "
            + f"to {destination}.\n"
            + f"{e}"
        )


# Create Scenes folder and add empty scene
def add_empty_scene(unity_dir):
    try:
        destination = os.path.join(unity_dir, "Assets", "Scenes")
        os.mkdir(destination)
        shutil.copy2(EMPTY_SCENE, os.path.join(destination, "Scene.unity"))
    except Exception:
        sys.exit(
            "Error: Unable to copy ExampleScene.unity" + f"({EMPTY_SCENE})"
        )
