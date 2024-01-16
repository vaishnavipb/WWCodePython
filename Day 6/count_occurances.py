# Write a program to count the occurrences of a specific character in a string.

string = "Hello! This is a sample sentence to count occurances"

char_to_count = 'o'
count = 0

for i in range(0, len(string)):
    if string[i] == char_to_count:
        count += 1

print(f'The character "{char_to_count}" appeared {count} times in the given string')