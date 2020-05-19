import math as m


def foo(n):  # str
    loading_bar = [int(m.floor(int(n) / 10)) * '%', int(m.floor((100 - int(n)) / 10)) * '.']
    if n == '100':
        print(f'{n}% Complete!\n[{loading_bar[0]}{loading_bar[1]}]')
    else:
        print(f'{n}% [{loading_bar[0]}{loading_bar[1]}]\nStill loading...')


num = input()
if int(num) <= 100:
    foo(num)
