# 18:35

rows, cols = list(map(int, input().split()))  # int, int
matrix = [input().split() for i in range(rows)]  # [str, str, str, str]
indices = list()
equals = 0

current_letter = ''
for li in range(len(matrix)):
    print(matrix[li])

    for ch in matrix[li]:
        if ch == current_letter:
            indices.append(matrix[li][index(ch)])
        else:
            current_letter = ch

    print()