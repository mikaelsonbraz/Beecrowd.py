casos = int(input())


for x in range(casos):
    eh_primo = int(input())
    primo = 0

    for y in range(1, eh_primo):
        if eh_primo % y == 0:
            primo += 1

    if primo >= 2:
        print(eh_primo, 'nao eh primo')
    else:
        print(eh_primo, 'eh primo')
