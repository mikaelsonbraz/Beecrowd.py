ent = int(input())
lista = []

for i in range(ent):
    num = int(input())
    lista.append(num)

for i in lista:
    if i == 0:
        print("NULL")
    elif i % 2 == 0 and i > 0:
        print("EVEN POSITIVE")
    elif i % 2 != 0 and i > 0:
        print("ODD POSITIVE")
    elif i % 2 == 0 and i < 0:
        print("EVEN NEGATIVE")
    else:
        print("ODD NEGATIVE")

