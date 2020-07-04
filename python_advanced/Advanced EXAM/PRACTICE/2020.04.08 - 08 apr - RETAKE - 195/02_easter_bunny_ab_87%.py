n = int(input())
matrix = [input().split() for _ in range(n)]
start_position = tuple((r, c) for r in range(n) for c in range(n) if matrix[r][c] == 'B')
row, col = start_position[0][0], start_position[0][1]
possible_directions = {
    'up': [[], []],
    'down': [[], []],
    'left': [[], []],
    'right': [[], []]}
amount = -1000

for row_up in range(row - 1, -1, -1):  # up
    if not matrix[row_up][col] == 'X':
        possible_directions['up'][0].append(int(matrix[row_up][col]))
        possible_directions['up'][1].append([row_up, col])
    else:
        break
for row_down in range(row + 1, n):  # down
    if not matrix[row_down][col] == 'X':
        possible_directions['down'][0].append(int(matrix[row_down][col]))
        possible_directions['down'][1].append([row_down, col])
    else:
        break
for col_left in range(col - 1, -1, -1):  # left
    if not matrix[row][col_left] == 'X':
        possible_directions['left'][0].append(int(matrix[row][col_left]))
        possible_directions['left'][1].append([row, col_left])
    else:
        break
for col_right in range(col + 1, n):  # right
    if not matrix[row][col_right] == 'X':
        possible_directions['right'][0].append(int(matrix[row][col_right]))
        possible_directions['right'][1].append([row, col_right])
    else:
        break

summed_possible_directions = {k: [sum((v[0])), v[1]] for k, v in possible_directions.items()}
fancy_direction_info = sorted(summed_possible_directions.items(), key=lambda x: x[1][0], reverse=True)[0]
direction, amount, coordinates = fancy_direction_info[0], fancy_direction_info[1][0], fancy_direction_info[1][1]

print(direction)
[print(i) for i in coordinates]
print(amount)

# 87/100
# брой колони са равни на брой редове - не гърми заради това