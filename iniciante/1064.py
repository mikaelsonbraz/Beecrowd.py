ent1 = float(input())
ent2 = float(input())
ent3 = float(input())
ent4 = float(input())
ent5 = float(input())
ent6 = float(input())

lista = [ent1, ent2, ent3, ent4, ent5, ent6]

num_posi = 0
media_posi = 0

for i in lista:
    if i > 0:
        num_posi += 1
        media_posi += i

print(f"{num_posi:.0f} valores positivos")
print(f"{media_posi / num_posi:.1f}")
