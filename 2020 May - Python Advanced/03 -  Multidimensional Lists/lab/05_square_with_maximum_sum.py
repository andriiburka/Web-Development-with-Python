(row_count, col_count) = map(int, input().split(', '))
mtx = [list(map(int, input().split(', '))) for _ in range(int(row_count))]

row, col = 0, 0
largest_sum = 0

for r in range(row_count - 1):
    for c in range(col_count - 1):
        summed = sum([mtx[r][c], mtx[r][c + 1], mtx[r + 1][c], mtx[r + 1][c + 1]])
        if summed > largest_sum:
            row, col = r, c
            largest_sum = summed

print('{} {}\n{} {}\n{}'.format(mtx[row][col], mtx[row][col + 1], mtx[row + 1][col], mtx[row + 1][col + 1], largest_sum))