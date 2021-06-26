entrada = input().split()
precos = [[1, 4], [2, 4.5], [3, 5], [4, 2], [5, 1.5]]

for i in precos:
    if int(entrada[0]) == i[0]:
        print(f"Total: R$ {int(entrada[1]) * i[1]:.2f}")
