def age_assignment(*names, **ages):
    return {name: value for name in names for key, value in ages.items() if name[0] == key}


# INPUTS
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))