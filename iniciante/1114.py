senha = 2002
while True:
    senha_inform = int(input())
    if senha_inform != senha:
        print("Senha Invalida")
    else:
        print("Acesso Permitido")
        break
