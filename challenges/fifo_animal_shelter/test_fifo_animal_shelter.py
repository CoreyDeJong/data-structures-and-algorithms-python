import pytest

from fifo_animal_shelter import Stack, Node, AnimalShelter

def test_create_node():
    one = Node(1)
    actual= one.value
    expected = 1
    assert actual == expected

# Test Enqueue Dog
def test_enqueue_dog():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("cat")
    actual = a.dog_shelter.peek()
    expected = "dog"
    assert actual == expected


# Test Enqueue Cat
def test_enqueue_cat():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("cat")
    actual = a.cat_shelter.peek()
    expected = "cat"
    assert actual == expected


# Test Enqueue Bad Cat
def test_enqueue_nocat():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    # a.enqueue("cat")
    # a.enqueue("cat")
    actual = a.cat_shelter.peek()
    expected = 'empty queue'
    assert actual == expected

# Test Enqueue Bad Doggie
def test_enqueue_nodog():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    # a.enqueue("cat")
    # a.enqueue("cat")
    actual = a.cat_shelter.peek()
    expected = 'empty queue'
    assert actual == expected


# Test deque dog
def test_dequeue_dog():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("cat")
    actual = a.dequeue("dog")
    expected = "dog"
    assert actual == expected

# Test deque cat
def test_dequeue_dog():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("cat")
    actual = a.dequeue("cat")
    expected = "cat"
    assert actual == expected

# Test deque Pineapple
def test_dequeue_pin():
    a = AnimalShelter()
    a.enqueue("dog")
    a.enqueue("dog")
    a.enqueue("cat")
    a.enqueue("cat")
    actual = a.dequeue("pineapple")
    expected = None
    assert actual == expected
