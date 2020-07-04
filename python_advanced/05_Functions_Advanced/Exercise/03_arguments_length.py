def args_length(*args):
    return len([i for i in args])


# INPUTS
print(args_length(1, 32, 5))            # 3
print(args_length("john", "peter"))     # 2
print(args_length([1, 2, 3]))           # 1

