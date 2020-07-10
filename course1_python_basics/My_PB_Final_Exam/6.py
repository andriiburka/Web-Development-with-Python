num_locations = int(input())
for location in range(num_locations):
    planned_kg_gold = float(input())
    days_in_current_location = int(input())
    gold_location = 0
    for day in range(days_in_current_location):
        gold_for_current_day = float(input())
        gold_location += gold_for_current_day
        average = gold_location / days_in_current_location
    if average < planned_kg_gold:
        diff = abs(average - planned_kg_gold)
        print(f'You need {diff:.2f} gold.')
    else:
        print(f'Good job! Average gold per day: {average:.2f}.')

