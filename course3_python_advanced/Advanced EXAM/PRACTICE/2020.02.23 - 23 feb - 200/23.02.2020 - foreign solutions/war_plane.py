def get_new_changes(dir_changes, s):
    return dir_changes[0] * s, dir_changes[1] * s


def is_valid(pos, plane_position, size):
    new_row = plane_position[0] + pos[0]
    new_col = plane_position[1] + pos[1]
    return 0 <= new_row < size and 0 <= new_col < size


def shoot(row, col, matrix):
    matrix[row][col] = "x"


def is_free(pos, plane_position, matrix):
    new_row = plane_position[0] + pos[0]
    new_col = plane_position[1] + pos[1]
    return matrix[new_row][new_col] == "."


def get_current_targets(matrix):
    targets = 0
    for row in matrix:
        targets += row.count("t")
    return targets


n = int(input())
field = []
plane_pos = []
targets_count = 0

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == "p":
            plane_pos = [i, j]
        elif line[j] == "t":
            targets_count += 1
    field.append(line)

m = int(input())

for _ in range(m):
    command = input().split()
    direction = command[1]
    direction_changes = directions[direction]
    step = int(command[2])
    new_changes = get_new_changes(direction_changes, step)

    if command[0] == "shoot":
        if is_valid(new_changes, plane_pos, n):
            shooting_row = plane_pos[0] + new_changes[0]
            shooting_col = plane_pos[1] + new_changes[1]
            shoot(shooting_row, shooting_col, field)

            if get_current_targets(field) == 0:
                print(f"Mission accomplished! All {targets_count} targets destroyed.")
                break
    else:
        if is_valid(new_changes, plane_pos, n) and is_free(new_changes, plane_pos, field):
            field[plane_pos[0]][plane_pos[1]] = "."
            plane_pos[0] += new_changes[0]
            plane_pos[1] += new_changes[1]
            field[plane_pos[0]][plane_pos[1]] = "p"

targets_left = get_current_targets(field)

if targets_left != 0:
    print(f"Mission failed! {targets_left} targets left.")

[print(" ".join(row)) for row in field]