day_of_week = input()

if day_of_week == 'Monday' or day_of_week == 'Tuesday' or day_of_week == 'Friday':
    price_ticket = 12
    print(price_ticket)
elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
    price_ticket = 14
    print(price_ticket)
elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    price_ticket = 16
    print(price_ticket)
