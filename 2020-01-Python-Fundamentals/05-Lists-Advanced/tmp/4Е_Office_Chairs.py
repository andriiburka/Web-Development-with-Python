rooms = int(input())
rooms_with_enough_chairs = 0
left = 0

for current_room in range(1, rooms + 1):
    needed = 0
    free_chairs_and_occupied = input().split(' ')

    chairs = len(free_chairs_and_occupied[0])
    people = int(free_chairs_and_occupied[1])

    if chairs >= people:
        rooms_with_enough_chairs += 1
    if chairs > people:
        left += abs(chairs - people)
    elif chairs < people:
        needed += abs(chairs - people)
        print(f'{needed} more chairs needed in room {current_room}')

    if rooms_with_enough_chairs == rooms:
        print(f'Game On, {left} free chairs left')



