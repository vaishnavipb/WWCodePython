# Day 24: Write a program to remove vowels from a given string.

string = input("Enter a string \n")
i = 0
while i < len(string):
    # print(i)
    try:
        if string[i] in ['a', 'e', 'i', 'o', 'u']:
            string = string[:i] + string[i + 1:]
            i -= 1
    except:
        pass
    i += 1

print(f"After removing vowels from the string, the new string is: '{string}'")
