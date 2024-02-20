wight = int(input())
length = int(input())
total_size_cake = wight * length
there_is_more_cake = True
command = input()
while command != 'STOP':
    current_number_of_cakes = int(command)
    total_size_cake -= current_number_of_cakes
    if total_size_cake <0:
        there_is_more_cake = False
        break
    command = input()
if there_is_more_cake:
    print(f"{total_size_cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_size_cake)} pieces more.")