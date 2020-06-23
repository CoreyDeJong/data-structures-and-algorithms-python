import pytest
from repeated_word import repeater

def test_1():
    stmt = "Once upon a time, there was a brave princess who..."
    actual = repeater(stmt)
    expected = "a"
    assert actual == expected

# def test_2():
#     stmt = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
#     actual = repeater(stmt)
#     expected = "summer"
#     assert actual == expected
