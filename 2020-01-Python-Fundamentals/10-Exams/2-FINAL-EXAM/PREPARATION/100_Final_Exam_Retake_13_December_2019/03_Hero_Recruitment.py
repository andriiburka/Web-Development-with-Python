'''
100/100
https://judge.softuni.bg/Contests/Practice/DownloadResource/7392
'''

heroes_dict = {}

while True:
    command = input().split()
    if "End" in command:
        break
    #______________________________________________________________________
    elif "Enroll" in command:
        if command[1] in heroes_dict:
            print(f"{command[1]} is already enrolled.")
        else:
            heroes_dict[command[1]] = []
    #______________________________________________________________________
    elif "Learn" in command:
        if command[1] in heroes_dict:
            if command[2] not in heroes_dict[command[1]]:
                heroes_dict[command[1]].append(command[2])
            else:
                print(f"{command[1]} has already learnt {command[2]}.")
                continue
        else:
            print(f"{command[1]} doesn't exist.")
    #______________________________________________________________________
    elif "Unlearn" in command:
        if command[1] in heroes_dict:
            if command[2] in heroes_dict[command[1]]:
                heroes_dict[command[1]].remove(command[2])
            else:
                print(f"{command[1]} doesn't know {command[2]}.")
                continue
        else:
            print(f"{command[1]} doesn't exist.")

#________________________________________________________________________
print("Heroes:")
for name, spell in sorted(heroes_dict.items(), key=lambda name0_spell1: (name0_spell1[1], name0_spell1[0])):
    print(f"== {name}: {', '.join(spell)}")

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