width = int(input())
length = int(input())
height = int(input())
total_volume = width * length * height
there_is_more_free_space = True
command = input()
while command != 'Done':
    current_number_of_boxs = int(command)
    total_volume -= current_number_of_boxs
    if total_volume < 0:
        there_is_more_free_space = False
        break
    command = input()
if there_is_more_free_space:
    print(f"{total_volume} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(total_volume)} Cubic meters more.")