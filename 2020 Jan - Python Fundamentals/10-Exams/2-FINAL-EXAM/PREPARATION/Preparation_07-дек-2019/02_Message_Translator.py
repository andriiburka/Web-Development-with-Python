import re

n = int(input())
for i in range(1, n + 1):
    usr_in = input()
    pattern = r"^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]$"
    match = re.findall(pattern, usr_in)
    if match:
        usr_in = match[0][0] + ":"
        for ascii_num in match[0][1]:
            usr_in += " " + str(ord(ascii_num))
        print(usr_in)
    else:
        print(f"The message is invalid")

# 2
# !Send!:[IvanisHere]
# *Time@:[Itis5amAlready]

# 3
# go:[outside]
# !drive!:YourCarToACarWash
# !Watch!:[LordofTheRings]
#

# 3
# !play!:[TheNewSong]
# !Ride!:[Bike]
# !Watch!:[LordofTheRings]
