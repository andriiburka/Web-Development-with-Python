parentheses = input()
s = []

pairs = {
    '{': '}',
    '[': ']',
    '(': ')'
}

valid = True

for el in parentheses:
    if el in "{([":
        s.append(el)
    elif el in "})]":
        if s:
            current = s[-1]
            if pairs[current] == el:
                s.pop()
            else:
                valid = False
                break
        else:
            valid = False
            break

if valid:
    print("YES")
else:
    print("NO")