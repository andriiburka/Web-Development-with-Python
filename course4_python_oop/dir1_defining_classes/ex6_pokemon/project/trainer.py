class Trainer:
    def __init__(self, name):
        self.name, self.pokemon = name, list()

    def add_pokemon(self, pokemon):
        if pokemon.name in [p.name for p in self.pokemon]:
            return f'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in [p.name for p in self.pokemon]:
            return f'Pokemon is not caught'
        p = [p for p in self.pokemon if p.name == pokemon_name][0]
        self.pokemon.remove(p)
        return f'You have released {pokemon_name}'

    def trainer_data(self):
        result = "Pokemon Trainer {trainer_name}\n" \
                 "Pokemon count {all_pokemons}\n".format(trainer_name=self.name, all_pokemons=len(self.pokemon))
        for x in self.pokemon:
            result += f'- {x.pokemon_details()}\n'
        return result
