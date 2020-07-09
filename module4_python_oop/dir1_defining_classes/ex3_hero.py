class Hero:
    def __init__(self, name, health):
        self.name, self.health = name, health

    def defend(self, damage):
        self.health -= damage
        self.health = 0 if self.health <= 0 else self.health
        return None if self.health else f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


# # readable
# class Hero:
#     def __init__(self, name, health):
#         self.name, self.health = name, health
#
#     def defend(self, damage):
#         self.health -= damage
#         if self.health <= 0:
#             self.health = 0
#             return f"{self.name} was defeated"
#
#     def heal(self, amount):
#         self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
