combustiveis = {"alcool": 0, "gaso": 0, "diesel": 0}
while True:
    combu = int(input())
    if combu == 1:
        combustiveis['alcool'] += 1
    elif combu == 2:
        combustiveis["gaso"] += 1
    elif combu == 3:
        combustiveis["diesel"] += 1
    elif combu == 4:
        break
    else:
        pass

print(f"MUITO OBRIGADO")
print(f"Alcool: {combustiveis['alcool']}")
print(f"Gasolina: {combustiveis['gaso']}")
print(f"Diesel: {combustiveis['diesel']}")
