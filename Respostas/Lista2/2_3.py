def funcao():
    array = input()
    expressao = [c for c in array]
    pilha = []
    for x in range (0, len(expressao)):
        print(expressao[x])
        if (expressao[x] == '(' or expressao[x] == '['):
            pilha.append(expressao[x])
        elif (expressao[x] == ')'):
            if (len(pilha) > 0):
                if(pilha[-1] == '('):
                    pilha.pop(-1)
                else:
                    print("Expressão incorreta")
                    return
            else:
                print("Expressão incorreta")
                return
        elif (expressao[x] == ']'):
            if (len(pilha) > 0):
                if (pilha[-1] == '['):
                    pilha.pop(-1)
                else:
                    print("Expressão incorreta")
                    return
            else:
                print("Expressão incorreta")
                return

    if(len(pilha) > 0):
        print("Expressão incorreta")
        return
    else:
        print("Expressão correta")
        return

funcao()
