air_ticket_price_going = float(input())
air_ticket_price_return = float(input())
ticket_game_price = float(input())
num_games = int(input())
percent_of_discount = int(input())
people = 1 + 5  # :D
sum_air_tickets = people * (air_ticket_price_going + air_ticket_price_return)
discounted_air_tickets = sum_air_tickets - sum_air_tickets * (percent_of_discount/100)
total_sum_game_tickets = people * num_games * ticket_game_price
total = discounted_air_tickets + total_sum_game_tickets
sum_per_friend = total / people
print(f'Total sum: {total:.2f} lv.')
print(f'Each friend has to pay {sum_per_friend:.2f} lv.')