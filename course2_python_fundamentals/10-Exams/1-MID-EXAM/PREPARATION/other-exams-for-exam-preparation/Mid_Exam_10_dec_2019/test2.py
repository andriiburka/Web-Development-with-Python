'''
Line 1----------------------------------------------------------------------------
        20|30|40|50|60

        targets_list = list(map(int, input().split("|")))


Line 2----------------------------------------------------
        Shoot Left@0@12  ==> ['Shoot Left', '0', '12']

        0 - 12 = -12

        while -12 < 0:
            -12 += len(target_list)

        -12 + 5 = -7

        while -12 < 0:
            -12 += len(target_list)

        -7 + 5 = -2

        while -12 < 0:
            -12 += len(target_list)

        -2 + 5 = 3




        ['20', '30', '40', '50', '60']
        start
          5     4      3     2     1
          10    9      8     7     6
                            12    11
                             |
                       index 3







Line 3----------------------------------------------------
        Shoot Right@4@5


Line 4----------------------------------------------------
        Shoot Right@6@5


Line 5----------------------------------------------------
        Reverse


Line 6----------------------------------------------------
        Game over


'''
targets_list = list(map(int, input().split("|")))
points = 0

while True:
    operations = input()
    if "Game over" in operations:
        print(" - ".join(str(targets_list).split(', '))[1:-1])
        print(f'Iskren finished the archery tournament with {points} points!')
        break

    elif "Reverse" in operations:
        targets_list = targets_list[::-1]
        continue
    else:

        # separating
        operations = operations.split("@")
        # bools
        start_index = int(operations[1])
        traverse_len = int(operations[2])
        command_is_shoot = 'Shoot' in operations[0].split()[0]
        direction_is_left = 'Left' in operations[0].split()[1]
        direction_is_right = 'Right' in operations[0].split()[1]

        # conditions
        if 0 <= start_index > len(targets_list):
            continue
        else:
            index = 0

            if command_is_shoot and direction_is_left:
                index = start_index - traverse_len
                if index < start_index:
                    while index < 0:
                        index += len(targets_list)

            elif command_is_shoot and direction_is_right:
                index = start_index + traverse_len
                if index >= len(targets_list):
                    while index > len(targets_list):
                        index -= len(targets_list)

            if targets_list[index] < 5:
                points += targets_list[index]
                targets_list[index] = 0
            else:
                targets_list[index] -= 5
                points += 5
