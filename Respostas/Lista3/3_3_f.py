def busca_ternaria(x, primeiro, ultimo, z):
    print(primeiro, ultimo)

    if (primeiro == ultimo):
        if (x[int(ultimo)] == z):
            print(int(ultimo))
            return

        else:
            print(-1)
            return

    elif (x[int((ultimo - primeiro)/3 + primeiro)] == z):
        print(int((ultimo-primeiro)/3 + primeiro))
        return

    elif (x[int((ultimo - primeiro)/3 + primeiro)] > z):
        busca_ternaria(x, int(primeiro), int((ultimo - primeiro)/3 + primeiro - 1), z)
        return

    elif (x[int(2*(ultimo - primeiro)/3 + primeiro)] == z):
        print(int(2*(ultimo - primeiro)/3 + primeiro))
        return

    elif (x[int(2*(ultimo - primeiro)/3 + primeiro)] > z):
        busca_ternaria(x, int((ultimo - primeiro)/3 + primeiro + 1), int(2*(ultimo - primeiro)/3 + primeiro - 1), z)
        return

    else:
        busca_ternaria(x, int(2*(ultimo - primeiro)/3 + primeiro + 1), int(ultimo), z)
        return

vetor = [1, 3, 5, 7, 9]
resultado = busca_ternaria(list(range(0, 1000000, 4)), 0, 249999, 6)