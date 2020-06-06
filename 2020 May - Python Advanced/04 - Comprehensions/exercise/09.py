names = input().split(', ')
matrix = {}

user_input = input().split()

while user_input:

    if "End" in user_input:
        break

    cmd = user_input
    name, item, cost = cmd[0], cmd[1], int(cmd[2])

    if name not in matrix:
        matrix.update({name: [{item}, cost]})
    elif item not in matrix[name][0]:
        matrix[name][0].add(item)
        matrix[name][1] += cost

    user_input = input()

[print(f"{name} -> Items: {len(values[0])}, Cost: {values[1]}") for name, values in matrix.items()]