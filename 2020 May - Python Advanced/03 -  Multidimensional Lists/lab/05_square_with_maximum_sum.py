# My solution
# 100/100

(row_count, col_count) = map(int, input().split(', '))
mtx = [list(map(int, input().split(', '))) for _ in range(int(row_count))]  # matrix ROW x COL
sub_matrix_winner = tuple
largest_sum = 0

for r in range(row_count - 1):
    for c in range(col_count - 1):
        sub_matrix_2x2 = [mtx[r][c], mtx[r][c + 1], mtx[r + 1][c], mtx[r + 1][c + 1]]

        if sum(sub_matrix_2x2) > largest_sum:
            sub_matrix_winner = sub_matrix_2x2
            largest_sum = sum(sub_matrix_2x2)

print('{} {}\n{} {}\n{}'.format(*sub_matrix_winner, largest_sum))