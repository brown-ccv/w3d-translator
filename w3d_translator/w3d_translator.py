import sys
import typer
import shutil
from pathlib import Path
from subprocess import Popen, PIPE

from validate import validate_project, validate_out
from errors import ValidationError, CopyError, UnityError

UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"  # noqa (ignore lint)
STARTER_PROJECT = "unity/CAVE"
LOG_FLAG = "CLI:"  # Flag to send prints from the CLI script onto the console


# Color string as cyan
def cyan(string: str):
    return typer.style(string, fg=typer.colors.CYAN, bold=True)


# Color string as green
def green(string: str):
    return typer.style(string, fg=typer.colors.GREEN, bold=True)


# Color string as bright red
def red(string: str):
    return typer.style(string, fg=typer.colors.BRIGHT_RED, bold=True)


# Opening message
def greeting(in_dir: Path, out_dir: Path):
    print("W3D TRANSLATOR")
    print(f"Unity Version:\t {cyan(UNITY_VERSION)}")
    print(f"IN_DIR:\t\t {cyan(in_dir)}")
    print(f"OUT_DIR:\t {cyan(out_dir)}")
    print()


# Ending message
def farewell():
    print()
    print("Translation Complete!")
    exit(0)


# Copy all files from source to destination
def copy_files(source: Path, destination: Path):
    # TODO: Catch this exception
    try:
        shutil.copytree(str(source), str(destination))
    except Exception as e:
        raise CopyError(
            f"Error: Failed to copy files from {source} "
            + f"to {destination}.\n"
            + f"{e}"
        )


# Translate a single project from W3D to Unity
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    try:
        print(f"Translating project:\t {cyan(project_dir.name)}")
        validate_project(project_dir)
        unity_dir = Path(out_dir, project_dir.name)

        # Create Unity project
        if not dev:
            try:
                copy_files(Path(STARTER_PROJECT), unity_dir)
                copy_files(
                    project_dir,
                    Path(unity_dir, "Assets", "Resources", "Original Project"),
                )
            except CopyError as e:
                # TODO: Handle this error (54)
                print(red(e), file=sys.stderr)

            # Build the project using Unity's CLI
            with Popen(
                [
                    f"{UNITY_PATH}",
                    "-batchmode",
                    "-quit",
                    "-projectPath",
                    f"{unity_dir}",
                    "-executeMethod",
                    "CLI.Start",
                    "-logFile",
                    "-",
                ],
                bufsize=1,
                stdout=PIPE,
                stderr=PIPE,
                universal_newlines=True,
            ) as sp, open(Path(unity_dir, "cli_log.txt"), "w") as logfile:
                # Process stdout and stderr as it's written to
                for line in sp.stdout:
                    if line.startswith(LOG_FLAG):
                        # Send prints from CLI script to console
                        print(green(line.strip(LOG_FLAG)), end="")
                    else:
                        # Send Unity logs to a the log file
                        logfile.write(line)

            # Check clean exit
            if sp.poll() != 0:
                raise UnityError(
                    "Error: Unity CLI exited with return code "
                    + f"{sp.returncode}.\n"
                    + f"See '{logfile}' for more details."
                )
    except (ValidationError, UnityError) as e:
        print(red(e), file=sys.stderr)


def main(
    in_dir: Path = typer.Argument(
        ..., help="Input folder containing the xml project(s)"
    ),
    out_dir: Path = typer.Argument(
        ..., help="Output folder for the translated project(s)"
    ),
    multiple: bool = typer.Option(False, help="Translate multiple projects?"),
    force: bool = typer.Option(False, help="Overwrite OUT_DIR?"),
    dev: bool = typer.Option(False, help="Don't create Unity projects"),
):
    """
    Translate W3D xml projects in in_dir to Unity projects in out_dir
    """
    greeting(in_dir, out_dir)

    # Create output folder
    try:
        validate_out(out_dir, force)
    except ValidationError as e:
        print(red(e), file=sys.stderr)
        exit(1)

    # Translate project(s)
    if multiple:
        projects = [p for p in in_dir.iterdir() if p.is_dir()]
        for project_dir in projects:
            translate_project(project_dir, out_dir, dev=dev)
    else:
        translate_project(in_dir, out_dir, dev=dev)

    # Print farewell and exit
    farewell()


if __name__ == "__main__":
    typer.run(main)
