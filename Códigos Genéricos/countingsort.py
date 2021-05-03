def countingSort(data):
    size = len(data)
    output = [0] * size

    maior = data[0]
    # Initialize count array
    for i in range(len(data)):
        if(data[i] > maior):
            maior = data[i]
    count = [0] * (maior + 1)

    # Store the count of each elements in count array
    for i in range(0, size):
        count[data[i]] += 1
    # Store the cummulative count
    for i in range(1, maior + 1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[data[i]] - 1] = data[i]
        count[data[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        data[i] = output[i]

data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print(data)