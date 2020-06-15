# My solution
# 100/100

(row_count, col_count) = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row_count)]  # matrix 4x5
largest_sum = -999  # edge case
output = tuple

for r in range(row_count - 2):
    for c in range(col_count - 2):
        sub_matrix_3x3 = (matrix[r][c], matrix[r][c + 1], matrix[r][c + 2],
                          matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2],
                          matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2])

        if sum(sub_matrix_3x3) > largest_sum:
            largest_sum = sum(sub_matrix_3x3)
            output = sub_matrix_3x3

print('Sum = {}\n{} {} {}\n{} {} {}\n{} {} {}'.format(largest_sum, *output))