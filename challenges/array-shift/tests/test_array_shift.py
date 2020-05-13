
from array_shift.array_shift import insertShiftArray

def test_shift1():
    actual = insertShiftArray((2,4,6,8),5)
    expected = 2,4,5,6,8
    assert actual == expected
