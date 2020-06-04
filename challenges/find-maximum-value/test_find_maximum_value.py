import pytest

from find_maximum_value import Node, BinarySearchTree, BinaryTree, Queue

def test_create_node():
    one = Node(1)
    actual= one.value
    expected = 1
    assert actual == expected



def test_max_value():
    bt = BinaryTree()
    bt.add(4)
    bt.add(2)
    bt.add(1)
    bt.add(7)
    bt.add(9)
    bt.add(11)
    bt.add(10)
    expected = 11
    actual = bt.find_maximum_value()
    assert actual == expected

def test_max_value_negative():
    bt = BinaryTree()
    bt.add(4)
    bt.add(2)
    bt.add(-1)
    bt.add(7)
    bt.add(-9)
    bt.add(1)
    bt.add(10)
    expected = 10
    actual = bt.find_maximum_value()
    assert actual == expected
