from dsa.challenges.array_reverse.array_reverse import reverseArray


def test_one():
    actual = reverseArray([1, 2, 3, 4, 5, 6])
    expected = [6, 5, 4, 3, 2, 1]
    assert actual == expected