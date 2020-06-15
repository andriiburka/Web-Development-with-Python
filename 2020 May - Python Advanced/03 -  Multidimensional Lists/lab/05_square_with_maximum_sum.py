# My solution
# 100/100

(row_count, col_count) = map(int, input().split(', '))
mtx = [list(map(int, input().split(', '))) for _ in range(int(row_count))]
x_row, x_col, largest_sum = 0, 0, 0

for horizontal in range(row_count - 1):
    for vertical in range(col_count - 1):
        amount = sum([
            mtx[horizontal][vertical],
            mtx[horizontal][vertical + 1],
            mtx[horizontal + 1][vertical],
            mtx[horizontal + 1][vertical + 1]])

        if amount > largest_sum:
            x_row, x_col = horizontal, vertical
            largest_sum = amount

print('{} {}\n{} {}\n{}'
      .format(mtx[x_row][x_col], mtx[x_row][x_col + 1], mtx[x_row + 1][x_col], mtx[x_row + 1][x_col + 1], largest_sum))