import math

price_per_tennis_racket = float(input())
number_of_tennis_rackets = int(input())
number_of_sneakers = int(input())

total_tennis_rackets = price_per_tennis_racket * number_of_tennis_rackets
price_per_sneakers = 1 / 6 * price_per_tennis_racket
total_sneakers = price_per_sneakers * number_of_sneakers
price_for_other_equipment = 0.2 * (total_sneakers + total_tennis_rackets)
total_price = total_tennis_rackets + total_sneakers + price_for_other_equipment
djokovic_part = 1 / 8 * total_price
sponsors_part = total_price - djokovic_part

print(f"Price to be paid by Djokovic {math.floor(djokovic_part)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_part)}")