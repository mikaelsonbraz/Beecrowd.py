ent1 = int(input())
ent2 = int(input())
ent3 = int(input())
ent4 = int(input())
ent5 = int(input())

lista = [ent1, ent2, ent3, ent4, ent5]

num_pares, num_impares, num_posi, num_nega = 0, 0, 0, 0
for i in lista:
    if i % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    if i > 0:
        num_posi += 1
    elif i < 0:
        num_nega += 1

print(f"{num_pares} valor(es) par(es)")
print(f"{num_impares} valor(es) impar(es)")
print(f"{num_posi} valor(es) positivo(s)")
print(f"{num_nega} valor(es) negativo(s)")
