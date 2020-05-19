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


#### Includes ####
# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

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



####### Appends #############

## linkedlist
def test_append():
    ll = LinkedList()
    ll.append("apples")
    ll.append("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"



### Error Test ######

def test_node_exception():
    with pytest.raises(TypeError):
        Node("sample", "this is NOT a Node")

# test to see if there is a node connected to lucy
# isinstance(lucy.next, node)

# @pytest.fixture()
# def prep_fruit():
#     ll = LinkedList()
#     ll.insert("apples")
#     ll.insert("bananas")
#     ll.insert("bananas2")