di = {}

usr_inp = input()
while not usr_inp.isdigit():
    name, phone = [x for x in usr_inp.split('-')]
    di[name] = phone
    usr_inp = input()

usr_inp = int(usr_inp)
for i in range(usr_inp):
    current_name = input()
    if current_name in di:
        print(f"{current_name} -> {di[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")