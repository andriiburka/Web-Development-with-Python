class Customer:
    def __init__(self, name, age, id):
        self.name, self.age, self.id, self.rented_dvds \
            = name, age, id, list()

    def __repr__(self):
        return "{}: {} of age {} has {} rented DVD's ({})" \
            .format(self.id,
                    self.name,
                    self.age,
                    len(self.rented_dvds),
                    ", ".join([d.name for d in self.rented_dvds]))
