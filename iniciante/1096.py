I, J = 1, 7

for x in range(15):
    print(f"I={I} J={J}")
    J -= 1
    if J == 4:
        I += 2
        J = 7
