number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
total_price_manu = number_chicken_menu * chicken_menu \
    + number_fish_menu * fish_menu \
    + number_vegetarian_menu * vegetarian_menu
desert = 0.2 * total_price_manu
delivery = 2.5
total_price_delivery = total_price_manu + desert +delivery

print(total_price_delivery)

