word_and_len = {word.replace(',', ''): len(word.replace(',', '')) for word in input().split()}
output = ['{} -> {}'.format(word, length) for word, length in word_and_len.items()]
print(str(output)[1:-1].replace("'", ""))


# my_dict = {name:len(name) for name in input().split(", ")}
# print(", ".join([f"{name} -> {leng}" for name, leng in my_dict.items()]))