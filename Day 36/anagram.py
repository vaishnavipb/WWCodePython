# Day 36: Write a Python program to check if two strings are anagrams

def string_dict(string):
    dictionary = {}
    for i in range(0, len(string)):
        if string[i] in dictionary:
            dictionary[string[i]] = dictionary[string[i]] + 1
        else:
            dictionary[string[i]] = 1
    return dictionary


def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    if string2 == string1:
        return True

    chars = string_dict(string1)
    for i in range(0, len(string2)):
        if string2[i] in chars:
            chars[string2[i]] = chars[string2[i]] - 1
        else:
            chars[string2[i]] = -1

    for key, value in chars.items():
        if value != 0:
            return False
    return True


s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

print(f"Strings {s1}, {s2} are anagrams? {is_anagram(s1, s2)}")
