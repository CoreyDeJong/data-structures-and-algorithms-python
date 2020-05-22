from array_shift.array_shift import insertShiftArray

def test_shift_even_array():
    actual = insertShiftArray([2, 4, 6, 8], 5)
    expected = [2, 4, 5, 6, 8]
    assert actual == expected

def test_shift_even_array2():
    actual = insertShiftArray([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 100)
    expected = [2, 4, 6, 8, 10, 100, 12, 14, 16, 18, 20]
    assert actual == expected

def test_shift_odd_array():
    actual = insertShiftArray([1, 2, 3, 5, 6, 7], 4)
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert actual == expected

def test_shift_odd_array2():
    actual = insertShiftArray([1, 2, 3, 4, 5, 7,  8, 9, 10, 11], 6)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert actual == expected