# Day 32: Create a function that calculates the average of a list of numbers

elements = [int(i) for i in input("Input a list\n").split()]

average = sum(elements)//len(elements)

print(f'The average of the list is: {average}')
