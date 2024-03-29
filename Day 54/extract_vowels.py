# Day 55: Create a function to find all words in a sentence that start with a vowel.

string = input("Input a string\n")


def extract_vowels(string):
    vowels = []
    words = string.split()
    for i in range(len(words)):
        if words[i][0] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(words[i])
    return vowels


print(extract_vowels(string))
