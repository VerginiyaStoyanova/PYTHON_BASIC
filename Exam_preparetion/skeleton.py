control_minutes = int(input())
control_seconds = int(input())
chute_length_meters = float(input())
seconds_to_100_meters = int(input())

total_seconds = chute_length_meters / 100 * seconds_to_100_meters
additional_time_seconds = chute_length_meters / 120 * 2.5
total_seconds -= additional_time_seconds

total_control_seconds = control_minutes * 60 + control_seconds

if total_seconds <= total_control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_seconds:.3f}.")
else:
    difference = abs(total_control_seconds - total_seconds)
    print(f"No, Marin failed! He was {difference:.3f} second slower.")