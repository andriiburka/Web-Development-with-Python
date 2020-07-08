mount_of_cards = int(input())
indices = list(map(int, input().split()))

cards = []
for num in range(1, mount_of_cards + 1):
    cards.append(num)
print(cards)
temp = []

for i in range(len(indices)):
    if indices[i] == 0 or indices[i] == 1:
        continue
    else:
        temp.clear()

        half_1 = cards[:indices[i]]
        half_2 = cards[-(mount_of_cards - len(half_1)):]

        shuffled = [i for tup in zip(half_1, half_2) for i in tup]
        temp.append(shuffled)

        if len(shuffled) != len(cards):
            diff = abs(len(shuffled) - len(cards))
            for abc in range(1, diff + 1):
                if len(half_1) > len(half_2):
                    print(-abc)
                    temp.append(half_1[-abc])
                else:
                    print(-abc)
                    temp.append(half_2[-(abs(len(shuffled) - len(cards)))])

        cards.clear()

        for i in temp:
            if type(i) == list:
                for num in i:
                    cards.append(int(num))
            else:
                cards.append(i)
cards = ''.join(str(cards).split(","))[1:-1]
print(cards)

