def age_assignment(*names, **ages):
    return {name: age for name in names for letter, age in ages.items() if name[0] == letter}


# INPUTS
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))