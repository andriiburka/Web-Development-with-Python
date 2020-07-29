class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0
        self.length = len(self.keys)

    def __iter__(self):
        return self

    def __next__(self):
        idx = self.index
        if idx == self.length:
            raise StopIteration
        current_key = self.keys[idx]
        current_value = self.dictionary[current_key]
        self.index += 1
        return current_key, current_value
