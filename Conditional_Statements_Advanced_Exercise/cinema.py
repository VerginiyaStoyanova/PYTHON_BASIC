movie_type = input()
rows = int(input())
columns = int(input())
total_seats = rows * columns
ticket_price = 0

if movie_type == 'Premiere':
    ticket_price = 12.00
elif movie_type == 'Normal':
    ticket_price = 7.50
elif movie_type == 'Discount':
    ticket_price = 5.00
total_income = total_seats * ticket_price

print(f'{total_income:.2f} leva')