result_first_match = input()
result_second_match = input()
result_third_match = input()
wins = 0
equality = 0
loss = 0

if result_first_match[0] > result_first_match[2]:
    wins += 1
elif result_first_match[0] == result_first_match[2]:
    equality += 1
elif result_first_match[0] < result_first_match[2]:
    loss += 1
if result_second_match[0] > result_second_match[2]:
    wins += 1
elif result_second_match[0] == result_second_match[2]:
    equality += 1
elif result_second_match[0] < result_second_match[2]:
    loss += 1
if result_third_match[0] > result_third_match[2]:
    wins += 1
elif result_third_match[0] == result_third_match[2]:
    equality += 1
elif result_third_match[0] < result_third_match[2]:
    loss += 1

print(f"Team won {wins} games.")
print(f"Team lost {loss} games.")
print(f"Drawn games: {equality}")