lista = []

for x in range(20):
    entrada = int(input())
    lista.append(entrada)

lista_reversa = list(reversed(lista))

for y in range(len(lista_reversa)):
    print(f"N[{y}] = {lista_reversa[y]}")
