# NOT FINALIZED
from collections import deque

expression = deque('10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *'.split())
evaluated = deque()
tmp = deque()

while expression:
    if expression[0].isdigit():
        tmp.append(expression.popleft())
    else:
        if expression[0] == "-":
            evaluated.append(tmp.popleft(), expression.popleft(), tmp.pop())
        elif expression[0] == "+":
            pass
        elif expression[0] == "/":
            pass
        elif expression[0] == "*":
            evaluated.append(tmp.popleft(), expression.popleft(), tmp.pop())