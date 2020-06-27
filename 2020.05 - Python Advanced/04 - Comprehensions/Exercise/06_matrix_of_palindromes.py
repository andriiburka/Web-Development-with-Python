rows, cols = [int(x) for x in input().split()]
alphabet = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
matrix = [[f"{alphabet[row]}{alphabet[col + row]}{alphabet[row]}" for col in range(cols)] for row in range(rows)]
[print(' '.join(row)) for row in matrix]