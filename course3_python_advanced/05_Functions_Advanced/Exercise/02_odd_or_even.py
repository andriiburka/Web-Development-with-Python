def odds(li_input):
    return sum([i for i in li_input if i % 2 == 1]) * len(li_input)


def evens(li_input):
    return sum([i for i in li_input if i % 2 == 0]) * len(li_input)


if __name__ == '__main__':
    cmd = input()
    li = [int(num) for num in input().split()]
    print(odds(li_input=li) if cmd.startswith('Odd') else evens(li_input=li))