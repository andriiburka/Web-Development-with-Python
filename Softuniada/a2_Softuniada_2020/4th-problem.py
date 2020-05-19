n_m = list(map(int, input().split()))
n = n_m[0]
m = n_m[1]
map_list = []

instructions = []

for row in range(1, n + 1):
    map_list.append(input())

for col in range(1, m + 1):
    instructions.append(input())

my_position_index = 0
dash_position = 0

for r in map_list:
    print(r)
    for a in range(len(map_list[0])):
        print(f'Current index of {r} is {a}')
        if (map_list[0])[a] == 'S':
            my_position_index = a
        if (map_list[0])[a] == '-':
            dash_position = a

for instruction in instructions:
    print(f'Current instruction is: {instruction}')

print(f'My position index is: {my_position_index}')
