# Day 55: Create a function that takes a string and returns the reverse of each word.

string = input("Input a string\n")


def reverse_words(string):
    words = string.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)


print(reverse_words(string))
