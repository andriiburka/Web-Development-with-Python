'''1.	Valid Usernames
A valid username is:
•	Has length between 3 and 16 characters
•	Contains only letters, numbers, hyphens and underscores
•	Has no redundant symbols before, after or in between

Examples:
Input
Output
---
sh, too_long_username, !lleg@l ch@rs, jeffbutt
jeffbutt
---
Jeff, john45, ab, cd, peter-ivanov, @smith
Jeff
John45
peter-ivanov
'''

names = input().split(", ")
names_list = [name for name in names if 3 <= len(name) <= 16 and name.isidentifier() or "-" in name]
print("\n".join([name for name in names_list]))


'''
string.isidentifier() - Returns true if the string is a valid identifier according to the language definition, 
section Identifiers and keywords from the Python docs.
'''