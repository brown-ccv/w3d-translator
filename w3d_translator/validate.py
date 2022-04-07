import os
import sys
import shutil

# TODO: Don't sys.exit, return the error


def validate_project(dir: str):
    # Path must be a directory
    if not os.path.isdir(dir):
        sys.exit(f"Error: Project is not a directory: {dir}")

    # Project must contain an xml file
    xml_files = list(
        filter(lambda file: file.endswith(".xml"), os.listdir(dir))
    )
    if not len(xml_files):
        sys.exit(f"Error: Project does not contain an xml file: {dir}")
    return


def validate_in_multiple(dir: str):
    # Path must be a directory
    if not os.path.isdir(dir):
        sys.exit(f"Error: IN_DIR is not a directory: {dir}")

    # Folder should only contain subfolders
    non_dirs = list(
        filter(
            lambda file: not os.path.isdir(os.path.join(dir, file)),
            os.listdir(dir),
        )
    )
    if len(non_dirs):
        sys.exit(f"Error: IN_DIR should not contain any files: {non_dirs}")
    return


# Creates output directory, if valid
def validate_out(dir, force):
    try:
        os.mkdir(dir)
    except FileExistsError:
        if force:
            # Remove and make directory
            shutil.rmtree(dir)
            os.mkdir(dir)
        else:
            sys.exit(
                f"Error: OUTPUT directory already exists: {dir}.\n"
                + "Use --force to overwrite"
            )
    except FileNotFoundError:
        sys.exit("Error: OUTPUT directory is not valid")
