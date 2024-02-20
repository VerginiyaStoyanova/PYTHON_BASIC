budget = float (input())
nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())
additional_costs = budget * (percent_additional_costs / 100)

if nights > 7:
    needed_money = nights * (price_per_night * 0.95) + additional_costs
else:
    needed_money = nights * price_per_night + additional_costs

difference = abs(budget - needed_money)
if budget >= needed_money:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")