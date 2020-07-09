from collections import deque


def biggest_order(li):
    return max(list(map(int, li)))


def solve(total_food, orders):
    print(biggest_order(li=orders))
    while orders:
        if total_food >= int(orders[0]):
            total_food -= int(orders.popleft())
        else:
            print(f'Orders left: {" ".join(orders)}')
            break
    else:
        print('Orders complete')


if __name__ == '__main__':
    total_quantity_of_food = int(input())
    list_quantity_of_orders = deque(input().split())
    solve(total_food=total_quantity_of_food, orders=list_quantity_of_orders)






# W/O Fn____________________________________________________________________
from collections import deque

food = int(input())
orders = deque(input().split())
print(max(list(map(int, orders))))
while orders:
    if food >= int(orders[0]):
        food -= int(orders.popleft())
    else:
        print(f'Orders left: {" ".join(orders)}')
        break
else:
    print('Orders complete')
