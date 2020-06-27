import re

user_input = input()
target = input()

pattern = rf"\b{target}\b"
matches = re.findall(pattern, user_input, re.IGNORECASE)
print(len(matches))