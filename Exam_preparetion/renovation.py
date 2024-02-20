from math import ceil

height = int(input())
weight = int(input())
percent_unpainted_parts = int(input())
area_walls = (height * weight) * 4
area_for_paint = ceil(area_walls - (area_walls * percent_unpainted_parts / 100))
painted_area = 0

command = input()

while command != 'Tired!':
    paint_litters = int(command)
    painted_area += paint_litters

    if painted_area > area_for_paint:
        difference = painted_area - area_for_paint
        print(f"All walls are painted and you have {difference} l paint left!")
        break
    elif painted_area == area_for_paint:
        print("All walls are painted! Great job, Pesho!")
        break

    command = input()

else:
    difference = area_for_paint - painted_area
    print(f"{difference} quadratic m left.")