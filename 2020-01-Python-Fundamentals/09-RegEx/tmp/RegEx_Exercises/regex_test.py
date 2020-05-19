import re
# name_age = '''
# Janice is 22 and Theon is 33
# Gabriel is 44 and Joey is 21
# '''
# ages = re.findall(r'\d{1,3}', name_age)
# names = re.findall(r'[A-Z][a-z]*', name_age)
# age_dict = {name: int(age) for name, age in zip(names, ages)}
# print(age_dict)


num = "123 1234 12345 123456 1234567"
print("Matches:", len(re.findall(r"\d{5,7}", num)))
print(re.findall(r"\d{5,7}", num))

