import pytest

from tree import Node, BinarySearchTree, BinaryTree

def test_create_node():
    one = Node(1)
    actual= one.value
    expected = 1
    assert actual == expected


# Test 2 - add a single node to an empty tree
def test_single_node_empty_tree():
    bst = BinarySearchTree()
    bst.add(4)
    expected = [4]
    actual = bst.pre_order()
    assert actual == expected

# Test 3 - add a left child and right child to a single root node
def test_left_right():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(4)
    bst.add(6)
    expected = [2, 4, 6]
    actual = bst.pre_order()
    assert actual == expected


# Test 4 - collection from a preorder traversal
def test_preorder():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(7)
    bst.add(5)
    bst.add(9)
    bst.add(2)
    bst.add(30)
    bst.add(-1)
    expected = [4, 2, -1, 7, 5, 9, 30]
    actual = bst.pre_order()
    assert actual == expected

# Test 5 - collection from a inorder traversal
def test_inorder():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(7)
    bst.add(5)
    bst.add(9)
    bst.add(2)
    bst.add(30)
    bst.add(-1)
    expected = [-1, 2,4,5,7,9,30]
    actual = bst.in_order()
    assert actual == expected

# Test 6 - collection from a postorder traversal
def test_postorder():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(7)
    bst.add(5)
    bst.add(9)
    bst.add(2)
    bst.add(30)
    bst.add(-1)
    expected = [30,9,5, 7, -1,2,4]
    actual = bst.post_order()
    assert actual == expected


# Test 7 - contains
def test_contains():
    bst = BinarySearchTree()
    bst.add(4)
    bst.add(7)
    bst.add(5)
    bst.add(9)
    bst.add(2)
    bst.add(30)
    bst.add(-1)
    expected = True
    actual = bst.contains(5)
    assert actual == expected
