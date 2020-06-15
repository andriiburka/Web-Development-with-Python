# My solution
# 100/100

(row_count, col_count) = map(int, input().split(', '))
mtx = [list(map(int, input().split(', '))) for _ in range(int(row_count))]
output = tuple
largest_sum = 0

for r in range(row_count - 1):
    for c in range(col_count - 1):
        amount = (mtx[r][c],
                  mtx[r][c + 1],
                  mtx[r + 1][c],
                  mtx[r + 1][c + 1])

        if amount > largest_sum:
            output = amount
            largest_sum = amount

print(output)
# print('{} {}\n{} {}\n{}'.format(*output, largest_sum))