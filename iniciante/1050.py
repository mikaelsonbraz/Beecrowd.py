entrada = int(input())
ddd = {61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora", 19: "Campinas",
       27: "Vitoria", 31: "Belo Horizonte"}
encontrado = 0
for item in ddd.keys():
    if item == entrada:
        encontrado += 1
        print(ddd.get(item))

if encontrado == 0:
    print("DDD nao cadastrado")
