import timeit
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(2500)

def linear_search(lists,key):
    for i in range(len(lists)):
        if key == lists[i]:
            print("found")
            return True
    print("not found")
    return False

def binary_search(l1, key):
    low = 0
    high = len(l1)-1

    while(low <= high):
        mid = (low+high)//2

        if(key == l1[mid]):
            return mid

        if(key < l1[mid]):
            high = mid-1
        if(key > l1[mid]):
            low = mid+1
    print(" Element Not found")

#binary_search tree
class Nodes:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


def insertion(root, data):
    if root is None:
        return Nodes(data)
    else:
        if root.value == data:
            return root
        elif data < root.value:
            root.left = insertion(root.left, data)
        elif data > root.value:
            root.right = insertion(root.right, data)
    return root


def searching(root, data):
    if root is None or root.value == data:
        return root

    if data < root.value:
        return searching(root.left, data)
    return searching(root.right, data)

#red-black trees
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


array = input("Enter the elements :  ")
key = int(input("Enter the data element to search : "))

array = array.split(" ")
new_array = []
for i in array:
    new_array.append(int(i))

start1 = timeit.default_timer()
lin = linear_search(new_array, key)
end_time1 = timeit.default_timer() - start1
start2 = timeit.default_timer()
bin1 = binary_search(new_array, key)
end_time2 = timeit.default_timer() - start2
start3 = timeit.default_timer()
r = Nodes(new_array[0])
for i in range(1,len(new_array)):
    r = insertion(r, new_array[i])
end_time3 = timeit.default_timer() - start3
start4 = timeit.default_timer()
bst = Red_Black_Trees()

for values in new_array:
    bst.insert(values)


bst.print_tree()

data = bst.searchTree(key)
end_time4 = timeit.default_timer() - start4

x = ["Linear Search", "Binary Search", "Binary Search Tree", "Red-Black Tree"]
y = [end_time1, end_time2, end_time3, end_time4]

plt.plot(x,y)
plt.xlabel("Search Algorithms")
plt.ylabel("Runtimes")
plt.title("Run time comparisions")
plt.show()
if data.item != 0:
    print(data.item)
    print("Found")
else:
    print("Not Found")

print(lin)
print(bin1)



