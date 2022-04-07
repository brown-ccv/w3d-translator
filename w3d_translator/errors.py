class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class UnityError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TranslationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
