numeros = []

for i in range(6):
    x = input()
    numeros.append(float(x))

posi = 0
for x in numeros:
    if x > 0:
        posi += 1

print(f"{posi} valores positivos")
