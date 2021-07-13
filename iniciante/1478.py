while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        lista = []
        for x in range(1, entrada + 1):
            listaLinha = []
            controle = x + 1
            for y in range(1, entrada + 1):
                if x > y:
                    controle -= 1
                elif x < y:
                    controle += 1
                else:
                    controle = 1
                listaLinha.append(controle)
            lista.append(listaLinha)

        for i in range(entrada):
            saida = ''
            for j in range(entrada):
                saida += " %3d" % lista[i][j]
            print(saida[1:])
        print("")
