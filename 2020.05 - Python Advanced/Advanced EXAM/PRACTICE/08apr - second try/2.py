matrix_size = int(input())
matrix = [list(map(str, input().split())) for _ in range(matrix_size)]
plane_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'p'][0]
targets = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 't'][0]

killed = 0

for i in range(int(input())):
    cmd = input().split()
    operation, direction, step = cmd[0], cmd[1], int(cmd[2])

    if operation == 'move':
        if direction == 'up':
            pass
        elif direction == 'down':
            pass
        elif direction == 'left':
            pass
        elif direction == 'right':
            pass

    elif operation == 'shoot':

        if direction == 'up':
            if plane_pos[0] - step < matrix_size and matrix[plane_pos[0] - step][plane_pos[1]] in ['t.']:
                if matrix[plane_pos[0] - step][plane_pos[1]] == 't':
                    killed += 1
                matrix[plane_pos[0] - step][plane_pos[1]] = 'x'


        elif direction == 'down':
            pass
        elif direction == 'left':
            pass
        elif direction == 'right':
            pass
