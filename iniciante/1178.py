entrada = float(input())
lista = []

for x in range(100):
    lista.append(entrada)
    entrada /= 2

for y in range(len(lista)):
    print(f"N[{y}] = {lista[y]:.4f}")
