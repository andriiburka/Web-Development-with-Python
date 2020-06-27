word = input()
# in this part you don't need to GiveAF how it works..
matrix = [list(map(str, "".join(input()))) for row in range(int(input()))]
p_position = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'P']
move = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}
new_p_position = ()

for _ in range(int(input())):
    direction = input()
    new_row = (p_position[0] + move[direction][0])
    new_col = p_position[1] + move[direction][1]
    new_p_position = (new_row, new_col)

    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        if matrix[new_row][new_col].isalpha():
            word += matrix[new_row][new_col]
            matrix[new_row][new_col] = "P"
            matrix[p_position[0]][p_position[1]] = "-"
            p_position = new_p_position
        else:
            matrix[new_row][new_col] = "P"
            matrix[p_position[0]][p_position[1]] = "-"
            p_position = new_p_position
    else:
        if len(word) >= 1:
            word = word[:-1]

print(word)
[print("".join(row)) for row in matrix]