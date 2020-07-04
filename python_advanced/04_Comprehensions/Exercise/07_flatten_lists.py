user_input = reversed(input().split("|"))
matrix = [li.split() for li in user_input]
print(" ".join(num for li in matrix for num in li))

# input = '1 2 3 |4 5 6 |  7  8'
# <list_reverseiterator object at 0x10dde3100>
# [['7', '8'], ['4', '5', '6'], ['1', '2', '3']]
# 7 8 4 5 6 1 2 3