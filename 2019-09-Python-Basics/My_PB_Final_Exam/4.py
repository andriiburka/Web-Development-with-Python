team = input()
n_games = int(input())
scores = 0
diff = 0
for game in range(1, n_games + 1):
    goals_plus = int(input())
    goals_minus = int(input())
    if goals_plus > goals_minus:
        scores += 3
    elif goals_plus == goals_minus:
        scores += 1
    diff += (goals_plus - goals_minus)
if diff >= 0:
    print(f'{team} has finished the group phase with {scores} points.')
    print(f'Goal difference: {diff}.')
else:
    print(f'{team} has been eliminated from the group phase.')
    print(f'Goal difference: {diff}.')


