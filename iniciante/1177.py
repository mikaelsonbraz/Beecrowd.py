entrada = int(input())
lista = []
controle = 0

for x in range(1000):
    lista.append(controle)
    controle += 1
    if controle == entrada:
        controle = 0

for x in range(len(lista)):
    print(f"N[{x}] = {lista[x]}")
