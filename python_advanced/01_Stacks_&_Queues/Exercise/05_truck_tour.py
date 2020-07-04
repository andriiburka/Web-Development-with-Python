from collections import deque

stations = [list(map(int, input().split())) for i in range(int(input()))]

for i in range(len(stations)):
    sliced_rotate = deque(stations[i:] + stations[:i])

    fuel = 0
    while sliced_rotate:
        petrol, distance = sliced_rotate.popleft()
        fuel += petrol
        fuel -= distance
        if fuel < 0:
            break

    if fuel >= 0:
        print(i)
        exit()