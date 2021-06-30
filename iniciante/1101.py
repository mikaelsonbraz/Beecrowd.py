lista_strs = []
while True:
    ent = input().split()
    num1, num2 = int(ent[0]), int(ent[1])
    if num1 <=0 or num2 <= 0:
        break
    else:
        soma = 0
        str_confusa = ''

        if num1 > num2:
            for x in range(num2, num1 + 1):
                str_confusa += f"{x} "
                soma += x

            lista_strs.append(str_confusa + "Sum=" + str(soma))

        else:
            for x in range(num1, num2 + 1):
                str_confusa += f"{x} "
                soma += x

            lista_strs.append(str_confusa + "Sum=" + str(soma))

for x in lista_strs:
    print(x)
