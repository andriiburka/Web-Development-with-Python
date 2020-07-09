text_string = "".join(input().split(" "))

count_chars_dict = {}

for char in text_string:
    if char in count_chars_dict:
        continue
    else:
        count_chars_dict[char] = text_string.count(char)

for key, value in count_chars_dict.items():
    print(f'{key} -> {value}')