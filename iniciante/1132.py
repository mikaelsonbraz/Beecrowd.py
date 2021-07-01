num1 = int(input())
num2 = int(input())
soma = 0

if num2 > num1:
    for x in range(num1, num2 + 1):
        if not x % 13 == 0:
            soma += x

else:
    for x in range(num2, num1 + 1):
        if not x % 13 == 0:
            soma += x

print(soma)
