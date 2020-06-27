def list_manipulator(x, y, *args):
    from collections import deque
    li, operation = deque(x), y
    n = None
    if len(args) > 1:
        n = args[1:]

    if operation == 'add':
        if n is not None:
            [li.appendleft(i) for i in reversed(n)] if 'beginning' in args else [li.append(i) for i in n]
    elif operation == 'remove':
        if n is None:
            li.popleft() if 'beginning' in args else li.pop()
        elif n is not None:
            n = int(n[0])
            [li.popleft() for i in range(n)] if 'beginning' in args else [li.pop() for i in range(n)]

    return [i for i in li]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))