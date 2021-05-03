def contadoringSort(arr):
    tamanho = len(arr)
    #saida =  [0] * tamanho
    maior = arr[0]

    for i in range(len(arr)):
        if(arr[i] > maior):
            maior = arr[i]
    contador = [0] * (maior + 1)
    posicoes = [0] * (maior + 1)
    intervalos = []

    for i in range(0, tamanho):
        if(contador[arr[i]] != 0):
            intervalos.append((posicoes[arr[i]], i))
            print("intervalo do valor", arr[i], ": (", posicoes[arr[i]], ", ", i, ")")
        contador[arr[i]] += 1
        posicoes[arr[i]] = i

'''
    for i in range(1, maior + 1):
        contador[i] += contador[i - 1]

    i = tamanho - 1
    while i >= 0:
        saida[contador[arr[i]] - 1] = arr[i]
        print(arr[i])
        print(saida)
        contador[arr[i]] -= 1
        i -= 1

    for i in range(0, tamanho):
        arr[i] = saida[i]
'''  

arr = [1, 4, 2, 2, 2, 8, 2, 3, 3, 7, 1, 1]
contadoringSort(arr)
