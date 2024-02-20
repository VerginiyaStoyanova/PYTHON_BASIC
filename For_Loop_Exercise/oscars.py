name_of_the_actor = input()
academy_points = float(input())
number_of_assessors = int(input())
total_points = academy_points
for assessor in range(number_of_assessors):
    name_of_the_assessor = input()
    assessor_points = float(input())
    total_assessor_points = (len(name_of_the_assessor) * assessor_points) / 2
    total_points += total_assessor_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {name_of_the_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {name_of_the_actor} you need {difference:.1f} more!")
