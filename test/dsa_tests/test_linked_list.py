import pytest
from dsa.data_structures.linked_list.linked_list.linked_list import LinkedList, Node

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

#### K from End ###########

def test_too_big(node_length):
    actual = node_length.from_end(8)
    expected = "k is too big"
    assert actual == expected

# def test_same_length(node_length):
#     actual = node_length.from_end(4)
#     expected = "Four"
#     assert actual == expected


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


# test to see if there is a node connected to lucy
# isinstance(lucy.next, node)

@pytest.fixture()
def prep_fruit():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    ll.insert("bananas2")

@pytest.fixture
def node_length():
    ll = LinkedList()
    ll.insert("One")
    ll.insert("Two")
    ll.insert("Three")
    ll.insert("Four")
    return ll
