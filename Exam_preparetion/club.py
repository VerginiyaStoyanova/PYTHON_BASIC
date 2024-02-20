desired_income = float(input())
total_income = 0

command = input()

while command != 'Party!':
    cocktail_name = command
    number_of_cocktails = int(input())
    cocktail_price = len(cocktail_name)
    total_cocktail_price = cocktail_price * number_of_cocktails

    if total_cocktail_price % 2 != 0:
        total_cocktail_price *= 0.75
    total_income += total_cocktail_price

    if total_income >= desired_income:
        print("Target acquired.")
        break

    command = input()

else:
    difference = abs(desired_income - total_income)
    print(f"We need {difference:.2f} leva more.")

print(f"Club income - {total_income:.2f} leva.")



