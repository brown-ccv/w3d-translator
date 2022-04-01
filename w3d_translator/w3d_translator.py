import typer
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

    # if multiple:
    #     # TODO Validate input for all subfolders
    #     print(multiple)
    # else:
    #     print(multiple)

if __name__ == '__main__':
    typer.run(main)