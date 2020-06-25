class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            # will keep going through the linked list while a current.next is true, it will make the next node current and then repeat until there is no more next nodes
            while current.next:
                current = current.next
            # once there are no more next nodes, you will make a new node
            current.next = node

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def __str__(self):
        """ { a } -> { b } -> { c } -> NULL """
        final_string = ""
        current = self.head
        while current:
            final_string += f"{{{current.data}}} -> "
            current = current.next
        return f"{final_string} NULL"