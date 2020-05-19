class LinkedList:
    
    def __init__(self, value=None):
        self.head = None
        # self.insert(value)

    def __repr__(self):
        return f"LinkedList: {self.head}"

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += "{ " + str(current.value) + " } -> "
            current = current.next

        return res + "NULL"
        
    def insert(self, value):

        self.head = Node(value, self.head)
    
    
    
    # Code6 = .append(value) which adds a new node with the given value to the end of the list
    # def append_value(self, value):
        
    #     if self.head is None:
    #         self.head = value
        # self.head = Node(value, self.head)

    # def append(self, value): 
    
    # # 1. Create a new node 
    # # 2. Put in the data 
    # # 3. Set next as None 
    #     new_node = Node(value) 
    
    # # 4. If the Linked List is empty, then make the 
    # #    new node as head 
    #     if self.head is None: 
    #             self.head = new_node 
    #             return
    
    # # 5. Else traverse till the last node 
    #     last = self.head 
    #     while (last.next): 
    #         last = last.next
    
    # # 6. Change the next of last node 
    #     last.next =  new_node 




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

