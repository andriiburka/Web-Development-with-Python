# 1 - def THIS_IS_FUNCTION():
#
# def GRADE_COMMENT(grade):
#     if 2.00 <= grade <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade <= 4.49:
#         return 'Good'
#     elif 4.50 <= grade <= 5.49:
#         return 'Very Good'
#     elif 5.50 <= grade <= 6.00:
#         return 'Excellent'
#
#
# grade_in = float(input())
# if __name__ == "__main__":
#     print(GRADE_COMMENT(grade_in))


# 2. Calculations
# import math as m
#
#
# def CALCULATION(operator_type, number1, number2):
#     global x
#     if operator_type == 'add':
#         x = m.floor(number1 + number2)
#     elif operator_type == 'subtract':
#         x = m.floor(number1 - number2)
#     elif operator_type == 'divide':
#         x = m.floor(number1 / number2)
#     elif operator_type == 'multiply':
#         x = m.floor(number1 * number2)
#     return x
#
#
# operator_in = input()
# n1 = int(input())
# n2 = int(input())
#
# if __name__ == '__main__':
#     print(CALCULATION(operator_in, n1, n2))


# 3. Repeat String
# def func_sum(string_input, repeating_times):
#     return string_input * repeating_times
#
#
# if __name__ == '__main__':
#     string_in = input()
#     times_repeating = int(input())
# print(func_sum(string_in, times_repeating))


# 4. Orders
# def CALCULATION(item_kind, n_items):
#     global price
#     if item_kind == 'coffee':
#         price = 1.50 * n_items
#     elif item_kind == 'water':
#         price = 1.00 * n_items
#     elif item_kind == 'coke':
#         price = 1.40 * n_items
#     elif item_kind == 'snacks':
#         price = 2.00 * n_items
#     return price
#
#
# drink = input()
# n = int(input())
# if __name__ == '__main__':
#     print(f'{CALCULATION(drink, n):.2f}')


# 5. Calculate Rectangle Area
# def CALC_RECT_AREA(a, b):
#     return a * b
#
#
# in_a = int(input())
# in_b = int(input())
# if __name__ == '__main__':
#     print(CALC_RECT_AREA(in_a, in_b))
