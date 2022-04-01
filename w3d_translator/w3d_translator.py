import typer
from glob import glob
from unity import UNITY_PATH, UNITY_VERSION
from validate import validate_input, validate_output

# Opening message
def greeting():
    print("W3D TRANSLATOR")
    print(f"Unity Version:\t {UNITY_VERSION}")
    print(f'Please ensure Unity is installed at {UNITY_PATH}\n')

def main(
    input: str,             # Folder containing the xml project
    output: str,            # Output folder for the translated project
    multiple: bool = False,  # Translate multiple projects?
    force: bool = False,     # Overwrite contents out output?
):
    """
    Translate W3D projects from INPUT to Unity projects in OUTPUT
    
    If --multiple: individual projects are subfolders of INPUT and OUTPUT
    """

    # Print greeting and validate parameters
    greeting()
    validate_input(input)
    validate_output(output, force)

    if multiple:
        projects = glob(f'{input}/*/')

        # Validate input subfolders
        [validate_input(project) for project in projects]

        print(f"Translating multiple projects from '{input}' to '{output}'")
    else:
        print(f"Translating project from '{input}' to '{output}'")

if __name__ == '__main__':
    typer.run(main)