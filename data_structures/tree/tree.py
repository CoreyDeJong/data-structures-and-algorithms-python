class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        #root, left, right
        output = []

        def walk(root):
            # base case that prevents something you don't want to get into the code
            if not root:
                return
            # deal with root
            output.append(root.value)
            # check the left sub-tree
            walk(root.left)
            # check the right sub-tree
            walk(root.right)
        walk(self.root)

        return output

    def in_order(self):
        #left, root, right
        output = []

        def walk(node):
            if not node:
                return
            # check the right sub-tree
            walk(node.left)
            # deal with root
            output.append(node.value)
            # check the left sub-tree
            walk(node.right)
        walk(self.root)

        return output

    def post_order(self):
        # left, right, root
        output = []

        def walk(node):
            if not node:
                return
            # check the left sub-tree
            walk(node.right)
            # check the right sub-tree
            walk(node.left)
            # deal with root
            output.append(node.value)
        walk(self.root)

        return output

    def breadth_first(self,tree):

        items = []

        breadth = Queue()

        # add root queue
        breadth.enqueue(tree.root)

        # while queue is not empty
        while not breadth.is_empty():

            # dequeue it
            front = breadth.dequeue()

            if not front:
                return
            # do what you need with the front/current ?
            items.append(front.value)

            # check front left and enqueue if it exists
            if front.left:
                breadth.enqueue(front.left)

            #check front right and enqueue as needed
            if front.right:
                breadth.enqueue(front.right)

        return items

    def add(self, value):

        def walk(node, node_to_add):

            # if not node:
            #     return

            if node_to_add.value < node.value:
                # go to the left
                if not node.left:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            else:
                # got to the right
                if not node.right:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)


        if not self.root:
            self.root = Node(value)
            return

        walk(self.root, Node(value))


class Queue:
    def __init__(self):
        self.storage = dequeue()

    def enqueue(self,value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0



class BinarySearchTree(BinaryTree):
    def add(self, value):

        def walk(node, node_to_add):

            # if not node:
            #     return

            if node_to_add.value < node.value:
                # go to the left
                if not node.left:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            else:
                # got to the right
                if not node.right:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)


        if not self.root:
            self.root = Node(value)
            return

        walk(self.root, Node(value))


    def contains(self, value):

        output = self.pre_order()

        if value in output:
            return True
        return False





class Node:
    def __init__(self, value, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

    # this will show the object as a string
    def __str__(self):
        return f"Node: {self.value}"

# bst = BinarySearchTree()
# bst.add(4)
# bst.add(7)
# bst.add(5)
# bst.add(9)
# bst.add(2)
# bst.add(30)
# bst.add(-1)
# print(bst.pre_order())
# print(bst.contains(30))

# Manual Add to BinaryTree/Node creation
if __name__ =="__main__":
    bt = BinaryTree()
    bt.add(4)
    bt.add(7)
    bt.add(5)
    bt.add(9)
    bt.add(2)
    bt.add(30)
    bt.add(-1)
    print(bt.breadth_first())





    # tree = BinaryTree()
    # apples = Node("apples")
    # tree.root = apples
    # bananas = Node("bananas")
    # apples.left = bananas
    # cucumbers = Node("cucumbers")
    # apples.right =cucumbers
    # print(apples)

#     output = tree.pre_order()
#     assert output == ("apples", "bananas", "cucumber")

    # output = tree.pre_order()
#     assert output == ("apples", "bananas", "cucumber"), output

#     assert tree.root.value = "apples"
#     assert tree.left.value = "bananas"
#     assert tree.right.value = "cucumbers"

