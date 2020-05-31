# v2
# matrix = [list(map(int, input().split())) for _ in range(int(input()))]
# diagonal1 = [(matrix[i][i]) for i in range(len(matrix))]
# diagonal2 = [(matrix[i][(len(matrix)-i-1)]) for i in range(len(matrix))]
# print(abs(sum(diagonal1) - sum(diagonal2)))



# v1 - faster
matrix = [list(map(int, input().split())) for _ in range(int(input()))]
diagonal1 = [(matrix[i][i]) for i in range(len(matrix))]
diagonal2 = [matrix[i[0]][i[1]] for i in tuple(
        zip([h for h in range(len(matrix))], [v for v in range(len(matrix) - 1, -1, -1)]))]
print(abs(sum(diagonal1) - sum(diagonal2)))
