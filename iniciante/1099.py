entrada = int(input())
listaimpares = []

for x in range(entrada):
    ent = input().split()
    num1, num2 = int(ent[0]), int(ent[1])
    soma = 0

    if num1 >= num2:
        lista = [i for i in range(num2 + 1, num1) if i % 2 != 0]
        soma += sum(lista)
        listaimpares.append(soma)
    else:
        lista = [i for i in range(num1 + 1, num2) if i % 2 != 0]
        soma += sum(lista)
        listaimpares.append(soma)

    soma = 0

for x in listaimpares:
    print(x)
