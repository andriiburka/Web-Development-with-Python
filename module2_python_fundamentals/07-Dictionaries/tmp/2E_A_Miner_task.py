metals_dict = {}

while True:
    str_input = input()
    if str_input == "stop":
        break
    else:
        int_input = int(input())

    if str_input in metals_dict:
        metals_dict[str_input] += int_input
    else:
        metals_dict[str_input] = int_input

for resource, quantity in metals_dict.items():
    print(f'{resource} -> {quantity}')
