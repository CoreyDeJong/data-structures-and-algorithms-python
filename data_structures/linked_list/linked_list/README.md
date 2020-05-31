# Singly Linked List
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

## Challenge
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.
Define a method called __str__ in which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
The majority of the code is at 0(1) given the assignment and singular complexity, whereas the while loops are at 0(n) due to the length of the linked lists that are used.

## API
insert method takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
includes method takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.



# Append, Insert Berfore and After
Insert nodes before, after and append

## Challenge
.append(value) which adds a new node with the given value to the end of the list .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node

## Approach & Efficiency
The majority of the code is at 0(1) given the assignment and singular complexity, whereas the while loops are at 0(n) due to the length of the linked lists that are used.

## Solution
[Append, Insert Before After](../../assets/append_insert_before_after.jpg)



# Kth Number from the end
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list.

## Challenge Description
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
The majority of the code is at 0(1) given the assignment and singular complexity, whereas the for loop is at 0(n) due to the length of the linked lists that are used.

## Solution
[link list k](../../../assets/link_list_k.jpg)
