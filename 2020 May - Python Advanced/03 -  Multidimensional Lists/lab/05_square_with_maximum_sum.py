(row_count, col_count) = map(int, input().split(', '))
matrix = [list(map(int, input().split(', '))) for _ in range(int(row_count))]

row, col = 0, 0
largest_sum = 0

for r in range(row_count - 1):
    for c in range(col_count - 1):

        summed = sum([matrix[r][c], matrix[r][c + 1], matrix[r + 1][c], matrix[r + 1][c + 1]])

        if summed > largest_sum:
            row, col = r, c
            largest_sum = summed

print('{} {}\n{} {}'.format(matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]))
print(largest_sum)