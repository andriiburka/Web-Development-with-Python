class Equipment:
    next_id = 1  # cannot be access via self init -> Class.next_id

    def __init__(self, name):
        self.name = name
        self.id = Equipment.next_id

        """now after initialisation we can increase id and increased id can be accessed when we call class again"""
        Equipment.next_id += 1

    @staticmethod
    def get_next_id():
        return Equipment.next_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
