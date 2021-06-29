entrada = float(input())

if entrada <= 2000.00:
    print("Isento")
elif 2000.01 <= entrada <= 3000.00:
    saldo = entrada - 2000
    print(f"R$ {saldo * 0.08:.2f}")
elif 3000.01 <= entrada <= 4500.00:
    saldo = entrada - 3000
    print(f"R$ {80 + (saldo * 0.18):.2f}")
else:
    saldo = entrada - 4500
    print(f"R$ {80 + 270 + (saldo * 0.28):.2f}")
