'''
ИЗГЪРМЯ ТЕСТ:5
Грешно:   if int(index) <= len(skill):
Правилно: if int(index) < len(skill):
'''

skill = input()

while True:
    command = input()
    if "For Azeroth" in command:
        break
    else:

        # _________________________________________________
        if "GladiatorStance" in command:
            skill = skill.upper()
            print(skill)

        # _________________________________________________
        elif "DefensiveStance" in command:
            skill = skill.lower()
            print(skill)

        # _________________________________________________
        elif "Dispel" in command:
            command = command.split()
            index = command[1]
            letter = command[2]

            if int(index) < len(skill):
                skill = skill.replace(skill[int(index)], letter, 1)
                print('Success!')
            else:
                print("Dispel too weak.")
                continue

        # _________________________________________________
        elif "Target Change" in command:
            command = command.split()
            old = command[2]
            new = command[3]

            skill = skill.replace(old, new)
            print(skill)

        # _________________________________________________
        elif "Target Remove" in command:
            command = command.split()
            letter_to_rm = command[2]

            skill = skill.replace(letter_to_rm, "")
            print(skill)

        # _________________________________________________
        else:
            print("Command doesn't exist!")
'''
     /\\\\\\\\\                            /\\\
    /\\////////\\\                         \/\\\
    /\\\       \/\\\                        \/\\\                   /\\\   /\\\
    \/\\\       \/\\\   /\\/\\\\\\           \/\\\    /\\/\\\\\\\   \///   \///
     \/\\\\\\\\\\\\\\\  \/\\\////\\\     /\\\\\\\\\   \/\\\/////\\\   /\\\   /\\\
      \/\\\/////////\\\  \/\\\  \//\\\   /\\\////\\\   \/\\\   \///   \/\\\  \/\\\
       \/\\\       \/\\\  \/\\\   \/\\\  \/\\\  \/\\\   \/\\\          \/\\\  \/\\\
        \/\\\       \/\\\  \/\\\   \/\\\  \//\\\\\\\/\\  \/\\\          \/\\\  \/\\\
         \///        \///   \///    \///    \///////\//   \///           \///   \///
            /\\\\\\\\\\\\\
            \/\\\/////////\\\                                 /\\\
             \/\\\       \/\\\                                \/\\\
              \/\\\\\\\\\\\\\\    /\\\    /\\\   /\\/\\\\\\\   \/\\\\\\\\      /\\\\\\\\\
               \/\\\/////////\\\  \/\\\   \/\\\  \/\\\/////\\\  \/\\\////\\\   \////////\\\
                \/\\\       \/\\\  \/\\\   \/\\\  \/\\\   \///   \/\\\\\\\\/      /\\\\\\\\\\
                 \/\\\       \/\\\  \/\\\   \/\\\  \/\\\          \/\\\///\\\     /\\\/////\\\
                  \/\\\\\\\\\\\\\/   \//\\\\\\\\\   \/\\\          \/\\\_\///\\\  \//\\\\\\\\/\\
                   \/////////////     \/////////     \///           \///    \///    \////////\//
'''