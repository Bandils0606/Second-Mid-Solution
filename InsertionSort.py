size = input("Enter size of an array: ")
print("Enter " + size + " element(s) of an array (seperated by line): ")
arr = []
for i in range (int(size)):
    element = int(input())
    arr.append(element)

print("Array before insertion sort:")
print(arr)
print("Sorting....")

#Algorithm of InsertionSort.
for i in range (1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        j = j-1

print("Array after insertion sort:")
print(arr)
