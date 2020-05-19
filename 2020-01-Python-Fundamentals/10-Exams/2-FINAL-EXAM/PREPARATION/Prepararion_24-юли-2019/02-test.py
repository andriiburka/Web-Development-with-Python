import re
string = 'Guns n\'roses:NOVEMBER RAIN'


pattern = r"^([A-Z][a-z']+(\s[a-z']+)*)[:]([A-Z]+(\s[A-Z]+)*)$"
is_match = re.match(pattern, string)

new_string = ''
if is_match:
    key = len(is_match.group(1))

    for i in string:
        if i.isupper():
            print('UPPER', i, ord(i), ord(i)+key, chr(ord(i)+key))

            print()
        elif i.islower():
            print(i)
            print('LOWER', i,  ord(i), ord(i)+key, chr(ord(i)+key))

            print()