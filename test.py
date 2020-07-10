class Bot:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


bot = Bot('Andrii', 32)
print(bot.get_name())

print(bot.get_age())
