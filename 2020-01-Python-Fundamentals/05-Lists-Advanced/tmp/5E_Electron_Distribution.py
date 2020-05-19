num = int(input())
list_electrons = []

for i in range(num):
    if sum(list_electrons) > num:
        break
    else:
        list_electrons.append(2 * ((i + 1) ** 2))

list_electrons.remove(list_electrons[-1])

if sum(list_electrons) < num:
    x = num - sum(list_electrons)
    list_electrons.append(x)

print(list_electrons)
