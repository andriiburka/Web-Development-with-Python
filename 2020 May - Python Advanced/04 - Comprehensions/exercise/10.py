n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
while True:
    line = input().split()
    if 'END' in line:
        break
    (row, column, value) = int(line[1]), int(line[2]), int(line[3])
    if 0 <= row < n and 0 <= column < n:
        if "Add" in line[0]:
            matrix[row][column] += value
        elif "Subtract" in line[0]:
            matrix[column][row] -= value
    else:
        print("Invalid coordinates")
[print(" ".join([str(x) for x in row]))for row in matrix]