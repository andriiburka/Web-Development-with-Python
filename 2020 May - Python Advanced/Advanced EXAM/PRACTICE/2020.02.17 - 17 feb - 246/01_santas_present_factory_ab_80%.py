from collections import deque


def get_toy_by(magic_value):
    for toy_foo, magic_price in toy_pricing.items():
        if magic_value == magic_price:
            return toy_foo


materials = list((map(int, input().split())))
magic_values = deque(map(int, input().split()))
toy_pricing = {'Doll': 150,
               'Wooden train': 250,
               'Teddy bear': 300,
               'Bicycle': 400,
               }
crafted = {'Doll': 0,
           'Wooden train': 0,
           'Teddy bear': 0,
           'Bicycle': 0,
           }

while materials and magic_values:
    result, material, magic = (materials[-1] * magic_values[0]), materials[-1], magic_values[0]
    if not material:
        materials.pop()
        continue
    elif not magic:
        magic_values.popleft()
        continue
    elif not material and not magic:
        materials.pop()
        magic_values.popleft()
        continue
    if result in toy_pricing.values():
        toy = get_toy_by(magic_value=result)
        if toy:
            crafted[toy] += 1
            materials.pop()
            magic_values.popleft()
    else:
        if result < 0:
            materials.append(materials.pop() + magic_values.popleft())
        elif result > 0:
            n = materials.append(materials.pop() + 15)
            magic_values.popleft()
sorted_toys = {k: v for k, v in sorted(crafted.items(), key=lambda x: (x[0], x[1]), reverse=False) if v > 0}
success_bool = (crafted['Doll'] > 0 and crafted['Wooden train'] > 0) or \
          (crafted['Teddy bear'] > 0 and crafted['Bicycle'] > 0)


# OUTPUT
print("The presents are crafted! Merry Christmas!" if success_bool else "No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(list(str(i) for i in reversed(materials)))}")
if magic_values:
    print(f"Magic left: {', '.join(list(str(i) for i in reversed(magic_values)))}")

{print(f"{k}: {v}") for k, v in sorted_toys.items()}