import math

min_number = math.inf

while True:
    text = input()

    if text == 'Stop':
        break

    current_number = int(text)

    if current_number < min_number:
        min_number = current_number

print(min_number)