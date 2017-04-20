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

    def insert(self, x):

        def ins(current_node, x):
            print("  ", current_node)
            if current_node.left is not None and current_node.data > x:
                print("  going left")
                ins(current_node.left, x)
            if current_node.right is not None and current_node.data < x:
                print("  going right")
                ins(current_node.right, x)
            if current_node.left is None and current_node.data > x:
                print("  inserting left")
                current_node.left = Node(x)
            elif current_node.right is None and current_node.data <= x:
                print("  inserting right")
                current_node.right = Node(x)
        if self.root is None:
            self.root = Node(x)
        else:
            print("inserting", x)
            ins(self.root, x)

x = Tree()

x.insert(2)
print(x)
x.insert(3)
print(x)
x.insert(5)
x.insert(4)
print(x)
