amount_nylon = int(input())
amount_paint = int(input())
amount_thinner = int(input())
hours_whole_work = int(input())
nylon_per_quare_meter = 1.50
paint_per_liter = 14.50
thinner_per_liter = 5
supplement_paint = 0.10 * amount_paint
supplement_nylon = 2
bags = 0.40
total_price_materials = (amount_nylon + supplement_nylon) * nylon_per_quare_meter \
    + (amount_paint + supplement_paint) * paint_per_liter \
    + amount_thinner * thinner_per_liter + bags
master_price_per_hour = 0.3 * total_price_materials
total_price = total_price_materials + master_price_per_hour * hours_whole_work

print(total_price)