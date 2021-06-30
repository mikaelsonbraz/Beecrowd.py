lista = []

while True:
    ent = input().split()
    num1, num2 = int(ent[0]), int(ent[1])
    if num1 > num2:
        lista.append("Decrescente")
    elif num2 > num1:
        lista.append("Crescente")
    else:
        break

for x in lista:
    print(x)
