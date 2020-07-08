# Version 2.0 -------------------------Version 2.0---------------------90/100 = Error 06: RuntimeError
def permute(nums):
    result_perms = [[]]
    for num in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [num] + perm[i:])
            result_perms = new_perms
    return reversed(result_perms)


digits_list = []
digit = 0
while len(digits_list) < 3:
    # for num in digits_list:
    #     if num == 0:
    #         break
    digit = int(input())
    digits_list.append(digit)


divider = sum(digits_list)
new_int_list = []
is_possible = False
length_list = len(new_int_list)

for x in permute(digits_list):
    x = str(x)[1:-1]
    a = int(''.join(x.split(', ')))
    new_int_list.append(a)

new_int_list.sort(reverse=True)
new_int_list = set(new_int_list)

for y in new_int_list:
    if y % divider == 0:
        result = f'{y / divider}:0f'
        is_possible = True
    else:
        result = y / divider

if is_possible:
    print('Digitivision successful!')
else:
    print('No digitivision possible.')


# # Version 1.0 --------------------------Version 1.0----------------------90/100 = Error 06: RuntimeError
# from itertools import chain, permutations
#
# n1 = input()
# n2 = input()
# n3 = input()
# str_nums = []
# str_nums.append(n1), str_nums.append(n2), str_nums.append(n3)
# divider = int(n1) + int(n2) + int(n3)
# is_successful = False
#
# filter = set(["".join(perm) for perm in chain.from_iterable(permutations(str_nums, len(str_nums)) for n in range(4))])
#
# for i in filter:
#     number = int(i)
#     if number % divider == 0:
#         is_successful = True
#
# if is_successful:
#     print("Digitivision successful!")
# else:
#     print("No digitivision possible.")
