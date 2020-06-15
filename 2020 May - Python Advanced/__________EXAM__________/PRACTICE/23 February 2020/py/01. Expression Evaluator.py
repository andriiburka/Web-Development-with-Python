from collections import deque


def sub_operation(*nums):
    num1, num2 = nums
    return '{} - {} - {} = {}'.format(last, num1, num2, ((last - num1) - num2)) if last and len(nums) > 2\
        else '{} - {} = {}'.format(num1, num2, num1 - num2)


def add_operation(*nums):
    num1, num2 = nums
    return '{} + {} + {} = {}'.format(last, num1, num2, ((last + num1) + num2)) if last \
        else '{} + {} = {}'.format(num1, num2, num1 + num2)


def mul_operation(*nums):
    num1, num2 = nums
    return '{} * {} * {} = {}'.format(last, num1, num2, ((last * num1) * num2)) if last \
        else '{} * {} = {}'.format(num1, num2, num1 * num2)


def div_operation(*nums):
    if len(nums) == 2:
        num1, num2 = nums
        return '{} / {} = {}'.format(num1, num2, (num1 / num2))

    elif len(nums) == 3:
        num1, num2, num3 = nums
        return '{} / {} / {} = {}'.format(num1, num2, num3, ((num1 / num2) / num3))



expression = deque('10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *'.split())

evaluate = []
tmp = deque()
last = 0

while expression:
    if expression[0].isdigit():
        tmp.append(int(expression.popleft()))
    else:

        if '-' in expression[0]:
            expression.popleft()

            if len(tmp) > 1:
                evaluate.append(sub_operation(*tmp))
            else:
                if last:
                    evaluate.append(sub_operation(last, *tmp))

            last = int(evaluate[-1][-1])
            tmp.clear()

        elif '+' in expression[0]:
            expression.popleft()

            if len(tmp) > 1:
                evaluate.append(add_operation(*tmp))
            else:
                if last:
                    evaluate.append(add_operation(last, *tmp))

            last = int(evaluate[-1][-1])
            tmp.clear()

        elif '*' in expression[0]:
            expression.popleft()

            if len(tmp) > 1:
                evaluate.append(mul_operation(*tmp))
            else:
                if last:
                    evaluate.append(mul_operation(last, *tmp))

            last = int(evaluate[-1][-1])
            tmp.clear()

        elif '/' in expression[0]:
            expression.popleft()

            if len(tmp) > 1:
                evaluate.append(div_operation(*tmp))
            else:
                if last:
                    evaluate.append(div_operation(last, *tmp))

            last = int(evaluate[-1][-1])
            tmp.clear()

[print(i) for i in evaluate]
