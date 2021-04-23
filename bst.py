class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


def insertion(root, data):
    if root is None:
        return Node(data)
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


array = input("enter the elements into the array : ")
data = int(input("enter the data element to be searched : "))
array = array.split(" ")

l1 = []
for i in array:
    l1.append(int(i))

r = Node(l1[0])
for i in range(1,len(l1)):
    r = insertion(r, l1[i])


key = searching(r, data)
try:
    print(key.value)
    print("Found")
except AttributeError:
    print("Not Found")


















    