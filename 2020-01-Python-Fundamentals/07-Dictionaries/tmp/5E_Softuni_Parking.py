visitors = {}
regs = int(input())

for i in range(regs):
    entry = input().split()
    command = entry[0]
    person = entry[1]
    if command == 'register':
        if person in visitors:
            print(f"ERROR: already registered with plate number {visitors[person]}")
        else:
            visitors[person] = entry[2]
            print(f"{person} registered {visitors[person]} successfully")
    if command == 'unregister':
        if person in visitors:
            print(f"{person} unregistered successfully")
            del visitors[person]
        else:
            print(f"ERROR: user {person} not found")

for visitor in visitors:
    print(f"{visitor} => {visitors[visitor]}")