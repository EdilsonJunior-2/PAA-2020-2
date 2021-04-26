n = int(input("Diga quantos elementos você quer inserir: "))
array = input()
lista = list(map(int,array.split(' ')))

if (len(lista) == 1):
    print('Intervalo = 0')
elif (lista[0] > lista[-1]):
    intervalo = str(lista[0] - lista[-1])
    print('Intervalo = ' + intervalo)
else:
    intervalo = str(lista[-1] - lista[0])
    print('Intervalo = ' + intervalo)
    