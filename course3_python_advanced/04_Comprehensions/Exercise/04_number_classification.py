class Check:
    def __init__(self, number):
        self.number = number

    def if_positive(self):
        return self.number >= 0

    def if_negative(self):
        return self.number < 0

    def if_even(self):
        return self.number % 2 == 0

    def if_odd(self):
        return self.number % 2 == 1


check = Check
nums = list(map(int, input().split(', ')))
positive, negative, even, odd = \
    [num for num in nums if check.if_positive(Check(num))], \
    [num for num in nums if check.if_negative(Check(num))], \
    [num for num in nums if check.if_even(Check(num))], \
    [num for num in nums if check.if_odd(Check(num))]

print(f'Positive: {str(positive)[1:-1]}\n'
      f'Negative: {str(negative)[1:-1]}\n'
      f'Even: {str(even)[1:-1]}\n'
      f'Odd: {str(odd)[1:-1]}')


# nums = list(map(int, input().split(', ')))
# positive, negative, even, odd = \
#     [num for num in nums if num >= 0], \
#     [num for num in nums if num < 0], \
#     [num for num in nums if num % 2 == 0], \
#     [num for num in nums if num % 2 == 1]
#
# print(f'Positive: {str(positive)[1:-1]}\n'
#       f'Negative: {str(negative)[1:-1]}\n'
#       f'Even: {str(even)[1:-1]}\n'
#       f'Odd: {str(odd)[1:-1]}')
