class Shop:
    def __init__(self, name, *args):
        self.name, self.items = name, args[0]

    def get_items_count(self):
        return len(self.items)

    def __str__(self):
        return self.get_items_count()


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
