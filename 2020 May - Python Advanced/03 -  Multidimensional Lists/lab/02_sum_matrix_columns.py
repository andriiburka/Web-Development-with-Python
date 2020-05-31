rows_count, columns_count = list(map(int, input().split(', ')))
matrix = [list(map(int, input().split())) for _ in range(rows_count)]
di = {col: 0 for col in range(columns_count)}

for row in range(rows_count):
    for col_i in range(len(matrix[row])):
        di[col_i] += matrix[row][col_i]

[print(summing) for summing in di.values()]