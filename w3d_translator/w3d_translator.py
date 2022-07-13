import typer
import subprocess
import shutil
from pathlib import Path

from generateDS.subclasses import parse
from validate import validate_project, validate_out, validate_xml
from errors import ValidationError, CopyError, UnityError
from translate import translate_objects

UNITY_VERSION = "2021.3.0f1"
UNITY_PATH = "C:\\Program Files\\Unity\\Hub\\Editor\\2021.3.0f1\\Editor\\Unity.exe"  # noqa (ignore lint)
STARTER_PROJECT = "unity/CAVE"


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
    typer.echo("W3D TRANSLATOR")
    typer.echo(f"Unity Version:\t {cyan(UNITY_VERSION)}")
    typer.echo(f"IN_DIR:\t\t {cyan(in_dir)}")
    typer.echo(f"OUT_DIR:\t {cyan(out_dir)}")
    typer.echo()


# Ending message
def farewell():
    typer.echo()
    typer.echo("Translation Complete!")
    exit(0)


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


# Translate a single project from W3D to Unity
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    try:
        typer.echo(f"Translating project:\t {cyan(project_dir.name)}")
        validate_project(project_dir)
        unity_dir = Path(out_dir, project_dir.name)

        # Create Unity project
        if not dev:

            # Copy starter project, then xml project into Assets subfolder
            copy_files(Path(STARTER_PROJECT), unity_dir)
            copy_files(
                project_dir,
                Path(unity_dir, "Assets", "Resources", "Original Project"),
            )

        # Translate .xml files to .unity files (skip invalid)
        # TODO: This loop should be done in C#
        # xml_files = [
        #     p
        #     for p in project_dir.iterdir()
        #     if (p.is_file() and p.suffix == ".xml")
        # ]
        # for file in xml_files:
        #     typer.echo(f"Translating file:\t {green(file.name)}")
        #     try:
        #         validate_xml(file)
        #     except XmlError as e:
        #         typer.echo(red(e), err=True)
        #     else:
        #         # Build and clean Story
        #         story = parse(file, silence=True)
        #         story.ObjectRoot = translate_objects(story.ObjectRoot.Object)

        #         # Build the Unity scene
        #         build_scene(Path(unity_dir, file.name), story)

        # Build the project using Unity's CLI
        logfile = Path(unity_dir, "cli_log.txt")
        try:
            subprocess.run(
                [
                    f"{UNITY_PATH}",
                    "-batchmode",
                    "-quit",
                    "-projectPath",
                    f"{unity_dir}",
                    "-executeMethod",
                    "CreateScene.NewScene",
                    "-logFile",
                    f"{logfile}",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            raise UnityError(
                f"Error: Unity CLI exited with error on command {e.cmd}.\n"
                + f"See '{logfile}' for more details."
            )

    except (ValidationError, UnityError) as e:
        typer.echo(red(e), err=True)


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
        typer.echo(red(e), err=True)
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
