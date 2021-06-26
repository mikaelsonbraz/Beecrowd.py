#Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos
# ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos,
# deverá ser impressa a mensagem “Fora de intervalo”.

entrada = float(input())
intervalos = [[0, 25], [25, 50], [50, 75], [75, 100]]
saida = "Fora de intervalo"
for i in intervalos:
    if i[0] <= entrada <= i[1]:
        if i[0] == 0:
            saida = f"Intervalo [{i[0]},{i[1]}]"
        elif i[0] == 25:
            saida = f"Intervalo ({i[0]},{i[1]}]"
        else:
            saida = f"Intervalo ({i[0]},{i[1]}]"
        break

print(saida)
