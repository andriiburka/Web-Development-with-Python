class Song:
    def __init__(self, name, length, single):
        self.name, self.length, self.single \
            = name, length, single

    def get_info(self):
        return f'{self.name} - {self.length}'
