def characters(let1, let2):
    li = [i for i in range(ord(let1) + 1, ord(let2))]
    return ' '.join(chr(x) for x in li)


l1 = input()
l2 = input()
print(characters(l1, l2))
