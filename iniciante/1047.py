entrada = input().split()
hcomeco = int(entrada[0])
mincomeco = int(entrada[1])
hfinal = int(entrada[2])
minfinal = int(entrada[3])

if hcomeco == hfinal and mincomeco == minfinal:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

if hfinal > hcomeco:
    if minfinal >= mincomeco:
        print(f"O JOGO DUROU {hfinal - hcomeco} HORA(S) E {minfinal - mincomeco} MINUTO(S)")
    elif mincomeco > minfinal:
        print(f"O JOGO DUROU {hfinal - hcomeco - 1} HORA(S) E {60 + (minfinal - mincomeco)} MINUTO(S)")

if hfinal == hcomeco:
    if mincomeco > minfinal:
        print(f"O JOGO DUROU {23} HORA(S) E {60 + (minfinal - mincomeco)} MINUTO(S)")
    elif minfinal > mincomeco:
        print(f"O JOGO DUROU 0 HORA(S) E {minfinal - mincomeco} MINUTO(S)")

if hfinal < hcomeco:
    if minfinal >= mincomeco:
        print(f"O JOGO DUROU {(24 - hcomeco) + hfinal} HORA(S) E {minfinal - mincomeco} MINUTO(S)")
    elif mincomeco > minfinal:
        print(f"O JOGO DUROU {((24 - hcomeco) + hfinal) - 1} HORA(S) E {60 + (minfinal - mincomeco)} MINUTO(S)")
