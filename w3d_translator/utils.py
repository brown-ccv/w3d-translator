# Converts "True" and "False" to their boolean values
def tf_to_bool(string: str):
    if string.lower() == "true":
        return True
    elif string.lower() == "false":
        return False
    else:
        print("Error reading attribute", string)
        return None


# Converts an "[r], [g], [b]" string to an RGBA dict. Alpha is always 255
def str_to_rgba(string: str):
    arr = string.split(", ")
    return {"r": int(arr[0]), "g": int(arr[1]), "b": int(arr[2]), "a": 255}
