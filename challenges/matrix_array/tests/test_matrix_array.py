from matrix_array.matrix_array import matrix_arr


def test_matrix1():
    actual = matrix_arr([[1,2,3],[3,5,7],[1,7,10]])
    expected = [6,15,18]
    assert actual == expected

def test_matrix2():
    actual = matrix_arr([[0,1,5],[-4,7,2],[-3,12,11]])
    expected = [6,5,20]
    assert actual == expected