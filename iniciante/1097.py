I, J = 1, 7

for x in range(1, 16):
    print(f"I={I} J={J}")
    J -= 1
    if x % 3 == 0:
        I += 2
        J += 5
