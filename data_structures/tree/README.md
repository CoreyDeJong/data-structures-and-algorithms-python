## Tree
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

## Challenge Description
Create a BinaryTree class
Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Create a BinarySearchTree class
Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
Efficiency is O(n^2) given the loops to iterate through the input.

## API
BinaryTree Class:
 - Pre-Order: depth first traversal order of root >> left >> right
 - In-Order: depth first traversal order of left >> root >> right
 - Post-Order: depth first traversal order of left >> right >> root

BinarySearchTree Class:
 - Add method will create a node and add it to the tree
 - Contains method will query the tree and return True or False if the value is within the Tree.


 # Breadth-first Traversal
Write a breadth first traversal method which takes a Binary Tree as its unique input.


## Challenge Description
Without utilizing any of the built-in methods available to your language, traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Approach & Efficiency
Efficiency is O(n^2) given the loops to iterate through the tree.

## Solution
[Breadth First Traversal](../../assets/breadth_first_traversal.jpg)
