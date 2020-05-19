import re

user_input = input()
user = r"( [a-zA-Z0-9]+[\.\-_]*[a-zA-Z0-9]*"
host = r"[a-zA-Z0-9\-]+(\.[a-zA-Z]+)+)"
emails = re.findall(f"{user}@{host}", user_input, re.I)
print("\n".join([i[0][1:] for i in emails]))