def busca_binaria(b, esquerda, direita, item):
    if direita < esquerda:
        return -1
    meio = (esquerda+direita) / 2
    if b[int(meio)] == item:
        print(b[int(meio)])
        return meio
    elif b[int(meio)] > item:
        return busca_binaria(b, int(esquerda), int(meio-1), item)
    else:
        return busca_binaria(b, int(meio+1), int(direita), item)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 2, 32, 45, 33, 67, 443, 123]

resultado = 2
indice1 = 0
indice2 = 0
flag = 0

for i in range(0, len(a)):
    quociente = resultado / a[i]
    termo2 = busca_binaria(b, 0, len(b) -1, quociente)
    print(termo2)
    if(termo2 != -1):
        indice2 = int(termo2)
        indice1 = i
        flag = 1
        break

if(flag == 1):
    print("Os termos que, multiplicados, dão", resultado, ":", a[indice1],  "e", b[indice2])
else:
    print("Os termos que, multiplicados, dão", resultado, "não foram encontrados")