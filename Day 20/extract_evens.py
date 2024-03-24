# Day 20: Write a function that takes a list of numbers and returns a new list containing only the even numbers.

n = input("Enter a list of numbers\n")

# given = [int(i) for i in n.split()]

evens = [int(i) for i in n.split() if int(i) % 2 == 0]

print("All the evens from the list are: ", evens)
