class MissingMatrixInputError(Exception):
    """Raised when a matrix constructor doesn't have the right number of arguments to implement the matrix

        Attributes:
            message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
