from array_binary_search.array_binary_search import BinarySearch


def test_versionH():
    actual = BinarySearch((1,2,7,33,45,46,77,78,89),77)
    expected = 6
    assert actual == expected

def test_versionL():
    actual = BinarySearch((1,2,7,33,45,46,77,78,89),33)
    expected = 3
    assert actual == expected

# def test_version0():
#     actual = find_index((1,2,7,33,45,46,77,78,89),3)
#     expected = -1
#     assert actual == expected
