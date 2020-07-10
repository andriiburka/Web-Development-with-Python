my_string = input()

n = int(input())
nw_pos = ()
play_pos = []
matrix = []

my_dict = {"up": (-1, 0), "down": (+1, 0), "left": (0, -1), "right": (0, +1)}

for row in range(n):
    line = [x for x in input()]
    for col in range(n):
        if line[col] == "P":
            play_pos = [row, col]
    matrix.append(line)
m = int(input())
for _ in range(m):
    command = input()
    new_row = play_pos[0] + my_dict[command][0]
    new_col = play_pos[1] + my_dict[command][1]
    nw_pos = (new_row, new_col)
    if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix):
        if matrix[new_row][new_col].isalpha():
            my_string += matrix[new_row][new_col]
            matrix[new_row][new_col] = "P"
            matrix[play_pos[0]][play_pos[1]] = "-"
            play_pos = nw_pos
        else:
            matrix[new_row][new_col] = "P"
            matrix[play_pos[0]][play_pos[1]] = "-"
            play_pos = nw_pos
    else:
        if len(my_string) >= 1:
            my_string = my_string[:-1]

print(my_string)
for r in range(len(matrix)):
    for c in range(len(matrix)):
        print(matrix[r][c], end="")
    print()
