class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.index = self.count

    def __iter__(self):
        return self

    def __next__(self):
        tmp_index = self.index
        if tmp_index < 0:
            raise StopIteration
        self.index -= 1
        return tmp_index


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
