notas_validas = 0
soma = 0
continua = 1
while continua == 1:
    nota = float(input())
    if nota < 0 or nota > 10.0:
        print("nota invalida")
    else:
        soma += nota
        notas_validas += 1
    if notas_validas == 2:
        print(f"media = {soma / 2:.2f}")
        print("novo calculo (1-sim 2-nao)")
        continua = int(input())
        while not continua in [1, 2]:
            print("novo calculo (1-sim 2-nao)")
            continua = int(input())
        if continua == 1:
            soma = 0
            notas_validas = 0
        elif continua == 2:
            break

