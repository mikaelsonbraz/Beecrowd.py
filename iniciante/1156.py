valor_S = 1
expoente = 2
for x in range(3, 40):
    if x % 2 != 0:
        valor_S += x / expoente
        expoente *= 2

print(f"{valor_S:.2f}")