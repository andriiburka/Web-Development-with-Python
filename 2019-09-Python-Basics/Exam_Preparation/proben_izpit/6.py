num = input()
if int(num[0]) != 0 and int(num[1]) != 0 and int(num[2]) != 0:
    for first in range(1, int(num[2]) + 1):
        for middle in range(1, int(num[1]) + 1):
            for last in range(1, int(num[0]) + 1):
                result = first * middle * last
                print(f'{first} * {middle} * {last} = {result};')
