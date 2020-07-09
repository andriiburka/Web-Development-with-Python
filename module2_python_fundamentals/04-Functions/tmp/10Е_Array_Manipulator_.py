# def exchange(li, operator_value):
#     max_index = 0
#     for i in range(len(li)):
#         max_index = i
#
#     if operator_value > max_index:
#         print('Invalid index')
#     else:
#         for i in range(1, operator_value + 2):
#             temp = li.pop(0)
#             li.append(temp)
#         return li
#
#
# def max_odd(li):
#     max_odd_list = []
#     for i in li:
#         if int(i) % 2 != 0:
#             max_odd_list.append(i)
#     for i in range(len(max_odd_list)):
#         if max_odd_list[i] == max(max_odd_list):
#             return i
#
#
# def min_odd(li):
#     min_odd_list = []
#     for i in li:
#         if int(i) % 2 != 0:
#             min_odd_list.append(i)
#     for i in range(len(min_odd_list)):
#         if min_odd_list[i] == min(min_odd_list):
#             return i
#
#
# def max_even(li):
#     max_even_index = 0
#     for i in range(len(li)):
#         if li[i] % 2 == 0:
#             if i > max_even_index:
#                 max_even_index = i
#     return max_even_index
#
#
# def min_even(li):
#     min_even_list = []
#     for ch in li:
#         if int(ch) % 2 == 0:
#             min_even_list.append(ch)
#
#     if len(min_even_list) == 0:
#         return 'No matches'
#     else:
#         for i in range(len(min_even_list)):
#             if min(min_even_list) == min_even_list[i]:
#                 return i
#
#
# def first_n_odd(li, operator_value):
#     odds = []
#     for i in range(len(li)):
#         if not li[i] % 2 == 0:
#             odds.append(li[i])
#     if len(odds) < int(operation[1]):
#         return odds
#     else:
#         first_odds = []
#         for index in range(operator_value):
#             first_odds.append(odds[index])
#         return first_odds
#
#
# def first_n_even(li, operator_value):
#     evens = []
#     for i in range(len(li)):
#         if li[i] % 2 == 0:
#             evens.append(li[i])
#
#     if len(evens) < int(operation[1]):
#         return 'Invalid count'
#     else:
#         first_evens = []
#         for index in range(operator_value):
#             first_evens.append(evens[index])
#         return first_evens
#
#
# def last_n_odd(li, operator_value):
#     odds = []
#
#     for i in range(len(li)):
#         if not li[i] % 2 == 0:
#             odds.append(li[i])
#     if len(odds) < operator_value:
#         return odds
#
#
# def last_n_even(li, operator_value):
#     last_n_even_list = []
#     for i in li:
#         if int(i) % 2 == 0:
#             last_n_even_list.append(i)
#     if len(last_n_even_list) == 0:
#         return last_n_even_list
#
#
# if __name__ == '__main__':
#     list_in = list(map(int, input().split()))
#     operation = list(map(str, input().split()))
#
#     while True:
#         if 'end' in operation:
#             break
#
#         elif 'exchange' in operation:
#             exchange(list_in, int(operation[1]))
#
#         elif 'max' in operation[0]:
#             if 'odd' in operation[1]:
#                 print(max_odd(list_in))
#             elif 'even' in operation[1]:
#                 print(max_even(list_in))
#
#         elif 'min' in operation[0]:
#             if 'odd' in operation:
#                 print(min_odd(list_in))
#             elif 'even' in operation:
#                 print(min_even(list_in))
#
#         elif 'first' in operation[0] and len(operation) == 3:
#             if 'odd' in operation:
#                 print(first_n_odd(list_in, int(operation[1])))
#             elif 'even' in operation:
#                 print(first_n_even(list_in, int(operation[1])))
#
#         elif 'last' in operation and len(operation) == 3:
#             if 'odd' in operation:
#                 print(last_n_odd(list_in, int(operation[1])))
#             elif 'even' in operation:
#                 print(last_n_even(list_in, int(operation[1])))
#
#         operation = list(map(str, input().split()))
#     print(list_in)


def exchange(ind, lst):
    if ind > len(lst) - 1 or ind < 0:
        print('Invalid index')
        return lst
    else:
        new = lst[ind + 1:] + lst[:ind + 1]
        return new


def get_odds(lst):
    return [x for x in lst if x % 2 != 0]


def get_even(lst):
    return [x for x in lst if x % 2 == 0]


def get_index_of_number(lst, number):
    return [ind for ind, num in enumerate(lst) if num == number]


def duplicate_val(lst, number):
    seen = set()
    res = []
    for ind, num in enumerate(lst):
        if num == number and num not in seen:
            seen.add(num)
        else:
            if num == number:
                res.append(ind)
    return max(res)


def get_element(lst, max_min, check, all_numbers=None):
    if all_numbers is None:
        all_numbers = []
    checks = {'even': get_even(lst), 'odd': get_odds(lst),
              'max': lambda x: max(x) if x else 'No matches',
              'min': lambda x: min(x) if x else 'No matches'}
    function = checks.get(check)
    all_numbers = function
    number = checks[max_min](all_numbers)
    if isinstance(number, int):
        if lst.count(number) > 1:
            return duplicate_val(lst, number)
        return lst.index(number)
    else:
        return number


def first(lst_check, count, lst):
    if count > len(lst):
        return 'Invalid count'
    if not lst_check:
        return lst_check
    return lst_check[:count]


def last(lst_check, count, lst):
    if count > len(lst):
        return 'Invalid count'
    if not lst_check:
        return lst_check
    return lst_check[-count:]


def first_last(lst, check, even_odd, count, lst_check=None):
    funcs_for_lists = {'odd': lambda x: get_odds(x), 'even': lambda x: get_even(x)}
    lst_check = funcs_for_lists[even_odd](lst)
    checks = {'first': first(lst_check, count, lst), 'last': last(lst_check, count, lst)}
    result = checks[check]
    return result


# Start
numbers = [int(x) for x in input().split()]
commands = input()
while commands != 'end':
    lst_commands = commands.split()
    if lst_commands[0] == 'exchange':
        index = int(lst_commands[1])
        numbers = exchange(index, numbers)
    elif lst_commands[0] == 'max' or lst_commands[0] == 'min':
        maxi_mini = lst_commands[0]
        odd_even = lst_commands[1]
        print(get_element(numbers, maxi_mini, odd_even))
    elif lst_commands[0] == 'first' or lst_commands[0] == 'last':
        chk = lst_commands[0]
        counter = int(lst_commands[1])
        odd_even = lst_commands[2]
        print(first_last(numbers, chk, odd_even, counter))
    commands = input()
print(numbers)
