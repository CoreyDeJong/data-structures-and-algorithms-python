from array_binary_search.array_binary_search import BinarySearch

def test_version_even():
    array = [1,2,7,33,45,46,77,78,89]
    n = 77
    actual = BinarySearch(array, n)
    expected = 6
    assert actual == expected

def test_version_odd():
    array = [1,2,7,33,45,46,55,77,78,89]
    n = 77
    actual = BinarySearch(array, n)
    expected = 7
    assert actual == expected

def test_version_none():
    array = [1,2,7,33,45,46,55,77,78,89]
    n = 49
    actual = BinarySearch(array, n)
    expected = -1
    assert actual == expected