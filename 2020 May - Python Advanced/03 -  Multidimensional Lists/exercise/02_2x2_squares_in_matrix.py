# # 18:35
#
# rows, cols = list(map(int, input().split()))  # int, int
# matrix = [input().split() for i in range(rows)]  # [str, str, str, str]
# indices = list()
# equals = 0
#

rows_count, cols_count = [int(x) for x in input().split()]

matrix = []
counter = 0
for _ in range(rows_count):
    line = [x for x in input().split()]
    matrix.append(line)
for row in range(rows_count - 1):
    for col in range(cols_count - 1):
        current = matrix[row][col]
        current_right = matrix[row][col + 1]
        bottom = matrix[row + 1][col]
        bottom_right = matrix[row + 1][col + 1]
        if current == current_right and current == bottom and current == bottom_right:
            counter += 1
print(counter)