month = input()
nights = int(input())
price_per_night_studio = 0
price_per_night_apartment = 0
total_sum_studio = 0
total_sum_apartment = 0
if month == 'May' or month == 'October':
    price_per_night_studio = 50
    price_per_night_apartment = 65
    if 7 < nights <= 14:
        price_per_night_studio *= 0.95
    elif nights > 14:
        price_per_night_studio *= 0.70
        price_per_night_apartment *= 0.90
elif month == 'June' or month == 'September':
    price_per_night_studio = 75.20
    price_per_night_apartment = 68.70
    if nights > 14:
        price_per_night_studio *= 0.80
        price_per_night_apartment *= 0.90
elif month == 'July' or month == 'August':
    price_per_night_studio = 76
    price_per_night_apartment = 77
    if nights > 14:
        price_per_night_apartment *= 0.90
total_sum_studio = nights * price_per_night_studio
total_sum_apartment = nights * price_per_night_apartment

print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")
