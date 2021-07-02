num_casos = int(input())

for teste in range(num_casos):
    entrada = input().split()
    cidade_menor = int(entrada[0])
    cidade_maior = int(entrada[1])
    crescimento_cidade_menor = float(entrada[2]) / 100
    crescimento_cidade_maior = float(entrada[3]) / 100
    anos = 0
    while cidade_menor <= cidade_maior:
        cidade_menor += int(cidade_menor * crescimento_cidade_menor)
        cidade_maior += int(cidade_maior * crescimento_cidade_maior)
        anos += 1
        if anos > 100:
            break

    if anos <= 100:
        print(anos, 'anos.')
    else:
        print('Mais de 1 seculo.')
        