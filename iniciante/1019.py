segundos = int(input())
horas = int(segundos / 3600)
sobra = segundos % 3600
minutos = int(sobra / 60)
seg = int(sobra % 60)
print(f"{horas}:{minutos}:{seg}")
