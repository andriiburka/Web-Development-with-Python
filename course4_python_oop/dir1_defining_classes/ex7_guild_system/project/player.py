class Player:
    def __init__(self, name, hp, mp):
        self.name, self.hp, self.mp, self.skills, self.guild \
            = name, hp, mp, dict(), 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        result = f'Name: {self.name}\n' \
                 f'Guild: {self.guild}\n' \
                 f'HP: {self.hp}\n' \
                 f'MP: {self.mp}\n'
        for k, v in self.skills.items():
            result += f'==={k} - {v}\n'
        return result
