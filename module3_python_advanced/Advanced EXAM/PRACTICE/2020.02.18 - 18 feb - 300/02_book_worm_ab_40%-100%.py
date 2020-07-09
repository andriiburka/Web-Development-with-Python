from collections import deque

word = input()
matrix = deque([list(map(str, "".join(input()))) for row in range(int(input()))])
p_position = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'P']
r, c = p_position[0]

for i in range(int(input())):
    cmd = input()

    if cmd == 'up':
        if r - 1 > -1:
            tmp = matrix[r][c]
            matrix[r][c] = '-'

            if matrix[r - 1][c].isalpha():
                word += matrix[r - 1][c]
            matrix[r - 1][c] = tmp
            r -= 1
            continue
        elif r - 1 < 0:
            word = word[:-1]

    elif cmd == 'down':
        if r + 1 < len(matrix):
            tmp = matrix[r][c]
            matrix[r][c] = '-'

            if matrix[r + 1][c].isalpha():
                word += matrix[r + 1][c]
            matrix[r + 1][c] = tmp
            r += 1
            continue
        elif r + 1 > len(matrix) - 1:
            word = word[:-1]

    elif cmd == 'left':
        if c - 1 >= 0:
            tmp = matrix[r][c]
            matrix[r][c] = '-'

            if matrix[r][c - 1].isalpha():
                word += matrix[r][c - 1]
            matrix[r][c - 1] = tmp
            c -= 1
            continue
        elif c - 1 < 0:
            word = word[:-1]

    elif cmd == 'right':
        if c + 1 < len(matrix):
            tmp = matrix[r][c]
            matrix[r][c] = '-'

            if matrix[r][c + 1].isalpha():
                word += matrix[r][c + 1]
            matrix[r][c + 1] = tmp
            c += 1
            continue
        elif c + 1 > len(matrix) - 1:

            word = word[:-1]

print(word)
[print("".join(row)) for row in matrix]