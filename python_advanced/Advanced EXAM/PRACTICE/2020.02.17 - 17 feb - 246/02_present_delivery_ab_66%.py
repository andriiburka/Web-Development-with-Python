def presents_for_all_nearby(cmd):
    global presents, good_kids_left

    possible_moves = ['up', 'down', 'left', 'right']
    if cmd == 'up':
        possible_moves.remove('down')
    elif cmd == 'down':
        possible_moves.remove('up')
    elif cmd == 'left':
        possible_moves.remove('right')
    elif cmd == 'right':
        possible_moves.remove('left')

    while possible_moves:
        direction = possible_moves.pop()
        if direction == 'up' and santa_pos[0] - 1 >= 0:
            if matrix[santa_pos[0] - 1][santa_pos[1]] != '-':
                presents -= 1
                if matrix[santa_pos[0] - 1][santa_pos[1]] == 'V':
                    good_kids_left -= 1
                matrix[santa_pos[0] - 1][santa_pos[1]] = '-'

        elif direction == 'down' and santa_pos[0] + 1 < len(matrix):
            if matrix[santa_pos[0] + 1][santa_pos[1]] != '-':
                presents -= 1
                if matrix[santa_pos[0] + 1][santa_pos[1]] == 'V':
                    good_kids_left -= 1
                matrix[santa_pos[0] + 1][santa_pos[1]] = '-'

        elif direction == 'left' and santa_pos[1] - 1 >= 0:
            if matrix[santa_pos[0]][santa_pos[1] - 1] != '-':
                presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] - 1] == 'V':
                    good_kids_left -= 1
                matrix[santa_pos[0]][santa_pos[1] - 1] = '-'

        elif direction == 'right' and santa_pos[1] + 1 < len(matrix):
            if matrix[santa_pos[0]][santa_pos[1] + 1] != '-':
                presents -= 1
                if matrix[santa_pos[0]][santa_pos[1] + 1] == 'V':
                    good_kids_left -= 1
                matrix[santa_pos[0]][santa_pos[1] + 1] = '-'


presents = int(input())
matrix = [input().split(' ') for i in range(int(input()))]

c_pos = []
c_in_matrix = ["C" for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'C']
if c_in_matrix:
    c_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'C'][0]

santa_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'S'][0]
good_kids_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'V']
all_good_kids = len(good_kids_pos)
good_kids_left = len(good_kids_pos)

while True:
    if not presents:
        break

    command = input()
    if not command or command == 'Christmas morning':
        break

    if command == 'up' and santa_pos[0] - 1 >= 0:
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos[0] -= 1
        matrix[santa_pos[0]][santa_pos[1]] = 'S'
        if santa_pos in good_kids_pos:
            presents -= 1
            good_kids_left -= 1
        elif santa_pos == c_pos:
            presents_for_all_nearby(cmd=command)

    elif command == 'down' and santa_pos[0] + 1 < len(matrix):
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos[0] += 1
        matrix[santa_pos[0]][santa_pos[1]] = 'S'
        if santa_pos in good_kids_pos:
            presents -= 1
            good_kids_left -= 1
        elif santa_pos == c_pos:
            presents_for_all_nearby(cmd=command)

    elif command == 'left' and santa_pos[1] - 1 >= 0:
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos[1] -= 1
        matrix[santa_pos[0]][santa_pos[1]] = 'S'
        if santa_pos in good_kids_pos:
            presents -= 1
            good_kids_left -= 1
        elif santa_pos == c_pos:
            presents_for_all_nearby(cmd=command)

    elif command == 'right' and santa_pos[1] + 1 < len(matrix):
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos[1] += 1
        matrix[santa_pos[0]][santa_pos[1]] = 'S'
        if santa_pos in good_kids_pos:
            presents -= 1
            good_kids_left -= 1
        elif santa_pos == c_pos:
            presents_for_all_nearby(cmd=command)

if not presents:
    print("Santa ran out of presents!")
[print(" ".join(i)) for i in matrix]
print(f"No presents for {good_kids_left} nice kid/s."
      if good_kids_left else f"Good job, Santa! {all_good_kids} happy nice kid/s.")
