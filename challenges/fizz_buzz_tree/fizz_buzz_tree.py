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


## input is a tree
def FizzBuzzTree(tree):

    ## output is a new tree
    output = []
    def walk(root):
        str_return = ""
        # base case that prevents something you don't want to get into the code
        if not root:
            return
        # deal with root
        if root.value % 3 == 0 and root.value % 5 == 0:
            str_return = 'FizzBuzz'
        elif root.value % 3 == 0:
            str_return = 'Fizz'
        elif root.value % 5 == 0:
            str_return =  'Buzz'
        else:
            str_return = root.value
            # return str_return or str(root)? to adjust the value to a string?

        # return str(num)
        output.append(str_return)
        # check the left sub-tree
        walk(root.left)
        # check the right sub-tree
        walk(root.right)
    walk(tree.root)

    return output


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


    # def contains(self, value):
    #     output = []

    #     def walk(node):
    #         if not node:
    #             return
    #         # deal with root
    #         output.append(node.value)
    #         # check the left sub-tree
    #         walk(node.left)
    #         # check the right sub-tree
    #         walk(node.right)
    #     walk(self.root)

    #     # return output

    #     for i in (len(output)):
    #         if value == output[i]:
    #             return True
    #         else:
    #             return False




class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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
# if __name__ =="__main__"
#     tree = BinaryTree()
#     apples = Node("apples")
#     tree.root = apples
#     bananas = Node("bananas")
#     apples.left = bananas
#     cucumbers = Node("cucumbers")
#     apples.right =cucumbers
#     print(apples)

#     output = tree.pre_order()
#     assert output == ("apples", "bananas", "cucumber")

    # output = tree.pre_order()
#     assert output == ("apples", "bananas", "cucumber"), output

#     assert tree.root.value = "apples"
#     assert tree.left.value = "bananas"
#     assert tree.right.value = "cucumbers"
