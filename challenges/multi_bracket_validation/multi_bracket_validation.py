from collections import deque

# referenced multiple internet sites for examples and class lecture

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


class Validation():
    def __init__(self):
        self.bracket_stack = Stack()

    def multi_bracket_validation(self, input):
        for i in range(len(input)):
            if input[i]=="(":
                self.bracket_stack.push(input[i])
                i += 1
            elif input[i]==")":
                # 1st figure out it's opening character
                opening_character="("

                # 2nd is the opening character on top of the stack
                if opening_character == self.bracket_stack.top.value:

                    # 2 - True: remove the opeing character from the stack
                    self.bracket_stack.pop()
                    i+=1
                else:
                    return False

            ###### Braces ##########
            elif input[i]=="[":
                self.bracket_stack.push(input[i])
                i += 1

            elif input[i]=="]":

                opening_character="["

                if opening_character == self.bracket_stack.top.value:

                    self.bracket_stack.pop()
                    i+=1
                else:
                    return False

            ##### Curly Bracket ######
            elif input[i]=="{":
                self.bracket_stack.push(input[i])
                i += 1

            elif input[i]=="}":

                opening_character="{"

                if opening_character == self.bracket_stack.top.value:

                    self.bracket_stack.pop()
                    i+=1
                else:
                    return False
            else:
                i+=1
        return True
