numbers = list(map(int, input().split(', ')))
max_number = max(numbers)

while max_number % 10 != 0:
    max_number += 1

for current_row in range(1, int(max_number / 10) + 1):
    x_list = []
    for current_num in numbers:

        if current_row * 10 - 10 < current_num <= current_row * 10:
            x_list.append(current_num)

    print(f"Group of {current_row * 10}'s: {x_list}")

numbers.clear()
