drink = input()
sugar = input()
number_of_drinks = int(input())
total_price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price_drink = 0.90
        price_drink *= 0.65
    elif sugar == 'Normal':
        price_drink = 1.00
    elif sugar == 'Extra':
        price_drink = 1.20
    if number_of_drinks >= 5:
        price_drink *= 0.75
    total_price = number_of_drinks * price_drink

elif drink == 'Cappuccino':
    if sugar == 'Without':
        price_drink = 1.00
        price_drink *= 0.65
    elif sugar == 'Normal':
        price_drink = 1.20
    elif sugar == 'Extra':
        price_drink = 1.60
    total_price = number_of_drinks * price_drink

elif drink == 'Tea':
    if sugar == 'Without':
        price_drink = 0.50
        price_drink *= 0.65
    elif sugar == 'Normal':
        price_drink = 0.60
    elif sugar == 'Extra':
        price_drink = 0.70
    total_price = number_of_drinks * price_drink

if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.")