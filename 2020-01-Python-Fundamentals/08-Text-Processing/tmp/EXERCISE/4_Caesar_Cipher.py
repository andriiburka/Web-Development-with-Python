string = input()
ciphered_string = ''
for ch in string:
    ciphered_string += chr(ord(ch) + 3)
print(ciphered_string)