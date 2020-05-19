string = input()
str_li = []
last_char = ''
for i in range(len(string)):
    if i == 0:
        last_char = string[i]
        str_li.append(string[i])
    elif string[i] != last_char:
        last_char = string[i]
        str_li.append(string[i])
print("".join(str_li))