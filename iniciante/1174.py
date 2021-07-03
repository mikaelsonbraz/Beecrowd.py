lista = []
for x in range(100):
    entrada = float(input())
    lista.append(entrada)

for y in range(len(lista)):
    if lista[y] <= 10:
        print(f"A[{y}] = {lista[y]:.1f}")
    else:
        pass
