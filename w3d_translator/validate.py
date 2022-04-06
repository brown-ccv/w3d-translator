import os
import sys
import shutil


# Ensure input folder is a directory
# TODO: More dir validation?
def validate_input(dir):
    if not os.path.isdir(dir):
        sys.exit(f"Error: INPUT is not a directory: {dir}")

    return


# Creates output directory, if valid
# TODO: More dir validation?
def validate_output(dir, force):
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
