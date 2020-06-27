# v1
matrix = {name: [[], []] for name in input().split(', ')}
while True:
    cmd = input().split('-')
    if "End" not in cmd:
        name, item, cost = cmd[0], cmd[1], cmd[2]
        if item not in matrix[name][0]:
            matrix[name][0].append(item), matrix[name][1].append(cost)
    else:
        break
[print('''{} -> Items: {}, Cost: {}'''.format(name, len(values[0]), sum([int(num) for num in values[1]]))) for
 name, values in matrix.items()]





# v2 _______________________________________________
heroes = {name: {} for name in input().split(", ")}
while True:
    command = input()
    if not command.startswith('End'):
        c = command.split("-")
        name, item, cost = c[0], c[1], int(c[2])
        if item not in heroes[name]:
            heroes[name][item] = cost
    else:
        break
[print("{} -> Items: {}, Cost: {}".format(name, len(heroes[name]), sum(heroes[name].values()))) for name in heroes]
