needed_money = float(input())
available_money = float(input())
past_days = 0
consecutive_days_of_spending = 0

while available_money < needed_money and consecutive_days_of_spending < 5:
    money_action = input()
    current_money = float(input())
    past_days += 1

    if money_action == 'spend':
        consecutive_days_of_spending += 1
        available_money -= current_money
        if available_money < 0:
            available_money = 0

    elif money_action == 'save':
        consecutive_days_of_spending = 0
        available_money += current_money

if consecutive_days_of_spending == 5:
    print(f"You can't save the money.")
    print(past_days)

if available_money >= needed_money:
    print(f"You saved the money for {past_days} days.")