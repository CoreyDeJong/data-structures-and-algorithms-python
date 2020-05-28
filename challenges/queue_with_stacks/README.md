## Queue with Stacks
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects.

## Challenge Description
enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

The Stack instances have only push, pop, and peek methods. You should use your own Stack implementation. Instantiate these Stack objects in your PseudoQueue constructor.

## Approach & Efficiency

<!-- My thought was to focus first on the length of both lists and accumulate a total. Then I could loop through the entire length and append each list at the corresponding index of i and append to a final merged list. -->

## Solution
![](../../assets/queue_with_stacks.jpg)