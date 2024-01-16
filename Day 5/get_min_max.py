# Write a program to find the maximum and minimum values in a list.

elements = [8, 3, 1, 4, 5, 6, 7, 9, 2]

#minimum, maximum = min(elements), max(elements)

minimum = maximum = elements[0]

for i in elements:
    minimum = i if i < minimum else minimum
    maximum = i if i > maximum else maximum

print(f"The min and max values of given list is {minimum}, {maximum}")