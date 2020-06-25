# Hashtables

Implement a Hashtable with the following methods:

## Challenge Description

add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get: takes in the key and returns the value from the table.
contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
hash: takes in an arbitrary key and returns an index in the collection.

## Approach & Efficiency
big 0(1) for writing and reading given key:value pairs



# Hashmap LEFT JOIN

Write a function that LEFT JOINs two hashmaps into a single data structure.


## Challenge Description

The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row. If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.

## Approach & Efficiency
big 0(n) given the loop through the hashmap and reading given key:value pairs
Space 0(1) given the space of a single hashmap as the output with a key and two values

## Solution
[Left Join](../../assets/left_join.PNG)