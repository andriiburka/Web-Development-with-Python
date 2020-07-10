''' 100/100
https://judge.softuni.bg/Contests/Practice/DownloadResource/7317
https://judge.softuni.bg/Contests/Practice/Index/1928#2
'''

user_emails = {}
while True:
    command = input().split('->')
    if "Statistics" in command:
        break
    else:
        #___________________________________________________
        if "Add" in command:
            if command[1] not in user_emails:
                user_emails[command[1]] = []
            else:
                print(f"{command[1]} is already registered")

        #___________________________________________________
        elif "Send" in command:
            email_txt = command[2]
            user_emails[command[1]].append(email_txt)

        #___________________________________________________
        elif "Delete" in command:
            if command[1] in user_emails:
                user_emails.pop(command[1])
            else:
                print(f"{command[1]} not found!")


print(f"Users count: {len(user_emails)}")
for key, value in sorted(user_emails.items(), key=lambda x: (-len(x[1]), x[0])):
    print(key)
    for mail in user_emails[key]:
        print(f" - {mail}")

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