budget = float(input())
season = input()
spent_money = 0
destination = ""
place = ""
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        spent_money = budget * 0.3
    elif season == 'winter':
        place = 'Hotel'
        spent_money = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        spent_money = budget * 0.4
    elif season == 'winter':
        place = 'Hotel'
        spent_money = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    place = 'Hotel'
    spent_money = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {spent_money:.2f}")