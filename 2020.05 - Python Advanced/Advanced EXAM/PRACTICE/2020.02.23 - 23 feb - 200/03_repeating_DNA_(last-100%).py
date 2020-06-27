# def get_repeating_DNA(raw_dna):
#     from collections import deque
#     raw_dna = deque(raw_dna)
#     repeated_dna = dict()
#
#     while raw_dna:
#         try:
#             new_str_len_10 = "".join([raw_dna.popleft() for _ in range(10)])
#         except IndexError:
#             continue
#
#         if new_str_len_10 in repeated_dna:
#             repeated_dna[new_str_len_10] += 1
#         else:
#             repeated_dna[new_str_len_10] = 1
#
#     if repeated_dna:
#         if len(repeated_dna) > 1:
#             return [k for k, v in repeated_dna.items() if v > 1]
#         else:
#             return [i for i in repeated_dna.keys()]
#     else:
#         return []


# def get_repeating_DNA(raw_dna):
#     repeated = dict()
#     start = 0
#     while start < len(raw_dna)-9:
#         current = raw_dna[start:start + 10]
#         if start + 10 <= len(raw_dna) and current in repeated:
#             repeated[current] += 1
#         elif start + 10 <= len(raw_dna):
#             repeated[current] = 1
#         start += 10
#     if len(repeated.keys()):
#         return [i for i in repeated.keys()]
#     return [key for key, value in repeated.items() if value > 1]


def get_repeating_DNA(string):
    repeated = []
    for i in range(len(string)-10):
        current = string[i:i+10]
        if current in string[i+1:] and current not in repeated:
            repeated.append(current)
    return repeated


test = "1111111111222222222233333333332222222222"
#test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
#test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
#test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)

