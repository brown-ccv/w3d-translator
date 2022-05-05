import shutil
from pathlib import Path

from errors import ValidationError


# Validate directory
def validate_project(dir: Path):

    # Path must be a directory
    if not dir.is_dir():
        raise ValidationError(f"Error: Project is not a directory: {dir}")

    # Project must contain an xml file
    xml_files = list(filter(lambda file: file.suffix == ".xml", dir.iterdir()))
    if not len(xml_files):
        raise ValidationError(
            f"Error: Project does not contain an xml file: {dir}"
        )


# Creates output directory, if valid
def validate_out(dir: Path, force: bool):
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
