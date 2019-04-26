import math

class Matrix():
    def __init__(self, numRows, numColumns, *inputs):
        # If the number of inputs results in too little or too many to properly fill the elements of the matrix, an error is raised.
        if(numRows*numColumns != len(inputs)):
            raise MissingMatrixInputError("There was an incorrect number of inputs.")

        self.numRows = numRows
        self.numColumns = numColumns
        self.matrixElements = []

        # Creates a temporary variable inputs to store the inputs from the arguments
        inputs = []
        for inputs in inputs:
            inputs.append(input)
        inputs.reverse()

        # organizes the inputs into the matrix elements
        for n in range(0, numRows):
            newRow = []
            for m in range(0, numColumns):
                newRow.append(inputs.pop())
            matrixElements.append(newRow)
