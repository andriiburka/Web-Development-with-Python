from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super(Vegetable, self).__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super(Fruit, self).__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super(Meat, self).__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super(Seed, self).__init__(quantity)
