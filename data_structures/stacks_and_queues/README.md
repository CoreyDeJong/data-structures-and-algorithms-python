# Stack and Queue
 - Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
 - Create a Stack class that has a top property. It creates an empty Stack when instantiated.
 - Create a Queue class that has a front property. It creates an empty Queue when instantiated.

### Challenge Description
This object should be aware of a default empty value assigned to top when the stack is created.
Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
Should raise exception when called on empty stack
Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Should raise exception when called on empty stack
Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.

### Approach & Efficiency
O(1) was achieved given the use of single functions, without any loops or duplicating lists

### API

- push(self, item): Takes in any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
- pop(self): Takes no arguments, removes the node from the top of the stack, and returns the node's value. Will raise an exception when called on an empty stack.
- peek(self): Takes no arguments and returns the value of the node located on top of the stack, without removing it from the stack.
- is_empty(self): Takes no arguments, and returns a boolean indicating whether or not the stack is empty.
- enqueue(self, item): Takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time Performance.
- dequeue(self): Takes no arguments, remove the node from the front of the queue, and returns the node's value.
- peek(self): Takes no arguments and returns the value of the node located in the front of the queue, without removing it from the queue.
