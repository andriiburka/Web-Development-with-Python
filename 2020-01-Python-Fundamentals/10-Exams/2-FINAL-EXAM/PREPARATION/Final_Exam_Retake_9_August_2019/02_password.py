import re
for i in range(1, int(input()) + 1):
    match = re.match(r"^([^\s]+)[>]([0-9]+)([|])([a-z]+)\3([A-Z]+)\3([^><]+)[<]\1$", input())
    if not match:
        print("Try another password!")
    else:
        print(f"Password: {match.group(2) + match.group(4) + match.group(5) + match.group(6)}")