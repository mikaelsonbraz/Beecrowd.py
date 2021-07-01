entrada = input().split()
colunas = int(entrada[0])
num = int(entrada[1])

lista = []
string = ''

for x in range(1, num + 1):
    lista.append(x)
    if len(lista) == colunas:
        for item in lista:
            if item != lista[-1]:
                string += f"{item} "
            else:
                string += f"{item}"
        print(string)
        string = ''
        lista = []
