y, x = list(map(int, input().split()))
matrix = list(list(map(str, input().split())) for i in range(y))
matches, square_corners = 0, 4
for row in range(y-1):
    for column in range(x-1):
        template = \
            [matrix[row][column],       # C top-left-corner
             matrix[row][column+1],     # D top-right-corner
             matrix[row+1][column],     # A bottom-left-corner
             matrix[row+1][column+1]]   # B bottom-right-corner
        first_letter = template[0]
        if list(first_letter * square_corners) == template:
            matches += 1
print(matches)