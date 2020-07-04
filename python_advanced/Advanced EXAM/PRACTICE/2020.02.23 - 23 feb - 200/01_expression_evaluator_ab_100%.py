from collections import deque
from operator import add, sub, mul, truediv
from math import floor

expression = deque(input().split())
math_ops = {"+": add, "-": sub, "*": mul, "/": truediv}
tmp, output = deque([]), []

while expression:
    x = expression.popleft()
    if x not in math_ops:
        tmp.append(int(x))
        continue

    result = 0
    if len(tmp) == 3:
        num1, num2, num3 = tmp.popleft(), tmp.popleft(), tmp.popleft()
        result = math_ops[x](math_ops[x](num1, num2), num3)
        output.append("{} {} {} {} {} {} {}".format(num1, x, num2, x, num3, '=', floor(result)))
    elif len(tmp) == 2:
        num1, num2 = tmp.popleft(), tmp.popleft()

        result = math_ops[x](num1, num2)

        output.append("{} {} {} {} {}".format(num1, x, num2, '=', floor(result)))
    tmp.append(floor(result))

print(output[-1].split()[-1])

''' 100/100
Moe решение
'''