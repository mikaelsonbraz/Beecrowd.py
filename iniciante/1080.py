lista = []
for i in range(100):
    ent = int(input())
    lista.append(ent)

print(max(lista))
print(lista.index(max(lista)) + 1)
