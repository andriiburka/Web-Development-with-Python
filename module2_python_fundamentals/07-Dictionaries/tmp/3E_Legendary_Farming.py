legendary_recipes = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
do_i_get_legendary_item = False
junk = {}

while True:
    if do_i_get_legendary_item:
        break
    else:
        user_input = input().lower().split(" ")
        for index in range(0, len(user_input), 2):
            user_input[index + 1] = user_input[index + 1]
            if user_input[index + 1] in key_materials:
                key_materials[user_input[index + 1]] += int(user_input[index])
                if key_materials[user_input[index + 1]] >= 250:
                    print(f"{legendary_recipes[user_input[index + 1]]} obtained!")
                    key_materials[user_input[index + 1]] = key_materials[user_input[index + 1]] - 250
                    do_i_get_legendary_item = True
                    break
            else:
                if user_input[index + 1] in junk:
                    junk[user_input[index + 1]] += int(user_input[index])
                else:
                    junk[user_input[index + 1]] = int(user_input[index])

for i in sorted(sorted(key_materials), key=lambda x: key_materials[x], reverse=True):
    print(f"{i}: {key_materials[i]}")

for i in sorted(junk):
    print(f"{i}: {junk[i]}")



# user_input = input().lower().split()
#
# #nums_list = [x for x in user_input if x.isdigit()]
# #items_list = [x for x in user_input if not x.isdigit()]
# value_list = []
# item_list = []
# for x in user_input:
#     if x.isdigit():
#         value_list.append(x)
#     else:
#         item_list.append(x)
#
# #user_input_dict = {key: value for key, value in zip(nums_list, items_list)}
# user_input_dict = {}
# for key, value in zip(value_list, item_list):
#     user_input_dict[key] = value
#
# key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
#
# winner = ''
# for key, value in user_input_dict.items():
#     key, value = value, key
#
#     if key in key_materials:
#         key_materials[key] += int(value)
#
#     if key_materials['shards'] >= 250:
#         key_materials['shards'] -= 250
#         winner = 'shards'
#         break
#     elif key_materials['fragments'] >= 250:
#         winner = 'fragments'
#         break
#     elif key_materials['motes'] >= 250:
#         winner = 'motes'
#         break
#
#
# print(winner)