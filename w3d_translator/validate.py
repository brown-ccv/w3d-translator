import shutil
from pathlib import Path

from errors import ValidationError


def validate_project(dir: str):

    # Path must be a directory
    if not Path(dir).is_dir():
        raise ValidationError(f"Error: Project is not a directory: {dir}")

    # Project must contain an xml file
    xml_files = list(
        filter(lambda file: file.suffix == ".xml", Path(dir).iterdir())
    )
    if not len(xml_files):
        raise ValidationError(
            f"Error: Project does not contain an xml file: {dir}"
        )


def validate_in_multiple(dir: str):
    # Path must be a directory
    if not Path(dir).is_dir():
        raise ValidationError(f"Error: IN_DIR is not a directory: {dir}")

    # Folder should only contain subfolders
    non_dirs = list(
        filter(
            lambda file: not Path(dir, file).is_dir(),
            Path(dir).iterdir(),
        )
    )
    if len(non_dirs):
        raise ValidationError(
            f"Error: IN_DIR should not contain any files: {non_dirs}"
        )


# Creates output directory, if valid
def validate_out(dir, force):
    dir = Path(dir)
    try:
        dir.mkdir()
    except FileExistsError:
        if force:
            shutil.rmtree(dir)
            dir.mkdir(exist_ok=True)
        else:
            raise ValidationError(
                f"Error: OUTPUT directory already exists: {dir}. "
                + "Use --force to overwrite"
            )
    except FileNotFoundError:
        raise ValidationError("Error: OUTPUT directory is not valid")
