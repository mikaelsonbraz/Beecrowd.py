ent1 = int(input())
ent2 = int(input())
ent3 = int(input())
ent4 = int(input())
ent5 = int(input())

lista = [ent1, ent2, ent3, ent4, ent5]

num_pares = 0
for i in lista:
    if i % 2 == 0:
        num_pares += 1

print(f"{num_pares} valores pares")
