casos = int(input())

for x in range(casos):

    entrada = int(input())
    fibo_0 = 0
    fibo_1 = 1
    lista_fibo = []
    lista_fibo.append(fibo_0)
    lista_fibo.append(fibo_1)


    for y in range(entrada):
        fibo_0, fibo_1 = fibo_1, fibo_0 + fibo_1
        lista_fibo.append(fibo_1)

    print(f"Fib({entrada}) = {lista_fibo[entrada]}")
