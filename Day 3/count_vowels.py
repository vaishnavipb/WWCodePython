# Write a function to count the number of vowels in a given string

given_string = "Hello! This is a sample sentence that contains vowels"

count = 0

for char in given_string:
    if char in 'aeiou':
        count += 1

print(f"The number of vowels in given string is {count}")