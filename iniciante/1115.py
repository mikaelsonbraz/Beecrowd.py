while True:
    ent = input().split()
    coord1, coord2 = int(ent[0]), int(ent[1])
    if coord1 == 0 or coord2 == 0:
        break
    else:
        if coord1 > 0 and coord2 > 0:
            print("primeiro")
        elif coord1 < 0 and coord2 < 0:
            print("terceiro")
        elif coord1 > 0 and coord2 < 0:
            print("quarto")
        else:
            print("segundo")
            