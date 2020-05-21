## Shift Array
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. 

## Challenge Description
Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency

<!-- My thought was to focus first on the length of the array given it could vary. Next was to take that length and divide in half to find the index to insert the second argument. Next was to loop through the array at each index and if the index was less than half of the array, keep the integer the same. If equal to the middle, append the new integer into this position. Any index greater than the middle index, would be added 1 index position -->

## Solution
![](../../assets/ll_merge.jpg)