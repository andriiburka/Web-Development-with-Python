matrix = [list(map(int, input().split())) for _ in range(int(input()))]
tmp_li = [(matrix[index_of_list][index_of_list]) for index_of_list in range(len(matrix))]
print(sum([num for num in tmp_li]))