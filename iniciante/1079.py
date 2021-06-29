ent = int(input())

lista_medias = []

for i in range(ent):
    medias = input().split()
    lista_medias.append((float(medias[0]) * 2 + float(medias[1]) * 3 + float(medias[2]) * 5) / 10)

for i in lista_medias:
    print(f"{i:.1f}")

