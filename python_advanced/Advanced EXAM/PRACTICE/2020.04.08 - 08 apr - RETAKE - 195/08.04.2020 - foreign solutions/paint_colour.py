from _collections import deque

list_colors = deque(input().lower().split())
main_colors = ["red", "yellow", "blue"]
second_col = ["orange", "purple", "green"]
found_colors = []

while list_colors:
    if len(list_colors) > 1:
        first = list_colors[0]
        second = list_colors[-1]
        result_1 = first + second
        result_2 = second + first

    else:
        result_1 = list_colors.popleft()
        result_2 = result_1

    if result_1 in main_colors or result_1 in second_col:
        found_colors.append(result_1)
        list_colors.popleft()
        list_colors.pop()
    else:

        if result_2 in main_colors or result_2 in second_col:
            found_colors.append(result_2)
            list_colors.popleft()
            list_colors.pop()
        else:
            if len(list_colors) > 0:
                first_back = list_colors.popleft()[:-1]
                sec_back = list_colors.pop()[:-1]
                if len(list_colors) > 1:
                    index = int(len(list_colors) / 2)
                    list_colors.insert(index, first_back)
                    list_colors.insert(index + 1, sec_back)

for colour in found_colors[::-1]:
    current = found_colors.pop()
    if current in main_colors:
        found_colors.append(current)
    else:
        if current == "orange":
            if "red" in main_colors and "yellow" in found_colors:
                found_colors.append(current)
        if current == "purple":
            if "red" in main_colors and "blue" in found_colors:
                found_colors.append(current)
        if current == "green":
            if "blue" in main_colors and "yellow" in found_colors:
                found_colors.append(current)

print(found_colors)
