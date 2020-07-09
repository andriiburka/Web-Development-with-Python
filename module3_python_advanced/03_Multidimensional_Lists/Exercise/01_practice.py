n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

diagonal_descending = sum([matrix[r][r] for r in range(n)])
diagonal_ascending = sum([matrix[c][n-c-1] for c in range(n)])

print(abs(diagonal_descending - diagonal_ascending))