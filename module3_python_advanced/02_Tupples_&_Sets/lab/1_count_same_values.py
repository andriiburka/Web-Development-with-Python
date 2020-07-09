def foo(values):
    nums_counter_d = {}

    for num in values:
        if num not in nums_counter_d:
            nums_counter_d[num] = 0
        nums_counter_d[num] += 1
    for k, v in nums_counter_d.items():
        print(f"{k} - {v} times")


user_input = input().split()
num_list = [float(num) for num in user_input]
foo(num_list)
