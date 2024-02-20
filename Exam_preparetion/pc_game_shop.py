number_of_games = int(input())
number_hearthstone = 0
number_fornite = 0
number_overwatch = 0
number_others = 0

for _ in range(1, number_of_games + 1):
    name_of_the_game = input()
    if name_of_the_game == 'Hearthstone':
        number_hearthstone += 1
    elif name_of_the_game == 'Fornite':
        number_fornite += 1
    elif name_of_the_game == 'Overwatch':
        number_overwatch += 1
    else:
        number_others += 1

percent_of_hearthstone = number_hearthstone / number_of_games * 100
percent_of_fornite = number_fornite / number_of_games * 100
percent_of_overwatch = number_overwatch / number_of_games * 100
percent_of_others = number_others / number_of_games * 100

print(f"Hearthstone - {percent_of_hearthstone:.2f}%")
print(f"Fornite - {percent_of_fornite:.2f}%")
print(f"Overwatch - {percent_of_overwatch:.2f}%")
print(f"Others - {percent_of_others:.2f}%")