import re
all_user_inputs = ''
while True:
    user_input = input()
    if not user_input:
        break
    else:
        all_user_inputs += (user_input + " \n")

nums = re.findall(r"\d+", all_user_inputs)

print(*nums)
