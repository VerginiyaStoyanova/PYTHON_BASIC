stage_of_the_championship = input()
type_of_ticket = input()
number_of_tickets = int(input())
trophy_picture = input()
picture_trophy_price = 40
price = 0

if stage_of_the_championship == 'Quarter final':
    if type_of_ticket == 'Standard':
        price = 55.50
    elif type_of_ticket == 'Premium':
        price = 105.20
    elif type_of_ticket == 'VIP':
        price = 118.90
elif stage_of_the_championship == 'Semi final':
    if type_of_ticket == 'Standard':
        price = 75.88
    elif type_of_ticket == 'Premium':
        price = 125.22
    elif type_of_ticket == 'VIP':
        price = 300.40
elif stage_of_the_championship == 'Final':
    if type_of_ticket == 'Standard':
        price = 110.10
    elif type_of_ticket == 'Premium':
        price = 160.66
    elif type_of_ticket == 'VIP':
        price = 400

total_price = price * number_of_tickets

if total_price > 4000:
    total_price *= 0.75
    picture_trophy_price = 0

elif total_price > 2500:
    total_price *= 0.9

if trophy_picture == 'Y' and total_price <= 4000:
    total_price += picture_trophy_price * number_of_tickets

print(f'{total_price:.2f}')