list_of_strings = list(map(str, input().split()))
temp = []

for word in list_of_strings:

    num = ''
    word_list = []

    for char in word:
        if char.isdigit():
            num += char
        else:
            word_list.append(char)
    character = chr(int(num))
    word_list.insert(0, character)

    if len(word_list) < 3:
        pass
    else:
        # Завъртане
        last_char = word_list.pop(1)
        word_list.insert(-1, last_char)
        second_char = word_list.pop()
        word_list.insert(1, second_char)

    temp.append(''.join(word_list))

list_of_strings.clear()
list_of_strings = temp
print(' '.join(list_of_strings))
