constant_number = int(input())
total_sum = 0

while True:
    current_number = int(input())
    total_sum += current_number

    if total_sum >= constant_number:
        print(total_sum)
        break