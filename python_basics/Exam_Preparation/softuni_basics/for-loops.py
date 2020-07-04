# 01_even_lines. nomera ot 1 do 100 ==============================================================================================

# for n in range(1, 100 + 1):
#     print(n)


# 02. Всички латински букви ===========================================================================================
# # ASCII inputs
# start = 97
# end = 123
#
# # ЗА променливата в диапазн от 97 до 123-1 (z = 122)
# for letter in range(start, end):
#     # chr превръща ASCII число в буква
#     print(chr(letter))


# 03. Character Sequence # ============================================================================================

# word = input()
# for index, letter in enumerate(word):
#     print(letter)

# 04. Vowels Sum # ====================================================================================================

# word = input()
# a = 1
# e = 2
# i = 3
# o = 4
# u = 5
# sum = 0
#
# for index, letter in enumerate(word):
#     if letter == 'a':
#         sum += 1
#     elif letter == 'e':
#         sum += 2
#     elif letter == 'i':
#         sum += 3
#     elif letter == 'o':
#         sum += 4
#     elif letter == 'u':
#         sum += 5
#     else:
#         sum += 0
# print(sum)


# 05. Sum numbers # ====================================================================================================
# n = int(input())
# sum = 0
#
# for a in range(n):
#     number = int(input())
#     sum += number
#
# print(sum)



# 06. Number sequence # ====================================================================================================
# import sys
# n = int(input())
# num_max = -sys.maxsize
# num_min = sys.maxsize
#
# for _ in range(n):
#     num = int(input())
#     if num > num_max:
#         num_max = num
#     if num < num_min:
#         num_min = num
#
# print(f'Max number: {num_max}')
# print(f'Min number: {num_min}')


# 07. Number sequence # =============================================================================================






# 8. Четна / нечетна сума ============================================================================================

# чете n-на брой цели числа, подадени от потребителя, и
# проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
#
# При равенство да се отпечатат два реда:
# "Yes"
# "Sum = {сумата}"
# В противен случай да се отпечата:
# "No"
# "Diff = {разликата}"
# Разликата да се изчисли по абсолютна стойност.

n = int(input())

even = 0
odd = 0

for position in range(1, n + 1):
    num = int(input())
    if position % 2 == 0:
        even += num
    else:
        odd += num

if even == odd:
    print('Yes')
    print(f'Sum = {odd}')
else:
    diff = abs(even - odd)
    print('No')
    print(f'Diff = {diff}')