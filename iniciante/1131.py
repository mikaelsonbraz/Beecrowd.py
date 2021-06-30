continua = 1
num_jogos, vitInter, vitGre, empate = 0, 0, 0, 0

while continua == 1:
    grenal = input().split()
    num_jogos += 1
    inter, gremio = int(grenal[0]), int(grenal[1])
    if inter > gremio:
        vitInter += 1
    elif gremio > inter:
        vitGre += 1
    else:
        empate += 1
    continua = int(input("Novo grenal (1-sim 2-nao)\n"))

print(f"{num_jogos} grenais")
print(f"Inter:{vitInter}")
print(f"Gremio:{vitGre}")
print(f"Empates:{empate}")
if vitInter > vitGre:
    print("Inter venceu mais")
elif vitGre > vitInter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
