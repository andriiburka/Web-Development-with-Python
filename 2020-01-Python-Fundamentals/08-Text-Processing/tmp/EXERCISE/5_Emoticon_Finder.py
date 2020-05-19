text = input().split()
for word in text:
    if ":" in word:
        current_index = 0
        for ch in word:
            if ch == ":":
                if current_index + 1 >= len(word):\
                    continue
                else:
                    print(f'{ch}{word[current_index + 1]}')
            current_index += 1
