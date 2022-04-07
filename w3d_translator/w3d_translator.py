import typer
import glob
import os

from unity import (
    UNITY_VERSION,
    UNITY_PATH,
    create_project,
    copy_files,
    add_empty_scene,
)
from validate import validate_input, validate_output
from xml_to_unity import xml_to_unity

# TODO: Configure typer character length (100)
# TODO: Configure color/style for typer.echo
# TODO: Prompt user for confirmation if --force is used (?)

# TEMPORARY OVERRIDES (for development)
# Skip validate_output
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


# Translate a single project
def translate_project(name: str, project_dir: str, out_dir: str):
    typer.echo(f"Translating Project: {name}")

    # Create Unity project and copy original files
    unity_dir = os.path.join(out_dir, name)

    # Create Unity project
    create_project(unity_dir)
    copy_files(project_dir, unity_dir)
    add_empty_scene(unity_dir)

    # Translate xml files in individual threads
    xml_files = [
        # os.path.join(project_dir, "run.xml") # TEMP Just use run.xml
        os.path.join(project_dir, file)
        for file in os.listdir(project_dir)
        if file.endswith(".xml")
    ]
    for idx, file in enumerate(xml_files):
        typer.echo(f"Translating file: {name}")

        # Will return a yaml file
        xml_to_unity(file)


# Ending message
def farewell():
    typer.echo()
    typer.echo("Translation Complete!")


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

    # Print greeting and validate arguments
    greeting(in_dir, out_dir)
    validate_input(in_dir)
    validate_output(out_dir, force)

    # Each project runs on a different thread
    if multiple:
        for idx, project_dir in enumerate(glob.glob(f"{in_dir}/*/")):
            validate_input(project_dir)
            translate_project(
                os.path.basename(os.path.normpath(project_dir)),
                project_dir,
                out_dir,
            )
    else:
        translate_project(
            os.path.basename(os.path.normpath(in_dir)), in_dir, out_dir
        )

    # Print farewell and exit
    farewell()


if __name__ == "__main__":
    typer.run(main)
