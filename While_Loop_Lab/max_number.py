import math

max_number = -math.inf

while True:
    text = input()

    if text == 'Stop':
        break

    current_number = int(text)

    if current_number > max_number:
        max_number = current_number

print(max_number)