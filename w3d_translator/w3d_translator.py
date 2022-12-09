import typer
import shutil
from pathlib import Path
from subprocess import Popen, PIPE
from rich.console import Console

from validate import validate_project, validate_xml
from errors import ValidationError, UnityError, XmlError

# TODO: Mac support (/Applications/Unity/Hub/Editor/2021.3.0f1/Unity.app)
UNITY_VERSION = "2022.1.21f1"
UNITY_PATH = Path(
    f"C:\\Program Files\\Unity\\Hub\\Editor\\{UNITY_VERSION}\\Editor\\Unity.exe"  # noqa
)
STARTER_PROJECT = Path("unity/CAVE")
LOG_FLAG = "LOG:"  # Flag to send prints from the CLI script onto the console
console = Console()
err_console = Console(stderr=True, style="bold red")

# TODO 137: Clean up rich colors (folder, file, warning, error, etc)


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
        # TODO 54: Retry a certain number of times?
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
        err_console.print(e)
        exit(1)


# Copy files from the project directory to the Unity output directory
def copy_files(project_dir: Path, unity_dir: Path, unity_copy: Path):
    try:
        with console.status("Copying files"):
            shutil.copytree(str(STARTER_PROJECT), str(unity_dir))
            shutil.copytree(
                project_dir,
                unity_copy,
            )
    except (ValidationError, UnityError, Exception) as e:
        err_console.print(e)
    else:
        console.print(
            f"Copied files from [cyan]{project_dir}/[/cyan]"
            + f" to [cyan]{unity_dir}\\"
        )


# Translate valid xml files (ignore invalid)
def translate_files(unity_dir: Path, unity_copy: Path):
    # TODO 138: Use a live progress group to keep track of the different files
    # TODO 3: Launch each file in its own process
    all_good = True
    for xml_path in unity_copy.rglob("*.xml"):
        console.print(f"Translating file: '{xml_path.name}'")
        try:
            translate_file(unity_dir, xml_path)
        except (XmlError, UnityError) as e:
            err_console.print(e)
            all_good = False

    if all_good:
        console.print(
            ":white_check_mark: "
            + f"[cyan]{unity_dir.name}/ "
            + "translated successfully[/cyan]\n"
        )
    else:
        console.print(
            f"[yellow]{unity_dir.name}/ "
            + "translated with some errors [/yellow]\n"
        )


# Translate an XML file using Unity's CLI
def translate_file(unity_dir: Path, xml_path: Path):
    validate_xml(xml_path)
    console.print(f"'{xml_path.name}' is valid")

    log = Path(unity_dir, "Logs", f"cli_{xml_path.stem}.log")
    log.parent.mkdir(exist_ok=True)

    # Run Unity CLI
    with Popen(
        [
            f"{UNITY_PATH}",
            "-batchmode",
            "-quit",
            "-logFile",
            "-",
            "-projectPath",
            f"{unity_dir}",
            "--xmlPath",
            Path(*xml_path.parts[2:]),
            "-executeMethod",
            "Writing3D.Editor.CLI.Main",
        ],
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True,
        bufsize=1,
    ) as sp, log.open("w+") as logfile, console.status("Running Unity CLI"):
        # Process stdout and stderr as it's written to
        for line in sp.stdout:
            if line.startswith(LOG_FLAG):
                # Send prints from CLI script to console
                console.log(line.strip(LOG_FLAG).strip())
            else:
                # Send Unity logs to the log file
                logfile.write(line)

    if sp.returncode != 0:
        # TODO 139: Make hyperlink
        raise UnityError(
            "Translation failed. " + f"See '{logfile.name}'for more details."
        )
    else:
        console.print(f"'{xml_path.name}' translated successfully")


# Translate a single project from W3D to Unity
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    console.print(f"Translating project: [cyan]{project_dir.name}/[/cyan]")

    # Validate project
    try:
        validate_project(project_dir)
    except (ValidationError, UnityError) as e:
        err_console.print(e)
    else:
        console.print(f"[cyan]{project_dir}/[/cyan] is valid")

    if dev:
        # Validate the xml files
        for xml_path in project_dir.rglob("*.xml"):
            try:
                validate_xml(xml_path)
            except XmlError as e:
                err_console.print(e)
            else:
                console.print(f"'{xml_path.name}' is valid")
    else:
        unity_dir = Path(out_dir, project_dir.name)
        unity_copy = Path(unity_dir, "Assets", "Resources", "Original Project")
        copy_files(project_dir, unity_dir, unity_copy)
        translate_files(unity_dir, unity_copy)


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
