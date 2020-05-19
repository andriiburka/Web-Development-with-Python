num_heroes = int(input())
max_hp = 100
max_mp = 200

heroes_dict = {}
for i in range(1, num_heroes + 1):
    name_hp_mp = input().split()
    name = name_hp_mp[0]
    hp = int(name_hp_mp[1])
    mp = int(name_hp_mp[2])
    heroes_dict[name] = {'hp': hp, 'mp': mp}

while True:
    command = input()
    if "End" in command:
        break

    command = command.split(' - ')

    if "Heal" in command:
        hero_name = command[1]
        amount = int(command[2])

        if heroes_dict[hero_name]['hp'] + amount <= max_hp:
            heroes_dict[hero_name]['hp'] += amount
            print(f"{hero_name} healed for {amount} HP!")
        else:
            diff = max_hp - (heroes_dict[hero_name]['hp'] + amount)
            new_amount = amount - abs(diff)

            heroes_dict[hero_name]['hp'] = max_hp
            print(f"{hero_name} healed for {new_amount} HP!")


    elif "Recharge" in command:
        hero_name = command[1]
        amount = int(command[2])

        if heroes_dict[hero_name]['mp'] + amount <= max_mp:
            heroes_dict[hero_name]['mp'] += amount
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            diff = max_mp - (heroes_dict[hero_name]['mp'] + amount)
            new_amount = amount - abs(diff)

            heroes_dict[hero_name]['mp'] = max_mp
            print(f"{hero_name} recharged for {new_amount} MP!")

    elif "TakeDamage" in command:
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]

        if not heroes_dict[hero_name]['hp'] - damage < 0:
            heroes_dict[hero_name]['hp'] -= damage
            print(f"Kyrre was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['hp']} HP left!")
        else:
            heroes_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif "CastSpell" in command:
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]

        if mp_needed <= heroes_dict[hero_name]['mp']:
            heroes_dict[hero_name]['mp'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['mp']} MP!")


for hero, value in heroes_dict.items():
    print(hero)
    for i in value:
        print(i[0])













