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


# used code from geeksforgeeks.org given I couldn't get my file to run tests

#This function is defined in Linked List class 
# Appends a new node at the end.  This method is 
#  defined inside LinkedList class shown above */
    def append(self, value):

    # 1. Create a new node 
   # 2. Put in the data 
   # 3. Set next as None
        new_node = Node(value)

 # 4. If the Linked List is empty, then make the 
   #    new node as head 
        if self.head is None:
            self.head = new_node
            return

   # 5. Else traverse till the last node
        last = self.head
        while(last.next):
            last = last.next

   # 6. Change the next of last node 
        last.next = new_node



####### Insert Before #########
    def insertBefore(self, newVal):
        new_node = Node(newVal)
        new_node.next = self.head
        self.head = new_node 

####### Insert After ###########
    def insertAfter(self, value, newVal):
        current = self.head
        while current:
            if current.value == value:
                current.next = Node(newVal, current.next)
                break
            if current.next == None:
                raise ValueError("Your value does not exist") 
            current = current.next




########## Includes ############
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