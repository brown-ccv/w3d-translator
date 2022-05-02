import typer
from pathlib import Path

# TODO: Always use Path not PurePath
# TODO: Convert from string to path sooner

from unity import (
    UNITY_VERSION,
    UNITY_PATH,
    # create_project,
    # copy_files,
    # add_empty_scene,
)
from validate import validate_project, validate_in_multiple, validate_out
from errors import ValidationError, TranslationError  # , UnityError
from xml_to_unity import xml_to_unity

# TODO: Configure typer character length (100)
# TODO: Configure color/style for typer.echo
# TODO: Prompt user for confirmation if --force is used (?)

# TEMPORARY OVERRIDES (for development)
# Skip validate_out
# Skip create_project and copy_files (xml_to_unity.py)
# Only translate run.xml (xml_to_unity.py)


# Opening message
def greeting(in_dir: str, out_dir: str):
    typer.echo("W3D TRANSLATOR")
    typer.echo(f"Unity Version:\t {UNITY_VERSION}")
    typer.echo(f"Please ensure Unity is installed at {UNITY_PATH}")
    typer.echo(f"IN_DIR:\t\t {in_dir}")
    typer.echo(f"OUT_DIR:\t {out_dir}")
    typer.echo()


# Ending message
def farewell():
    typer.echo()
    typer.echo("Translation Complete!")
    exit(0)


# Farewell message on error
def farewell_error():
    typer.echo()
    typer.echo("Tranlsation Completed with errors")
    typer.echo("Please see the command line for a list of issues")
    exit(1)


# Translate a single project
def translate_project(project_dir: str, out_dir: str):
    # ! Don't create a new Unity project while in development
    # Create Unity project and copy original files
    # unity_dir = Path(out_dir, Path(project_dir).name)
    # try:
    # create_project(unity_dir)
    # copy_files(project_dir, unity_dir)
    # add_empty_scene(unity_dir)
    # except UnityError as e:
    # typer.echo(e, err=True)

    # Translate xml files in individual threads
    xml_files = [
        p
        for p in Path(project_dir).iterdir()
        if (p.is_file() and p.suffix == ".xml")
    ]
    for file in xml_files:
        typer.echo(f"Translating file: {file.name}")

        # Will return a yaml file
        xml_to_unity(file)


def main(
    in_dir: str = typer.Argument(
        ..., help="Input folder containing the xml project"
    ),
    out_dir: str = typer.Argument(
        ..., help="Output folder for the translated project"
    ),
    multiple: bool = typer.Option(False, help="Translate multiple projects?"),
    force: bool = typer.Option(False, help="Overwite OUT_DIR?"),
):
    """
    Translate W3D xml projects in IN_DIR to Unity projects in OUT_DIR

    --multiple: Translate multiple projects. \
        Each one is a subfolder of IN_DIR and OUT_DIR
    --force: Overwrite OUT_DIR folder if it exists
    """

    # Print greeting and create output folder
    greeting(in_dir, out_dir)
    try:
        validate_out(out_dir, force)
    except ValidationError as e:
        # Exit with error
        typer.echo(e.message, err=True)
        exit(1)

    # Translate project(s)
    if multiple:
        try:
            validate_in_multiple(in_dir)
        except ValidationError as e:
            typer.echo(e, err=True)

        projects = [p for p in Path(in_dir).iterdir() if p.is_dir()]
        for project_dir in projects:
            try:
                validate_project(project_dir)
            except ValidationError as e:
                typer.echo(e, err=True)

            # PARKING LOT: Optimize with async?
            try:
                translate_project(
                    project_dir,
                    out_dir,
                )
            except TranslationError as e:
                typer.echo(e, err=True)
    else:
        try:
            validate_project(in_dir)
        except ValidationError as e:
            typer.echo(e, err=True)

        try:
            translate_project(in_dir, out_dir)
        except TranslationError as e:
            typer.echo(e, err=True)

    # Print farewell and exit
    farewell()


if __name__ == "__main__":
    typer.run(main)
