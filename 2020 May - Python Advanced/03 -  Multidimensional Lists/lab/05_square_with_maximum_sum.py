(row_count, col_count) = map(int, input().split(', '))
mtx = [list(map(int, input().split(', '))) for _ in range(int(row_count))]

r, c, largest_sum = 0, 0, 0

for h in range(row_count - 1):
    for v in range(col_count - 1):
        summed = sum([mtx[h][v], mtx[h][v + 1], mtx[h + 1][v], mtx[h + 1][v + 1]])
        if summed > largest_sum:
            r, c = h, v
            largest_sum = summed

print('{} {}\n{} {}\n{}'.format(mtx[r][c], mtx[r][c + 1], mtx[r + 1][c], mtx[r + 1][c + 1], largest_sum))