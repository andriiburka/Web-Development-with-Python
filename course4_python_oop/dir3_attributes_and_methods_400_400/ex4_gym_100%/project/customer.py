class Customer:
    next_id = 1  # cannot be access via self init -> Class.next_id

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.next_id

        """now after initialisation we can increase id and increased id can be accessed when we call class again"""
        Customer.next_id += 1

    @staticmethod
    def get_next_id():
        return Customer.next_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
