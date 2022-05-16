from errors import TranslationError


def str_to_tuple(string: str) -> tuple:
    """Converts a comma seperated string into a tuple"""
    split = (
        string.replace("(", "").replace(")", "").replace(" ", "").split(",")
    )
    list = [float(x) for x in split]
    return tuple(list)


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
