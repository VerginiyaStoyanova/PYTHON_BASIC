annual_tax = int(input())
sneakers_price = annual_tax * 0.6
equipment_price = sneakers_price * 0.8
ball_price = equipment_price / 4
accessories_price = ball_price / 5
total_sum = annual_tax \
            + sneakers_price \
            + equipment_price \
            + ball_price \
            + accessories_price

print(total_sum)