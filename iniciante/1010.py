total = 0
for i in range(2):
    linha = input().split()
    total += int(linha[1]) * float(linha[2])
print(f"VALOR A PAGAR: R$ {total:.2f}")
