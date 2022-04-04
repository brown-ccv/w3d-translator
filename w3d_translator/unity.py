import subprocess
import shutil
import os
import sys

# Path to Unity executable
UNITY_VERSION = "2020.3.26f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2020.3.26f1\\Editor\\Unity.exe"

# TODO Create a Unity project at the given folder
# Create Unity project
def create_project(folder):
    try:
        # TEMP - Just create folder structure
        os.mkdir(folder)
        os.mkdir(os.path.join(folder, "Assets"))
        os.mkdir(os.path.join(folder, "Library"))
        os.mkdir(os.path.join(folder, "Logs"))
        os.mkdir(os.path.join(folder, "Packages"))
        os.mkdir(os.path.join(folder, "ProjectSettings"))
        os.mkdir(os.path.join(folder, "UserSettings"))

        # subprocess.run(f'{UNITY_PATH} -createProject "{folder}" -batchmode -quit')
    except FileNotFoundError:
        sys.exit(f"Error: OUTPUT directory is not valid")
        
# Copy project into [unity_dir]/Assets/originals
def copy_files(project_dir, unity_dir):
    destination = os.path.join(unity_dir, "Assets", "originals")
    shutil.copytree(project_dir, destination)
        