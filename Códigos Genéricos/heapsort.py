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
    print(arr)

arr = [700, 13, 11, 7, 6, 5]
heapSort(arr)
print(arr)
