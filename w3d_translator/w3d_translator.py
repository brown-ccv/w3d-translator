import typer
from pathlib import Path

from unity import (
    UNITY_VERSION,
    create_project,
    copy_files,
    add_empty_scene,
    build_project
)
from validate import validate_project, validate_out
from errors import ValidationError, TranslationError, UnityError
from read_xml import read_xml


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


# Farewell message on error
def farewell_error():
    typer.echo()
    typer.echo("Tranlsation Completed with errors")
    typer.echo("Please see the command line for a list of issues")
    exit(1)


# Translate a single project
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    try:
        typer.echo(f"Translating project:\t {cyan(project_dir.name)}")
        validate_project(project_dir)

        # Create Unity project and copy original files
        unity_dir = Path(out_dir, project_dir.name)
        if not dev:
            create_project(unity_dir)
            copy_files(project_dir, unity_dir)
            add_empty_scene(unity_dir)

        # Translate .xml files to .unity files
        xml_files = [
            p
            for p in project_dir.iterdir()
            if (p.is_file() and p.suffix == ".xml")
        ]
        for file in xml_files:
            # Build Story dataclass and Unity project
            typer.echo(f"Translating file:\t {green(file.name)}")
            story = read_xml(file)
            build_project(unity_dir, story)

    except (ValidationError, UnityError, TranslationError) as e:
        typer.echo(red(e), err=True)


def main(
    in_dir: Path = typer.Argument(
        ..., help="Input folder containing the xml project"
    ),
    out_dir: Path = typer.Argument(
        ..., help="Output folder for the translated project"
    ),
    multiple: bool = typer.Option(False, help="Translate multiple projects?"),
    force: bool = typer.Option(False, help="Overwite OUT_DIR?"),
    dev: bool = typer.Option(False, help="Don't create Unity projects"),
):
    """
    Translate W3D xml projects in IN_DIR to Unity projects in OUT_DIR
    """

    # Print greeting and create output folder
    greeting(in_dir, out_dir)
    try:
        validate_out(out_dir, force)
    except ValidationError as e:
        # Exit with error
        typer.echo(red(e.message), err=True)
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
