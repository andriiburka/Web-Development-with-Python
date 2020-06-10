from collections import deque

materials = [i for i in input().split()]
magic_values = deque(i for i in input().split())
magic_levels = {'Doll': 150,
                'Wooden train': 250,
                'Teddy bear': 300,
                'Bicycle': 400}
crafted_toys = []

for i in range(len(materials) - 1, -1, -1):
    material, magic = materials[i], magic_values[-i - 1]
    if int(material) == 0:
        materials.remove(material)
        i += -1
    elif int(magic) == 0:
        magic_values.remove(magic)
        i += -1
    elif int(material) == 0 and int(magic) == 0:
        materials.remove(material)
        magic_values.remove(magic)
        i += -1

    result = 0
    if int(material) * int(magic) < 0:  # is negative
        result = int(material) + int(magic)
    else:
        result = int(material) * int(magic)

    if result >= 400:
        crafted_toys.append('Bicycle')
        # remove both (material, magic)
    elif 300 < result < 399:
        crafted_toys.append('Teddy bear')
        # remove both (material, magic)
    elif 250 < result < 299:
        crafted_toys.append('Wooden train')
        # remove both (material, magic)
    elif result >= 150:
        crafted_toys.append('Doll')
        # remove both (material, magic)

print(crafted_toys)
