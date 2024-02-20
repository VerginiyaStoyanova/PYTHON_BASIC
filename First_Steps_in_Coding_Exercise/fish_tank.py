lenght = int(input())
widht = int(input())
height = int(input())
percent_non_free_volume = float(input())
fish_tank_volume_centimeters = lenght * widht * height
fish_tank_volume_liters = fish_tank_volume_centimeters * 0.001
free_percentage = (100 - percent_non_free_volume) / 100
needed_liters = fish_tank_volume_liters * free_percentage

print(needed_liters)