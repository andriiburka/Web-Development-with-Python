from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        # TODO: Не добавяме fuel а го сетваме - за това проверката долу е с = а не +=
        self.__fuel = value if value + self.__fuel <= self.fuel_tank else self.fuel_tank

    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self.__fuel:
            self.__fuel -= fuel_needed
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        if self.get_capacity(self.fuel_tank, self.__fuel + liters) != 'Capacity reached!':
            self.__fuel += liters
        return self.__fuel
