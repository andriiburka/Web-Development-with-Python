import re
pattern = r"\b_{1}[a-zA-Z0-9]+\b"
res = re.findall(pattern, input())
print(",".join([i[1:]for i in res]))