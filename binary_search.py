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

    


array = input("Enter the elements :  ")
key = int(input("Enter the data element to search : "))

array = array.split(" ")

l1 = []
for i in array:
    l1.append(int(i))


value = binary_search(l1, key)
print("The Element is Found at index", value)









