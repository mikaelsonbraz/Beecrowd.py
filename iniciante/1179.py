lista_pares: list = []
lista_impares: list = []

for x in range(15):
    entrada = int(input())
    if entrada % 2 == 0:
        lista_pares.append(entrada)
    else:
        lista_impares.append(entrada)

lista_pares.reverse()
lista_impares.reverse()

if lista_pares[len(lista_pares) - 1] < lista_impares[len(lista_impares) - 1]:
    for y in range(5):
        print(f"par[{y}] = {lista_pares.pop()}")

    for z in range(5):
        print(f"impar[{z}] = {lista_impares.pop()}")

    lista_pares.reverse()
    lista_impares.reverse()

    for w in range(len(lista_impares)):
        print(f"impar[{w}] = {lista_impares[w]}")

    for t in range(len(lista_pares)):
        print(f"par[{t}] = {lista_pares[t]}")

else:
    for z in range(5):
        print(f"impar[{z}] = {lista_impares.pop()}")

    for y in range(5):
        print(f"par[{y}] = {lista_pares.pop()}")

    lista_pares.reverse()
    lista_impares.reverse()

    for w in range(len(lista_impares)):
        print(f"impar[{w}] = {lista_impares[w]}")

    for t in range(len(lista_pares)):
        print(f"par[{t}] = {lista_pares[t]}")

