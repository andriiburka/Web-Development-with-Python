stack = list(map(int, '5 4 8 6 3 8 7 7 9'.split()))
racks = []
capacity = 16
sum_clothes = 0

while sum_clothes < capacity:
    sum_clothes += stack.pop()

    if sum_clothes == capacity:
        racks.append(sum_clothes)

    elif sum_clothes > capacity:
        sum_clothes -= capacity
        racks.append(capacity)
        