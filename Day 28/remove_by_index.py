# Day 28: Create a program that removes the nth element from a list.

elements = input("Enter List: ").split()

n = int(input("Enter the index of the element to remove: "))

if n < len(elements):
    elements.pop(n)
    print(f"List after removing {n}th index: {elements}")

else:
    print(f"Index out of range")


