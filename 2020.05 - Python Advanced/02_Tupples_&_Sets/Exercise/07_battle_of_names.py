odd, even = set(), set()

for divider in range(1, int(input()) + 1):
    name_sum = sum([ord(letter) for letter in input()]) // divider
    even.add(name_sum) if name_sum % 2 == 0 else odd.add(name_sum)

if sum(odd) == sum(even):
    print(', '.join([str(x) for x in odd.union(even)]))
elif sum(odd) > sum(even):
    print(', '.join([str(x) for x in odd.difference(even)]))
elif sum(odd) < sum(even):
    print(', '.join([str(x) for x in odd.symmetric_difference(even)]))