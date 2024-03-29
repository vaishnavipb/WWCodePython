# Day 43: Write a program that removes all whitespaces from a given string.

string = input("Enter a string: ")
i = 0
while i < len(string):
    if string[i] == " ":
        string = string[:i] + string[i + 1:]
        i -= 1
    i += 1

print(f"The resultant string after removing all whilespaces is {string}")
