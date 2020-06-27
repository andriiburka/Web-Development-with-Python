'''

First you start with the letter before the number.
•	If it's uppercase you divide the number by the letter's position in the alphabet.
•	If it's lowercase you multiply the number with the letter's position in the alphabet.

Then you move to the letter after the number.
•	If it's uppercase you subtract its position from the resulted number.
•	If it's lowercase you add its position to the resulted number.

He decided to complicate it a bit by doing the same but with multiple strings keeping track of only the total sum of all results.

Write a program that calculates the sum of all numbers after the operations on each number have been done.

For example, you are given the sequence "A12b s17G":
We start with the letter before the number on the first string. A is Uppercase and its position in the alphabet is 1.
So we divide the number 12 with the position 1 (12/1 = 12). Then we move to the letter after the number.
b is lowercase and its position is 2. So we add 2 to the resulted number (12+2=14).

Similarly for the second string s is lowercase and its position is 19 so we multiply it with the number (17*19 = 323).
Then we have Uppercase G with position 7, so we subtract it from the resulted number (323 – 7 = 316).
]
Finally, we sum the 2 results and we get 14 + 316=330.

Input
The input comes from the console as a single line, holding the sequence of strings.
Strings are separated by one or more white spaces.
The input data will always be valid and in the format described. There is no need to check it explicitly.

Output
Print at the console a single number:
the total sum of all processed numbers rounded up to two digits after the decimal separator.

Constraints
The count of the strings will be in the range [1 … 10].
•	The numbers between the letters will be integers in range [1 … 2 147 483 647].
•	Time limit: 0.3 sec. Memory limit: 16 MB.

'''
text = input().replace("  ", "").split()
alphabet = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}
total = []
for word_index in range(len(text)):  # for word in text
    tup = int(text[word_index][1:-1]), text[word_index][0], text[word_index][-1]

    current = 0
    for char in range(1, len(tup)):
        if char == 1:
            if tup[char].isupper():  # ДЕЛИМ
                first_lower = tup[char].lower()
                for upper_first_letter, place in alphabet.items():
                    if upper_first_letter == first_lower:
                        current += (tup[0] / place)
                        break
            elif tup[char].islower():  # УМНОЖАВАМЕ
                for lower_first_letter, place in alphabet.items():
                    if lower_first_letter == tup[1]:
                        current += (tup[0] * place)
                        break
        elif char == 2:
            if tup[char].isupper():  # МАХАМЕ от CURRENT
                second_lower = tup[char].lower()
                for upper_second_letter, place in alphabet.items():
                    if upper_second_letter == second_lower:
                        current -= place
                        break
            elif tup[char].islower():  # ДОБАВЯМЕ към CURRENT
                second_word = tup[char]
                for lower_second_letter, place in alphabet.items():
                    if lower_second_letter == second_word:
                        current += place
                        break
    total.append(current)
print(f'{sum(total):.2f}')





# text = input().split()
# alphabet = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}
# total = 0
# for i in range(len(text)):
#     num = int(text[i][1:-1])
#     # first
#     if text[i][0] in alphabet:                      # A isn't in alphabet !!!
#         total += num * alphabet[text[i][0]]
#     elif text[i][0].lower() in alphabet:
#         total += num / alphabet[text[i][0].lower()]
#     # last
#     if text[i][-1] in alphabet:
#         total += alphabet[text[i][-1]]
#     elif text[i][-1].lower() in alphabet:
#         total -= alphabet[text[i][-1].lower()]
# print(f'{total:.2f}')