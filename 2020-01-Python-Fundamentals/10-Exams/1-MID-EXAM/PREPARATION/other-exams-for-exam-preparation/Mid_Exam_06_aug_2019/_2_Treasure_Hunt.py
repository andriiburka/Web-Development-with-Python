# 1
treasure_chest = list(map(str, input().split('|')))
stolen_items = []

# 2
while True:
    command = list(map(str, input().split()))
    if command[0] == 'Yohoho!':
        break
    else:
        if command[0] == 'Loot':
            for item in command[1:]:
                if item in treasure_chest:
                    continue
                else:
                    treasure_chest.insert(0, item)

        elif command[0] == 'Drop':
            index = int(command[1])
            if 0 <= index < len(treasure_chest):
                treasure_chest.append(treasure_chest.pop(int(command[1])))

        elif command[0] == 'Steal':
            for s_item in range(-int(command[1]), 0):
                stolen_items.append(treasure_chest[s_item])
                treasure_chest.remove(treasure_chest[s_item])

sum_of_chars = 0
for thing in treasure_chest:
    sum_of_chars += len(thing)

divider = len(treasure_chest)

if sum_of_chars == 0 or divider == 0:
    print(', '.join(stolen_items))
    print('Failed treasure hunt.')
else:
    average_gain = sum_of_chars / divider
    print(', '.join(stolen_items))
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")