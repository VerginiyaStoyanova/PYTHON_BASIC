country = input()
equipment = input()

if country == 'Russia':
    if equipment == 'ribbon':
        difficulty = 9.100
        evaluation = 9.400
    elif equipment == 'hoop':
        difficulty = 9.300
        evaluation = 9.800
    elif equipment == 'rope':
        difficulty = 9.600
        evaluation = 9.000
elif country == 'Bulgaria':
    if equipment == 'ribbon':
        difficulty = 9.600
        evaluation = 9.400
    elif equipment == 'hoop':
        difficulty = 9.550
        evaluation = 9.750
    elif equipment == 'rope':
        difficulty = 9.500
        evaluation = 9.400
elif country == 'Italy':
    if equipment == 'ribbon':
        difficulty = 9.200
        evaluation = 9.500
    elif equipment == 'hoop':
        difficulty = 9.450
        evaluation = 9.350
    elif equipment == 'rope':
        difficulty = 9.700
        evaluation = 9.150

total_score = difficulty + evaluation
needed_percent_to_all_score = (20 - total_score) / 20 * 100

print(f"The team of {country} get {total_score:.3f} on {equipment}.")
print(f"{needed_percent_to_all_score:.2f}%")