## Shift Array
Write a function called insertShiftArray which takes in an array and the value to be added. 

## Challenge Description
Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
My thought was to focus first on the length of the array given it could vary. Next was to take that length and divide in half to find the index to insert the second argument. Next was to loop through the array at each index and if the index was less than half of the array, keep the integer the same. If equal to the middle, append the new integer into this position. Any index greater than the middle index, would be added 1 index position

## Solution
![](../../assets/array_shift.jpg)