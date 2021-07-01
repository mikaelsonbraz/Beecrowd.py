X = int(input())
Z = int(input())
while Z <= X:
    Z = int(input())

soma = 0
contagem = 0
for x in range(X, Z):
    soma += x
    contagem += 1
    if soma >= Z:
        break

print(contagem)
