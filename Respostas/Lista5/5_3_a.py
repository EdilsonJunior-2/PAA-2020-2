def maxHeapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if (largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)

arr = [(1,3), (2, 3), (4, 5), (4, 7), (4, 5)]
arr_2 = []

for i in range(len(arr)):
    for j in range(arr[i][0], arr[i][-1] + 1):
        arr_2.append(j)

print(arr_2)
heapSort(arr_2)
print(arr_2)
