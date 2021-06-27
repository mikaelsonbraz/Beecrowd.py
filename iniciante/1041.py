pontos = input().split()

if float(pontos[0]) > 0 and float(pontos[1]) > 0:
    print("Q1")
elif float(pontos[0]) < 0 and float(pontos[1]) < 0:
    print("Q3")
elif float(pontos[0]) > 0 and float(pontos[1]) < 0:
    print("Q4")
elif float(pontos[0]) < 0 and float(pontos[1]) > 0:
    print("Q2")
elif float(pontos[0]) != 0.0 and float(pontos[1]) == 0.0:
    print("Eixo X")
elif float(pontos[0]) == 0.0 and float(pontos[1]) != 0.0:
    print("Eixo Y")
else:
    print("Origem")
