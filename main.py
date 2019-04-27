import math
import MissingMatrixInputError


class Matrix():
    def __init__(self, numRows, numColumns, *inputs):
        # If the number of inputs results in too little or too many to properly fill the elements of the matrix, an error is raised.
        if(numRows*numColumns != len(inputs)):
            raise MissingMatrixInputError("There was an incorrect number of inputs.")

        for input in inputs:
            if not isinstance(input, int) and not isinstance(input, float):
                raise TypeError()

        self.numRows = numRows
        self.numColumns = numColumns
        self.matrixElements = []

        # Creates a temporary variable inputs to store the inputs from the arguments
        functionInputs = []
        for input in inputs:
            functionInputs.append(input)
        functionInputs.reverse()

        # organizes the inputs into the matrix elements
        for n in range(0, numRows):
            newRow = []
            for m in range(0, numColumns):
                newRow.append(functionInputs.pop())
            self.matrixElements.append(newRow)

    def to_string(self):
        stringRepresentation  = ""
        for n in range(0, self.numRows):
            stringRepresentation = stringRepresentation + "[ "
            for m in range(0, self.numColumns):
                stringRepresentation = stringRepresentation + str(self.matrixElements[n][m]) + " "
            stringRepresentation = stringRepresentation + "]" + "\n"

        return stringRepresentation;


    def scalar_mult(self, alpha):
        if not isinstance(alpha, int) and not isinstance(alpha, float):
            raise TypeError()

        for n in range(0, self.numRows):
            for m in range(0, self.numColumns):
                self.matrixElements[n][m] = self.matrixElements[n][m] * alpha

x = Matrix(2, 3, 1, 2, 3, 4, 5, 6)
print(x.to_string())
x.scalar_mult(5.5)
print(x.to_string())
