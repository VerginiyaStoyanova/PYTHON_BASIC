from math import pi

figure = input()
if figure == "square":
    length_side = float(input())
    area = length_side ** 2
    print(f"{area:.3f}")
elif figure == "rectangle":
    length_side_a = float(input())
    length_side_b = float(input())
    area = length_side_a * length_side_b
    print(f"{area:.3f}")
elif figure == "circle":
    circle_radius = float(input())
    area = pi * (circle_radius ** 2)
    print(f"{area:.3f}")
elif figure == "triangle":
    length_side = float(input())
    length_height = float(input())
    area = (length_side * length_height) / 2
    print(f"{area:.3f}")
