budget = float(input())
costs = 0
counter_of_products = 0
needed_money = 0

while True:
    name_of_product = input()
    if name_of_product == 'Stop':
        break
    product_price = float(input())
    counter_of_products += 1

    if counter_of_products % 3 == 0:
        product_price /= 2

    if product_price > budget:
        needed_money = product_price - budget
        break

    costs += product_price
    budget -= product_price

if needed_money == 0:
    print(f"You bought {counter_of_products} products for {costs:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")