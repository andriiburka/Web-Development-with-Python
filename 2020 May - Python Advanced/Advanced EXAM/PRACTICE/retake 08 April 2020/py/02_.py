'''

Input
•	Number representing the size of the field (matrix NxN)
•	Matrix representing the field (each position separated by single space)


'''

# n = int(input())
#
# matrix =


# matrix = [
#     [4, 18, 9, 7, 24, 41, 52, 11],
#     [54, 21, 19, 'X', 6, 34, 75, 57],
#     [76, 67, 7, 44, 76, 27, 56, 37],
#     [92, 35, 25, 37, 52, 34, 56, 72],
#     [35, 'X', 1, 45, 4, 'X', 37, 63],
#     [105, 'X', 'B', 2, 12, 43, 5, 19],
#     [48, 19, 35, 20, 32, 27, 42, 4],
#     [73, 88, 78, 32, 37, 52, 'X', 22]
# ]

n = 5
matrix = [[1, 3, 7, 9, 11],
          ['X', 5, 4, 'X', 63],
          [7, 3, 21, 95, 1],
          ['B', 1, 73, 4, 9],
          [9, 2, 33, 2, 0]]

possible_directions = {
    'up': [],
    'down': [],
    'left': [],
    'right': []}

coordinates = []
position = 0, 0
tot = 0

tmp = []
for r in range(n):
    for c in range(n):
        if matrix[r][c] == 'B':
            position = r, c

            # up
            for i_up in range(r - 1, -1, -1):
                if matrix[i_up][c] == 'X' or r == 0:  # if not X or NOT START ROW
                    break
                else:
                    possible_directions['up'].append(matrix[i_up][c])
                    # if sum(possible_directions['up']) > tot:
                    #     tot = sum(possible_directions['up'])
                    coordinates.append([i_up, c])

            # down
            for i_down in range(r + 1, n):
                if matrix[i_down][c] == 'X' or r == n - 1:
                    break
                else:
                    possible_directions['down'].append(matrix[i_down][c])

            # left
            for i_left in range(c - 1, -1, -1):
                if matrix[i_left][c] == 'X':
                    break
                elif c <= 0:  # MOVING LEFT - NOT IMPOSIBRU
                    continue
                else:
                    possible_directions['left'].append(matrix[i_left][c])

            # right
            for i_right in range(c + 1, n):
                print(i_right, c)
                print(matrix[i_right][c])
                print('-' * 10)
                # if matrix[i_right][c] == 'X':
                #     break
                # elif c >= n-1:  # MOVING RIGHT - NOT IMPOSIBRU
                #     continue
                # else:
                #     possible_directions['right'].append(matrix[i_right][c])

print(possible_directions)
