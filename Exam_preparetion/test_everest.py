meters_counter = 5364
days_counters = 1
failed = False
command = input()

while command != 'END':
    climbed_meters = int(input())
    if command == 'Yes':
        days_counters += 1
        if days_counters > 5:
            failed = True
            break
        meters_counter += climbed_meters
    elif command == 'No':
        meters_counter += climbed_meters
    if meters_counter >= 8848:
        print(f"Goal reached for {days_counters} days!")
        break

    command = input()

else:
    failed = True
if failed:
    print("Failed!")
    print(f"{meters_counter}")