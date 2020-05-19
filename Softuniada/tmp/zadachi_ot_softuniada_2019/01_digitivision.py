from itertools import chain, permutations

no_remainder = False
str_list = []
max_list = 3
divider = 0

while len(str_list) < max_list:
    input_num = input()
    str_list.append(input_num)
    divider += int(input_num)

loops = ["".join(perm) for perm in chain.from_iterable(permutations(str_list, len(str_list)) for n in range(4))]
loops = set(loops)

for i in loops:
    number = int(i)
    if number % divider == 0:
        no_remainder = True

if no_remainder:
    print('Digitivision successful!')
else:
    print('No digitivision possible.')