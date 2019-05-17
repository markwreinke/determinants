class NotApplicableError(Exception):
    """Raised when a matrix cannot perform the requested action

        Attributes:
            message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
