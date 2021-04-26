n = int(input("Diga quantos elementos você quer inserir: "))
array = input()
lista = list(map(int,array.split(' ')))

if (len(lista) == 1):
    print('intervalo = 0')
else:
    if (lista[0] < lista[1]):
        menor = lista[0]
        maior = lista[1]
    else:
        menor = lista[1]
        maior = lista[0]
    
    for x in range(2, len(lista)):
        if (lista[x] < menor):
            menor = lista[x]
        elif (lista[x] > maior):
            maior = lista[x]
    
    intervalo = str(maior - menor)
    print('Intervalo = ' + intervalo)
