import random


class Class(list):
    def get_random(self):
        random_el = random.choice(self)
        self.remove(random_el)
        return random_el, self


first = Class([1, 2, 3])

print(first.get_random())
