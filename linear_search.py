def linear_search(lists,key):

    for i in range(len(lists)):
        if key == lists[i]:
            print("found")
            return True
    print("not found")
    return False


array = input("Enter the elements :  ")
key = int(input("Enter the data element to search : "))

array = array.split(" ")
new_array = []
for i in array:
    new_array.append(int(i))

linear_search(new_array, key)


