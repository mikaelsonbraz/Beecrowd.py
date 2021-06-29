ent1 = int(input())
ent2 = int(input())

if ent1 > ent2:
    soma_impar = 0
    for i in range(ent2 + 1, ent1):
        if i % 2 != 0:
            soma_impar += i

else:
    soma_impar = 0
    for i in range(ent1 + 1, ent2):
        if i % 2 != 0:
            soma_impar += i

print(soma_impar)
