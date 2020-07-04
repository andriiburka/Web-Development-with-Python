with open('text.txt', 'r') as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            print(i+1, line)
