soma_media = input().title()

matriz = []
soma = 0
nuns = 0
for x in range(12):
    matrizX = []
    for y in range(12):
        entrada = float(input())
        matrizX.append(entrada)
        if y > x:
            soma += entrada
            nuns += 1
        else:
            pass
    matriz.append(matrizX)

if soma_media == 'S':
    print(f"{soma:.1f}")
elif soma_media == 'M':
    print(f"{soma / nuns:.1f}")
