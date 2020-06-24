
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def __str__(self):
        return self.value

    def contains(self, value):

        output = self.post_order()

        if value in output:
            return True
        return False

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

    
# 1. create function that takes in two trees(tree1, tree2)
def tree_matcher(tree1, tree2):
    # 2. create an empty list called tree1 values
    tree1_values= tree1.post_order()
    # 3. Create an empty list called tree2 values
    tree2_values= tree2.post_order()
    # 4. Create an empty list called matching values
    matching_values=[]

    # 6. Create a for loop that goes through each value in tree1 values and compares to each value in tree2 values, if any of the values are equal, add that value to the matching values list
    for items in tree1_values:
        if tree2.contains(items):
            matching_values.append(tree1)
    
    
    # 7. Return the matching values list
    return matching_values


class Node:
    def __init__(self, value, left=None, right=None, next=None):
        self.value = value
        self.left = left
        self.right = right
        self.next = next

    # this will show the object as a string
    def __str__(self):
        return f"Node: {self.value}"


# if __name__ == "__main__":
    # tree1 = BinaryTree()
    # tree1.add(4)
    # tree1.add(5)
    # tree1.add(7)
    # tree2=BinaryTree()
    # tree2.add(7)
    # # print(tree1)
    # # print(tree2)
    # print(tree_matcher(tree1,tree2))