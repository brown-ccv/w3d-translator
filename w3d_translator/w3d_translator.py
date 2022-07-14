import sys
import typer
import shutil
from pathlib import Path
from subprocess import Popen, PIPE
from rich.console import Console

from validate import validate_project, validate_out
from errors import ValidationError, UnityError

UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = Path(
    "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"
)  # noqa (ignore lint)
STARTER_PROJECT = Path("unity/CAVE")
LOG_FLAG = "LOG:"  # Flag to send prints from the CLI script onto the console
console = Console()
err_console = Console(stderr=True)


# Opening message
def greeting(in_dir: Path, out_dir: Path):
    console.rule("[bold]W3D TRANSLATOR", align="left")
    console.print(f"Unity Version:\t [cyan]{UNITY_VERSION}[/cyan]")
    console.print(f"IN_DIR:\t\t [cyan]{in_dir}[/cyan]")
    console.print(f"OUT_DIR:\t [cyan]{out_dir}[/cyan]")
    console.print()


# Ending message
def farewell():
    console.print("Translation Complete!")
    exit(0)


# Copy files from the project directory to the Unity output directory
def copy_files(project_dir: Path, unity_dir: Path):
    try:
        shutil.copytree(str(STARTER_PROJECT), str(unity_dir))
        shutil.copytree(
            project_dir,
            str(Path(unity_dir, "Assets", "Resources", "Original Project")),
        )
    except Exception as e:
        # TODO 55: Catch this expression
        err_console.print(e, file=sys.stderr, style="red")


# Translate a single project from W3D to Unity
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    try:
        console.print(
            f"Translating project:\t [cyan]{project_dir.name}[/cyan]"
        )
        with console.status("Validating project"):
            validate_project(project_dir)
        console.print("Project is valid")

        # Create Unity project
        unity_dir = Path(out_dir, project_dir.name)
        if not dev:
            with console.status("Copying files"):
                copy_files(project_dir, unity_dir)
            console.print("Copied files")

            # Build the project using Unity's CLI
            with console.status("Running Unity CLI:"):
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
                            console.print(line.strip(LOG_FLAG), end="")
                        else:
                            # Send Unity logs to a the log file
                            logfile.write(line)

                # Check clean exit
                if sp.poll() != 0:
                    raise UnityError(
                        "Error: Unity CLI exited with return code "
                        + f"{sp.returncode}.\n"
                        + f"See '{logfile.name}' for more details."
                    )
    except (ValidationError, UnityError) as e:
        err_console.print(e, file=sys.stderr, style="red")
    else:
        console.print("Done!\n")


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
        err_console.print(e, file=sys.stderr, style="red")
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
