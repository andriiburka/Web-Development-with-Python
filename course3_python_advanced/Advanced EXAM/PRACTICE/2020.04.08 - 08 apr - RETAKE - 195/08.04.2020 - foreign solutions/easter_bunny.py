import sys

n = int(input())
matrix = [[x for x in input().split()] for i in range(n)]

result = dict()

direction = str()

for r, row in enumerate(matrix):
    for c in range(len(row)):
        element = matrix[r][c]
        if element == "B":
            rabit = [r, c]
            for i in range(1, n + 1):
                if 0 <= r + i < len(matrix):
                    direction = "down"
                    next_element = matrix[r + i][c]
                    if next_element == "X":
                        break
                    else:
                        if direction not in result:
                            result[direction] = [], []
                        result[direction][0].append(int(next_element))
                        result[direction][1].append([r + i, c])

            for i in range(1, n + 1):
                if 0 <= r - i < len(matrix):
                    direction = "up"
                    next_element = matrix[r - i][c]
                    if next_element == "X":
                        break
                    else:
                        if direction not in result:
                            result[direction] = [], []
                        result[direction][0].append(int(next_element))
                        result[direction][1].append([r - i, c])

            for j in range(1, len(row) + 1):
                if 0 <= c - j < len(row):
                    direction = "left"
                    next_element = matrix[r][c - j]
                    if next_element == "X":
                        break
                    else:
                        if direction not in result:
                            result[direction] = [], []
                        result[direction][0].append(int(next_element))
                        result[direction][1].append([r, c - j])

            for j in range(1, len(row) + 1):
                if 0 <= c + j < len(row):
                    direction = "right"
                    next_element = matrix[r][c + j]
                    if next_element == "X":
                        break
                    else:
                        if direction not in result:
                            result[direction] = [], []
                        result[direction][0].append(int(next_element))
                        result[direction][1].append([r, c + j])
max_val = -sys.maxsize
result_direction = str()
for k, v in result.items():
    if sum(v[0]) > max_val:
        max_val = sum(v[0])
        result_direction = k
print(result_direction)
[print(x) for x in result[result_direction][1]]
print(max_val)