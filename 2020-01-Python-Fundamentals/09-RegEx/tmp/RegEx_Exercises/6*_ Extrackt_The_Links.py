import re

web_list = []
while True:
    usr_in = input()
    pat = r"(www\.[A-Za-z0-9\-]+(\.[a-zA-Z]+)+)"
    if usr_in:
        if re.findall(pat, usr_in):
            web_list.append(re.findall(pat, usr_in)[0][0])
    else:
        [print(i) for i in web_list]
        break


