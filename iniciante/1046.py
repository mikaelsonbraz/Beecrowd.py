entrada = input().split()
tempo = 24
a = int(entrada[0])
b = int(entrada[1])
if b > a:
    print(f"O JOGO DUROU {b - a} HORA(S)")
elif a > b:
    print(f"O JOGO DUROU {(tempo - a) + b} HORA(S)")
else:
    print(f"O JOGO DUROU {tempo} HORA(S)")
