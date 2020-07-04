# Вариант 1
# string = list(map(int, input().split('.')))
#
# string[2] += 1
#
# if string[2] > 9:
#     string[2] = 0
#     string[1] += 1
#
# if string[1] > 9:
#     string[1] = 0
#     string[0] += 1
#
# # print(f'{string[0]}.{string[1]}.{string[2]}')
# print('.'.join(map(str, string)))


# Вариант 2
# old_version = list(map(str, input().split('.')))
# new_version = ''.join(old_version)
# new_version = int(new_version)
# new_version += 1
# new_version = str(new_version)
# print('.'.join(map(str, new_version)))


# Вариант 3
def new_ver(old):
    old += 1
    new_version = str(old)
    return '.'.join(map(str, new_version))


string_to_int = int(''.join(list(map(str, input().split('.')))))
old_version = string_to_int

print(new_ver(old_version))
