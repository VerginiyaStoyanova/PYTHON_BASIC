budget = float(input())
number_of_statists = int(input())
one_dress_price = float(input())

decore_price = budget * 0.10
dresses_price = number_of_statists * one_dress_price
if number_of_statists > 150:
    dresses_price *= 0.90
needed_money = decore_price + dresses_price
difference = abs(budget - needed_money)
if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")