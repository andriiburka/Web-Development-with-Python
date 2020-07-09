followers = {}

new_dict = {}

while True:
    cmd = input()
    if "Log out" in cmd:
        break
    else:

        if "New follower" in cmd:
            cmd = cmd.split(': ')
            name = cmd[1]
            if name not in followers:
                followers[name] = {'likes': 0, 'comments': 0}

        if "Like" in cmd:
            cmd = cmd.split(': ')
            name = cmd[1]

            if name not in followers:
                followers[name] = {'likes': int(cmd[2])}
            else:
                followers[name] = {'likes': 0}
                followers[name]['likes'] += 1
            print(followers)

        if "Comment" in cmd:
            cmd = cmd.split(': ')
            name = cmd[1]

            if name not in followers:
                followers[name] = {'comments': 1}
            else:
                print(followers['comments'])

            print(followers)


        if "Blocked" in cmd:
            cmd = cmd.split(': ')
            if cmd[1] not in followers:
                print(f"{cmd[1]} doesn't exist.")
            else:
                followers[cmd[1]]['likes'] = 0
                followers[cmd[1]].update()
            print(followers)

followers_count = 0
for follower in followers:
    followers_count += 1

print(f"{followers_count} followers")
