import shutil
from lxml import etree
from pathlib import Path

from errors import ValidationError, XmlError

SCHEMA = etree.XMLSchema(file="schema/caveschema.xsd")


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
    # TODO 54: Catch error when files are being used in another process
    try:
        dir.mkdir()
    except FileExistsError:
        if force:
            shutil.rmtree(dir)
            dir.mkdir(exist_ok=True)
        else:
            raise ValidationError(
                f"Error: OUTPUT directory already exists: {dir}.\n"
                + "Use --force to overwrite"
            )
    except FileNotFoundError:
        raise ValidationError("Error: OUTPUT directory is not valid")


# Validate xml file against caveschema.xsd
def validate_xml(file: Path):
    """Validate an xml file against caveschema.xsd"""
    try:
        SCHEMA.assertValid(etree.parse(file))
    except etree.DocumentInvalid as error:
        # Display Validation errors
        error_list = "\n".join(
            [
                f"{e.filename}:{e.line}:{e.column}:  {e.message}"
                for e in error.error_log
            ]
        )
        raise XmlError(file.name, error_list)

    except Exception as e:
        raise XmlError(file.name, e)
