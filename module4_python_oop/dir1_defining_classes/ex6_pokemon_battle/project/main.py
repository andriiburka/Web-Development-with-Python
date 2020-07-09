from module4_python_oop.defining_classes_1.zip.pokemon_battle.project.pokemon import Pokemon
from module4_python_oop.defining_classes_1.zip.pokemon_battle.project.trainer import Trainer


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
