import typer
from pathlib import Path

from generateDS.subclasses import parse
from unity import (
    copy_files,
    create_project,
    build_project,
    UNITY_VERSION,
)
from validate import validate_project, validate_out, validate_xml
from errors import ValidationError, XmlError, UnityError
from translate import translate_objects


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


# Translate a single project
def translate_project(project_dir: Path, out_dir: Path, dev: bool = False):
    '''TODO: NEW SUBPROCCESS
        Copy Base project
        Copy files into originals subfolder
        For each XML file:
            Validate file
            Create new scene from CAVE.scenetemplate
                Do anything with C# callbacks?
            Parse xml file into Python
            Clean python
            Create classes and project (Move to C# here?)
    '''
    try:
        typer.echo(f"Translating project:\t {cyan(project_dir.name)}")
        validate_project(project_dir)
        unity_dir = Path(out_dir, project_dir.name)

        # Create Unity project
        if not dev:
            
            # Copy starter project 
            copy_files(Path("unity/CAVE"), unity_dir)
            # Copy original project into Unity Assets folder
            copy_files(project_dir, Path(unity_dir, "Assets", "Originals"))
            

        # Translate .xml files to .unity files (skip invalid)
        xml_files = [
            p
            for p in project_dir.iterdir()
            if (p.is_file() and p.suffix == ".xml")
        ]
        for file in xml_files:
            typer.echo(f"Translating file:\t {green(file.name)}")
            try:
                validate_xml(file)
            except XmlError as e:
                typer.echo(red(e), err=True)
            else:
                # Build and clean Story
                story = parse(file, silence=True)

                # objects = translate_objects(story.ObjectRoot.Object)
                # print(objects)

                # build_project(unity_dir, story)
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
