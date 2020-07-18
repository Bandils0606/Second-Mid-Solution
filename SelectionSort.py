size = input("Enter size of an array: ")
print("Enter " + size + " element(s) of an array (seperated by line): ")
arr = []
for i in range (int(size)):
    element = int(input())
    arr.append(element)

print("Array before selection sort:")
print(arr)
print("Sorting....")

#Algorithm of SelectionSort.
for i in range (len(arr)):
    min = i
    for j in range (i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]

print("Array after bubble sort:")
print(arr)