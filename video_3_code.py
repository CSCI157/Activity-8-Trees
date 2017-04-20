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
        # Create a 2D that represents the tree
        i = 0
        nodes = [[self.root]]
        string = [[str(self.root)]]
        if self.root.left is not None or self.root.right is not None:
            more_branches = True
        else:
            more_branches = False
        while more_branches:
            more_branches = False
            nodes.append([])
            string.append([])
            for node in nodes[i]:
                if node is not None:
                    nodes[i+1].append(node.left)
                    nodes[i+1].append(node.right)
                    string[i+1].append(str(node.left))
                    string[i+1].append(str(node.right))
                    if node.left is not None or node.right is not None:
                        more_branches = True
                else:
                    nodes[i+1].append(None)
                    nodes[i+1].append(None)
                    string[i+1].append(str(None))
                    string[i+1].append(str(None))

            if more_branches:
                i += 1
        del nodes[i+1]
        del string[i+1]

        # Format the 2D array into a string
        max_entry_size = 0
        for i in range(len(string)):
            for j in range(len(string[i])):
                if string[i][j] == 'None':
                    string[i][j] = ""
                if len(string[i][j]) > max_entry_size:
                    max_entry_size = len(string[i][j])
        s = ""
        num_rows = len(string)
        for i in range(num_rows):
            left_margin = (2**(num_rows-i-1)-1)*max_entry_size
            spacing = (2**(num_rows-i)-1)*max_entry_size
            s += left_margin*" "
            for j in range(len(string[i])):
                l = len(string[i][j])
                s += int(round((max_entry_size - l)/2))*" " + string[i][j] + \
                     (max_entry_size - l - int(round((max_entry_size - l)/2)))*" " + spacing*" "
            s += "\n"
        return s

    def insert(self, x):
        def ins(current_node, x):
            if current_node.left is not None and current_node.data > x:
                ins(current_node.left, x)
            if current_node.right is not None and current_node.data < x:
                ins(current_node.right, x)
            if current_node.left is None and current_node.data > x:
                current_node.left = Node(x)
            elif current_node.right is None and current_node.data <= x:
                current_node.right = Node(x)
        if self.root is None:
            self.root = Node(x)
        else:
            ins(self.root, x)

x = Tree()

x.insert(21)
x.insert(11)
x.insert(35)
x.insert(6)
x.insert(1)
x.insert(27)
x.insert(45)
x.insert(3)
x.insert(8)
x.insert(17)
x.insert(14)
x.insert(18)
x.insert(0)
print(x)
