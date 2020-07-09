username = input()

while True:
    command = input()
    if "Sign up" in command:
        break

    elif "Case lower" in command:
        username = username.lower()
        print(username)

    elif "Case upper" in command:
        username = username.upper()
        print(username)

    elif "Reverse" in command:
        command = command.split()
        word = username[int(command[1]):int(command[2])+1][::-1]
        print(word)

    elif "Cut" in command:
        command = command.split()
        if command[1] in username:
            username = username.replace(command[1], '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {command[1]}.")

    elif "Replace" in command:
        command = command.split()
        username = username.replace(command[1], '*')
        print(username)

    elif "Check" in command:
        command = command.split()
        if command[1] in username:
            print('Valid!')
        else:
            print(f"Your username must contain {command[1]}.")
