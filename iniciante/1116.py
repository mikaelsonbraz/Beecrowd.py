ent = int(input())
lista = []
for x in range(ent):
    nums = input().split()
    num1, num2 = int(nums[0]), int(nums[1])
    if num2 == 0:
        lista.append("divisao impossivel")
    else:
        lista.append(num1 / num2)

for x in lista:
    print(x)
