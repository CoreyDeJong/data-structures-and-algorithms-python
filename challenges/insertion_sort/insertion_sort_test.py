import pytest

from insertion_sort import insertion_sort

def test_sort1():
    arr = [8,4,23,42,16,15]
    actual = insertion_sort(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort2():
    arr = [20,18,12,8,5,-2]
    actual = insertion_sort(arr)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_sort3():
    arr = [5,12,7,5,5,7]
    actual = insertion_sort(arr)
    expected = [5,5,5,7,7,12]
    assert actual == expected


def test_sort4():
    arr = [2,3,5,7,13,11]
    actual = insertion_sort(arr)
    expected = [2,3,5,7,11,13]
    assert actual == expected
