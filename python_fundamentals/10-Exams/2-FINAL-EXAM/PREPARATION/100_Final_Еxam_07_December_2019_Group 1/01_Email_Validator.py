''' 100/100
https://judge.softuni.bg/Contests/Practice/DownloadResource/7315
https://judge.softuni.bg/Contests/Practice/Index/1928#0
'''

email = input()
while True:
    command = input()
    if "Complete" in command:
        break
    #____________________________________
    if "Make Upper" in command:
        email = email.upper()
        print(email)

    #____________________________________
    elif "Make Lower" in command:
        email = email.lower()
        print(email)

    #____________________________________
    elif "GetDomain" in command:
        command = command.split()
        index = int(command[1])
        print(email[-index:])

    #____________________________________
    elif "GetUsername" in command:
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
            continue
        print(email.split("@")[0])

    #____________________________________
    elif "Replace" in command:
        command = command.split()
        email = email.replace(command[1], "-")
        print(email)

    #____________________________________
    elif "Encrypt" in command:
        [print(ord(ch), end=' ') for ch in email]


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