import os
import shutil


class ValidationException(Exception):
    def __init__(self, message):
        self.message = message


def validate_project(dir: str):
    # Path must be a directory
    if not os.path.isdir(dir):
        raise ValidationException(f"Error: Project is not a directory: {dir}")

    # Project must contain an xml file
    xml_files = list(
        filter(lambda file: file.endswith(".xml"), os.listdir(dir))
    )
    if not len(xml_files):
        raise ValidationException(
            f"Error: Project does not contain an xml file: {dir}"
        )


def validate_in_multiple(dir: str):
    # Path must be a directory
    if not os.path.isdir(dir):
        raise ValidationException(f"Error: IN_DIR is not a directory: {dir}")

    # Folder should only contain subfolders
    non_dirs = list(
        filter(
            lambda file: not os.path.isdir(os.path.join(dir, file)),
            os.listdir(dir),
        )
    )
    if len(non_dirs):
        raise ValidationException(
            f"Error: IN_DIR should not contain any files: {non_dirs}"
        )


# Creates output directory, if valid
def validate_out(dir, force):
    try:
        if force:
            shutil.rmtree(dir)
        os.mkdir(dir)
    except FileExistsError:
        raise ValidationException(
            f"Error: OUTPUT directory already exists: {dir}. "
            + "Use --force to overwrite"
        )
    except FileNotFoundError:
        raise ValidationException("Error: OUTPUT directory is not valid")
