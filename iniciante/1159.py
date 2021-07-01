while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        soma = 0
        for x in range(entrada, entrada + 10):
            if x % 2 == 0:
                soma += x
    print(soma)
