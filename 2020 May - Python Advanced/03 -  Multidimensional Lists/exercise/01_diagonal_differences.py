# # v2
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


# # REGULAR SHOW
# n = int(input())
# matrix = list()
# for _ in range(n):
#     matrix.append(
#         list(map(int, input().split()))
#     )
# diagonal_started_top_left = list()
# for i in range(len(matrix)):
#     diagonal_started_top_left.append(
#         matrix[i][i]
#     )
# diagonal_started_top_right = list()
# list_1 = list()
# for h in range(len(matrix)):
#     list_1.append(h)
# list_2 = []
# for v in range(len(matrix) - 1, -1, -1):
#     list_2.append(v)
# for i in tuple(zip(list_1, list_2)):
#     vertical, horizontal = i[0], i[1]
#     diagonal_started_top_right.append(
#         matrix[vertical][horizontal]
#     )
# summed_top_left, summed_top_right = sum(diagonal_started_top_left), sum(diagonal_started_top_right)
# result = summed_top_left - summed_top_right
# print(abs(result))