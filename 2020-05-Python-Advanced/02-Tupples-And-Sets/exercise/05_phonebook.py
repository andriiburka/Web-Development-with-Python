di = {}

while True:
    usr_inp = input()
    if usr_inp.isdigit():
        usr_inp = int(usr_inp)
        for i in range(usr_inp):
            print(i)
    else:
        usr_inp = usr_inp.split('-')
        key = usr_inp[0]
        value = usr_inp[1]
        di[key] = value


print(di)