from collections import deque



class Stack():
    def __init__(self):
        self.storage = []
    def push(self, item):
        self.storage.append(item)
    def pop(self):
        if not self.is_empty():
            return self.storage.pop()
        else:
            return "empty stack"
    def is_empty(self):
        return not len(self.storage)
        # if len(self.storage) == 0:
        #     return True
        # return False
    def peek(self):
        if not self.is_empty():
            return self.storage[-1]
        else:
            return "empty stack"



class Queue():
    def __init__(self):
        self.storage = deque()
    def enqueue(self, item):
        self.storage.appendleft(item) #O(1)
    def dequeue(self):
        return self.storage.pop()
    def peek(self):
        return self.storage[-1]
    def is_empty(self):
        return len(self.storage)==0


class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
       return f"{self.value} : {self.next}"
