from collections import deque

effects = deque((map(int, input().split(', '))))
casing = list(map(int, input().split(', ')))
pricing_dict = {40: 'Datura Bombs', 60: 'Cherry Bombs', 120: 'Smoke Decoy Bombs'}
pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}

while effects and casing:
    if pouch['Datura Bombs'] >= 3 and pouch['Cherry Bombs'] >= 3 and pouch['Smoke Decoy Bombs'] >= 3:
        break
    if effects[0] + casing[-1] in pricing_dict:
        bomb_name = pricing_dict[effects.popleft() + casing.pop()]
        pouch[bomb_name] += 1
    else:
        casing[-1] -= 5

if pouch['Datura Bombs'] >= 3 and pouch['Cherry Bombs'] >= 3 and pouch['Smoke Decoy Bombs'] >= 3:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

bomb_effects = "".join(str([i for i in effects])[1:-1])
bomb_casings = "".join(str([i for i in casing])[1:-1])
print(f"Bomb Effects: {bomb_effects if effects else 'empty'}")
print(f"Bomb Casings: {bomb_casings if casing else 'empty'}")

for k, v in sorted(pouch.items()):
    print(f"{k}: {v}")