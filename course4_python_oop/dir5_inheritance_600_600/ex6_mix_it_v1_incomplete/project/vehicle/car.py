from course4_python_oop.dir5_inheritance.ex6_mix_it_v1_incomplete.project import CapacityMixin
from course4_python_oop.dir5_inheritance.ex6_mix_it_v1_incomplete.project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel  # резервоар

    # fuel.getter
    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        self.__fuel = fuel if (self.__fuel + fuel <= self.fuel_tank) else self.fuel_tank

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption * distance) / 100

        if self.__fuel >= fuel_needed:
            self.__fuel -= (self.fuel_consumption * distance) / 100
            # TODO: UNCOMMENT BEFORE SUBMIT!
            # return "We've enjoyed the travel!"

            # TODO: DELETE_2 START
            return f"Needed: {distance * self.fuel_consumption / 100} <= Owned: {self.__fuel} " \
                   f"- We've enjoyed the travel!"
        else:
            return f"Needed: {distance * self.fuel_consumption / 100} > Owned: {self.__fuel} " \
                   f"- The fuel isn't enough"
            # # TODO: DELETE_2 END

    def refuel(self, liters):
        CapacityMixin.get_capacity(self.fuel_tank, self.__fuel)

        is_enough_space = self.fuel_tank - self.__fuel >= liters
        if is_enough_space:
            self.__fuel += liters
            return self.__fuel
        else:
            self.__fuel = self.fuel_tank
            return "Capacity reached!"

    def __repr__(self):
        return f"Fuel in the tank: {self.__fuel}/{self.fuel_tank}"


car1 = Car(4, 50, 3, 20)
print(car1.drive(1000))
car1.refuel(40)

print(car1.__repr__())
