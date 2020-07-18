size = input("Enter size of an array: ")
print("Enter " + size + " element(s) of an array (seperated by line): ")
arr = []
for i in range (int(size)):
    element = int(input())
    arr.append(element)

print("Array before bubble sort:")
print(arr)
print("Sorting....")

#Algorithm of BubbleSort.
for i in range (len(arr)-1):
    for j in range (0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Array after bubble sort:")
print(arr)