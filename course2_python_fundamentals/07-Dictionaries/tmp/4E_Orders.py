items_list = []
items_dict = {}

while True:
    user_input = input()
    if user_input == 'buy':
        break
    else:
        user_input = user_input.split(" ")
        quantity = int(user_input[2])
    if user_input[0] not in items_list:
        items_list.append(user_input[0])
        items_dict[user_input[0]] = [float(user_input[1]), quantity]
    else:
        old_quantity = items_dict[user_input[0]][1]
        items_dict[user_input[0]] = [float(user_input[1]), quantity + old_quantity]

for i in items_list:
    print(f"{i} -> {items_dict[i][0] * items_dict[i][1]:.2f}")