word = input()
sum = 0
for letter in range(0, len(word)):
    if word[letter] == 'a':
        sum += 1
    elif word[letter] == 'e':
        sum += 2
    elif word[letter] == 'i':
        sum += 3
    elif word[letter] == 'o':
        sum += 4
    elif word[letter] == 'u':
        sum += 5
print(sum)