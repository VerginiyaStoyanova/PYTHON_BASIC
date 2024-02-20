number_of_pans = int(input())
number_of_markers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input())
price_per_pen = 5.80
price_per_marker = 7.20
price_per_liter_detergent = 1.20
needed_sum = number_of_pans * price_per_pen + \
             number_of_markers * price_per_marker + \
             liters_of_detergent * price_per_liter_detergent
needed_sum = needed_sum - needed_sum * percent_discount / 100

print(needed_sum)