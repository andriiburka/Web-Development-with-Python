from itertools import permutations


def possible_permutations(my_list):
    for permutation in permutations(my_list):
        yield list(permutation)
