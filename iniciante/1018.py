dinheiro = int(input())
cem = int(dinheiro / 100)
sobra = dinheiro % 100
cinquentinha = int(sobra / 50)
sobra2 = sobra % 50
vintinho = int(sobra2 / 20)
sobra3 = sobra2 % 20
dez = int(sobra3 / 10)
sobra4 = sobra3 % 10
cinquinho = int(sobra4 / 5)
sobra5 = sobra4 % 5
doireal = int(sobra5 / 2)
umreal = int(sobra5 % 2)
print(f"{dinheiro}\n"
      f"{cem} nota(s) de R$ 100,00\n"
      f"{cinquentinha} nota(s) de R$ 50,00\n"
      f"{vintinho} nota(s) de R$ 20,00\n"
      f"{dez} nota(s) de R$ 10,00\n"
      f"{cinquinho} nota(s) de R$ 5,00\n"
      f"{doireal} nota(s) de R$ 2,00\n"
      f"{umreal} nota(s) de R$ 1,00")
