import tkinter as tk
from tkinter import *
import timeit
import sys
sys.setrecursionlimit(2500)

root = tk.Tk()
root.geometry("500x250")
root.title("GUI")
root.configure(bg='black')


def linear_search(lists,key):
    start = timeit.default_timer()
    display_canvas.delete("all")
    runtime.delete("all")
    key = int(key)
    array = lists.split(" ")
    new_array = []
    for i in array:
        new_array.append(int(i))
    for i in range(len(new_array)):
        if key == new_array[i]:
            print("found")
            display_canvas.create_text(50, 50, text="Found", fill="green")
            end_time = timeit.default_timer() - start
            runtime.create_text(120,40, text=end_time)
            return True
    display_canvas.create_text(50, 50, text="Not Found", fill="red")
    end_time = timeit.default_timer() - start
    runtime.create_text(120, 40, text=end_time)
    print("not found")
    return False





def newWindow():
    global sample_text, display_canvas, runtime

    sample_text = StringVar()
    newWindow = tk.Tk()
    newWindow.geometry("500x250")
    newWindow.title("Linear Search")
    Label(newWindow, text="Enter the input array : ", font=('Helvetica 12 ')).place(x=80, y=70)
    sample_text = tk.Entry(newWindow)
    sample_text.place(x=240, y=70)
    Label(newWindow, text="Enter the element to be searched : ", font=('Helvetica 12 ')).place(x=80, y=110)
    sample_text1 = tk.Entry(newWindow)
    sample_text1.place(x=360, y=110)
    Button(newWindow, text="Search", command=lambda:linear_search(sample_text.get(),sample_text1.get())).place(x=220, y=140)
    Label(newWindow, text="Result : ", font=('Helvetica 10 ')).place(x=80, y=135)
    display_canvas = tk.Canvas(newWindow, bg="white", width=100, height=100)
    display_canvas.place(x=80, y=160)
    Label(newWindow, text="Runtime : ", font=('Helvetica 10 ')).place(x=290, y=155)
    runtime = tk.Canvas(newWindow, bg="white", width=300, height=50)
    runtime.place(x=220, y=180)
    newWindow.mainloop()


def binary_search(l1, key):
    start = timeit.default_timer()
    display_canvas1.delete("all")
    runtime1.delete("all")
    key = int(key)
    array = l1.split(" ")
    new_array = []
    new_array.sort()
    for i in array:
        new_array.append(int(i))
    low = 0
    high = len(new_array) - 1

    while (low <= high):
        mid = (low + high) // 2

        if (key == new_array[mid]):
            print("found")
            display_canvas1.create_text(50, 50, text="Found", fill="green")
            end_time = timeit.default_timer() - start
            runtime1.create_text(120, 40, text=end_time)
            return mid

        if (key < new_array[mid]):
            high = mid - 1
        if (key > new_array[mid]):
            low = mid + 1
    print(" Element Not found")
    display_canvas1.create_text(50, 50, text="Not Found", fill="red")
    end_time = timeit.default_timer() - start
    runtime1.create_text(120, 40, text=end_time)


def newWindow2():
    global s_text, s_text1, display_canvas1, runtime1
    newWindow2 = tk.Tk()
    newWindow2.geometry("500x250")
    newWindow2.title("Binary Search")
    Label(newWindow2, text="Enter the input sorted array : ", font=('Helvetica 12 ')).place(x=80, y=70)
    s_text = tk.Entry(newWindow2)
    s_text.place(x=280, y=70)
    Label(newWindow2, text="Enter the element to be searched : ", font=('Helvetica 12 ')).place(x=80, y=110)
    s_text1 = tk.Entry(newWindow2)
    s_text1.place(x=360, y=110)
    Button(newWindow2, text="Search", command=lambda: binary_search(s_text.get(), s_text1.get())).place(x=220,y=140)
    Label(newWindow2, text="Result : ", font=('Helvetica 10 ')).place(x=80, y=135)
    display_canvas1 = tk.Canvas(newWindow2, bg="white", width=100, height=100)
    display_canvas1.place(x=80, y=160)
    Label(newWindow2, text="Runtime : ", font=('Helvetica 10 ')).place(x=290, y=155)
    runtime1 = tk.Canvas(newWindow2, bg="white", width=300, height=50)
    runtime1.place(x=270, y=180)
    newWindow2.mainloop()

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
    start = timeit.default_timer()
    display_canvas2.delete("all")
    runtime2.delete("all")
    if root is None or root.value == data:
        return root

    if data < root.value:
        return searching(root.left, data)
    return searching(root.right, data)


