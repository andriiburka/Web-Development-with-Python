s = ''''''

for _ in range(int(input())):
    s += f" {input()}"

[print(x) for x in set(s.split())]