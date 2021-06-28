entrada = float(input())

if 0 <= entrada <= 400.00:
    print(f"Novo salario: {entrada + (entrada * 0.15):.2f}\n"
          f"Reajuste ganho: {entrada * 0.15:.2f}\n"
          f"Em percentual: 15 %")

elif 400.01 <= entrada <= 800.00:
    print(f"Novo salario: {entrada + (entrada * 0.12):.2f}\n"
          f"Reajuste ganho: {entrada * 0.12:.2f}\n"
          f"Em percentual: 12 %")

elif 800.01 <= entrada <= 1200.00:
    print(f"Novo salario: {entrada + (entrada * 0.1):.2f}\n"
          f"Reajuste ganho: {entrada * 0.1:.2f}\n"
          f"Em percentual: 10 %")

elif 1200.01 <= entrada <= 2000.00:
    print(f"Novo salario: {entrada + (entrada * 0.07):.2f}\n"
          f"Reajuste ganho: {entrada * 0.07:.2f}\n"
          f"Em percentual: 7 %")

else:
    print(f"Novo salario: {entrada + (entrada * 0.04):.2f}\n"
          f"Reajuste ganho: {entrada * 0.04:.2f}\n"
          f"Em percentual: 4 %")
