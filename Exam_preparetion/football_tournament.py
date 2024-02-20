team_name = input()
number_of_matches_played = int(input())
points = 0
wins = 0
equality = 0
loss = 0

if number_of_matches_played > 0:
    for _ in range(1, number_of_matches_played + 1):
        result = input()
        if result == 'W':
            points += 3
            wins += 1
        elif result == 'D':
            points += 1
            equality += 1
        elif result == 'L':
            points += 0
            loss += 1
    print(f"{team_name} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {equality}")
    print(f"## L: {loss}")
    percent_wins = wins / number_of_matches_played * 100
    print(f"Win rate: {percent_wins:.2f}%")
else:
    print(f"{team_name} hasn't played any games during this season.")
