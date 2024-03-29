# Day 46: Write a program to find the most common words in a text file.

def is_list_sorted(elements):
    for i in range(1, len(elements)):
        if elements[i - 1] > elements[i]:
            return "The elements are not sorted"
    return "The elements are sorted"

elements = [int(i) for i in input("Input a list\n").split()]

print(is_list_sorted(elements))