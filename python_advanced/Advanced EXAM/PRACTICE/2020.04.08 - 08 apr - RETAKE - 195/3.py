def find_strongest_eggs(*args):
    nums, step = args
    sub_lists = [nums[start::step] for start in range(step)]
    powerful_eggs = []
    for li in sub_lists:
        mid_ind = len(li) // 2
        prev_num, mid_num, nxt_num = li[mid_ind - 1], li[mid_ind], li[mid_ind + 1]

        while True:
            if len(set(li)) < len(li):
                break
            elif prev_num < nxt_num < mid_num:
                powerful_eggs.append(mid_num)
                break
            else:
                mid_ind += 1

    return powerful_eggs


test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))