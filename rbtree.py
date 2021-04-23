import sys
sys.setrecursionlimit(2500)

class Node():
    def __init__(self, key):
        self.item = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1

class Red_Black_Trees():
    def __init__(self):
        self.Null_Tree = Node(0)
        self.Null_Tree.color = 0
        self.Null_Tree.left = None
        self.Null_Tree.right = None
        self.root = self.Null_Tree

    def search_tree(self, node, key):
        if key == node.item or node == self.Null_Tree:
            return node

        if key < node.item:
            return self.search_tree(node.left, key)
        elif key > node.item:
            return self.search_tree(node.right, key)
        print("Node not Found")

    def insert_rotation(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print(self, node, indent, last):
        if node != self.Null_Tree:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print(node.left, indent, False)
            self.__print(node.right, indent, True)

    def searchTree(self, k):
        return self.search_tree(self.root, k)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.Null_Tree:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.Null_Tree:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.Null_Tree
        node.right = self.Null_Tree
        node.color = 1

        y = None
        x = self.root

        while x != self.Null_Tree:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.insert_rotation(node)

    def get_root(self):
        return self.root

    def print_tree(self):
        self.__print(self.root, "", True)


if __name__ == "__main__":
    bst = Red_Black_Trees()

    bst.insert(55)
    bst.insert(40)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)

    bst.print_tree()

    data = bst.searchTree(10)
    if data.item != 0:
        print(data.item)
        print("Found")
    else:
        print("Not Found")