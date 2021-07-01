entrada = int(input())

fatorial = entrada
for x in range(1, entrada):
    fatorial *= (entrada - x)

print(fatorial)
