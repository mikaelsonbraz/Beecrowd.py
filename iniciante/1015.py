ponto1 = input().split()
ponto2 = input().split()
xquad = (float(ponto2[0]) - float(ponto1[0])) ** 2
yquad = (float(ponto2[1]) - float(ponto1[1])) ** 2
print(f"{(xquad + yquad) ** 0.5:.4f}")
