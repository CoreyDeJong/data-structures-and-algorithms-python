class LinkedList:
    
    def __init__(self, value=None):
        self.head = None
        # self.insert(value)

    def __repr__(self):
        return f"LinkedList : {self.head}"

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += "{ " + str(current.value) + " } -> "
            current = current.next

        return res + "NULL"
        
    def insert(self, value):

        self.head = Node(value, self.head)

# Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


 
# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node
class Node:
 
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

        if not isinstance(next_, Node) and next_ != None:
            raise TypeError("Next must be a Node") 
    
    def __repr__(self):
       return f"{self.value} : {self.next}"

