entrada = input().split()
a, b, c, d = entrada
media = (float(a) * 2 + float(b) * 3 + float(c) * 4 + float(d)) / 10

if media < 5.0:
    print(f"Media: {media:.1f}\n"
          f"Aluno reprovado.")

elif media >= 7.0:
    print(f"Media: {media:.1f}\n"
          f"Aluno aprovado.")

else:
    exame = float(input())
    mediafinal = (media + exame) / 2
    if mediafinal > 5.0:
        print(f"Media: {media:.1f}\n"
              f"Aluno em exame.\n"
              f"Nota do exame: {exame:.1f}\n"
              f"Aluno aprovado.\n"
              f"Media final: {mediafinal:.1f}")
    else:
        print(f"Media: {media:.1f}\n"
              f"Aluno em exame.\n"
              f"Nota do exame: {exame:.1f}\n"
              f"Aluno reprovado.\n"
              f"Media final: {mediafinal:.1f}")
