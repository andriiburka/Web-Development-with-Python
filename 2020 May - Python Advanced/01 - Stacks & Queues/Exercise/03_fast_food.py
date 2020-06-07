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
    solve(
        total_food=total_quantity_of_food,
        orders=list_quantity_of_orders
    )
