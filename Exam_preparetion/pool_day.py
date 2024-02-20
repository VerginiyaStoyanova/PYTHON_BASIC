from math import ceil

people_number = int(input())
entrance_fee = float(input())
price_per_sun_lounger = float(input())
price_per_umbrella = float(input())

total_entrance_fee = people_number * entrance_fee
total_price_sun_lounger = ceil(people_number * 0.75) * price_per_sun_lounger
total_price_umbrella = ceil(people_number / 2) * price_per_umbrella
total_fee = total_entrance_fee + total_price_umbrella + total_price_sun_lounger

print(f"{total_fee:.2f} lv.")