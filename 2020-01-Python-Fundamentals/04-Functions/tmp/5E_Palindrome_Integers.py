def foo_palindromic_check(str_in):
    for number in str_in:
        is_palindromic = [number[i - 1] for i in range(1, int(len(number) / 2) + 1)] ==\
                     [number[-i2] for i2 in range(1, int(len(number) / 2) + 1)]
        print(is_palindromic)


string_in = input().split(', ')
foo_palindromic_check(string_in)

# Example:
# 123, 323, 421, 121, 32, 2, 232, 1010
# False, True, False, True, False, True, True, False
