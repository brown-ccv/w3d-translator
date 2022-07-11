class ValidationError(Exception):
    """Raised on invalid folder structure - in_dir and out_dir"""

    pass


class UnityError(Exception):
    """Raised when the Unity subprocess fails to execute"""

    pass


class CopyError(Exception):
    """Raised when python fails to copy files/folders"""

    pass


class XmlError(Exception):
    """Raised when an XML file does not follow the defined schema"""

    def __init__(self, filename, error):
        self.filename = filename
        self.error = error
        super().__init__(f"{filename} does not conform to the defined schema")

    def __str__(self):
        return (
            f"{self.filename} does not match schema\n"
            + self.error
            + "\n"
            + f"Skipping {self.filename}\n"
        )
