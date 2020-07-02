from collections import deque

# referenced multiple internet sites for examples

class Stack():
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f"Top is {self.top}"

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node


    def pop(self):
        if self.top == None:
            raise Exception ("empty stack")

        else:
            pop_node = self.top
            self.top = self.top.next
            pop_node.next = None
            return pop_node.value

    def peek(self):
        if self.top != None:
            return self.top.value
        else:
            return "empty stack"

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = self.rear.next

    def dequeue(self):
        if self.front != None:
            temp_node = self.front
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            temp_node.next = None
            return temp_node.value
        else:
            return "empty queue"

    def peek(self):
        if self.front != None:
            return self.front.value
        else:
            return "empty queue"

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False


class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
       return f"{self.value} : {self.next}"


