class Subscription:
    next_id = 1  # cannot be access via self init -> Class.incremented_id

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.next_id

        """now after initialisation we can increase id and increased id can be accessed when we call class again"""
        Subscription.next_id += 1

    @staticmethod
    def get_next_id():
        return Subscription.next_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
