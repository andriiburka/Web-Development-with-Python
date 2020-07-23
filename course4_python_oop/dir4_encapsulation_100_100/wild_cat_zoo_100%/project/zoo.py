# from course4_python_oop.dir4_encapsulation_100_100.wild_cat_zoo_100%.ed.caretaker import Caretaker
# from course4_python_oop.dir4_encapsulation_100_100.wild_cat_zoo_100%.ed.cheetah import Cheetah
# from course4_python_oop.dir4_encapsulation_100_100.wild_cat_zoo_100%.ed.keeper import Keeper
# from course4_python_oop.dir4_encapsulation_100_100.wild_cat_zoo_100%.ed.tiger import Tiger
# from course4_python_oop.dir4_encapsulation_100_100.wild_cat_zoo_100%.ed.lion import Lion
# from course4_python_oop.dir4_encapsulation_100_100.wild_cat_zoo_100%.ed.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if (self.__budget >= price) and (len(self.animals) < self.__animal_capacity):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def tend_animals(self):
        cheetah_needs = sum([a.get_needs() for a in self.animals if a.__class__.__name__ == "Cheetah"])
        tiger_needs = sum([a.get_needs() for a in self.animals if a.__class__.__name__ == "Tiger"])
        lion_needs = sum([a.get_needs() for a in self.animals if a.__class__.__name__ == "Lion"])
        animals_needs = sum([cheetah_needs, tiger_needs, lion_needs])
        if self.__budget >= animals_needs:
            self.__budget -= animals_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def pay_workers(self):
        caretaker_salaries = sum([c.salary for c in self.workers if c.__class__.__name__ == "Caretaker"])
        keeper_salaries = sum([k.salary for k in self.workers if k.__class__.__name__ == "Keeper"])
        vet_salaries = sum([v.salary for v in self.workers if v.__class__.__name__ == "Vet"])
        workers_salaries = sum([caretaker_salaries, keeper_salaries, vet_salaries])
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def fire_worker(self, worker_name):
        if worker_name in [w.name for w in self.workers]:
            [self.workers.remove(w) for w in self.workers if w.name == worker_name]
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        # Lions
        result += f"\n----- {len([a.name for a in self.animals if a.__class__.__name__ == 'Lion'])} Lions:"
        result += '\n'+'\n'.join([a.__repr__() for a in self.animals if a.__class__.__name__ == 'Lion'])
        # Tigers
        result += f"\n----- {len([a.name for a in self.animals if a.__class__.__name__ == 'Tiger'])} Tigers:"
        result += '\n'+'\n'.join([a.__repr__() for a in self.animals if a.__class__.__name__ == 'Tiger'])
        # Cheetahs
        result += f"\n----- {len([a.name for a in self.animals if a.__class__.__name__ == 'Cheetah'])} Cheetahs:"
        result += '\n'+'\n'.join([a.__repr__() for a in self.animals if a.__class__.__name__ == 'Cheetah'])
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        # Keepers
        result += f"\n----- {len([w.name for w in self.workers if w.__class__.__name__ == 'Keeper'])} Keepers:"
        result += '\n' + '\n'.join([w.__repr__() for w in self.workers if w.__class__.__name__ == 'Keeper'])
        # Caretakers
        result += f"\n----- {len([w.name for w in self.workers if w.__class__.__name__ == 'Caretaker'])} Caretakers:"
        result += '\n' + '\n'.join([w.__repr__() for w in self.workers if w.__class__.__name__ == 'Caretaker'])
        # Vets
        result += f"\n----- {len([w.name for w in self.workers if w.__class__.__name__ == 'Vet'])} Vets:"
        result += '\n' + '\n'.join([w.__repr__() for w in self.workers if w.__class__.__name__ == 'Vet'])
        return result

    def profit(self, amount):
        self.__budget += amount


# zoo = Zoo("Zootopia", 3000, 5, 8)
# animals = [Cheetah("Cheeto", "Male", 2),
#            Cheetah("Cheetia", "Female", 1),
#            Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3),
#            Tiger("Tigeria", "Female", 1),
#            Lion("Nala", "Female", 4)]
# prices = [200, 190, 204, 156, 211, 140]
# workers = [Keeper("John", 26, 100),
#            Keeper("Adam", 29, 80),
#            Keeper("Anna", 31, 95),
#            Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105),
#            Caretaker("Stacy", 35, 140),
#            Vet("Peter", 40, 300),
#            Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
# for worker in workers:
#     print(zoo.hire_worker(worker))
# print(zoo.tend_animals())
# print(zoo.pay_workers())
# print(zoo.fire_worker("Adam"))
# print(zoo.animals_status())
# print(zoo.workers_status())
#
#
# """ EXPECTED
# Cheeto the Cheetah added to the zoo
# Cheetia the Cheetah added to the zoo
# Simba the Lion added to the zoo
# Zuba the Tiger added to the zoo
# Tigeria the Tiger added to the zoo
# Not enough space for animal
# John the Keeper hired successfully
# Adam the Keeper hired successfully
# Anna the Keeper hired successfully
# Bill the Caretaker hired successfully
# Marie the Caretaker hired successfully
# Stacy the Caretaker hired successfully
# Peter the Vet hired successfully
# Kasey the Vet hired successfully
# Not enough space for worker
# You tended all the animals. They are happy. Budget left: 1779
# You payed your workers. They are happy. Budget left: 611
# Adam fired successfully
# You have 5 animals
# ----- 1 Lions:
# Name: Simba, Age: 4, Gender: Male
# ----- 2 Tigers:
# Name: Zuba, Age: 3, Gender: Male
# Name: Tigeria, Age: 1, Gender: Female
# ----- 2 Cheetahs:
# Name: Cheeto, Age: 2, Gender: Male
# Name: Cheetia, Age: 1, Gender: Female
# You have 7 workers
# ----- 2 Keepers:
# Name: John, Age: 26, Salary: 100
# Name: Anna, Age: 31, Salary: 95
# ----- 3 Caretakers:
# Name: Bill, Age: 21, Salary: 68
# Name: Marie, Age: 32, Salary: 105
# Name: Stacy, Age: 35, Salary: 140
# ----- 2 Vets:
# Name: Peter, Age: 40, Salary: 300
# Name: Kasey, Age: 37, Salary: 280
# """


