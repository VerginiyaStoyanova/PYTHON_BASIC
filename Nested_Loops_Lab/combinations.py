number = int(input())
combinations = 0

#x1 + x2 + x3 = n
for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range (number + 1):

            if x1 + x2 + x3 == number:
                combinations += 1

print(combinations)