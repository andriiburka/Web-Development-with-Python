class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        self.ingredients[ingredient] = quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] - quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * ingredient_price

    def repr_ingredients_and_quantity(self):
        formated_ing_list = []
        for ing, quantity in self.ingredients.items():
            formated_ing_list.append(f"{ing}: {quantity}")
        return formated_ing_list

    def pizza_ordered(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(self.repr_ingredients_and_quantity())} " \
               f"and the price will be {self.price}lv."
