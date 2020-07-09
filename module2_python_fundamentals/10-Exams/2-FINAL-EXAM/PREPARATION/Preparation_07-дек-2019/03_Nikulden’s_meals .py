import re

liked_dict = {}
unliked_dict = {}
while True:
    usr_in = re.split("-", input())

    if "Stop" not in usr_in:

        if "Like" in usr_in:
            user = usr_in[1]
            if user not in liked_dict:
                liked_dict[usr_in[1]] = [usr_in[2]]
            else:
                liked_dict[usr_in[1]].append(usr_in[2])

        elif "Unlike" in usr_in:
            user = usr_in[1]
            if user not in unliked_dict:
                unliked_dict[usr_in[1]] = [usr_in[2]]
            else:
                unliked_dict[usr_in[1]].append(usr_in[2])
    else:
        break

for k, v in liked_dict.items():
    print(f"{k}:", *v)
print(f"Unliked meals: {len(unliked_dict)}")
