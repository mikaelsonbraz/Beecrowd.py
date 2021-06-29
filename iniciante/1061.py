ent1 = input().split()
ent2 = input().split()
ent3 = input().split()
ent4 = input().split()

dia1 = int(ent1[1])
hora1 = int(ent2[0])
minuto1 = int(ent2[2])
segundo1 = int(ent2[4])

dia2 = int(ent3[1])
hora2 = int(ent4[0])
minuto2 = int(ent4[2])
segundo2 = int(ent4[4])

dif_dias = dia2 - dia1

dif_horas = hora2 - hora1
if dif_horas < 0:
    dif_horas += 24
    dif_dias -= 1

dif_minutos = minuto2 - minuto1
if dif_minutos < 0:
    dif_minutos += 60
    dif_horas -= 1
    if dif_horas < 0:
        dif_horas += 24
        dif_dias -= 1

dif_segundos = segundo2 - segundo1
if dif_segundos < 0:
    dif_segundos += 60
    dif_minutos -= 1
    if dif_minutos < 0:
        dif_minutos += 60
        dif_horas -= 1
        if dif_horas < 0:
            dif_horas += 24
            dif_dias -= 1

print(f"{dif_dias} dia(s)\n"
      f"{dif_horas} hora(s)\n"
      f"{dif_minutos} minuto(s)\n"
      f"{dif_segundos} segundo(s)\n")
