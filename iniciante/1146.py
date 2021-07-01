while True:
    entrada = int(input())
    if entrada == 0:
        break
    else:
        string = ''
        for x in range(1, entrada + 1):
            if x != entrada:
                string += f"{x} "
            else:
                string += f"{x}"
        print(string)
        