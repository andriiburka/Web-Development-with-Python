from _collections import deque

my_dict = {}
toy = None
materials = list(map(int, input().split()))
magic_values = deque(list(map(int, input().split())))

while magic_values and materials:
    current_material = materials.pop()
    if current_material == 0:
        if magic_values[0]==0:
            magic_values.popleft()
        continue
    current_magic_value = magic_values.popleft()
    if current_magic_value == 0:

        continue

    magic_level = current_material * current_magic_value

    if magic_level > 0:
        if magic_level == 150:
            toy = "Doll"
            if toy not in my_dict:
                my_dict[toy] = 0
            my_dict[toy] += 1

        elif magic_level == 250:
            toy = "Wooden train"
            if toy not in my_dict:
                my_dict[toy] = 0
            my_dict[toy] += 1

        elif magic_level == 300:
            toy = "Teddy bear"
            if toy not in my_dict:
                my_dict[toy] = 0
            my_dict[toy] += 1


        elif magic_level == 400:
            toy = "Bicycle"
            if toy not in my_dict:
                my_dict[toy] = 0
            my_dict[toy] += 1

        else:
            materials[-1] += 15






    elif magic_level < 0:
        nw_material = current_magic_value + current_material

        materials.append(nw_material)

if ("Teddy bear" and "Bicycle" in my_dict) or ("Doll" and "Wooden train" in my_dict):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if len(materials) > 0:
    print(f"Materials left: " + ', '.join([str(x) for x in materials[::-1]]))
if len(magic_values):
    print(f"Magic left: " + ', '.join([str(x) for x in magic_values]))
for toy, count in sorted(my_dict.items(), key=lambda x: x):
    if count >0:
     print(f"{toy}: {count}")
