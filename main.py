import math
from MissingMatrixInputError import MissingMatrixInputError



class Matrix():
    def __init__(self, numRows, numColumns, *inputs):
        # If the number of inputs results in too little or too many to properly fill the elements of the matrix, an error is raised.
        if(numRows*numColumns != len(inputs)):
            raise MissingMatrixInputError("There was an incorrect number of inputs.")

        for input in inputs:
            self.__isNumber__(input)

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

    # A function to display the matrix as a matrix on the screen
    def to_string(self):
        stringRepresentation  = ""
        for n in range(0, self.numRows):
            stringRepresentation = stringRepresentation + "[ "
            for m in range(0, self.numColumns):
                stringRepresentation = stringRepresentation + str(self.matrixElements[n][m]) + " "
            stringRepresentation = stringRepresentation + "]" + "\n"

        return stringRepresentation;

    # Function to multiply the matrix by a scalar
    def scalar_mult(self, alpha):
        self.__isNumber__(alpha)

        for n in range(0, self.numRows):
            for m in range(0, self.numColumns):
                self.matrixElements[n][m] = self.matrixElements[n][m] * alpha

    # Private function to perform a row operation - multiply a row by a scalar
    def __rowMult__(self, row, scalar):
        self.__isNumber__(scalar, row)
        if row > self.numRows or row <= 0:
            raise MissingMatrixInputError("There is no row with that number!")

        for m in range(0, self.numColumns):
            self.matrixElements[row - 1][m] = self.matrixElements[row - 1][m] * scalar

    # Private function to switch two numRows
    def __switchRows__(self, rowOne, rowTwo):
        self.__isNumber__(rowOne, rowTwo)
        if rowOne > self.numRows or rowOne <= 0:
            raise MissingMatrixInputError("The first mentioned row does not exist")
        if rowTwo > self.numRows or rowTwo <= 0:
            raise MissingMatrixInputError("The second mentioned row does not exist")
        tempRow = []
        for m in range(0, self.numColumns):
            tempRow.append(self.matrixElements[rowOne - 1][m])
            self.matrixElements[rowOne - 1][m] = self.matrixElements[rowTwo - 1][m]
            self.matrixElements[rowTwo - 1][m] = tempRow[m]


    # Simple function to raise a TypeError for nonnumbers
    def __isNumber__(self, *inputs):
        for input in inputs:
            if not isinstance(input, int) and not isinstance(input, float):
                raise TypeError()


# Simple tests since I don't know junit test in python yet since I'm a noob
x = Matrix(2, 3, 1, 0, 5, -1, 8, 5)
print(x.to_string())
x.scalar_mult(5)
print(x.to_string())
x.__rowMult__(2,4)
print(x.to_string())
x.__switchRows__(1,2)
print(x.to_string())
