'''100/100
https://judge.softuni.bg/Contests/Practice/DownloadResource/6228
https://judge.softuni.bg/Contests/Practice/Index/1759#0
'''

import re
bands_dict = {}
bands_time = {}
band_to_print = ''

while True:
    command = re.split("; ", input())
    #___________________________________________
    if "start of concert" in command:
        band_to_print = input()
        break

    #___________________________________________
    elif "Add" in command:
        stars_add = re.split(", ", command[2])
        if command[1] not in bands_dict:
            bands_dict[command[1]] = stars_add
        else:
            [bands_dict[command[1]].append(name) for name in stars_add if name not in bands_dict[command[1]]]

    #___________________________________________
    elif "Play" in command:
        if command[1] not in bands_time:
            bands_time[command[1]] = int(command[2])
        else:
            bands_time[command[1]] += int(command[2])


print(f"Total time: {sum([time for band, time in bands_time.items()])}")
[print(f"{band} -> {time}") for band, time in sorted(bands_time.items(), key=lambda x: (-x[1], x[0]))]
if band_to_print in bands_dict:
    print(band_to_print)
    [print(f"=> {star}") for star in bands_dict[band_to_print]]