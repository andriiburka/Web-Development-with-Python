
from collections import deque as d


def find_station(arg):
    li_cp = d(stations[arg:] + stations[:arg])
    tmp = 0
    while li_cp:
        amount, distance = li_cp.popleft()
        tmp += amount - distance
        if tmp < 0:
            break
    return tmp


num = int(input())
stations = [[int(i) for i in input().split()] for i in range(num)]

for x in range(len(stations)):
    if find_station(arg=x) >= 0:
        print(x)
        exit()