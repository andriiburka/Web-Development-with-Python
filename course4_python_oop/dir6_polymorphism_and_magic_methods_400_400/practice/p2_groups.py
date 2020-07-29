class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, second):
        return self.name.__add__(f" {second.surname}")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __add__(self, group2):
        return self.people.__add__(group2.people)

    def __len__(self):
        return self.people.__len__()

    def __str__(self):
        return f"Group {self.name} with members {', '.join([i.__str__() for i in self.people])}"

    def __getitem__(self, x):
        return f'Person {x}: {self.people[x]}'


# #INPUT
p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(first_group[0])

for person in third_group:
    print(person)



# import unittest
#
#
# class TestGroups(unittest.TestCase):
#     def setUp(self):
#         self.p0 = Person('Aliko', 'Dangote')
#         self.p1 = Person('Bill', 'Gates')
#         self.p2 = Person('Warren', 'Buffet')
#         self.p3 = Person('Elon', 'Musk')
#
#     def test_group_get_item(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(first_group[0], "Person 0: Aliko Dangote")
#
#
# if __name__ == "__main__":
#     unittest.main()