def bst(array, data):
    start = timeit.default_timer()
    array = array.split(" ")
    data = int(data)
    l1 = []
    for i in array:
        l1.append(int(i))

    r = Nodes(l1[0])
    for i in range(1, len(l1)):
        r = insertion(r, l1[i])

    key = searching(r, data)
    try:
        print(key.value)
        print("Found")
        display_canvas2.create_text(50, 50, text="Found", fill="green")
        end_time = timeit.default_timer() - start
        runtime2.create_text(120, 40, text=end_time)
    except AttributeError:
        print("Not Found")
        display_canvas2.create_text(50, 50, text="Not Found", fill="red")
        end_time = timeit.default_timer() - start
        runtime2.create_text(120, 40, text=end_time)

def newWindow3():
    global s_text, s_text1, display_canvas2, runtime2
    newWindow3 = tk.Tk()
    newWindow3.geometry("500x250")
    newWindow3.title("Binary Search Tree")
    Label(newWindow3, text="Enter the input array : ", font=('Helvetica 12 ')).place(x=80, y=70)
    s_text = tk.Entry(newWindow3)
    s_text.place(x=240, y=70)

    Label(newWindow3, text="Enter the element to be searched : ", font=('Helvetica 12 ')).place(x=80, y=110)
    s_text1 = tk.Entry(newWindow3)
    s_text1.place(x=360, y=110)

    Button(newWindow3, text="Search", command=lambda:bst(s_text.get(), s_text1.get())).place(x=220, y=140)
    Label(newWindow3, text="Result : ", font=('Helvetica 10 ')).place(x=80, y=135)
    display_canvas2 = tk.Canvas(newWindow3, bg="white", width=100, height=100)
    display_canvas2.place(x=80, y=160)

    Label(newWindow3, text="Runtime : ", font=('Helvetica 10 ')).place(x=290, y=155)
    runtime2 = tk.Canvas(newWindow3, bg="white", width=300, height=50)
    runtime2.place(x=270, y=180)

    newWindow3.mainloop()


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


def rb(array, data):
    start = timeit.default_timer()
    bst = Red_Black_Trees()
    array = array.split(" ")
    data = int(data)
    l1 = []
    for i in array:
        l1.append(int(i))

    for value in l1:
        bst.insert(value)

    bst.print_tree()
    returned_value = bst.searchTree(data)
    print(returned_value)
    display_canvas2.delete("all")
    runtime2.delete("all")
    if returned_value.item !=None:
        print(returned_value.item)
        print("Found")
        display_canvas2.create_text(50, 50, text="Found", fill="green")
        end_time = timeit.default_timer() - start
        runtime2.create_text(120, 40, text=end_time)
    else:
        print("Not Found")
        display_canvas2.create_text(50, 50, text="Not Found", fill="red")
        end_time = timeit.default_timer() - start
        runtime2.create_text(120, 40, text=end_time)


def newWindow4():
    global s_text, s_text1, display_canvas2, runtime2
    newWindow4 = tk.Tk()
    newWindow4.geometry("500x250")
    newWindow4.title("Red-Black Tree")
    Label(newWindow4, text="Enter the input array : ", font=('Helvetica 12 ')).place(x=80, y=70)
    s_text = tk.Entry(newWindow4)
    s_text.place(x=240, y=70)

    Label(newWindow4, text="Enter the element to be searched : ", font=('Helvetica 12 ')).place(x=80, y=110)
    s_text1 = tk.Entry(newWindow4)
    s_text1.place(x=360, y=110)

    Button(newWindow4, text="Search", command=lambda: rb(s_text.get(), s_text1.get())).place(x=220, y=140)
    Label(newWindow4, text="Result : ", font=('Helvetica 10 ')).place(x=80, y=135)
    display_canvas2 = tk.Canvas(newWindow4, bg="white", width=100, height=100)
    display_canvas2.place(x=80, y=160)

    Label(newWindow4, text="Runtime : ", font=('Helvetica 10 ')).place(x=290, y=155)
    runtime2 = tk.Canvas(newWindow4, bg="white", width=300, height=50)
    runtime2.place(x=270, y=180)

    newWindow4.mainloop()



label2 = tk.Label(root, text= "choose the searching algorithm you want to use :", font= ('Helvetica 12 '))
label2.place(x=80 , y=70)

B = tk.Button(root, text ="Linear Search", command=newWindow)
B.place(x=80,y=125)

W = tk.Button(root, text ="Binary Search", command=newWindow2)
W.place(x=320,y=125)

N = tk.Button(root, text ="Binary Search Tree", command=newWindow3)
N.place(x=80,y=180)

R = tk.Button(root, text ="Red-Black-Tree", command=newWindow4)
R.place(x=320,y=180)

root.mainloop()
