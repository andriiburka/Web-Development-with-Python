import re

data_list = []
total = 0
while True:
    user_input = input()
    if "Purchase" in user_input:
        break
    else:
        pattern = r">>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)"
        match = re.match(pattern, user_input)

        if match:
            article = match.group(1)
            price = float(match.group(2)) * float(match.group(3))
            for i in re.findall(pattern, user_input):
                data_list.append(article)
                total += price

print("Bought furniture:")
[print(thing) for thing in data_list]
print(f"Total money spend: {total:.2f}")
