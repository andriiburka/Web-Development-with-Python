from _collections import deque
import math


inp_raw = input().split()

operator = ["*", "+", "-", "/"]
evaluate_list = deque()
result = 0
for el in inp_raw:
    result = 0
    if el not in operator:
        current_digit = int(el)
        evaluate_list.append(current_digit)
    else:
        if el == "*":
            result = 1
            while evaluate_list:
                result *= evaluate_list.popleft()

            evaluate_list.appendleft(result)
        elif el == "/":
            result = 1
            for k in range(len(evaluate_list)):
                if k == 0:
                    result *= evaluate_list.popleft()
                else:
                    result /= evaluate_list.popleft()
            evaluate_list.appendleft(math.floor(result))
        elif el == "+":
            while evaluate_list:
                result += evaluate_list.popleft()
            evaluate_list.appendleft(result)
        elif el == "-":
            for i in range(len(evaluate_list)):
                if i == 0:
                    result += evaluate_list.popleft()
                else:
                    result -= evaluate_list.popleft()

            evaluate_list.appendleft(result)

print(math.floor(result))
