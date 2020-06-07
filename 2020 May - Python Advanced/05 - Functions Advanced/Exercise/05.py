def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


# LAST PIECE OF PUZZLE
def func_executor(*args):
    return [foo(*nums) for foo, nums in args]


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))