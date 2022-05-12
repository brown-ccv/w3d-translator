from errors import TranslationError


def split_str(string: str, parenthesis=True) -> list:
    """Splits a string based on commas, removes parenthesis if in str"""
    string = string.replace("(", "").replace(")", "")

    return string.split(", ")


def tf_to_bool(string: str) -> bool:
    """Converts 'True' and 'False' to their boolean values"""
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False
    else:
        raise TranslationError(
            f"Attribute {string} was neither 'true' or 'false'"
        )


def str_to_rgba(string: str) -> dict:
    """
    Converts an "[r], [g], [b]" string to an RGBA dict.
    Alpha is always 255.
    """
    # arr = string.split(", ")
    list = split_str(string, parenthesis=False)
    return {"r": int(list[0]), "g": int(list[1]), "b": int(list[2]), "a": 255}


def str_to_xy(string: str) -> dict:
    list = split_str(string)
    return {"x": float(list[0]), "y": float(list[1])}


def str_to_xyz(string: str) -> dict:
    list = split_str(string)
    return {"x": float(list[0]), "y": float(list[1]), "z": float(list[2])}
