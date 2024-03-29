# Day 52: Create a program that checks if a string is a palindrome.

string = input("Input a string\n")


def palindrome(string):
    start, end = 0, len(string) - 1

    while start <= end:
        if string[start] != string[end]:
            return f"{string} is not a palindrome"
        start += 1
        end -= 1
    return f"{string} is a palindrome"


print(palindrome(string))
