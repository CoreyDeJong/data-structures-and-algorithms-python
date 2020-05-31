import pytest
from linked_list.linked_list import LinkedList, Node

## linkedlist head
def test_instance():
    ll = LinkedList()
    assert ll.head == None

## linkedlist repr
def test_linked_list_repr():
    ll = LinkedList()
    actual = repr(ll)
    expected = "LinkedList : None"
    assert actual == expected



#### Insert ######

## linkedlist str
# Define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
# "{ a } -> { b } -> { c } -> NULL"
def test_linked_list_str():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert str(ll) == "{ bananas } -> { apples } -> NULL"

## linkedlist insert
def test_insert_empty():
    ll = LinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"

## linkedlist
def test_insert_full():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"


#### Append #######

def test_append_1():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.append("pineapple")
    assert str(ll) == "{ bananas } -> { apples } -> { pineapple } -> NULL"


#### Insert Before #######

def test_insert_1():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insertBefore("pineapple")
    assert str(ll) == "{ pineapple } -> { bananas } -> { apples } -> NULL"

#### Insert After #######

def test_insert_2():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    ll.insertAfter("b", "c")
    assert str(ll) == "{ b } -> { c } -> { a } -> NULL"


#### Includes ####

def test_includes_true():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("tomato")
    actual = ll.includes("apples")
    expected = True
    assert actual == expected

def test_includes_false():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("tomato")
    actual = ll.includes('pineapple')
    expected = False
    assert actual == expected

#### Kth from End ###########
# test 1
def test_too_big(node_length):
    actual = node_length.from_end(8)
    expected = "k is too big"
    assert actual == expected

# test 2
def test_same_length(node_length):
    actual = node_length.from_end(4)
    expected = 4
    assert actual == expected

# test 3
def test_negative(node_length):
    actual = node_length.from_end(-2)
    expected = "k is bigger than length"
    assert actual == expected

# test 4
def test_same_length():
    ll = LinkedList()
    ll.insert(1)
    return ll
    actual = from_end(1)
    expected = 1
    assert actual == expected

# Test 5
def test_some_middle(node_length):
    actual = node_length.from_end(2)
    expected = 2
    assert actual == expected


### Error Test ######

def test_node_exception():
    with pytest.raises(TypeError):
        Node("sample", "this is NOT a Node")

def test_node_exception2():
    ll = LinkedList()
    ll.insert("a")
    ll.insert("b")
    with pytest.raises(ValueError):
        ll.insertAfter("f", "c")



######################

@pytest.fixture()
def prep_fruit():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("bananas2")

@pytest.fixture
def node_length():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll
