class Customer:
    def __init__(self, name, age, id):
        self.name, self.age, self.id, self.rented_dvds = name, age, id, []

    def __repr__(self):
        return "{id}: {customer} of age {years} has {count} rented DVD's ({collection})"\
            .format(id=self.id,
                    customer=self.name,
                    years=self.age,
                    count=len(self.rented_dvds),
                    collection=", ".join([d.name for d in self.rented_dvds]))
