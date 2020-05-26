def count_racks(quantities, capacity, racks=1, temp=0):
    while quantities:
        if temp + quantities[-1] <= capacity:
            temp += quantities.pop()
        else:
            racks += 1
            temp = 0
    print(racks)


if __name__ == '__main__':
    count_racks(
        quantities=[int(x) for x in input().split()][::-1],
        capacity=int(input())
    )


# # mirokrastev version
# def count_racks(popped):
#     stack[-1].append(popped)
#     if sum(stack[-1]) > capacity:
#         stack[-1].pop()
#         stack.append([popped])
#
#
# quantities = [int(i) for i in input().split()]
# capacity = int(input())
# stack = [[]]
#
# while quantities:
#     count_racks(quantities.pop())
#
# print(len(stack))



# quantities = [int(x) for x in input().split()][::-1]
# capacity = int(input())
# racks = 1
# temp = 0
#
# while quantities:
#     if temp + quantities[-1] <= capacity:
#         temp += quantities.pop()
#     else:
#         racks += 1
#         temp = 0
#
# print(racks)
