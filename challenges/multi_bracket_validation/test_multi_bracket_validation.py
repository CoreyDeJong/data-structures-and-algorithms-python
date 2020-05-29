import pytest

from multi_bracket_validation import Stack, Node, Validation

def test_create_node():
    one = Node(1)
    actual= one.value
    expected = 1
    assert actual == expected

def test_dog_house():
    v=Validation()
    actual = v.multi_bracket_validation("(dog)")
    expected = True
    assert actual == expected

def test_two_pairs():
    v=Validation()
    actual = v.multi_bracket_validation("()[]")
    expected = True
    assert actual == expected

def test_three_pairs():
    v=Validation()
    actual = v.multi_bracket_validation("()[]{}")
    expected = True
    assert actual == expected

def test_fail():
    v=Validation()
    actual = v.multi_bracket_validation("(]{)})")
    expected = False
    assert actual == expected

def test_fail_with_integers_strings():
    v=Validation()
    actual = v.multi_bracket_validation("(ho88dy]{)})")
    expected = False
    assert actual == expected
















# # Test Enqueue Dog
# def test_enqueue_dog():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     a.enqueue("cat")
#     a.enqueue("cat")
#     actual = a.dog_shelter.peek()
#     expected = "dog"
#     assert actual == expected


# # Test Enqueue Cat
# def test_enqueue_cat():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     a.enqueue("cat")
#     a.enqueue("cat")
#     actual = a.cat_shelter.peek()
#     expected = "cat"
#     assert actual == expected


# # Test Enqueue Bad Cat
# def test_enqueue_nocat():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     # a.enqueue("cat")
#     # a.enqueue("cat")
#     actual = a.cat_shelter.peek()
#     expected = 'empty queue'
#     assert actual == expected

# # Test Enqueue Bad Doggie
# def test_enqueue_nodog():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     # a.enqueue("cat")
#     # a.enqueue("cat")
#     actual = a.cat_shelter.peek()
#     expected = 'empty queue'
#     assert actual == expected


# # Test deque dog
# def test_dequeue_dog():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     a.enqueue("cat")
#     a.enqueue("cat")
#     actual = a.dequeue("dog")
#     expected = "dog"
#     assert actual == expected

# # Test deque cat
# def test_dequeue_dog():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     a.enqueue("cat")
#     a.enqueue("cat")
#     actual = a.dequeue("cat")
#     expected = "cat"
#     assert actual == expected

# # Test deque Pineapple
# def test_dequeue_pin():
#     a = AnimalShelter()
#     a.enqueue("dog")
#     a.enqueue("dog")
#     a.enqueue("cat")
#     a.enqueue("cat")
#     actual = a.dequeue("pineapple")
#     expected = None
#     assert actual == expected
