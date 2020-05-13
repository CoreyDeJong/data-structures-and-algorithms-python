# from array_shift import __version__


# def test_version():
#     assert __version__ == '0.1.0'


from array_shift.array_shift import insertShiftArray

def test_shift1():
    actual = insertShiftArray(1)
    expected = 1
    assert actual == expected
