excursion_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_tracks = int(input())
puzzle_price = 2.60
dolls_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
track_price = 2
total_order_toys = number_of_puzzles * puzzle_price \
    + number_of_dolls * dolls_price \
    + number_of_teddy_bears * teddy_bear_price \
    + number_of_minions * minion_price \
    + number_of_tracks * track_price
number_of_toys = number_of_puzzles \
                 + number_of_dolls \
                 + number_of_teddy_bears + number_of_minions \
                 + number_of_tracks
if number_of_toys >= 50:
    total_order_toys *= 0.75
income = total_order_toys - total_order_toys * 0.10
difference = abs(income - excursion_price)
if income >= excursion_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")

