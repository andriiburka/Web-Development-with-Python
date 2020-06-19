def find_strongest_eggs(*tst):
    from math import ceil
    sequence, n_sub_lists = tst
    start = len(sequence) >= 3
    matrix = [sequence[i::2] for i in range(n_sub_lists)] if n_sub_lists > 1 else [sequence]

    res = []
    if start:
        for li in matrix:
            middle = ceil(len(li) / 2) - 1
            is_nums_after_middle_are_more_than_one = len(li[middle + 1:1:-1]) > 1

            if is_nums_after_middle_are_more_than_one:
                for i in range(middle, len(li)):
                    if str(li[i]).isdigit():
                        if i + 1 == len(li):  # проверка за последно число
                            continue
                        else:
                            prv, mid, nxt = li[i - 1], li[i], li[i + 1]
                            is_middle_bigger = prv < nxt < mid
                            is_right_bigger_than_left = nxt > prv

                            if is_middle_bigger and is_right_bigger_than_left:
                                res.append(mid)
                                str(mid).replace(str(mid), '')
                    else:
                        continue

            else:
                prv, mid, nxt = li[middle - 1], li[middle], li[middle + 1]
                is_middle_bigger = prv < nxt < mid
                is_right_bigger_than_left = nxt > prv

                # if mid == nxt or mid == prv:
                #     continue

                if is_middle_bigger and is_right_bigger_than_left:
                    res.append(li[middle])
    return res


# test = ([-1, 7, 3, 15, 2, 12], 2)
# print(find_strongest_eggs(*test))
#
# test = ([-1, 0, 2, 5, 2, 3], 2)
# print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))

# test = ([2, 3, 4, 16, 3, 15], 2)
# print(find_strongest_eggs(*test))
#
# test = ([2, 15, 3], 1)
# print(find_strongest_eggs(*test))
