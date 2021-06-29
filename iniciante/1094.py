ent = int(input())

coelhos, ratos, sapos = 0, 0, 0

for i in range(ent):
    cobaia = input().split()
    if cobaia[1] == 'C':
        coelhos += int(cobaia[0])
    elif cobaia[1] == 'R':
        ratos += int(cobaia[0])
    else:
        sapos += int(cobaia[0])

total = coelhos + ratos + sapos

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(coelhos * 100) / total:.2f} %")
print(f"Percentual de ratos: {(ratos * 100) / total:.2f} %")
print(f"Percentual de sapos: {(sapos * 100) / total:.2f} %")
