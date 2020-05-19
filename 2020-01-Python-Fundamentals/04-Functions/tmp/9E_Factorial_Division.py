import math


def factorial(n1, n2):
    factorial_n1 = math.factorial(n1)
    factorial_n2 = math.factorial(n2)
    result = factorial_n1 / factorial_n2
    return f'{result:.2f}'


num1 = int(input())
num2 = int(input())

print(factorial(num1, num2))
