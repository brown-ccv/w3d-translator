import typer
from glob import glob

from unity import UNITY_PATH, UNITY_VERSION
from validate import validate_input, validate_output

# TODO: Configure typer character length (100)
# TODO: Configure color/style for typer.echo
# TODO: Prompt user for confirmation if --force is used (?)

# Opening message
def greeting():
    typer.echo("W3D TRANSLATOR")
    typer.echo(f"Unity Version:\t {UNITY_VERSION}")
    typer.echo(f'Please ensure Unity is installed at {UNITY_PATH}\n')

# Info message about translating multiple projects
def info_multiple(in_dir, out_dir):
    typer.echo(f"Translating multiple projects from '{in_dir}' to '{out_dir}'")
    return

# Info message about translating a single project
def info_single(in_dir, out_dir):
    typer.echo(f"Translating project from '{in_dir}' to '{out_dir}'")
    return

def main(         
    in_dir: str = typer.Argument(..., help="Input folder containing the xml project"),
    out_dir: str = typer.Argument(..., help="Output folder for the translated project"),
    multiple: bool = typer.Option(False, help="Translate multiple projects?"),
    force: bool = typer.Option(False, help="Overwite OUT_DIR?"),
):
    """
    Translate W3D xml projects in IN_DIR to Unity projects in OUT_DIR
    
    --multiple: Translate multiple projects. Each one is a subfolder of IN_DIR and OUT_DIR
    --force: Overwrite OUT_DIR folder if it exists
    """

    # Print greeting and validate parameters
    greeting()
    validate_input(in_dir)
    validate_output(out_dir, force)

    if multiple:
        info_multiple(in_dir, out_dir)
        
        # Glob only collects folders 
        projects = glob(f'{input}/*/')
        typer.echo("Projects:", projects)
        
        # TODO: Add warning if individual files in "in_dir"

        # Validate input subfolders
        [validate_input(project) for project in projects]

        
    else:
        info_single(in_dir, out_dir)
        

if __name__ == '__main__':
    typer.run(main)