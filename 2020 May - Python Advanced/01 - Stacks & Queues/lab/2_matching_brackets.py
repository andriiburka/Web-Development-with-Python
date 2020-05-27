# # READABLE
# def f_matching_brackets(expression):
#     stack = []
#     for current_index in range(len(expression)):
#         if expression[current_index] == '(':
#             stack.append(current_index)
#         elif expression[current_index] == ')':
#             start = stack.pop()
#             end = current_index + 1
#             print(expression[start:end])
#
#
# if __name__ == '__main__':
#     f_matching_brackets(expression=input())


# COMPREHENSION
expression = input()
stack = []
[stack.append(i) if expression[i] == '(' else print(expression[stack.pop():i + 1]) if expression[i] == ')'
 else 'ако махна този else, гърми защото очаква else... така или иначе тази проверка няма да се изпълне...'
 for i in range(len(expression))]
