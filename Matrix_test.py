from Matrix import Matrix


def test_determinant():
    testMatrix = Matrix(3,3,5,0,0,0,7,0,0,0,4);
    assert testMatrix.determinant() == 140, "Should be 140"

def test_to_string():
    testMatrix = Matrix(2, 3, 1, 0, 5, -1, 8, 5);
    testString = "[ 1 0 5 ]\n[ -1 8 5 ]\n";
    assert testMatrix.to_string() == testString, "\nShould be: \n[ 1 0 5 ] \n[ -1 8 5 ]"

def test_scalar_mult():
    ##### DOESN't WORK YET AND IDK WHY YET 
    testMatrix = Matrix(2, 3, 1, 0, 5, -1, 8, 5);
    finalMatrix = Matrix(2, 3, 5, 0, 25, -5, 40, 25);
    medianMatrix = testMatrix.scalar_mult(5)
    assert  medianMatrix == testMatrix.scalar_mult(5) == finalMatrix, "Should be: \n" + Matrix(2, 3, 5, 0, 25, -5, 40, 25).to_string()

if __name__=="__main__":
    test_determinant()
    test_to_string()
    test_scalar_mult()
    print("Everything passed")
