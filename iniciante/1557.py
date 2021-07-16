while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        lista = []
        for x in range(1, entrada + 1):
            listaLinha = []
            for y in range(1, entrada + 1):
                if x == 1:
                    if y == 1:
                        listaLinha.append(1)
                    else:
                        listaLinha.append(2 ** (y - 1))
                else:
                    if y == 1:
                        controle = 2 ** (x - 1)
                        listaLinha.append(controle)
                    else:
                        controle *= 2
                        listaLinha.append(controle)
            lista.append(listaLinha)

        T = len(str(lista[entrada - 1][entrada - 1]))
        for i in range(entrada):
            for j in range(entrada):
                lista[i][j] = str(lista[i][j])
                while len(lista[i][j]) < T:
                    lista[i][j] = ' ' + lista[i][j]
            M = ' '.join(lista[i])

            print(M)
        print()
