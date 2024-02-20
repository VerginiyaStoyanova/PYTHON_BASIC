annual_basketball_fee = int(input())

basketball_sneakers = annual_basketball_fee * 0.6
basketball_outfit = basketball_sneakers * 0.8
basketball_ball = 0.25 * basketball_outfit
basketball_accessories = 0.2 * basketball_ball

total_price = annual_basketball_fee + basketball_sneakers + basketball_outfit + basketball_ball + basketball_accessories

print(f'{total_price:.2f}')