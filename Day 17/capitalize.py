# Day 17: Create a program that capitalizes the first letter of each word in a sentence.

sentence = input("Enter a sentence to get capitalized output\n")

print("Here is the capitalized output:")
for word in sentence.split():
    print(f"{word[0].upper()}{word[1:]} ", end = "")