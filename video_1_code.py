class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        s = ""

        def traverse(current_node):
            nonlocal s
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node is not None:
                s += str(current_node)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return s


one = Node("1")
two = Node("2")
three = Node("3", two, one)
four = Node("4")
five = Node("5", four, three)

oak = Tree(five)
print(oak)
