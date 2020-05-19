''' 0/100
https://judge.softuni.bg/Contests/Practice/DownloadResource/6229
https://judge.softuni.bg/Contests/Practice/Index/1759#1
'''
import re




while True:
    command = input()
    if "end" in command:
        break
    else:
        pattern = r"^([A-Z][a-z']+(\s[a-z']+)*)[:]([A-Z]+(\s[A-Z]+)*)$"
        is_match = re.match(pattern, command)

        if is_match:
            key = len(is_match.group(1))
            encryption = ''

            for i in command:
                if i == " " or i == "'":
                    encryption += i
                elif i == ":":
                    encryption += "@"

                else:
                    encryption += chr(ord(i) + key)


            print(f'Successful encryption: {encryption}')
        # else:
        #     print('Invalid input!')


