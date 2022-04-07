import typer
import glob
import os

from unity import (
    UNITY_VERSION,
    UNITY_PATH,
    # create_project,
    # copy_files,
    # add_empty_scene,
)
from validate import validate_project, validate_in_multiple, validate_out
from errors import ValidationError, TranslationError, UnityError
from xml_to_unity import xml_to_unity

# TODO: Configure typer character length (100)
# TODO: Configure color/style for typer.echo
# TODO: Prompt user for confirmation if --force is used (?)

# TEMPORARY OVERRIDES (for development)
# Skip validate_out
# Skip create_project and copy_files (xml_to_unity.py)
# Only translate run.xml (xml_to_unity.py)

""" TODO NEXT
Beginning translating Story (separate PRs)
"""

is_error = False


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
def translate_project(name: str, project_dir: str, out_dir: str):
    # Create Unity project and copy original files
    # unity_dir = os.path.join(out_dir, name)
    # try:
    # create_project(unity_dir)
    # copy_files(project_dir, unity_dir)
    # add_empty_scene(unity_dir)
    # except UnityError as e:
    # handleError(e)

    # Translate xml files in individual threads
    xml_files = [
        os.path.join(project_dir, file)
        for file in os.listdir(project_dir)
        if file.endswith(".xml")
    ]
    for file in xml_files:
        typer.echo(f"Translating file: {os.path.basename(file)}")

        # Will return a yaml file
        xml_to_unity(file)


def handleError(e):
    typer.echo(e, err=True)
    global is_error
    is_error = True


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
            handleError(e)

        for idx, project_dir in enumerate(glob.glob(f"{in_dir}/*/")):
            try:
                validate_project(project_dir)
            except ValidationError as e:
                handleError(e)

            # PARKING LOT: Optimize with async?
            try:
                translate_project(
                    os.path.basename(os.path.normpath(project_dir)),
                    project_dir,
                    out_dir,
                )
            except TranslationError as e:
                handleError(e)
    else:
        try:
            validate_project(in_dir)
        except ValidationError as e:
            handleError(e)

        try:
            translate_project(
                os.path.basename(os.path.normpath(in_dir)), in_dir, out_dir
            )
        except TranslationError as e:
            handleError(e)

    # Print farewell and exit
    farewell_error() if is_error else farewell()


if __name__ == "__main__":
    typer.run(main)
