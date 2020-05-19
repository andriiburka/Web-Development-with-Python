string = input()

while True:
    command = input().split()
    if "Done" in command:
        break
    elif "TakeOdd" in command:
        temp = ''
        for i in range(len(string)):
            if i % 2 == 1:
                temp += string[i]
        string = temp
        print(string)
    elif "Cut" in command:
        string = string[:int(command[1])] + string[int(command[1]) + int(command[2]):]
        print(string)
    elif "Substitute" in command:
        if command[1] in string:
            string = string.replace(command[1], command[2])
            print(string)
        else:
            print("Nothing to replace!")

print(f"Your password is: {string}")