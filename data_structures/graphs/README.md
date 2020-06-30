# Graphs
Implement a Graph. The graph should be represented as an adjacency list

## Challenge / API
include the following methods:

- AddNode()
    - Adds a new node to the graph
    - Takes in the value of that node
    - Returns the added node
- AddEdge()
    - Adds a new edge between two nodes in the graph
    - Include the ability to have a “weight”
    - Takes in the two nodes to be connected by the edge
    - Both nodes should already be in the Graph
- GetNodes()
    - Returns all of the nodes in the graph as a collection (set, list, or similar)
- GetNeighbors()
    - Returns a collection of edges connected to the given node
    - Takes in a given node
    - Include the weight of the connection in the returned collection
- Size()
    - Returns the total number of nodes in the graph

## Approach & Efficiency
BigO is O(n) given the length of the graphs are unknown




 # Breadth-first Traversal - Graph
Implement a breadth-first traversal on a graph.


## Challenge Description
Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Approach & Efficiency
Efficiency is O(n) given the loop to iterate through the graph.

## Solution
[Breadth First Traversal](../../assets/breadth_first.PNG)

