from collections import deque

# referenced multiple internet sites for examples

class Node():
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node")

    def __repr__(self):
       return f"{self.value} : {self.next}"



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


class PseudoQueue():
    def __init__(self):
        # self.stack1 = Stack()
        # self.stack2 = Stack()
        self.inbox = Stack()
        self.outbox = Stack()



    def enqueue(self, value):
        # self.stack1.push(value)

        while self.outbox != None:
            self.inbox.push(self.outbox.pop())
        self.inbox.push(value)

# dequeue does not take any arguments?
    def dequeue(self):

        while self.inbox != None:
            value = self.inbox.pop()
            self.outbox.push(value)


        if self.outbox == None:


            # outgoing value is already being used
            outgoing = self.outbox.pop()
            return outgoing







        #### Original attempt#####
        # while self.stack1 != None:
        #     self.stack2.push(self.stack1.pop())
        # return self.stack2.pop()
        # pass


