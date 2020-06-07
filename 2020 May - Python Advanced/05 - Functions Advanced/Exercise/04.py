def even_odd(*args):
    return [i for i in args[:-1] if i % 2 == 0] if 'even' in args[-1] else [i for i in args[:-1] if i % 2 == 1]


# INPUTS
print(even_odd(1, 2, 3, 4, 5, 6, "even"))  # [2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))  # [1, 3, 5, 7, 9]
