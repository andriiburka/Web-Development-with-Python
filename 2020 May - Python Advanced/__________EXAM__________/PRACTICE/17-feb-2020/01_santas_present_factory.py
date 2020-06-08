from collections import deque
# NEDOVARSHENA !!!!!!!!!!!!!!!!

def get_toy(x):
    if x >= 150:
        return 'Doll'
    elif x >= 250:
        return 'Wooden train'
    elif x >= 300:
        return 'Teddy bear'
    elif x >= 400:
        return 'Bicycle'


materials = deque(i for i in input().split())
magic_level = deque(i for i in input().split())

print(len(materials), len(magic_level))
