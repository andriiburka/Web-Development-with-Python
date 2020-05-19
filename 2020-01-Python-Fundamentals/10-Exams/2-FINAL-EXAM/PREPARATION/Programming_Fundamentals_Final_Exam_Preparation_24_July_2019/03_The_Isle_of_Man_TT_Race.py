import re

while True:
    info = input().split("!!")
    name_racer = r"([#\$%\*&])([A-Za-z0-9]+)\1"
    length = r"=([0-9]+)"
    geohash_code = rf"!!([a-zA-Z0-9#\$%\*&\[\]\(\)!]{length})"
    if not info:
        break
    else:
        match = re.match(name_racer, info[0])
        if match:
            print("Match")
        else:
            print('not match')
