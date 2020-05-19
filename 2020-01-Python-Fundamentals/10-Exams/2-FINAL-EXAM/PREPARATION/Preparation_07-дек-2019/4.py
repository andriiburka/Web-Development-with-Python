import re

likes = {}
unlikes = 0

while True:
    usr_in = input()
    if "Stop" in usr_in:
        break
    else:                                                                                                                                                                                                                                                                                           yttttyyikk
        usr_in = re.split('-', usr_in)

        if "Like" in usr_in[0]:
            if usr_in[1] not in likes:
                likes[usr_in[1]] = [usr_in[2]]
            else:
                likes[usr_in[1]].append(usr_in[2])

        elif "Unlike" in usr_in[0]:
            if usr_in[1] in likes:
                print(usr_in[1])
                if usr_in[2] in likes:
                    print(usr_in[2])


print(likes)
print(unlikes)






