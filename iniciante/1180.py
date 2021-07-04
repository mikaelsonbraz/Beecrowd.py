vetorN = int(input())
listaN = []

entrada = input().split()

for item in entrada:
    listaN.append(int(item))

print(f"Menor valor: {min(listaN)}")
print(f"Posicao: {listaN.index(min(listaN))}")
