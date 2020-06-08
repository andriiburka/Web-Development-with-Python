# THE LAST PIECE OF PUZZLE
def kwargs_length(**di):
    return len(di)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
