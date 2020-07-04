cmd = input().split()
n = {int(input()) for _ in range(int(cmd[0]))}
m = {int(input()) for _ in range(int(cmd[1]))}
[print(x) for x in n.intersection(m)]