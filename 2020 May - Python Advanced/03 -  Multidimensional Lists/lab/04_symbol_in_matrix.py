matrix = [[x for x in input()] for row in range(int(input()))]
symbol = input()
is_found = False

for current_list in range(len(matrix)):
    if symbol in matrix[current_list]:
        row, column = current_list, matrix[current_list].index(symbol)
        print(f"({row}, {column})")
        is_found = True
        break

if not is_found:
    print(f"{symbol} does not occur in the matrix")