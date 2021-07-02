casos = int(input())

for x in range(casos):
    entrada = int(input())
    eh_perfeito = 0

    for y in range(1, entrada):
        if entrada % y == 0:
            eh_perfeito += y

    if entrada == eh_perfeito:
        print(entrada, 'eh perfeito')
    else:
        print(entrada, 'nao eh perfeito')
