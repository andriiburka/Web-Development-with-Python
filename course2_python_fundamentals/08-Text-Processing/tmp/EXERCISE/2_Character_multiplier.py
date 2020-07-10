string = input().split()
word1 = string[0]
word2 = string[1]
total = 0
longer_word = word1 if len(word1) > len(word2) else word2
shorter_word = word1 if len(word1) < len(word2) else word2
diff = abs(len(word1) - len(word2))

for i in range(min(len(word1), len(word2))):
    ch1 = ord(word1[i])
    ch2 = ord(word2[i])
    total += ch1 * ch2

for ind in range(-diff, 0):
    total += ord(longer_word[ind])

print(total)
