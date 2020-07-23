class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id, self.topic, self.storage_folder = id, topic, storage_folder

    def edit(self, new_topic, new_storage_folder):
        self.topic, self.storage_folder = new_topic, new_storage_folder

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
