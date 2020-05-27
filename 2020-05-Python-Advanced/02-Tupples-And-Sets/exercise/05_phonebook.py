def solve(usr_inp):
    contacts_di = {}
    while not usr_inp.isdigit():
        name, phone = usr_inp.split('-')
        contacts_di[name] = phone
        usr_inp = input()
    usr_inp = int(usr_inp)
    for _ in range(usr_inp):
        current_name = input()
        if current_name in contacts_di:
            print(f"{current_name} -> {contacts_di[current_name]}")
        else:
            print(f"Contact {current_name} does not exist.")


if __name__ == '__main__':
    solve(usr_inp=input())