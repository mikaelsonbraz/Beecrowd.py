entrada = int(input())


def fibonacci(num):
    nums = [0]
    a, b = 0, 1
    while len(nums) < num:
        nums.append(b)
        a, b = b, a + b
    return nums

string = ''
for x in fibonacci(entrada):
    if x == fibonacci(entrada)[-1]:
        string += f"{x}"
    else:
        string += f"{x} "


print(string)
