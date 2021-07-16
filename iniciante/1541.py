while True:
    try:
        entrada = input().split()

        lado1 = int(entrada[0])
        lado2 = int(entrada[1])
        porcentagem = int(entrada[2])

        if lado1 == 0 or lado2 == 0 or porcentagem == 0:
            break

        else:
            print(f"{int((((lado1 * lado2) * 100) / porcentagem) ** 0.5)}")
    except IndexError:
        break
