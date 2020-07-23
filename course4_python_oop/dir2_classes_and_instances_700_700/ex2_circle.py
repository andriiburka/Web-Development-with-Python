import math


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        result = (Circle.pi * self.radius * self.radius)
        return result

    def get_circumference(self):
        result = (2 * Circle.pi * self.radius)
        return result
