def particao_reversa(a, ini, fim):
    pivo = a[fim - 1]
    print("pivo: ", pivo)
    for i in range(ini, fim):
        print(a[i])
        if a[i] < pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1

def quick_sort_reverso(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao_reversa(a, ini, fim)
        quick_sort_reverso(a, ini, pp)
        quick_sort_reverso(a, pp + 1, fim)
    return a

def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a

def particao(a, ini, fim):
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] > pivo:
            fim += 1
        else:
            fim += 1
            ini += 1
            a[i], a[ini - 1] = a[ini - 1], a[i]
    return ini - 1

a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
pivo = a[0]
ini = 0
fim = 0

'''for inicial: separar pares dos ímpares'''
for i in range(0, len(a)):
    if(a[i] % 2 == 0):
        fim += 1
    else:
        fim += 1
        ini += 1
        a[i], a[ini - 1] = a[ini - 1], a[i]
print(ini, fim)
print(a)

'''ordenando os pares'''
a = quick_sort(a, 0, ini) 
'''ordenando os ímpares'''
a = quick_sort_reverso(a, ini, fim)

print(a)

'''print(quick_sort(a))'''
