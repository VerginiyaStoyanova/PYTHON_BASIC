command = input()

while command != 'End':
    destination = command
    minimal_budget = float(input())
    sum_of_saved_money = 0
    while sum_of_saved_money < minimal_budget:
        current_amount = float(input())
        sum_of_saved_money += current_amount
    print(f"Going to {destination}!")

    command = input()
