rows, _ = list(map(int, input().split(', ')))
matrix = [list(map(int, input().split(', '))) for _ in range(rows)]
summed = sum([sum(li) for li in matrix])
print(f"{summed}\n{matrix}")