entrada = input().split()
lista = [int(i) for i in entrada]
if max(lista) % min(lista) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
