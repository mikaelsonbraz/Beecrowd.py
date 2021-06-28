a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

lista = sorted((a, b, c), reverse=True)

a = lista[0]
b = lista[1]
c = lista[2]

if a >= b + c:
    print("NAO FORMA TRIANGULO")

if a < b + c:
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    elif a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")
