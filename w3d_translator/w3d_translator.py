import sys
import typer
import shutil
from pathlib import Path
from subprocess import Popen, PIPE
from rich.console import Console

from validate import validate_project, validate_xml
from errors import ValidationError, UnityError, XmlError

# TODO: Hard coded paths won't work on others' machines
UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = Path(
    "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"
)
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


# Validate and create the output folder
def create_out(out_dir: Path, force: bool):
    try:
        out_dir.mkdir()
    except PermissionError:
        # TODO 54: Catch error when files are being used in another process
        # TODO: Retry a certain number of times?
        # Output folder currently in use, pause and try again
        pass
    except FileExistsError:
        if force:
            shutil.rmtree(out_dir)
            out_dir.mkdir(exist_ok=True)
        else:
            raise ValidationError(
                f"Error: OUTPUT directory already exists: {out_dir}.\n"
                + "Use --force to overwrite"
            )
    except FileNotFoundError:
        raise ValidationError("Error: OUTPUT directory is not valid")
    except ValidationError as e:
        err_console.print(e, file=sys.stderr, style="red")
        exit(1)


# Copy files from the project directory to the Unity output directory
def copy_files(project_dir: Path, unity_dir: Path, unity_copy: Path):
    try:
        shutil.copytree(str(STARTER_PROJECT), str(unity_dir))
        shutil.copytree(
            project_dir,
            unity_copy,
        )
    except Exception as e:
        # TODO 55: Catch this exception (skip file)
        err_console.print(e, file=sys.stderr, style="red")


# Translate an XML file using Unity's CLI
def translate_file(unity_dir: Path, xml_path: Path, filename: str):
    try:
        validate_xml(xml_path)
    except XmlError as e:
        err_console.print(e, file=sys.stderr, style="red")
    else:
        console.print(f"'{filename}' is valid")

    # Run Unity CLI
    with Popen(
        [
            f"{UNITY_PATH}",
            "-batchmode",
            "-quit",
            "-projectPath",
            f"{unity_dir}",
            "-logFile",
            "-",
            "-executeMethod",
            "CLI.Main",
            "--xmlPath",
            Path(*xml_path.parts[2:]),  # Path relative to unity_dir
        ],
        bufsize=1,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
    ) as sp, open(
        Path(unity_dir, "Logs", f"cli_{xml_path.stem}.log"), "w"
    ) as logfile:
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


# Translate a single project from W3D to Unity
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    console.print(f"Translating project: [cyan]{project_dir.name}[/cyan]")

    try:
        # Validate project
        with console.status("Validating project"):
            validate_project(project_dir)
        console.print(f"'{project_dir}' is valid")

        # Create the Unity project
        if not dev:
            unity_dir = Path(out_dir, project_dir.name)
            unity_copy = Path(
                unity_dir, "Assets", "Resources", "Original Project"
            )

            with console.status("Copying files"):
                copy_files(project_dir, unity_dir, unity_copy)
            console.print(
                f"Copied files from '{project_dir}' to '{unity_dir}'"
            )

            # Translate valid .xml files (skip invalid)
            for xml_path in unity_copy.rglob("*.xml"):
                with console.status(
                    "Translating file: "
                    + f"[cyan]{project_dir.name}/{xml_path.name}[/cyan]"
                ):
                    translate_file(unity_dir, xml_path, xml_path.name)
    except (ValidationError, UnityError) as e:
        err_console.print(e, file=sys.stderr, style="red")
    else:
        console.print(
            ":white_check_mark: "
            + f"[cyan]{project_dir.name}/{xml_path.name}[/cyan] "
            + "translated successfully\n"
        )


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

    with console.status("Creating output folder"):
        create_out(out_dir, force)
    console.print(f"'{out_dir}' created successfully\n")

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
