entrada = int(input())

for x in range(entrada):
    XY = input().split()
    X = int(XY[0])
    Y = int(XY[1])

    controle = 0
    soma = 0
    for x in range(X, 2000000):
        if x % 2 != 0:
            soma += x
            controle += 1
            if controle == Y:
                break

    print(soma)
