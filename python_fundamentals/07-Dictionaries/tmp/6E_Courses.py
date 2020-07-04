import collections as c

courses = c.defaultdict(list)
while True:
    command = input()
    if command == 'end':
        break
    command = command.split(' : ')
    courses[command[0]].append(command[1])

for course in sorted(courses, key=lambda x: len(courses[x]), reverse=True):
    print(f"{course}: {len(courses[course])}")
    for name in sorted(courses[course]):
        print(f"-- {name}")
