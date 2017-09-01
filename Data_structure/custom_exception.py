class Error(Exception):
    pass


class RangeError(Error):
    def __init__(self, message):
        self.message = message

class SizeError(Error):
    def __init__(self, message):
        self.message = message
