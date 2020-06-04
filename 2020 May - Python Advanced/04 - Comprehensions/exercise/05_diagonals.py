n = int(input())
matrix = [list(map(int, input().split(', '))) for i in range(n)]

first = [matrix[i][i] for i in range(n)]
second = [matrix[i][n-i-1] for i in range(n)]

print('First diagonal: {}. Sum: {}'.format(str(first)[1:-1], sum(first)))
print('Second diagonal: {}. Sum: {}'.format(str(second)[1:-1], sum(second)))