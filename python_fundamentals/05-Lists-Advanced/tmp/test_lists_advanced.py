indices = list(map(int, input().split()))

cards = [1, 5, 4, 3, 2]

temp = []

for i in range(len(1, indices)):
    temp.clear()

    half_1 = cards[:indices[i]]
    half_2 = cards[-(len(cards) - len(half_1)):]

    if len(half_1) < len(half_2):
        dif = abs(len(half_2) - len(half_1))

    shuffled = [i for tup in zip(half_1, half_2) for i in tup]
    temp.append(shuffled)

    if len(shuffled) < len(cards):
        if len(half_1) > len(half_2):
            temp.append(half_1[-(abs(len(shuffled) - len(cards)))])
        else:
            temp.append(half_2[-(abs(len(shuffled) - len(cards)))])

    cards.clear()

    for i in temp:
        if type(i) == list:
            for num in i:
                cards.append(int(num))
        else:
            cards.append(i)

    print(cards)
