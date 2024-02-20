name_of_move = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percent_for_cinema = int(input())

profit_per_day = number_of_tickets * price_per_ticket
total_profit_all_days = profit_per_day * number_of_days
cinema_percent = total_profit_all_days * (percent_for_cinema / 100)
total_movie_profit = total_profit_all_days - cinema_percent

print(f"The profit from the movie {name_of_move} is {total_movie_profit:.2f} lv.")