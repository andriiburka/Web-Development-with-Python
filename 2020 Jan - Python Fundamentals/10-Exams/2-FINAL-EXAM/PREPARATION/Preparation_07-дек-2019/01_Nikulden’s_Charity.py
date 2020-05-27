import re

usr_in = input()
while True:
    command = input()
    if "Finish" not in command:
        command = command.split()
        if "Replace" in command:
            old_char = command[1]
            new_char = command[2]
            usr_in = usr_in.replace(old_char, new_char)
            print(usr_in)
        elif "Make" in command:
            if "Upper" in command[1]:
                usr_in = usr_in.upper()
                print(usr_in)
            elif "Lower" in command[1]:
                usr_in = usr_in.lower()
                print(usr_in)
        elif "Check" in command:
            match = re.findall(command[1], usr_in)
            if match:
                print(f"Message contains {command[1]}")
            else:
                print(f"Message doesn't contain {command[1]}")
        elif "Sum" in command:
            start = int(command[1])
            end = int(command[2])
            total = 0
            length = len(usr_in)
            if 0 <= start <= length and 0 <= end <= length:
                for i in range(start, end + 1):
                    total += ord(usr_in[i])
                print(total)
            else:
                print("Invalid indexes!")
        elif "Cut" in command:
            start = int(command[1])
            end = int(command[2])
            length = len(usr_in)-1
            if 0 <= start <= length and 0 <= end <= length:
                usr_in = usr_in.replace(usr_in[start:end + 1], "")
                print(usr_in)
            else:
                print("Invalid indexes!")
    else:
        break
