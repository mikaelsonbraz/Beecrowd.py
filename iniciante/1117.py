notas_validas = 0
soma = 0
while True:
    nota = float(input())
    if nota < 0 or nota > 10.0:
        print("nota invalida")
    else:
        soma += nota
        notas_validas += 1
    if notas_validas == 2:
        print(f"media = {soma / 2:.2f}")
        break
