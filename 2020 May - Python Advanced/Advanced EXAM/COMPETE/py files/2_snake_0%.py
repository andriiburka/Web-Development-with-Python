matrix = [list(map(str, "".join(input()))) for _ in range(int(input()))]
snake_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'S'][0]
B_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == 'B']
food_pos = [[row, col] for row in range(len(matrix)) for col in range(len(matrix[row])) if matrix[row][col] == '*']
its_not_possible_to_hack_NASA_with_CSS = True
food_quantity = 0
game_over = False

while its_not_possible_to_hack_NASA_with_CSS:
    cmd = input()

    if cmd == 'up':  # row-1
        if snake_pos[0] - 1 < 0:
            game_over = True
            break

        elif matrix[snake_pos[0] - 1][snake_pos[1]] == 'B':
            matrix[snake_pos[0] - 1][snake_pos[1]] = '.'
            snake_pos[0] -= 1

            for curr_b_pos in B_pos:
                if snake_pos != curr_b_pos:
                    snake_pos = curr_b_pos

            matrix[snake_pos[0]][snake_pos[1]] = 'S'

        elif matrix[snake_pos[0] - 1][snake_pos[1]] == '*':
            matrix[snake_pos[0] - 1][snake_pos[1]] = ''
            snake_pos[0] -= 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'
            food_quantity += 1
        else:
            matrix[snake_pos[0]][snake_pos[1]] = '.'
            snake_pos[0] -= 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'

    elif cmd == 'down':
        if snake_pos[0] + 1 == len(matrix):
            game_over = True
            break
        elif matrix[snake_pos[0] + 1][snake_pos[1]] == 'B':
            matrix[snake_pos[0] + 1][snake_pos[1]] = '.'
            snake_pos[0] += 1

            for curr_b_pos in B_pos:
                if snake_pos != curr_b_pos:
                    snake_pos = curr_b_pos

            matrix[snake_pos[0]][snake_pos[1]] = '.'

        elif matrix[snake_pos[0] + 1][snake_pos[1]] == '*':
            matrix[snake_pos[0] + 1][snake_pos[1]] = '.'
            snake_pos[0] += 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'
            food_quantity += 1
        else:
            matrix[snake_pos[0]][snake_pos[1]] = '.'
            snake_pos[0] += 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'

    elif cmd == 'left':
        if snake_pos[1] - 1 < 0:
            game_over = True
            break
        elif matrix[snake_pos[0]][snake_pos[1] - 1] == 'B':
            matrix[snake_pos[0]][snake_pos[1] - 1] = '.'
            snake_pos[1] -= 1

            for curr_b_pos in B_pos:
                if snake_pos != curr_b_pos:
                    snake_pos = curr_b_pos

            matrix[snake_pos[0]][snake_pos[1]] = 'S'

        elif matrix[snake_pos[0]][snake_pos[1] - 1] == '*':
            matrix[snake_pos[0]][snake_pos[1] - 1] = '.'
            snake_pos[1] -= 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'
            food_quantity += 1
        else:
            matrix[snake_pos[0]][snake_pos[1]] = '.'
            snake_pos[1] -= 1
            matrix[snake_pos[0]][snake_pos[1]] = '.'

    elif cmd == 'right':
        if snake_pos[1] + 1 == len(matrix):
            game_over = True
            break
        elif matrix[snake_pos[0]][snake_pos[1] + 1] == 'B':
            matrix[snake_pos[0]][snake_pos[1] + 1] = '.'
            snake_pos[1] += 1

            for curr_b_pos in B_pos:
                if snake_pos != curr_b_pos:
                    snake_pos = curr_b_pos

            matrix[snake_pos[0]][snake_pos[1]] = '.'

        elif matrix[snake_pos[0]][snake_pos[1] + 1] == '*':
            matrix[snake_pos[0]][snake_pos[1] + 1] = '.'
            snake_pos[1] += 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'
            food_quantity += 1
        else:
            matrix[snake_pos[0]][snake_pos[1]] = '.'
            snake_pos[1] += 1
            matrix[snake_pos[0]][snake_pos[1]] = 'S'

if not game_over or food_quantity >= 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food_quantity}")
[print("".join(i)) for i in matrix]
