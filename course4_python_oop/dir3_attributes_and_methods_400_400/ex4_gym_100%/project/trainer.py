class Trainer:
    next_id = 1  # cannot be access via self init -> Class.next_id

    def __init__(self, name):
        self.name = name
        self.id = Trainer.next_id

        """now after initialisation we can increase id and increased id can be accessed when we call class again"""
        Trainer.next_id += 1

    @staticmethod
    def get_next_id():
        return Trainer.next_id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
