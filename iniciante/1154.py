soma_idades = 0
num = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        soma_idades += idade
        num += 1

print(f"{soma_idades / num:.2f}")
