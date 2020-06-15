(row_count, col_count) = map(int, input().split())
n = 0

matrix = [list(map(str, input().split())) for _ in range(row_count)]

square_indices = []
for r in range(row_count - 1):
    for c in range(col_count - 1):
        is_square_of_b = matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]
        if is_square_of_b:
            square_indices.append(matrix[r][c])

print(square_indices.__len__())