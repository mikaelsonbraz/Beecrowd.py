while True:
    try:
        entrada = int(input())
        lista = []

        for x in range(entrada):
            listaLinha = []
            for y in range(entrada):
                if x + y + 1 == entrada:
                    listaLinha.append(2)
                elif x == y:
                    listaLinha.append(1)
                else:
                    listaLinha.append(3)
            lista.append(listaLinha)

        for item in lista:
            linha = ''
            for y in item:
                linha += str(y)
            print(linha)
    except EOFError:
        break
