class Car:
    def __init__(self, name, model, engine):
        self.name, self.model, self.engine = name, model, engine

    def get_info(self):
        return type(f"This is {self.name} {self.model} with engine {self.engine}")


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())
