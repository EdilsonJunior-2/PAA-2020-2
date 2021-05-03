def maxHeapify(string_arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and len(string_arr[largest]) > len(string_arr[l]):
        largest = l
 
    if r < n and len(string_arr[largest]) > len(string_arr[r]):
        largest = r
 
    if (largest != i):
        string_arr[i], string_arr[largest] = string_arr[largest], string_arr[i]
        maxHeapify(string_arr, n, largest)
    
def maxRemoveHeapify(string_arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and len(string_arr[largest]) >= len(string_arr[l]):
        largest = l
 
    if r < n and len(string_arr[largest]) >= len(string_arr[r]):
        largest = r
 
    if (largest != i):
        string_arr[i], string_arr[largest] = string_arr[largest], string_arr[i]
        maxRemoveHeapify(string_arr, n, largest)
    

def heapSort(string_arr):
    n = len(string_arr)
 
    for i in range(n//2 - 1, -1, -1):
        maxHeapify(string_arr, n, i)
    print(string_arr)

    for i in range(n-1, 0, -1):
        string_arr[i], string_arr[0] = string_arr[0], string_arr[i]
        maxRemoveHeapify(string_arr, i, 0)


string_arr = ["Este", "é", "um", "exemplo", "de", "array", "pra", "testar", "a", "questão", ":)"]

heapSort(string_arr)
print(string_arr)
