num = input().split()
# a) a área do triângulo retângulo que tem A por base e C por altura.
print(f"TRIANGULO: {(float(num[0]) * float(num[2])) / 2:.3f}")
# b) a área do círculo de raio C. (pi = 3.14159)
print(f"CIRCULO: {3.14159 * (float(num[2]) ** 2):.3f}")
# c) a área do trapézio que tem A e B por bases e C por altura.
print(f"TRAPEZIO: {((float(num[0]) + float(num[1])) * float(num[2])) / 2:.3f}")
# d) a área do quadrado que tem lado B.
print(f"QUADRADO: {float(num[1]) ** 2:.3f}")
# e) a área do retângulo que tem lados A e B.
print(f"RETANGULO: {float(num[0]) * float(num[1]):.3f}")