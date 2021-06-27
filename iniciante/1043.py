entrada = input().split()
lista = [float(i) for i in entrada]
triangulo = True

for i in lista:
    if i >= (sum(lista) - i):
        triangulo = False

if triangulo:
    print(f"Perimetro = {sum(lista):.1f}")
else:
    print(f"Area = {((lista[0] + lista[1]) * lista[2]) / 2:.1f}")
