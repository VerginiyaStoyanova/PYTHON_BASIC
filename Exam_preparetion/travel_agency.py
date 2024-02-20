city_name = input()
package_type = input()
vip_discount = input()
days = int(input())
total_price = 0

if city_name == 'Bansko' or city_name == 'Borovets':
    if days < 1:
        print("Days must be positive number!")
    else:
        if days > 7:
            days -= 1
        if package_type == 'withEquipment':
            if vip_discount == 'yes':
                price_per_night = 100 * 0.90
            elif vip_discount == 'no':
                price_per_night = 100
            total_price = days * price_per_night
            print(f"The price is {total_price:.2f}lv! Have a nice time!")
        elif package_type == 'noEquipment':
            if vip_discount == 'yes':
                price_per_night = 80 * 0.95
            elif vip_discount == 'no':
                price_per_night = 80
            total_price = days * price_per_night
            print(f"The price is {total_price:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")

elif city_name == 'Varna' or city_name == 'Burgas':
    if days < 1:
        print("Days must be positive number!")
    else:
        if days > 7:
            days -= 1
        if package_type == 'withBreakfast':
            if vip_discount == 'yes':
                price_per_night = 130 * 0.88
            elif vip_discount == 'no':
                price_per_night = 130
            total_price = days * price_per_night
            print(f"The price is {total_price:.2f}lv! Have a nice time!")
        elif package_type == 'noBreakfast':
            if vip_discount == 'yes':
                price_per_night = 100 * 0.93
            elif vip_discount == 'no':
                price_per_night = 100
            total_price = days * price_per_night
            print(f"The price is {total_price:.2f}lv! Have a nice time!")
        else:
            print("Invalid input!")

else:
    print("Invalid input!")