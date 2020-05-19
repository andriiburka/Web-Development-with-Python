def sum_numbers(n1, n2, n3):
    return n1 + n2 - n3


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(sum_numbers(num1, num2, num3))



# # 2. Add and Subtract
#
# # local variables inside
# def sum_numbers(num1, num2):
#     return num1 + num2
#
# # local variables inside
# def subtract(result_sum, num3):
#     return result_sum - num3
#
# # final function
# def foo(f_num_1, f_num_2, f_num_3):
#     res = sum_numbers(f_num_1, f_num_2)
#     subtracted = res - f_num_3
#     return subtracted
#
# # start program
# if __name__ == '__main__':
#     number_1 = int(input())
#     number_2 = int(input())
#     number_3 = int(input())
#     print(foo(number_1, number_2, number_3))