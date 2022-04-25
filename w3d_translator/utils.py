from errors import TranslationError


# Converts "True" and "False" to their boolean values
def tf_to_bool(string: str) -> bool:
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False
    else:
        raise TranslationError(f"Attribute {string} was neither 'true' or 'false'")


# Converts an "[r], [g], [b]" string to an RGBA dict. Alpha is always 255
def str_to_rgba(string: str) -> dict:
    arr = string.split(", ")
    return {"r": int(arr[0]), "g": int(arr[1]), "b": int(arr[2]), "a": 255}
