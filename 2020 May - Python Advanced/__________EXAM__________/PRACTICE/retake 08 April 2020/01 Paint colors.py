# Самостоятелно решение
# 80/100

from collections import deque

li = deque(input().split())
colors = ['red', 'yellow', 'blue']
complex_colors = ['orange', 'purple', 'green']
output = []

while li:
    prefix, suffix = li[0], li[-1]

    if (prefix in colors) or (prefix + suffix in colors) or (suffix + prefix in colors):
        if prefix == suffix and (prefix in colors):
            output.append(li.pop())
        elif (prefix and suffix) and (prefix + suffix in colors):
            output.append(li.popleft() + li.pop())
        elif (suffix and prefix) and (suffix + prefix) in colors:
            output.append(li.pop() + li.popleft())

    elif (prefix in complex_colors) or (prefix + suffix in complex_colors) or (suffix + prefix in complex_colors):
        if prefix and not (prefix and suffix) and (prefix in complex_colors):
            output.append(li.pop())
        elif (prefix and suffix) and (prefix + suffix in complex_colors):
            output.append(li.popleft() + li.pop())
        elif (suffix and prefix) and (suffix + prefix) in complex_colors:
            output.append(li.pop() + li.popleft())
    else:
        if len(li) == 1:
            li.pop()
        else:
            middle_index = len(li) // 2 - 1
            pop_left, pop_right = li.popleft()[:-1], li.pop()[:-1]
            if pop_left != '':
                li.insert(middle_index, pop_left)
            if pop_right != '':
                li.insert(middle_index, pop_right)

if 'orange' in output and not ('red' and 'yellow') in output:
    output.remove('orange')
if 'purple' in output and not ('red' and 'blue') in output:
    output.remove('purple')
if 'green' in output and not ('yellow' and 'blue') in output:
    output.remove('green')

print(output)