import pytest

from tree_intersection import Node, BinaryTree, tree_matcher

def test_intersect1():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.add(4)
    tree1.add(5)
    tree1.add(7)
    tree2.add(7)
    expected = 7
    actual = tree_matcher(tree1,tree2)
    assert actual == expected

def test_intersect2():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.add(4)
    tree1.add(5)
    tree1.add(-7)
    tree2.add(-7)
    expected = -7
    actual = tree_matcher(tree1,tree2)
    assert actual == expected


def test_intersect3():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    tree1.add(-4)
    tree1.add(-5)
    tree1.add(-7)
    tree2.add(-7)
    expected = -7
    actual = tree_matcher(tree1,tree2)
    assert actual == expected