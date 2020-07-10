def perfect_num(func_num):
    li = []
    for for_num in range(1, func_num):
        if func_num % for_num == 0:
            li.append(for_num)
    return sum(li)


num = int(input())
if perfect_num(num) == num:
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')